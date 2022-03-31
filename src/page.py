from junegrape.webpage import WebPage

url = "https://www.instagram.com/explore/tags/%EB%8B%A4%EB%8F%85%EC%9D%B4%EC%B1%8C%EB%A6%B0%EC%A7%80/?hl=ko"

elements = {
    "test": ".v1Nh3"
}

instagram = WebPage("instagram", url, elements)
