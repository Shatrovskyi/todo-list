from django import forms
from todo.models import Task


class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            "datetime_field": forms.DateTimeInput(format="%m.%d.%Y %H:%M"),
        }
