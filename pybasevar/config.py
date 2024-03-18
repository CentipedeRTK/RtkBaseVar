import serial
import io
from decimal import *
## 00-START socat TODO
socat="socat -d -d pty,raw,echo=0 pty,raw,echo=0 &>/dev/null"
## 01-Start caster
# "mount point name or identifier; signal format (RTCM); signal details (list of rtcm messages); carrier phase information ; nav system (GPS+GLO+ ...);network name;country;latitude;longitude;require nmea;solution type (base, network); stream generator; compression algorithm; authentification; fee; bitrate,miscellaneous info
ntripc="str2str -in serial://pts/2:115200:8:n:1:off -n 1 -b 1 -out ntripc://@:9999/ME:ME;RTCM3;;2;GPS+GLO+GAL+BDS+QZS;NONE;NONE;;;1;0;RTKBaseVar;NONE;N;N;100;  &>/dev/null"
## 02-Start a generic stream RTCM3 in
stream1="str2str -in ntrip://:@caster.centipede.fr:80/"
stream2=" -out serial://pts/1:115200:8:n:1:off &>/dev/null"
## 1-Analyse nmea from gnss ntripclient for get lon lat
ser = serial.Serial('/dev/pts/1', 115200, timeout=1)
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))
