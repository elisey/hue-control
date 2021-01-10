import argparse
from pathlib import Path
import logging
from phue import Bridge, AllLights, Light

__version__ = "0.1.0"


def int_from_0_to_100(x):
    x = int(x)
    if x < 0 or x > 100:
        raise argparse.ArgumentTypeError("Valid value from 0 to 100")
    return x


class HueUtility:
    @staticmethod
    def connect(ip):
        Bridge(ip=ip)

    DEFAULT_LAMP_ID = 1

    def __init__(self, lamp_id):
        self.logger = logging.getLogger('hue_utility')
        self.logger.setLevel(logging.DEBUG)
        self.bridge = Bridge()

        # LAMP_NAME = "Лампа"
        # lights = self.bridge.get_light_objects(mode="name")
        # self.light = lights[LAMP_NAME]
        self.light = Light(self.bridge, lamp_id)

    def on(self):
        self.logger.debug("on")
        self.light.on = True

    def off(self):
        self.logger.debug("off")
        self.light.on = False

    def is_on(self):
        self.logger.debug("is_on")
        return self.light.on is True

    def brightness(self, brightness):
        self.logger.debug(f"brightness={brightness}")

        if brightness == 0:
            self.off()
            return

        real_brightness = 254 * brightness // 100

        if not self.is_on():
            self.on()
        self.light.brightness = real_brightness

    def hue(self, hue):
        self.logger.debug(f"hue={hue}")
        self.light.hue = hue

    def saturation(self, saturation):
        self.logger.debug(f"saturation={saturation}")
        self.light.saturation = saturation

    def temperature(self, temperature):
        self.logger.debug(f"temperature={temperature}")
        self.light.colortemp_k = temperature

    def xy(self, xy):
        self.logger.debug(f"xy={xy}")
        self.light.xy = xy

    def hsv(self, hsv):
        self.logger.debug(f"hsv={hsv}")
        self.hue(hsv[0])
        self.saturation(hsv[1])

    def scene(self, name):
        self.logger.debug(f"scene={name}")

        scenes = self.bridge.scenes
        for scene in scenes:
            if scene.name == name:
                group = AllLights()
                self.logger.debug(f"scene id={scene.scene_id}")
                self.logger.debug(f"group id={group.group_id}")
                self.bridge.activate_scene(group.group_id, scene.scene_id, transition_time=1)
                return

        self.logger.error(f"Scene {name} not found")

    def alert(self, alert_command):
        self.logger.debug(f"alert={alert_command}")

        if alert_command == "single":
            self.light.alert = "select"
        elif alert_command == "start":
            self.light.alert = "lselect"
        elif alert_command == "stop":
            self.light.alert = "none"

    def effect(self, effect_command):
        self.logger.debug(f"effect={effect_command}")

        if effect_command == "start":
            self.light.effect = "colorloop"
        elif effect_command == "stop":
            self.light.effect = "none"


def main():
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest="command", help="Command")

    parser_connect = subparser.add_parser("connect", help="Connect to bridge. You should do it only once")
    parser_connect.add_argument("ip", type=str, help="Bridge IP address")

    subparser.add_parser("on", help="Turn on the device")
    subparser.add_parser("off", help="Turn off the device")

    parser_brightness = subparser.add_parser("br", help="Set device brightness")
    parser_brightness.add_argument("brightness", type=int, help="Device brightness. 0-100")

    parser_hue = subparser.add_parser("hue", help="Set device hue")
    parser_hue.add_argument("hue", type=int, help="Device hue. 0-65535")

    parser_saturation = subparser.add_parser("saturation", help="Set device saturation")
    parser_saturation.add_argument("saturation", type=int, help="Device saturation. 0-254")

    parser_temp = subparser.add_parser("temp", help="Set device light temperature in K")
    parser_temp.add_argument("temperature", type=int, help="Device light temperature. 2000-6500 K")

    parser_xy = subparser.add_parser("xy", help="Set device color in xy color space")
    parser_xy.add_argument("xy", type=float, nargs=2, help="Color in xy color space. [0.0-1.0, 0.0-1.0]")

    parser_hsv = subparser.add_parser("hsv", help="Set device color in hsv color space")
    parser_hsv.add_argument("hsv", type=int, nargs=2, help="Color hsv color space, hue (0-65535), saturation (0-254)")

    parser_scene = subparser.add_parser("scene", help="Run scene")
    parser_scene.add_argument("name", type=str, help="Scene name")

    parser_alert = subparser.add_parser("alert", help="Alert")
    parser_alert.add_argument("alert_command", type=str, choices=["single", "start", "stop"], help="Alert command")

    parser_effect = subparser.add_parser("effect", help="Start of stop effect color hopping")
    parser_effect.add_argument("effect_command", type=str, choices=["start", "stop"], help="Effect command")

    parser_scene = subparser.add_parser("script", help="Run custom script")
    parser_scene.add_argument("name", type=Path, help="Script file path")

    parser.add_argument("-i", default=HueUtility.DEFAULT_LAMP_ID, type=int, help="Lamp id")

    args = parser.parse_args()
    command = args.command

    if command == "connect":
        input("Press Link button on Hue Bridge than press Enter")
        HueUtility.connect(args.ip)
        print("Bridge is connected. Credentials are stored in ~/.python_hue file")
        return

    utility = HueUtility(lamp_id=args.i)
    if command == "on":
        utility.on()
    elif command == "off":
        utility.off()

    elif command == "br":
        utility.brightness(args.brightness)

    elif command == "hue":
        utility.hue(args.hue)

    elif command == "saturation":
        utility.saturation(args.saturation)

    elif command == "temp":
        utility.temperature(args.temperature)

    elif command == "xy":
        utility.xy(args.xy)

    elif command == "hsv":
        utility.hsv(args.hsv)

    elif command == "scene":
        utility.scene(args.name)

    elif command == "alert":
        utility.alert(args.alert_command)

    elif command == "effect":
        utility.effect(args.effect_command)


if __name__ == '__main__':
    main()
