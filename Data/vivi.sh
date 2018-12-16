for (( i=0; ;i++ ))
do
    adb -s UONJUS7S99999999  shell am start -n ufovpn.free.unblock.proxy.vpn/ufovpn.free.unblock.proxy.vpn.home.ui.WelcomeActivity
	sleep $(expr $[RANDOM%20+1])
    adb -s UONJUS7S99999999  shell input tap 520 830
    sleep $(expr $[RANDOM%90+20])
    adb -s UONJUS7S99999999  shell input tap 520 830
    sleep $(expr $[RANDOM%20+1])
    adb -s UONJUS7S99999999  shell am force-stop ufovpn.free.unblock.proxy.vpn
    sleep $(expr $[RANDOM%20+1])
    echo $i
done
