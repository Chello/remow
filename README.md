# remow
Choose dinamically what window to VNC directly from the remote host.


## The remote server needs:
    *screen* (```apt install screen```)
    *x11vnc* (```apt install x11vnc*```)

## The client needs:
    *pip* (apt install python3-pip)
    *remmina* (```apt install remmina```)

    ### Also needs following pip packages:
        *pexpect*, in particular *pxssh* (```pip3 install pexpect```)
        *configparser* (```pip3 install configparser```)
        *stormssh* (```pip3 install stormssh```), per aprire il file di configurazione di ssh
        *cerberus* (```pip3 install cerberus```), per validare gli oggetti
    
    For installing all pip packages need to run:
    ```pip3 install stormssh cerberus configparser pexpect```