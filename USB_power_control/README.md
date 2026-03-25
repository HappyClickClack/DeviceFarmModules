<img width="392" height="388" alt="image" src="https://github.com/user-attachments/assets/f09ca587-8372-403f-aa10-ad9b77f06184" />

Для дистанционного отключения устройств от USB питания можно использовать  USB хабы, [совместимые с утилитой uhubctl](https://github.com/mvp/uhubctl#compatible-usb-hubs). Желательно выбирать хабы с внешним питанием для более быстрой зарядки подключенных устройств.

Для своих задач мы используем вот такие хабы:
* j5create JCH377 ([где купить](https://ru.microless.com/product/j5create-usb-type-c-3-0-7-port-hub-jch377/))
* RSH-ST10C-6 ([где купить](https://aliexpress.ru/item/1005008160865046.html))

Управление портами осуществляется утилитой uhubtcl:
```
$ uhubctl -h
uhubctl: utility to control USB port power for smart hubs.
Usage: uhubctl [options]
Without options, show status for all smart hubs.

Options [defaults in brackets]:
--action,   -a - action to off/on/cycle/toggle (0/1/2/3) for affected ports.
--ports,    -p - ports to operate on    [all hub ports].
--location, -l - limit hub by location  [all smart hubs].
--level     -L - limit hub by location level (e.g. a-b.c is level 3).
--vendor,   -n - limit hub by vendor id [any] (partial ok).
--search,   -s - limit hub by attached device description.
--delay,    -d - delay for cycle action [2 sec].
--repeat,   -r - repeat power off count [1] (some devices need it to turn off).
--exact,    -e - exact location (no USB3 duality handling).
--force,    -f - force operation even on unsupported hubs.
--nodesc,   -N - do not query device description (helpful for unresponsive devices).
--nosysfs,  -S - do not use the Linux sysfs port disable interface.
--reset,    -R - reset hub after each power-on action, causing all devices to reassociate.
--wait,     -w - wait before repeat power off [20 ms].
--version,  -v - print program version.
--help,     -h - print this text.

Send bugs and requests to: https://github.com/mvp/uhubctl
version: 2.5.0-1

```

Пример работы с утилитой:
1. проверяем доступные для управления порты, просто позовем утилиту:
```
$ sudo uhubctl
Current status for hub 1-8 [05e3:0608 USB2.0 Hub, USB 2.10, 4 ports]
  Port 1: 0503 power highspeed enable connect [22d9:2769 OPPO CPH2325 9TxxxxxxxxxWS]
  Port 2: 0100 power
  Port 3: 0503 power highspeed enable connect [04e8:6860 SAMSUNG SAMSUNG_Android 52xxxxxxxxxa7]
  Port 4: 0100 power
```
, _здесь видно, что хаб `1-8` поддерживает управление на 4х портах, на двух из которых подключены устройства OPPO и Samsung_.
На устройстве Samsung идет зарядка (скрин с экрана телефона):<br> <img width="394" height="187" alt="image" src="https://github.com/user-attachments/assets/271c5cde-d0a6-4cac-8822-df34b4cf43d7" />


2. Отключим порт Samsung:
```
$ sudo uhubctl -l 1-8 -a off -p 3
Current status for hub 1-8 [05e3:0608 USB2.0 Hub, USB 2.10, 4 ports]
  Port 3: 0503 power highspeed enable connect [04e8:6860 SAMSUNG SAMSUNG_Android 52xxxxxxxxxa7]
Sent power off request
New status for hub 1-8 [05e3:0608 USB2.0 Hub, USB 2.10, 4 ports]
  Port 3: 0000 off
```
, _здесь укажем номер хаба `-l 1-8`, команду `-a off` и номер порта `-p 3`_.
Устройство Samsung переключается на батарею:<br> <img width="397" height="186" alt="image" src="https://github.com/user-attachments/assets/a69e2b0f-ffd1-4953-bf2c-7dcfa982dcdf" />

3. Включим обратно:
```
$ sudo uhubctl -l 1-8 -a on -p 3
Current status for hub 1-8 [05e3:0608 USB2.0 Hub, USB 2.10, 4 ports]
  Port 3: 0000 off
Sent power on request
New status for hub 1-8 [05e3:0608 USB2.0 Hub, USB 2.10, 4 ports]
  Port 3: 0100 power
```
, _здесь укажем обратную команду `-a on`_.
Зарядка вернулась, устройство показывает уровень заряда 100%:<br> <img width="398" height="493" alt="image" src="https://github.com/user-attachments/assets/8cbe0d40-86cf-4cdc-8435-23a8035bf6b3" />

При отключении порта USB связь с устройством пропадает и ADB отладка по проводу не возможна. Для контроля над устройством при отключеннмо USB порте можно использовать WiFi подключение (`adb connect IP:PORT`). 
