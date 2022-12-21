

# Get h1 tag from the website
def get_h1_tag(data: str) -> str:
    return data.split("<h1>")[1].split("</h1>")[0]



