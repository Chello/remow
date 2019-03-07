# remow
Choose dinamically what window to VNC directly from the remote host.


## The remote server needs:

    *ssh server* (```apt install openssh-server```)
    *x11vnc* (```apt install x11vnc*```)
    *screen*
    *wmctrl* (```apt install wmctrl```)
    
    For installing all packages need to run:
    ```apt install openssh-server x11vnc* wmctrl```

## The client needs:

    *pip* (apt install python3-pip)
    *remmina* (```apt install remmina```)

    ### Also needs following pip packages:
        *pexpect*, in particular *pxssh* (```pip3 install pexpect```)
        *configparser* (```pip3 install configparser```)
        *stormssh* (```pip3 install stormssh```)
        *cerberus* (```pip3 install cerberus```), for validating objects configurations
	*sshconf* (```pip3 install sshconf```), used for read ssh configurations
    
    For installing all pip packages need to run:
    ```pip3 install stormssh cerberus configparser pexpect sshconf```
