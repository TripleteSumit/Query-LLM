import os
from embedchain import App

from django.conf import settings


class Gen:
    os.environ["GOOGLE_API_KEY"] = settings.API_KEY
    app = App.from_config(settings.CONFIG_FILE)
    sources = ['https://techyshim.com/is-fampay-safe/', 'https://www.famapp.in/',
               'https://blog.famapp.in/blog/curious-about-famcard-heres-everything-to-know/', 'https://blog.famapp.in/blog/fampays-guide-to-digital-payments-for-teens-important-dos-and-donts/', 'https://www.triotech.co.in/privacy/', 'https://www.triotech.co.in/terms/', 'https://www.quora.com/What-is-Fampay-How-does-it-work', 'https://thebusinessrule.com/what-is-fampay-how-does-it-make-money-business-model-explained/']

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
