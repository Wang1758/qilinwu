import os
import sys
import webbrowser
import threading
import logging
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
import pystray
from PIL import Image

# 配置日志
logging.basicConfig(
    filename='server.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class CustomHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.base_path = os.path.join(
            sys._MEIPASS if getattr(sys, 'frozen', False) else os.path.dirname(os.path.abspath(__file__)),
            "site"
        )
        super().__init__(*args, directory=self.base_path, **kwargs)

    def log_message(self, format, *args):
        # 记录请求日志
        logging.info("%s - - [%s] %s" % (self.address_string(), self.log_date_time_string(), format % args))

def start_server():
    # 启动 HTTP 服务器
    try:
        # 获取资源路径
        if getattr(sys, 'frozen', False):
            base_dir = sys._MEIPASS
        else:
            base_dir = os.path.dirname(os.path.abspath(__file__))

        # 切换到静态文件目录
        site_dir = os.path.join(base_dir, "site")
        os.chdir(site_dir)

        # 启动服务器
        with TCPServer(("", 8000), CustomHandler) as httpd:
            logging.info("=" * 50)
            logging.info("服务器已启动: http://localhost:8000")
            logging.info("=" * 50)
            logging.info("工作目录: %s", os.getcwd())
            webbrowser.open("http://localhost:8000")
            httpd.serve_forever()


    except Exception as e:
        logging.error("服务器错误: %s", str(e), exc_info=True)

def create_tray_icon():
    # 动态获取图标路径
    if getattr(sys, 'frozen', False):
        base_dir = sys._MEIPASS
    else:
        base_dir = os.path.dirname(os.path.abspath(__file__))

    icon_path = os.path.join(base_dir, "icon.png")
    # 创建系统托盘图标
    image = Image.open(icon_path) if os.path.exists("icon.png") else Image.new('RGB', (64, 64), (255, 255, 255))
    menu = pystray.Menu(
        pystray.MenuItem("打开浏览器", lambda: webbrowser.open("http://localhost:8000")),
        pystray.MenuItem("退出", lambda: os._exit(0))
    )
    icon = pystray.Icon("MyDocs", image, "文档服务器", menu)
    icon.run()

if __name__ == "__main__":
    # 启动服务器线程
    server_thread = threading.Thread(target=start_server, daemon=True)
    server_thread.start()

    # 显示托盘图标
    create_tray_icon()
