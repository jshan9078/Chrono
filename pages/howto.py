
from taipy.gui import Gui, Markdown


title="Chrono"
step1 = "1. Upload a screenshot of all your schedules on the 'Upload' Page."
step2 = "2. Download the CSV file that contains your events from the 'Tasks' Page"
step3 = "3. Head over to Google Calendar and hit the gear icon and then 'settings'."
step4 = "4. On the left navbar, select 'import and export'"
step5 = "5. Upload your CSV file and select the right calendar. Then, hit 'Import'."
step6= "6. Now you can get back to work!"

# Definition of the page
howto_page = Markdown("""
<|{title}|id=title|>
## Uploading to Google calendar

<|{step1}|text|id=step|>
                      
<|{step2}|text|id=step|>
                      
<|{step3}|text|id=step|>
                      
<|{step4}|text|id=step|>
                      
<|{step5}|text|id=step|> 
                      
<|{step6}|text|id=step|> 

""")



#Gui(page).run()
