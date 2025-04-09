# 坪山麒麟舞
这是坪山麒麟舞项目

### 目录结构
- `docs/`:要写的markdown文档
- `site/`: 生成的静态网站
- `mkdocs.yml`: mkdocs配置文件
- `server.py`: 启动静态网站的python脚本
- `打包步骤.txt`: 把这个项目打包成静态网站的步骤

### 打包步骤
1. 安装打包python的脚本
`pip install pyinstaller`

2. 处理系统托盘图标的脚本
`pip install pystray pillow`

3. 执行`mkdocs build`命令，在根目录下生成一个site目录，里面存放静态文件

4. 网上找一个icon图片(.png)，存放到site目录里

5. 根目录编写server.py文件

6. 控制台运行下面的命令，将资源打包成exe
` pyinstaller --onefile --noconsole --add-data "site;site" --add-data "icon.png;." --name "MyDocs" server.py`

7. 根目录自动生成dist目录，双击MyDocs.exe就会启动服务器，系统右下角托盘会显示出图标

### 项目完成情况
- 大万的框架✅
- 其他三个地区的框架❌
- 打包成exe文件本地运行✅
- 网站背景图❌
- 动态效果（翻页等❌