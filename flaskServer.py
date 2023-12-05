from flask import Flask, request, jsonify
import opencv_server_api

app = Flask(__name__)

@app.route('/classify_book', methods=['POST'])
def classify_book():
    # 接收客户端发送的文件
    tmp_path = './opencv/tmp/book_tmp.jpg'
    file = request.files['image']
    file.save(tmp_path)
    # 在这里添加处理文件的代码，例如进行图像识别或特征提取

    knn_result = opencv_server_api.knn(tmp_path)
    svm_result = opencv_server_api.svm(tmp_path)

    # 返回处理结果给客户端
    response = {'knn_result': knn_result, 'svm_resukt': svm_result}
    return jsonify(response)


@app.route('/classify_people', methods=['POST'])
def classify_people():
    # 接收客户端发送的文件
    tmp_path = './opencv/tmp/people_tmp.jpg'
    file = request.files['image']
    file.save(tmp_path)
    # 在这里添加处理文件的代码，例如进行图像识别或特征提取

    lbphface_result = opencv_server_api.lbphface(tmp_path)

    # 返回处理结果给客户端
    response = {'lbphface_result': lbphface_result}
    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0',  port=9898)
