from django import forms
from .models import Comment
from .models import Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'comment_desc']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['comment_desc'].label = "Comment"


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs['autofocus'] = True

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0'
