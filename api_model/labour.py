from pydantic import BaseModel
from typing import Union
class DefaultTemplete(BaseModel):
    product_list:Union[list,None]=None  # 产品列表
    labour_categories:list