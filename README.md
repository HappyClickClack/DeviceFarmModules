# Коллекция идей и кода для работы с Android устройствами в тестовой ферме.

**Содержание**:
- [Работа с Android устройствами в контейнерах, проброс ADB сервера в контейнеры](https://github.com/HappyClickClack/DeviceFarmModules/edit/main/README.md#%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0-%D1%81-android-%D1%83%D1%81%D1%82%D1%80%D0%BE%D0%B9%D1%81%D1%82%D0%B2%D0%B0%D0%BC%D0%B8-%D0%B2-%D0%BA%D0%BE%D0%BD%D1%82%D0%B5%D0%B9%D0%BD%D0%B5%D1%80%D0%B0%D1%85-%D0%BF%D1%80%D0%BE%D0%B1%D1%80%D0%BE%D1%81-adb-%D1%81%D0%B5%D1%80%D0%B2%D0%B5%D1%80%D0%B0-%D0%B2-%D0%BA%D0%BE%D0%BD%D1%82%D0%B5%D0%B9%D0%BD%D0%B5%D1%80%D1%8B)
- [Web интерфейс для работы с устройствами](https://github.com/HappyClickClack/DeviceFarmModules/edit/main/README.md#web-%D0%B8%D0%BD%D1%82%D0%B5%D1%80%D1%84%D0%B5%D0%B9%D1%81-%D0%B4%D0%BB%D1%8F-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B-%D1%81-%D1%83%D1%81%D1%82%D1%80%D0%BE%D0%B9%D1%81%D1%82%D0%B2%D0%B0%D0%BC%D0%B8)
- [Трансляция экрана Android устройств, работа с видеофреймами в Python](https://github.com/HappyClickClack/DeviceFarmModules/edit/main/README.md#%D1%82%D1%80%D0%B0%D0%BD%D1%81%D0%BB%D1%8F%D1%86%D0%B8%D1%8F-%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0-android-%D1%83%D1%81%D1%82%D1%80%D0%BE%D0%B9%D1%81%D1%82%D0%B2-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0-%D1%81-%D1%84%D1%80%D0%B5%D0%B9%D0%BC%D0%B0%D0%BC%D0%B8-%D0%B2-python)
- [Управление питанием устройств](https://github.com/HappyClickClack/DeviceFarmModules/edit/main/README.md#%D1%83%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5-%D0%BF%D0%B8%D1%82%D0%B0%D0%BD%D0%B8%D0%B5%D0%BC-%D1%83%D1%81%D1%82%D1%80%D0%BE%D0%B9%D1%81%D1%82%D0%B2)

В этом репо представлены идеи и примеры модулей для автоматизации работы с Android устройствами (и не только) и построения своей маленькой электрофермы.

Вот, кмк, самая простая схема для запуска тестов на устройствах при использовании Jenkins
<img width="1005" height="565" alt="image" src="https://github.com/user-attachments/assets/4177fa7b-6972-4a57-b06a-1dca6b9e6d44" />

Небольшое пояснение: после запуска пайплайн проходит предварительные шаги подготовки данных, встает на ADB узел Jenkins с меткой "adb_client". Далее Python cкрипт берет из параметров идентификатор устройства и взаимодействует только с выбранным устройством (серийник устройства можно передавать в параметрах сборки) - прогоняет тесты. 
При таком подходе Jenkins сам управляет очередями, занимает устройство в только в момент начала работы с ним, а любое завершение пайплайна, в т.ч. падение и т.п., автоматически освобождает устройство. Очень просто и надежно. 

Однако, у этой схемы помимо ее простоты есть и существенный недостаток - это низкая пропускная способность. Поскольку здесь один Jenkins узел, то все тесты, даже на разных устройствах, стоят в общей очереди на этот узел.

## Работа с Android устройствами в контейнерах, проброс ADB сервера в контейнеры
<img width="1226" height="766" alt="image" src="https://github.com/user-attachments/assets/691b1c9c-cdd1-4076-9a19-0b8d5e150bec" />

Для устранения этого недостатка можно использовать независимые узлы в отдельных контейнерах для каждого устройства, и, например, пробрасывать доступ до ADB сервера в каждый контейнер.
Подробнее об этой схеме и примеры реализации см [здесь](https://github.com/HappyClickClack/DeviceFarmModules/blob/main/ADB_server_forwarding/README.md).

## Web интерфейс для работы с устройствами
<img width="861" height="608" alt="image" src="https://github.com/user-attachments/assets/31223ca6-af90-49fb-9cd0-29575da06bcb" />

При необходимости наблюдения за экраном устройства и/или для интерактивного взаимодействия с Android устройством существует очень удобная утилита [scrcpy](https://github.com/genymobile/scrcpy) ("**scr**een **c**o**py**").
Эта утилита предназначена для зеркалирования экрана Android-устройств на ПК (Windows, macOS, Linux) и управления ими с помощью мыши и клавиатуры.

Но как и при любом подключении по ADB первое подключение `scrcpy` требует подтверждения сопряжения/авторизации на устройстве. Т.е. для локального использования нужно либо прописывать ADB ключи в устройство и потом следить за их актуальностью, либо один раз настроить `scrcpy` на доверенном узле и предоставлять доступ как веб сервис. Рассмотрим второй вариант побробнее.

Существует программное обеспечение, предназначенное для удаленного запуска графических приложений (X11) и рабочих столов с дальнейшим отображением этих приложений на экранах других компьютеров или в браузере. Примером такого ПО является [Xpra](https://github.com/Xpra-org/xpra/). Если настроить Xpra сервер на хосте с подключенными Android устройствами и в качестве приложения запустить scrcpy, то затем с scrcpy можно работать в браузере на другой машине.
Подробнее про запуск Xpra + scrcpy см [тут](https://github.com/HappyClickClack/DeviceFarmModules/blob/main/xpra_scrcpy/README.md).

## Трансляция экрана Android устройств, работа с фреймами в Python
<img width="638" height="602" alt="image" src="https://github.com/user-attachments/assets/3383ce3e-b358-4d73-91ab-a435093359a1" />

Если возникает необходимость транслировать экран устройства как каких-либо задач видеоналитики, то опять же можно использовать утилиту [scrcpy](https://github.com/genymobile/scrcpy) в режиме [автономного сервера/standalone server](https://github.com/Genymobile/scrcpy/blob/master/doc/develop.md#standalone-server).
Примеры настройки и использования см [здесь](https://github.com/HappyClickClack/DeviceFarmModules/blob/main/screen_streem_capture/README.md).

## Управление питанием устройств
<img width="392" height="388" alt="image" src="https://github.com/user-attachments/assets/f09ca587-8372-403f-aa10-ad9b77f06184" />

Еще одна распространненная задача при работе с устройствами - это возможность дистанционного отключения устройства от внешнего питания, в случае электрофермы - от USB порта. Для решения этой задачи можно использовать готовые USB хабы с поддержкой Per Port Power Switching (PPPS) и утилиту [uhubctl](https://github.com/mvp/uhubctl). Подробнее об этой утилите и список совместимых USB хабов см [здесь](https://github.com/mvp/uhubctl).
Примеры управления питанием и др детали см [тут](https://github.com/HappyClickClack/DeviceFarmModules/blob/main/USB_power_control/README.md).
