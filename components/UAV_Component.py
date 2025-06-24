import pandas as pd

# Use the absolute path
df = pd.read_excel(r"c:\Users\Manan\Desktop\TRY AYTHING\Avi-ai\components\UAV_Component.xlsx")

markdown = df.to_markdown(index=False)
print(markdown)