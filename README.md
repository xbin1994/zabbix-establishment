Zabbix的安装都可按照官方文档的步骤进行。此处使用的是Zabbix-Server-with-Mysql版本。

[官方文档地址](https://www.zabbix.com/documentation/3.2/manual/installation/install_from_packages)

PS:可选包安装或者docker安装，配置方法类似。

# zabbix环境配置


![zabbix](https://raw.githubusercontent.com/xbin1994/zabbix-establishment/master/images/zabbix.png)  


#### **基础配置**  


Zabbix需要将数据存进数据库中，因此需要在/etc/zabbix/zabbix_server.conf中设置
  
DBHost(数据库地址),
  
DBUser(数据库用户名),
  
DBPassword(数据库密码)。

httpd配置也需要修改ServerName字段为localhost:80

另：如果服务器上安装并开启了zabbix-agent且提示agent开启失败，就需要修改/etc/zabbix/web/zabbix.conf.php文件中的$ZBX_SERVER字段，从localhost改为服务器的IP地址。



#### **汉化配置**

因为zabbix官方的中文包是有bug的，后台一半以上的显示都是方块，所以需要替换掉zabbix自带的字体包。步骤如下：  

1. 打开window系统中的C:/Windows/Fonts文件夹  
   ![windows-font](https://raw.githubusercontent.com/xbin1994/zabbix-establishment/master/images/windows-font.png)

2. 拷贝文件夹下的'微软雅黑:常规'字体到zabbix服务器下的/usr/share/zabbix/fonts文件夹中，并改名为'msyh.ttf'。  

3. 修改/usr/share/zabbix/include文件夹下的define.inc.php文件,将‘ZBX_GRAPH_FONT_NAME’字段对应的值改为msyh, 然后重启zabbix即可。  
 
       ![font-config](https://raw.githubusercontent.com/xbin1994/zabbix-establishment/master/images/font-config.png)  

4. 在浏览器中输入zabbix服务器的ip/zabbix即可进入zabbix仪表板!  

       ![zabbix-dashboard](https://raw.githubusercontent.com/xbin1994/zabbix-establishment/master/images/dashborad.png)