from taipy.gui import Gui
from pages.howto import howto_page
from pages.upload import upload_page
from pages.tasks import tasks_page

pages = {
 "/": "<center><|navbar|></center>",
"upload": upload_page,
"usage": howto_page,
 "tasks":tasks_page,
}

Gui(pages=pages).run()
