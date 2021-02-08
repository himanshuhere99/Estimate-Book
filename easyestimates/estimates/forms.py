from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
    	model = User
    	fields = ["username", "email", "password1", "password2"]

class AddItemForm(ModelForm):
    class Meta:
        model = models.Item
        fields = ["Item Name", "Item Code", "Unit", "MRP", "Rate"]

# class EstimateForm(ModelForm):
#     privately_share_with = forms.CharField(widget=forms.Textarea, required=False, max_length=1000,
#                                            validators=[validate_shared_email])
#     co_authors = forms.CharField(widget=forms.Textarea, required=False, max_length=500,
#                                  validators=[validate_shared_email])
#     tags = forms.CharField(widget=forms.Textarea, required=True, max_length=150)
#
#     def clean(self):
#         super(IdeaForm, self).clean()
#         if self.data.get('is_private'):
#             if is_empty(self.data.get('privately_share_with'), raise_exception=False):
#                 self.add_error('privately_share_with', "Required field cannot be empty")
#             else:
#                 if not is_empty(self.data.get('co_authors'), raise_exception=False):
#                     co_authors = set(self.data.get('co_authors').split(','))
#                     privately_shared = set(self.data.get('privately_share_with').split(','))
#                     common_users = co_authors.intersection(privately_shared)
#                     if common_users:
#                         common_users = ', '.join(common_users)
#                         msg = f"Cannot Privately share Idea with Co-Authors: {common_users}"
#                         self.add_error('privately_share_with', msg)
#
#     class Meta:
#         model = models.Item
#         fields = ["Item", "MRP", "Rate", "Quantity", "Amount"]
