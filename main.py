from urllib import request


MAX_PAGE = 26
page_number = 1

while (page_number <= MAX_PAGE):
    request.urlretrieve(
        f"http://diss.natlib.uz/ResearchWork/GetPageN?id=47759&fileName=&pageNumber={page_number}",
        f"downloads/{page_number}.pdf"
    )
    page_number += 1
