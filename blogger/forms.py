from django import forms 
class CommentForm(forms.Form):
    authour=forms.CharField(
        
        max_length=60,
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'your name'
        })
    )
    body=forms.CharField(widget=forms.Textarea(attrs={
        'class':'form-control',
        'placeholder':'Leave a comment'
    })
    )