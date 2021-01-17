[![Build Status](https://travis-ci.org/elisey/hue-utility.svg?branch=master)](https://travis-ci.org/elisey/hue-utility)

# Hue control utility

Utility for controling Hue smart lams

## Initial connection to the Bridge. You should do it only once

```bash
hue connect 192.168.x.x
```

Credentials will be stored in ~/.python_hue file

## Basic commands

Turn lamp on and off

```bash
hue on
hue off
```

You can pass **id** of your lamp. By default **id** is 1.

```bash
hue -i 2 on
hue -i 2 off
```

Set brightness to maximum

```bash
hue br 100
```

Set brightness 10%

```bash
hue br 10
```

## Set custom color

Set color with hue and saturation parameters:

```bash
hue hue 3000
hue saturation 100
```

Set color with xy parameters

```bash
hue xy 0.1 0.2
```

Set color with hsv parameters

```bash
hue hsv 3000 100
```

## Special commands

Run scene by name

```bash
hue scene <scene_name>
```

Blink with lamp one time

```bash
hue alert single
```

Blinkin with lamp for 5 seconds

```bash
hue alert start
sleep 5
hue alert stop
```

Built in smooth color changing

```bash
hue effect start
sleep 5
hue effect stop
```

## TODO

- Addressing lamp by name
- Custom scripts support for contolling lamps
