from django import forms

CHOICES= (
('1','Used Cars'),
('2','Rentals')
)

class PostForm(forms.Form):
    category = forms.CharField(label='Category',widget=forms.Select(choices=CHOICES))   
    post_title = forms.CharField(label='Title',max_length=100)
    post_text = forms.CharField(label='Description',widget=forms.Textarea,max_length=1000)
    post_price = forms.IntegerField(label='Price')
    post_contact = forms.EmailField(label='Contact Information',max_length=100,help_text='A valid email address, please.')
    post_owner = forms.CharField(label='Contact Name',max_length=100)
