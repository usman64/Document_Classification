import pytesseract
import re
from PIL import Image

alltext = pytesseract.image_to_string(Image.open("test1.jpg"),lang="eng")
# alltext = [alltext]
print(alltext)
# (?# PATTERN = r"\w+")
# x=re.findall(PATTERN, alltext)
# print(alltext)
# print(x)