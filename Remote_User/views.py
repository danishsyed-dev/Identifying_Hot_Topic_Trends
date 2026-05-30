from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
import joblib
import os

from django.conf import settings as django_settings
from Remote_User.models import ClientRegister_Model, predict_hot_topic


def login(request):
    if request.method == "POST" and 'submit1' in request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        enter = ClientRegister_Model.objects.filter(username=username).first()
        if enter and check_password(password, enter.password):
            request.session["userid"] = enter.id
            return redirect('ViewYourProfile')

    return render(request, 'RUser/login.html')


def Register1(request):
    if request.method == "POST":
        username = request.POST.get('username')
        # Prevent duplicate usernames
        if ClientRegister_Model.objects.filter(username=username).exists():
            return render(request, 'RUser/Register1.html', {'error': 'Username already exists!'})
        email = request.POST.get('email')
        password = make_password(request.POST.get('password'))
        phoneno = request.POST.get('phoneno')
        country = request.POST.get('country')
        state = request.POST.get('state')
        city = request.POST.get('city')
        ClientRegister_Model.objects.create(
            username=username, email=email, password=password,
            phoneno=phoneno, country=country, state=state, city=city
        )
        return render(request, 'RUser/Register1.html', {'success': 'Registration successful! Please login.'})
    return render(request, 'RUser/Register1.html')


def ViewYourProfile(request):
    userid = request.session.get('userid')
    if not userid:
        return redirect('login')
    obj = ClientRegister_Model.objects.get(id=userid)
    return render(request, 'RUser/ViewYourProfile.html', {'object': obj})


def Predict_Identifying_Hot_Topic_Trends(request):
    userid = request.session.get('userid')
    if not userid:
        return redirect('login')

    if request.method == "POST":
        Sno = request.POST.get('Sno')
        PDate = request.POST.get('PDate')
        Headline = request.POST.get('Headline')
        Description = request.POST.get('Description')
        Source = request.POST.get('Source')

        # Load pre-trained models instead of retraining every request
        model_dir = os.path.join(django_settings.BASE_DIR, 'trained_models')
        vectorizer_path = os.path.join(model_dir, 'vectorizer.joblib')
        classifier_path = os.path.join(model_dir, 'classifier.joblib')

        if not os.path.exists(vectorizer_path) or not os.path.exists(classifier_path):
            return render(request, 'RUser/Predict_Identifying_Hot_Topic_Trends.html',
                          {'objs': 'Error: Models not trained yet. Ask admin to train models first.'})

        cv = joblib.load(vectorizer_path)
        classifier = joblib.load(classifier_path)

        # Transform input and predict
        vector1 = cv.transform([Description]).toarray()
        predict_text = classifier.predict(vector1)
        prediction = int(predict_text[0])

        if prediction == 0:
            val = 'Normal Topic'
        elif prediction == 1:
            val = 'Hot Topic'
        else:
            val = 'Unknown'

        predict_hot_topic.objects.create(
            Sno=Sno, PDate=PDate, Headline=Headline,
            Description=Description, Source=Source, Prediction=val
        )

        return render(request, 'RUser/Predict_Identifying_Hot_Topic_Trends.html', {'objs': val})

    return render(request, 'RUser/Predict_Identifying_Hot_Topic_Trends.html')
