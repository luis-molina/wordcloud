from django.shortcuts import render
from django.http import HttpResponse
from .forms import TextForm
from .controllers.freq_dist_calc import calculateAndGenerateCloud

default_input_text = "What is Lorem Ipsum?\n\nLorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\n\nWhy do we use it?\n\nIt is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like)."
default_max_words = 50
default_language = "english"
default_custom_stopwords_text = ""
all_languages = (("danish","Danish"),("dutch","Dutch"),("english","English"),("finnish","Finnish"),("french","French"),("german","German"),("hungarian","Hungarian"),("italian","Italian"),("norwegian","Norwegian"),("portuguese","Portuguese"),("russian","Russian"),("spanish","Spanish"),("swedish","Swedish"),("turkish","Turkish"))

def homePageView(request):
    # if the request method is POST
    if request.method == "POST":
        # load the request values in the Form object
        form = TextForm(request.POST)

        #if the form is valid
        if form.is_valid():
            # generate the cloud with the attributes obtained from the form
            calculateAndGenerateCloud(form.cleaned_data['input_text'],form.cleaned_data['max_words'],form.cleaned_data['language'],form.cleaned_data['custom_stopwords_text'])
            # show the page with the values previously submitted in the form
            return render(request, 'home.html',{"input_text":form.cleaned_data['input_text'],"max_words":form.cleaned_data['max_words'],"all_languages":all_languages,"language":form.cleaned_data['language'],"custom_stopwords_text":form.cleaned_data['custom_stopwords_text']})
        else:
            return HttpResponse('Invalid')
    else:
        # generate the cloud with the default attributes
        calculateAndGenerateCloud(default_input_text,default_max_words,default_language,default_custom_stopwords_text)
        # show the page with the default form values
        return render(request, 'home.html',{"input_text":default_input_text,"max_words":default_max_words,"all_languages":all_languages,"language":default_language,"custom_stopwords_text":default_custom_stopwords_text})
