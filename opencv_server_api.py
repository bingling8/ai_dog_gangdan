import os
import cv2
import numpy as np

#
label_mapping = {'1000.0': 'huobiyuweilai', '1001.0': 'manhuasuanfa', '1002.0': 'yueliangyuliubianshi', '1003.0': 'bailuyuan',
                 '1': 'xlbttn', '2': 'hlkwe', '3': 'klsaws'}


orb = cv2.ORB_create(nfeatures=100)
sift = cv2.SIFT_create(nfeatures=100)
model_knn = cv2.ml.KNearest_create()
model_svm = cv2.ml.SVM_create()

haar_face_cascade = cv2.CascadeClassifier('./opencv/model_common/haarcascade_frontalface_default.xml')
model_lbphface = cv2.face.LBPHFaceRecognizer_create()


## KNN
model_knn = model_knn.load('./opencv/model_books/book_classifier_knn_sift.xml')

## SVM
model_svm = model_svm.load('./opencv/model_books/book_classifier_svm_sift.xml')

## LBPHFACE
model_lbphface.read('./opencv/model_people/people_classifier_lbphface_sift.xml')


######################KNN
def knn(img_path):
    test_img = cv2.cvtColor(cv2.imread(img_path), cv2.COLOR_BGR2GRAY)
    kps, dess = sift.detectAndCompute(test_img, None)
    np_arra = np.array([dess[:90].reshape(-1)]).astype(np.float32)
    _, result, a, conf = model_knn.findNearest(np_arra, 5)
    return label_mapping[str(_)]

######################KNN




######################SVM

def svm(img_path):
    test_img = cv2.cvtColor(cv2.imread(img_path), cv2.COLOR_BGR2GRAY)
    kps, dess = sift.detectAndCompute(test_img, None)
    np_arra = np.array([dess[:90].reshape(-1)]).astype(np.float32)
    pred_labels = model_svm.predict(np_arra)
    return label_mapping[str(pred_labels[1][0][0])]

######################SVM
#label_mapping = {'huobiyuweilai': 1000.0, 'manhuasuanfa': 1001.0, 'yueliangyuliubianshi': 1002.0, 'bailuyuan': 1003.0}



######################SVM
def getFaceFeatures(test_img):
    gray = cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)
    faces = haar_face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        face = gray[y:y + h, x:x + w]
    # print(face)
    return face

def lbphface(img_path):
    test_img = cv2.imread(img_path)
    face = getFaceFeatures(test_img)
    label, confidence = model_lbphface.predict(face)
    # print(f'Label: {label} | Confidence: {confidence}')
    return label_mapping[str(label)]

######################SVM


