Трансляция экран и перехват потока в Python коде
<img width="790" height="750" alt="image" src="https://github.com/user-attachments/assets/38471a6a-62df-4472-bd9f-33720db976df" />

[Инструкция от scrcpy](https://github.com/Genymobile/scrcpy/blob/master/doc/develop.md#standalone-server)
 
- запустим контейнер с [пробросом ADB](https://github.com/HappyClickClack/DeviceFarmModules/blob/main/ADB_server_forwarding/README.md) на базе образа, например, [xpra_scrcpy](https://github.com/HappyClickClack/DeviceFarmModules/blob/main/xpra_scrcpy/README.md).
```
docker run -d --add-host=host.docker.internal:host-gateway \
-e "ANDROID_ADB_SERVER_ADDRESS=host.docker.internal" \
--name=android-web-interface \
-v $(pwd)/script:/mounted-scripts \
-p 18080-18085:8080-8085 \
xpra_scrcpy_image
```
- в контейнере выполним:
```
wget https://github.com/Genymobile/scrcpy/releases/download/v3.3.4/scrcpy-server-v3.3.4
adb -s <DEVICE_SERIAL> push scrcpy-server-v3.3.4 /data/local/tmp/scrcpy-server-manual.jar
adb -s <DEVICE_SERIAL> forward tcp:1234 localabstract:scrcpy
adb -s <DEVICE_SERIAL> shell CLASSPATH=/data/local/tmp/scrcpy-server-manual.jar app_process / com.genymobile.scrcpy.Server 3.3.4 tunnel_forward=true audio=false control=false cleanup=false raw_stream=true max_size=1920
```
после этого на хосте на порту `1234` будет подготовлен сокет для трансляции экрана. Трансляция начнется после подключения к сокету и при наличии каких-либо изменений на экране, для тестов можно запустить секундомер на экране телефона чтобы иметь надежный источник изменений.

Для подключения к порту и записи экрана можно использовать ffmpeg `ffmpeg -i tcp://<HOST_IP>:1234 -f h264 -c:v copy ./test.mp4`
или воспользоваться скриптом [scrcpy_cv2.py](https://github.com/HappyClickClack/DeviceFarmModules/blob/main/screen_streem_capture/scrcpy_cv2.py).

При отключении от порта трансляция автоматически завершается и для повторного подключения нужно занво запускать scrcpy-server на устройстве.
