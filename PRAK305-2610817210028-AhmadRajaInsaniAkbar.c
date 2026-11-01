#include<stdio.h>

int main(){

    int hari, jam, menit, detik, n;
    scanf("%d",&n);

    hari  = n / 86400;
    jam   = (n % 86400) / 3600;
    menit = (n % 3600) / 60;
    detik = n % 60;
    if(n<=86400) {
        printf("%02d:%02d:%02d", jam, menit, detik);
    } else if(n>86400) {
        printf("%d hari %02d:%02d:%02d", hari, jam, menit, detik);
    }
    return 0;



    }



