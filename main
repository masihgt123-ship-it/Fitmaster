import os

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.utils import platform


class FitMasterApp(App):
    def build(self):
        Clock.schedule_once(self.open_page, 0)
        return Widget()

    def open_page(self, *args):
        if platform != "android":
            print("این فایل برای اجرا روی اندروید است.")
            return

        from android.runnable import run_on_ui_thread
        from jnius import autoclass

        WebView = autoclass("android.webkit.WebView")
        WebViewClient = autoclass("android.webkit.WebViewClient")
        PythonActivity = autoclass("org.kivy.android.PythonActivity")
        activity = PythonActivity.mActivity

        base = os.path.dirname(os.path.abspath(__file__))
        html_path = os.path.join(base, "index.html")
        with open(html_path, "r", encoding="utf-8") as f:
            html = f.read()

        @run_on_ui_thread
        def start():
            web = WebView(activity)
            settings = web.getSettings()
            settings.setJavaScriptEnabled(True)
            settings.setDomStorageEnabled(True)
            settings.setAllowFileAccess(True)
            settings.setAllowContentAccess(True)
            try:
                settings.setAllowFileAccessFromFileURLs(True)
                settings.setAllowUniversalAccessFromFileURLs(True)
            except Exception:
                pass
            web.setWebViewClient(WebViewClient())
            activity.setContentView(web)
            web.loadDataWithBaseURL(
                "file://" + base + "/",
                html,
                "text/html",
                "utf-8",
                None,
            )

        start()


if __name__ == "__main__":
    FitMasterApp().run()
