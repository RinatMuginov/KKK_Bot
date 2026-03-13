from pydantic import BaseModel
from datetime import date
from typing import List
from aiogram.fsm.state import StatesGroup, State

class Cinema(BaseModel):
    id:int
    title:str
    year:int
    descr:str
    date_of_watch:date

class CinemaForm(StatesGroup):
    waiting_for_title = State()
    waiting_for_year = State()
    waiting_for_descr = State()
    waiting_for_date_of_watch = State()

class TwoWeeksCinema(BaseModel):
    id:int
    title:str
    date_of_start:date
    date_of_finish:date
    cinemas:List[Cinema]

class TwoWeeksCinemaForm(StatesGroup):
    waiting_for_title = State()
    waiting_for_date_of_start = State()
    waiting_for_date_of_finish = State()
    waiting_for_cinemas = State()
