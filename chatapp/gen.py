import os
from embedchain import App

from django.conf import settings


class Gen:
    os.environ["GOOGLE_API_KEY"] = settings.API_KEY
    app = App.from_config(settings.CONFIG_FILE)
    sources = ['https://techyshim.com/is-fampay-safe/', 'https://www.famapp.in/',
               'https://blog.famapp.in/blog/curious-about-famcard-heres-everything-to-know/', 'https://blog.famapp.in/blog/fampays-guide-to-digital-payments-for-teens-important-dos-and-donts/', 'https://tallwinlife.co.in/fampay-is-real-or-fake/#:~:text=Steps%20to%20create%20a%20FamPay%20account%3A%201%20Download,conditions.%207%20Your%20FamPay%20account%20is%20now%20created%21']

    def input_knowledge(self):
        for s in self.sources:
            self.app.add(s)

    def query(self, query: str):
        if not query:
            return "Query must Not be Empty!"
        response = self.app.query(query)
        return response

    def get_sources(self) -> list:
        return self.sources
