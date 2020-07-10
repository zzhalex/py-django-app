from django import forms


class PostForm(forms.Form):
    category = forms.CharField()
    post_text = forms.CharField(max_length=1000)
    post_title = forms.CharField(max_length=100)
    post_price = forms.CharField()
    post_contact = forms.CharField(max_length=100)
    post_owner = forms.CharField(max_length=100)
