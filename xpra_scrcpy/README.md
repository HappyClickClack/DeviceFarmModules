# Web интерфейс для устройств

Для организации web интерфейса для устройств фермы можно использовать комбинацию [Xpra](https://github.com/Xpra-org/xpra/) и [scrcpy](https://github.com/genymobile/scrcpy).

<img width="866" height="609" alt="image" src="https://github.com/user-attachments/assets/fb67067e-6c29-4f94-a479-d8e88029c8bc" />


# Установка окружения и запуск:
<details>
  <summary>Инструкция</summary>
  
- Клонируйте репозиторий:
```
git clone https://github.com/HappyClickClack/DeviceFarmModules
```  
- создайте образ:
```
cd DeviceFarmModules/xpra_scrcpy/
docker build -t xpra_scrcpy_image .
```
- ограничим права на каталог со скриптом:
```
chmod -R 700 ./script/
```
- запустите ADB сервер на хосте:
```
adb kill-server
pkill -9 adb
adb -a nodaemon server start &> /dev/null &
```
- запустите контейнер с пробросом ADB сервера:
```
docker run -d --add-host=host.docker.internal:host-gateway \
-e "ANDROID_ADB_SERVER_ADDRESS=host.docker.internal" \
--name=android-web-interface \
-v $(pwd)/script:/mounted-scripts \
-p 18080-18085:8080-8085 \
xpra_scrcpy_image
```
- спустя пару минут (_время необходимое для старта сервиса_) проверьте доступ http://localhost:18080, http://localhost:18081, http://localhost:18082. Пароль для нового пользователя webconnuser - `123`, указан в скрипте [start.sh](https://github.com/HappyClickClack/DeviceFarmModules/blob/main/xpra_scrcpy/script/start.sh#L10), пользователь создается в [dockerfile](https://github.com/HappyClickClack/DeviceFarmModules/blob/main/xpra_scrcpy/dockerfile#L43).
  - На порту 18080 должно появиться окно Xterm:<br>
    <img width="532" height="426" alt="image" src="https://github.com/user-attachments/assets/f0b037ad-fe59-447b-b384-9a343ca00e1b" />

  - На порту 18081 в скрипте start.sh указан пользователь - webconuser и запрошена авторизация - нужно ввести пароль для подключения, затем должно появиться окно lxterminal:<br>
    <img width="545" height="475" alt="image" src="https://github.com/user-attachments/assets/b18b8afa-8a2e-470b-ab04-65b014ccedb5" /><br>
    <img width="465" height="187" alt="image" src="https://github.com/user-attachments/assets/d716a4aa-e89b-4693-a6cc-c981caa1537a" />


  - На порту 18082 также нужно ввести пароль и должно появиться окно scrcpy как на изображении выше.
- права пользователя webconnuser ограничены и он не может прочитать каталог скрипта:<br>
  <img width="715" height="481" alt="image" src="https://github.com/user-attachments/assets/25901404-8260-4c7e-ba84-72eac9edeed8" />


_Для корректной работы с устройствами необходимо запустить ADB сервер на хосте `adb -a nodaemon server start &> /dev/null &` (подробнее см [здесь](https://github.com/HappyClickClack/DeviceFarmModules/blob/main/ADB_server_forwarding/README.md)) и указать [DEVICE_SERIAL в скрипте](https://github.com/HappyClickClack/DeviceFarmModules/blob/main/xpra_scrcpy/script/start.sh#L15)._
  
</details>

# Структура каталога:
/:
- `dockerfile` - заготовка для образа.

/script/:
- `start.sh` - скрипт настройки сервисов на портах.

# Если возникли сложности:
- проверьте логи контейнера
- проверьте, что устройства доступны в контейнере, для этого выполните в контейнере `adb devices -l`
