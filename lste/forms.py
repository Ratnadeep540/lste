from string import Template
from django.utils.safestring import mark_safe
from django.forms import ImageField

class PictureWidget(forms.widgets.Widget):
    def render(self, name, value, attrs=None, **kwargs):
        html =  Template("""<img src="https://firebasestorage.googleapis.com/v0/b/health-report-334d5.appspot.com/o/Images%2Fone.png?alt=media&token=25e2a26b-bcdc-4afb-a3e3-22368abdba13"/>""")
        return mark_safe(html.substitute(link=value))

class UserProfileForm(forms.ModelForm):
    photo = ImageField(widget=PictureWidget)
    