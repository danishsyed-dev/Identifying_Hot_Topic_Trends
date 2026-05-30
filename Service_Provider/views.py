import os

import numpy as np
import pandas as pd
import xlwt
import joblib
from django.db.models import Count, Avg, Q
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings as django_settings

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn import svm
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier, VotingClassifier

from Remote_User.models import ClientRegister_Model, predict_hot_topic, detection_ratio, detection_accuracy


def serviceproviderlogin(request):
    if request.method == "POST":
        admin = request.POST.get('username')
        password = request.POST.get('password')
        if admin == django_settings.ADMIN_USERNAME and password == django_settings.ADMIN_PASSWORD:
            request.session['is_admin'] = True
            detection_accuracy.objects.all().delete()
            return redirect('View_Remote_Users')

    return render(request, 'SProvider/serviceproviderlogin.html')


def _check_admin(request):
    """Check if the current session is an authenticated admin."""
    return request.session.get('is_admin', False)


def View_Predicted_Identifying_Hot_Topic_Trends_Ratio(request):
    if not _check_admin(request):
        return redirect('serviceproviderlogin')

    detection_ratio.objects.all().delete()

    kword = 'Hot Topic'
    obj = predict_hot_topic.objects.filter(Prediction=kword)
    obj_all = predict_hot_topic.objects.all()
    count = obj.count()
    count_all = obj_all.count()
    if count_all > 0:
        ratio = (count / count_all) * 100
        if ratio != 0:
            detection_ratio.objects.create(names=kword, ratio=ratio)

    kword1 = 'Normal Topic'
    obj1 = predict_hot_topic.objects.filter(Prediction=kword1)
    count1 = obj1.count()
    if count_all > 0:
        ratio1 = (count1 / count_all) * 100
        if ratio1 != 0:
            detection_ratio.objects.create(names=kword1, ratio=ratio1)

    obj = detection_ratio.objects.all()
    return render(request, 'SProvider/View_Predicted_Identifying_Hot_Topic_Trends_Ratio.html', {'objs': obj})


def View_Remote_Users(request):
    if not _check_admin(request):
        return redirect('serviceproviderlogin')
    obj = ClientRegister_Model.objects.all()
    return render(request, 'SProvider/View_Remote_Users.html', {'objects': obj})


def charts(request, chart_type):
    if not _check_admin(request):
        return redirect('serviceproviderlogin')
    chart1 = detection_ratio.objects.values('names').annotate(dcount=Avg('ratio'))
    return render(request, "SProvider/charts.html", {'form': chart1, 'chart_type': chart_type})


def charts1(request, chart_type):
    if not _check_admin(request):
        return redirect('serviceproviderlogin')
    chart1 = detection_accuracy.objects.values('names').annotate(dcount=Avg('ratio'))
    return render(request, "SProvider/charts1.html", {'form': chart1, 'chart_type': chart_type})


def View_Predicted_Identifying_Hot_Topic_Trends(request):
    if not _check_admin(request):
        return redirect('serviceproviderlogin')
    obj = predict_hot_topic.objects.all()
    return render(request, 'SProvider/View_Predicted_Identifying_Hot_Topic_Trends.html', {'list_objects': obj})


def likeschart(request, like_chart):
    if not _check_admin(request):
        return redirect('serviceproviderlogin')
    charts = detection_accuracy.objects.values('names').annotate(dcount=Avg('ratio'))
    return render(request, "SProvider/likeschart.html", {'form': charts, 'like_chart': like_chart})


def Download_Trained_DataSets(request):
    if not _check_admin(request):
        return redirect('serviceproviderlogin')

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Predicted_Data.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet("sheet1")
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    obj = predict_hot_topic.objects.all()
    for my_row in obj:
        row_num = row_num + 1
        ws.write(row_num, 0, my_row.Sno, font_style)
        ws.write(row_num, 1, my_row.PDate, font_style)
        ws.write(row_num, 2, my_row.Headline, font_style)
        ws.write(row_num, 3, my_row.Description, font_style)
        ws.write(row_num, 4, my_row.Source, font_style)
        ws.write(row_num, 5, my_row.Prediction, font_style)

    wb.save(response)
    return response


def train_model(request):
    if not _check_admin(request):
        return redirect('serviceproviderlogin')

    detection_accuracy.objects.all().delete()

    dataset_path = os.path.join(django_settings.BASE_DIR, 'Datasets.csv')
    data = pd.read_csv(dataset_path, encoding='latin-1')

    x = data['Description']
    y = data['Label']

    cv = CountVectorizer()
    x = cv.fit_transform(x)

    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=42)

    # 1. Naive Bayes
    NB = MultinomialNB()
    NB.fit(X_train, y_train)
    predict_nb = NB.predict(X_test)
    naivebayes = accuracy_score(y_test, predict_nb) * 100
    detection_accuracy.objects.create(names="Naive Bayes", ratio=naivebayes)

    # 2. SVM
    lin_clf = svm.LinearSVC()
    lin_clf.fit(X_train, y_train)
    predict_svm = lin_clf.predict(X_test)
    svm_acc = accuracy_score(y_test, predict_svm) * 100
    detection_accuracy.objects.create(names="SVM", ratio=svm_acc)

    # 3. Logistic Regression
    reg = LogisticRegression(random_state=0, solver='lbfgs').fit(X_train, y_train)
    y_pred_lr = reg.predict(X_test)
    lr_acc = accuracy_score(y_test, y_pred_lr) * 100
    detection_accuracy.objects.create(names="Logistic Regression", ratio=lr_acc)

    # 4. Decision Tree
    dtc = DecisionTreeClassifier()
    dtc.fit(X_train, y_train)
    dtcpredict = dtc.predict(X_test)
    dtc_acc = accuracy_score(y_test, dtcpredict) * 100
    detection_accuracy.objects.create(names="Decision Tree Classifier", ratio=dtc_acc)

    # 5. Gradient Boosting
    clf = GradientBoostingClassifier(n_estimators=100, learning_rate=1.0, max_depth=1, random_state=0)
    clf.fit(X_train, y_train)
    clfpredict = clf.predict(X_test)
    gb_acc = accuracy_score(y_test, clfpredict) * 100
    detection_accuracy.objects.create(names="Gradient Boosting", ratio=gb_acc)

    # Build ensemble VotingClassifier with all 5 models and persist
    models_list = [
        ('naive_bayes', NB),
        ('svm', lin_clf),
        ('logistic', reg),
        ('decision_tree', dtc),
        ('gradient_boosting', clf),
    ]
    classifier = VotingClassifier(estimators=models_list, voting='hard')
    classifier.fit(X_train, y_train)

    # Save trained models for prediction use
    model_dir = os.path.join(django_settings.BASE_DIR, 'trained_models')
    os.makedirs(model_dir, exist_ok=True)
    joblib.dump(cv, os.path.join(model_dir, 'vectorizer.joblib'))
    joblib.dump(classifier, os.path.join(model_dir, 'classifier.joblib'))

    # Save labeled data
    labeled_path = os.path.join(django_settings.BASE_DIR, 'Labeled_Data.csv')
    data.to_csv(labeled_path, index=False)

    obj = detection_accuracy.objects.all()
    return render(request, 'SProvider/train_model.html', {'objs': obj})