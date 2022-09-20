import fastapi
from deta import Base, Drive
from fastapi.templating import Jinja2Templates

pages = Jinja2Templates(directory="pages")
files = Drive("files")
base = Base("stats")
todo = Base("homework")
app = fastapi.FastAPI()

# HTML


@app.get("/", response_class=fastapi.responses.HTMLResponse)
async def home(request: fastapi.Request):
    return pages.TemplateResponse("links.html", {"request": request})
