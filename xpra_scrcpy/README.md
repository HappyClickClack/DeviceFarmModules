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
- запустите контейнер:
```
docker run -v $(pwd)/script:/mounted-scripts -d -p 18080:8080 --name=android-web-interface xpra_scrcpy_image
```
- спустя пару минут (время необходимое для старта серсвиса) проверьте доступ http://localhost:18080:
  
</details>

# Структура каталога:
/:
- `dockerfile` - заготовка для образа.

/script/:
- `start.sh` - скрипт настройки сервисов на портах.
