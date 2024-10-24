
from dataclasses import dataclass
from fastapi import APIRouter, Request, status
from fastapi.responses import RedirectResponse
from pywebsite.config import html_templates

router = APIRouter(prefix="/resume", tags=["resume"])


@router.get("/")
def about(request: Request):
    context = {"request": request, "name": "Хуила"}
    return RedirectResponse(url="/resume/temp", status_code=status.HTTP_302_FOUND)


@router.get("/temp")
def about(request: Request):
    @dataclass
    class Job:
          company: str
          post: str
          start: str
          end: str
          desc: str

    @dataclass
    class Project:
        name: str
        version: str
        lang: str
        hashtags: list[str]
        gh_url: str | None
        tg_url: str | None
        site_url: str | None
        desc: str
        
        
    jobs = [

        # Job(
        #     company="Самокат",
        #     post="Курьер",
        #     start="Фев. 2022",
        #     end="Апр. 2023",
        #     desc="Доставка еды в короткие сроку заказчику"
        # ),

        Job(
            company="Gloria Jeans",
            post="Продавец part-timer",
            start="Апрель 2023",
            end="Сентябрь 2023",
            desc="Работа с кассовым терминалом, коммуникация с покупателями"
        ),
        Job(
            company="ПЭСК",
            post="Инженер-программист",
            start="Сентябрь 2023",
            end="Настоящее время",
            desc="Программирование и пусконаладка ПЛК, SCADA, HMI, работа с Modbus, OPC, Ethernet и т.д."
        )
    ]
    
    projects = [
        Project(
            name="Окей, Горный бот",
            version="2.0.0",
            lang="Python",
            hashtags=["временно_неактивный"],
            gh_url="https://github.com/karrless/og_bots",
            tg_url=None,
            site_url=None,
            desc=('Бот для группы ВК "Окей, Горный", '
                  'с помощью которого модераторы группы могли отвечать на вопросы первокурсников, '
                  'а также первокурсники могли найти своих соседей по комнате в общежитии')
        ),
        Project(
            name="АПМ-21 бот",
            version="2.1.0",
            lang="Python",
            hashtags=["активный"],
            gh_url=None,
            tg_url=None,
            site_url=None,
            desc="Телеграм бот для моей учебной группы АПМ-21, в котором есть расписание занятий, "
                 "оповещения о ближайших парах и различные inline-штучки."
        ),
        Project(
            name="Вентиляция горного бот",
            version="0.1.1",
            lang="Python",
            hashtags=["в_разработке"],
            gh_url="https://github.com/karrless/spmi_vent_tg_bot",
            tg_url=None,
            site_url=None,
            desc='Телеграм бот для оповещения персонала Горного университета об авариях '
                 'вентиляции различных корпусов 1 учебного центра, предоставление графиков различных параметров. '
                 'В данный момент находится в разработке.'
        ),
        Project(
            name="Хакатон цифрогаз",
            version="1.0.0",
            lang="Python",
            hashtags=["неактивный"],
            gh_url="https://github.com/karrless/digitalgaz",
            tg_url="tg://resolve?domain=oosd_spmu_bot",
            site_url="https://digitalgaz.karrless.ru",
            desc="Бэкенд для сайта и бот, с помощью которого можно считать данные с фотографии датчика расхода воды."
                 "Был выполнен в рамках хакатона Газпрома Цифрогаз-2024."
        ),
        Project(
            name="Этот сайт",
            version="0.1.1",
            lang="Python",
            hashtags=["в_разработке", "активный"],
            gh_url="https://github.com/karrless/pywebsite",
            site_url="https://karrless.ru",
            tg_url=None,
            desc="Персональный сайт-визитка, на котором вы находитесь. "
                 "На данный момент доступна только одна временная страница, в дальнейшем всё будет лучше и красивее"
        ),
    ]
    context = {"request": request, "jobs": jobs, "projects": projects, "title": "Резюме "}
    return html_templates.TemplateResponse(name="resume_temp.html", context=context)
