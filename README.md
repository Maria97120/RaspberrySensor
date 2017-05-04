# RaspberryEX
温度传感器型号：DHT11    channel-->7 3.3v
人体传感器：            channel-->12 3.3v
烟雾探测传感器:MQ-2      channel-->18 3v~5v OD接口
雨滴传感器：MH-RD        channel-->16 0~5v OD接口
pcf8591:AD模拟量转换     channel-->3(SDA)  channel-->5(SCL) 5v 


docker运行命令: docker run -p 8000:8000 --device /dev/mem:/dev/mem --privileged name:tap /bin/bash
