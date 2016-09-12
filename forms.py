from django import forms
from .models import GroupInfo

class GroupInfoForm(forms.ModelForm):

	class Meta:
		model = GroupInfo
		fields = ('first_name', 'last_name', 'group_name','class_name',)

class GroupInfoDeleteForm(forms.ModelForm):

	class Meta:
		model = GroupInfo
		fields = ('last_name',)