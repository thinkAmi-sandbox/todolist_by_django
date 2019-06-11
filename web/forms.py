from django.forms import ModelForm, ValidationError
from web.models import ToDo


class ToDoModelForm(ModelForm):

    def clean_title(self):
        title = self.cleaned_data['title']
        if title.upper() != title:
            raise ValidationError('タイトルの英字は、すべて大文字にしてください')
        return title

    class Meta:
        model = ToDo
        fields = ('title', 'content', 'priority')
