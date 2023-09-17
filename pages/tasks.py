from taipy.gui import Gui, Markdown
import pandas as pd

data = pd.read_csv('placeholder.csv')

download='./assignments.csv'

# Definition of the page
tasks_page = Markdown("""
## Your Tasks
<|Refresh|button|on_action=update_assignments|><|{download}|file_download|label=Download CSV|name=assignments.csv|>
<|{data}|table|page_size=10|filter=true|>

""")

def update_assignments(state):
    state.data=pd.read_csv('assignments.csv')

#Gui(page).run()
