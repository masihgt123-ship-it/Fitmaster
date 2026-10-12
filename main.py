import os
from pathlib import Path

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.utils import platform


class FitMasterApp(App):
    def build(self):
        self.title = "FitMaster Pro"

        if platform != "android":
            return Label(text="این برنامه برای اجرا روی اندروید ساخته شده است.")

        self.html_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "index.html",
        )

        if not os.path.isfile(self.html_path):
            return Label(
                text="فایل index.html پیدا نشد.\n"
                     "آن را کنار main.py قرار بده.",
                halign="center",
            )

        Clock.schedule_once(self.open_page, 0)
        return Widget()

    def open_page(self, *args):
        from android.runnable import run_on_ui_thread
        from jnius import autoclass

        WebView = autoclass("android.webkit.WebView")
        WebViewClient = autoclass("android.webkit.WebViewClient")
        PythonActivity = autoclass("org.kivy.android.PythonActivity")
        activity = PythonActivity.mActivity
        page_url = Path(self.html_path).as_uri()

        @run_on_ui_thread
        def start():
            web = WebView(activity)
            settings = web.getSettings()

            settings.setJavaScriptEnabled(True)
            settings.setDomStorageEnabled(True)
            settings.setAllowFileAccess(True)

            web.setWebViewClient(WebViewClient())
            activity.setContentView(web)
            web.loadUrl(page_url)

            self.web_view = web

        start()


if __name__ == "__main__":
    FitMasterApp().run()
