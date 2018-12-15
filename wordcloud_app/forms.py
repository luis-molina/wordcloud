from django import forms

class TextForm(forms.Form):
    input_text = forms.CharField(label='Input the text to process:')
    max_words = forms.IntegerField(label='Max words wanted',min_value=1)
    language = forms.ChoiceField(label='Language',choices=(("danish","Danish"),("dutch","Dutch"),("english","English"),("finnish","Finnish"),("french","French"),("german","German"),("hungarian","Hungarian"),("italian","Italian"),("norwegian","Norwegian"),("portuguese","Portuguese"),("russian","Russian"),("spanish","Spanish"),("swedish","Swedish"),("turkish","Turkish")))
    custom_stopwords_text = forms.CharField(label='Input extra stopwords you want to consider (one per line):',required=False)