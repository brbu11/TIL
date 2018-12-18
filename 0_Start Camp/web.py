import webbrowser


keywords = [
    "Mando",
    "water",
    "상반기반도체"
]

for i in keywords:
    url = 'https://www.google.com/search?q=' + i
    webbrowser.open_new(url)
