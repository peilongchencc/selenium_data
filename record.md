# selenium

selenium爬取数据。<br>

安装selenium:

```bash
pip install selenium
```

安装无头版Chrome，即没有界面的Chrome。<br>

```bash
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb
```

安装位置默认为:<br>

```txt
update-alternatives: using /usr/bin/google-chrome-stable to provide /usr/bin/x-www-browser (x-www-browser) in auto mode
update-alternatives: using /usr/bin/google-chrome-stable to provide /usr/bin/gnome-www-browser (gnome-www-browser) in auto mode
update-alternatives: using /usr/bin/google-chrome-stable to provide /usr/bin/google-chrome (google-chrome) in auto mode
```

如果Chrome安装成功，使用以下指令查看Chrome版本:<br>

```bash
google-chrome --version
```

笔者终端显示:<br>

```txt
Google Chrome 120.0.6099.199 
```

使用`webdriver_manager`确保自动下载匹配的Chrome驱动:<br>

```bash
pip install webdriver_manager
```