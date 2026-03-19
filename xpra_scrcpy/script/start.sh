# !/bin/sh
# root on 8080
xpra start --start-child-on-connect=xterm \
           --bind-tcp=0.0.0.0:8080 \
           --html=on 

# user on port 8081, password 123
xpra start --start-child-on-connect="lxterminal -e bash" -d auth \
           --sharing=yes --lock=no \
           --bind-tcp=0.0.0.0:8081,auth=password,value=123 \
           --html=on --bandwidth-limit=1Mbps --exit-with-children=no --idle-timeout=600 --uid=1001 --gid=1001 \
           --clipboard=yes --clipboard-direction=both 

# scrcpy on port 8082, password 123
xpra start --start-child-on-connect="xterm -hold -e scrcpy -s <DEVICE_SERIAL> --tunnel-host=172.17.0.1 --no-audio" -d auth \
           --sharing=yes --lock=no \
           --bind-tcp=0.0.0.0:8082,auth=password,value=123 \
           --html=on --bandwidth-limit=1Mbps --exit-with-children=no --idle-timeout=600 --uid=1001 --gid=1001 \
           --clipboard=yes --clipboard-direction=both 

tail -f /dev/null
