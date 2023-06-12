from django import forms
from pybo.models import Question, Answer


class QuestionForm(forms.ModelForm):
    image = forms.ImageField(required=False)  # 이미지 필드 추가

    class Meta:
        model = Question
        fields = ['subject', 'content', 'image']
        labels = {
            'subject': '제목',
            'content': '내용',
            'image': '이미지',  # 이미지 필드 레이블
        }


class AnswerForm(forms.ModelForm):
    image = forms.ImageField(required=False)  # 이미지 필드 추가

    class Meta:
        model = Answer
        fields = ['content', 'image']
        labels = {
            'content': '답변내용',
            'image': '이미지',  # 이미지 필드 레이블
        }

