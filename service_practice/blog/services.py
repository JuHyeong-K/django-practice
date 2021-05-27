from .models import Article, Category
from dataclasses import dataclass


@dataclass
class EditDto():
    article_pk: int
    title: str
    content: str

ERROR_MSG = {
    'EXIST_ID': 'EXIST_ID',
    'MISSING_INPUT': 'MISSING_INPUT',
    'PASSWORD_CHECK': 'PASSWORD_CHECK',
    'NOT_EXIST_ID': 'NOT_EXIST_ID',
    'PW_CHECK': 'PW_CHECK',
}

class BlogService():
    def edit(dto: EditDto):
        if (not dto.title or not dto.content):
            return {'error': {'state': True, 'msg': ERROR_MSG['MISSING_INPUT']}}
        
        article = Article.objects.filter(pk=dto.article_pk).update(
            topic=dto.title,
            content=dto.content
        )
        return {'error': {'state': False}, 'article': article}