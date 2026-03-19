# Web интерфейс для устройств

Для организации web интерфейса для устройств фермы можно использовать комбинацию Xpra и scrcpy.
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
cd xpra_scrcpy
docker build -t xpra_scrcpy_image .
```
- запустите контейнер с пробросом ADB сервера:
```
docker run -d --add-host=host.docker.internal:host-gateway \
-e "ANDROID_ADB_SERVER_ADDRESS=host.docker.internal" \
--name=android-web-interface \
-v $(pwd)/script:/mounted-scripts \
-p 18080:8080 \
xpra_scrcpy_image
```
- спустя пару минут (_время необходимое для старта сервиса_) проверьте доступ http://localhost:18080, http://localhost:18081, http://localhost:18082. Пароль для webconnuser - `123`, указан в скрипте start.sh.

_Для корректной работы с устройствами необходимо запустить ADB сервер на хосте `adb -a nodaemon server start &> /dev/null &` и указать DEVICE_SERIAL в скрипте._
  
</details>

# Структура каталога:
/:
- `dockerfile` - заготовка для образа.

/script/:
- `start.sh` - скрипт настройки сервисов на портах.

# Если возникли сложности:
- проверьте логи контейнера
- проверьте, что устройства доступны в контейнере `adb devices`
