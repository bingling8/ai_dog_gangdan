# coding=utf-8

word_face_recogniton='人脸识别后你可能是{}'
word_book_recognition='图书识别后这本书可能是{}'
word_book_add_request_two='请读出书籍背面条形码第二行的所有数字'
word_hello='你好，我是钢蛋，很高兴为你服务!'
word_jump='跳一下'
word_listen_to_instructions='听指令'
word_please_speaking='请讲'
word_chatting='闲聊'
word_gangdan_likes_chatting_the_most='钢蛋最喜欢唠嗑了'
word_sorry_i_cant_understand='不好意思，我现在还听不懂这个指令哦'
word_speech_recognition_error='语音识别出错'
word_take_a_break='休息一下'
word_i_sat_down='我坐下了'
word_wnder_around='溜达溜达'
word_automatic_obstacle_avoidance='好嘞，我要启动自动避障程序了' 
word_stop='停下来'
word_okay='好嘞'
word_face_recongnition='人脸识别启动'
word_you_are='你好，人脸识别后，我判断你是{}'
word_book_recongnition='图书识别启动'
word_borrow_book_recongnition='借书'
word_return_book_recongnition='还书'
word_book_is='你好，图书识别后，我判断这本书可能是{}，请问是否识别准确？'
word_recongnition_false='错误'
word_recongnition_false_2='不对'
word_book_true_is='请问这本书正确的名字叫什么'
word_book_people_capture='为保证拍摄，请稍微远离摄像头，保证人和书在一起'
word_book_flow_success='已经拍摄完毕，谢谢配合'
word_book_recommendation='图书推荐'
word_book_new_one='新增图书'
word_book_new_two='添加图书'
word_book_add_request='请将书本的条形码放到摄像头前面进行识别'
word_please_turn_on_book_recommendation='请开启图书推荐服务'
word_recommand_next_boot='推荐下一本书'
word_move_forward='向前走两步'
word_moving='好嘞，钢蛋要向前走了'
word_move_backwards='先后走两步'
word_moving_back='好嘞，钢弹要向后走了'
word_jump='跳一下'
word_cannot_jump_high='好嘞，但我跳的不高哦'
word_shake_hands='握个手'
word_lets_shake_hands='好嘞，来握手'
word_pee='狗狗撒尿'
word_so_embarrassing='怪不好意思的'
word_time_now='现在几点'
word_time_now_is='现在时间是{}年{}月{}日{}点{}分{}秒'
word_weather_today='今天天气怎么样'
word_weather_tommorrow='明天天气怎么样'
word_processor_usage='处理器使用率'
word_memory_usage='内存使用率'
word_processor_usage_rate='你好，cpu使用率：{}%'
word_memory_usage_rate='你好，内存使用率：{}%'
word_space_walk='太空步'
word_show_a_piece='我还没完全学会，但我可以给你表演一段'
word_downward_facing_dog_pose='下犬式'
word_upward_facing_dog_pose='上犬式'
word_dance='跳个舞'
word_king_of_dancing='狗界舞王就是我'
word_thanks='谢谢'
word_please_switch_to_english='切换成英语'
word_please_switch_to_chinese='切换成中文'
word_request_book_recongnition='请将图书放到靠近摄像头的地方， 方便进行识别'
word_request_face_recongnition='请确保脸在摄像头的拍摄画面中， 方便进行识别'
word_face_recogniton_failed='未识别到人脸'
word_learn_english='口语和听力练习'
word_book_flow_fail='流程存在问题'
word_exception_restarted='钢蛋网络异常，已恢复到{}模式'
word_i_will_talk_to_you_as_interview='好吧，我会像雅思口语面试一样和你说话'
word_sorry_i_cant_understand_this='抱歉，我没理解你的意思'
word_goodbye='再见，要再找我玩哦'

def initLanguage(language):
    global word_hello
    global word_jump
    global word_listen_to_instructions
    global word_please_speaking
    global word_chatting
    global word_gangdan_likes_chatting_the_most
    global word_sorry_i_cant_understand
    global word_speech_recognition_error
    global word_take_a_break
    global word_i_sat_down
    global word_wnder_around
    global word_automatic_obstacle_avoidance
    global word_stop
    global word_okay
    global word_face_recongnition
    global word_you_are
    global word_book_recongnition
    global word_borrow_book_recongnition
    global word_return_book_recongnition
    global word_book_is
    global word_recongnition_false
    global word_recongnition_false_2
    global word_book_true_is
    global word_book_people_capture
    global word_book_flow_success
    global word_book_recommendation
    global word_book_new_one
    global word_book_new_two
    global word_please_turn_on_book_recommendation
    global word_recommand_next_boot
    global word_move_forward
    global word_moving
    global word_move_backwards
    global word_moving_back
    global word_jump
    global word_cannot_jump_high
    global word_shake_hands
    global word_lets_shake_hands
    global word_pee
    global word_so_embarrassing
    global word_time_now
    global word_time_now_is
    global word_weather_today
    global word_weather_tommorrow
    global word_processor_usage
    global word_memory_usage
    global word_processor_usage_rate
    global word_memory_usage_rate
    global word_space_walk
    global word_show_a_piece
    global word_downward_facing_dog_pose
    global word_upward_facing_dog_pose
    global word_dance
    global word_king_of_dancing
    global word_thanks
    global word_please_switch_to_english
    global word_please_switch_to_chinese
    global word_request_book_recongnition
    global word_book_add_request
    global word_learn_english
    global word_book_flow_fail
    global word_i_will_talk_to_you_as_interview
    global word_learn_english
    global word_book_add_request_two
    global word_exception_restarted
    global word_sorry_i_cant_understand_this
    global word_face_recogniton
    global word_book_recognition
    global word_request_face_recongnition
    global word_face_recogniton_failed
    global word_goodbye
    if language=="en":
        word_book_add_request_two='Please read all the numbers on the second line of the barcode on the back of the book'
        word_hello="hello, I'm Eric, nice to meet you!"
        word_jump='jump once time'
        word_listen_to_instructions='listen to instructions'
        word_please_speaking='please speaking'
        word_chatting='chat'
        word_gangdan_likes_chatting_the_most='Eric likes chatting the most'
        word_sorry_i_cant_understand='Sorry, I still don not understand this command'
        word_speech_recognition_error='speech recognition error'
        word_take_a_break='take a break'
        word_i_sat_down='I sat down'
        word_wnder_around='wander around'
        word_automatic_obstacle_avoidance='Alright,I am going to active the automatic obstacle avoidance program'
        word_stop='stop'
        word_okay='okay'
        word_face_recongnition='face recognition'
        word_you_are='hello, you are {}'
        word_book_recongnition='book recognition'
        word_borrow_book_recongnition='borrow books'
        word_return_book_recongnition='return books'
        word_book_is='the book may be {}, Is the identification accurate'
        word_book_new_one='add book'
        word_book_new_two='add new book'
        word_recongnition_false='no'
        word_recongnition_false_2='wrong'
        word_book_true_is='What is the name of this book？'
        word_book_flow_success='The shooting has been completed. Thank you for your cooperation'
        word_book_people_capture='To ensure shooting, please stay slightly away from the camera and keep the person and book together'
        word_book_recommendation='book recommendation'
        word_please_turn_on_book_recommendation='please turn on the book recommendation service'
        word_recommand_next_boot='please recommend next book'
        word_move_forward='move forward'
        word_moving='Alright, Eric is moving forward'
        word_move_backwards='move backwards'
        word_moving_back='Alright, Erics is going backwards'
        word_jump='jump'
        word_cannot_jump_high='Okay, but i can not jump high'
        word_shake_hands='shake hands'
        word_lets_shake_hands='okay, let us shake hands'
        word_pee='pee'
        word_so_embarrassing='so embarrassing'
        word_time_now='what time is it now'
        word_time_now_is='the current time is '
        word_weather_today='how is the weather today'
        word_weather_tommorrow='how is the weather tomorrow'
        word_processor_usage='process usage'
        word_processor_usage_rate='Process usage: {}%'
        word_memory_usage='memory usage'
        word_memory_usage_rate='memory usage: {}%'
        word_space_walk='space walk'
        word_show_a_piece='I have not quite learned it yet, but i can show you a piece'
        word_downward_facing_dog_pose='downward facing dog'
        word_upward_facing_dog_pose='upward facing dog'
        word_dance='dance'
        word_king_of_dancing='I am the king of dancing in the dog world'
        word_thanks='thanks'
        word_please_switch_to_english='switch to English'
        word_please_switch_to_chinese='switch to Chinese'
        word_book_add_request='Please place the barcode of the book in front of the camera for identification'
        word_i_will_talk_to_you_as_interview='okay, I will talk to you like an IELTS speaking test interview'
        word_learn_english='speaking and listening practice'
        word_book_flow_fail='something is wrong.'
        word_exception_restarted='Eric network is abnormal and has returned to {} mode' 
        word_request_book_recongnition='Please place the book near the camera for easy identification'
        word_sorry_i_cant_understand_this='Sorry, I do not understand what you mean'
        word_face_recogniton='After facial recognition, you may be {}'
        word_book_recognition='After book recognition, this book may be {}'
        word_request_face_recongnition='Please ensure that the face is in the captured image of the camera for easy recognition'
        word_face_recogniton_failed='No facial recognition'
        word_goodbye='Goodbye'
    elif language=="zh":
        word_face_recogniton_failed='未识别到人脸'
        word_request_face_recongnition='请确保脸在摄像头的拍摄画面中， 方便进行识别'
        word_book_recognition='图书识别后这本书可能是{}'
        word_face_recogniton='人脸识别后你可能是{}'
        word_book_add_request_two='请读出书籍背面条形码第二行的所有数字'
        word_hello='你好，我是钢蛋，很高兴为你服务!'
        word_jump='跳一下'
        word_listen_to_instructions='听指令'
        word_please_speaking='请讲'
        word_chatting='闲聊'
        word_gangdan_likes_chatting_the_most='钢蛋最喜欢唠嗑了'
        word_sorry_i_cant_understand='不好意思，我现在还听不懂这个指令哦'
        word_speech_recognition_error='语音识别出错'
        word_take_a_break='休息一下'
        word_i_sat_down='我坐下了'
        word_wnder_around='溜达溜达'
        word_automatic_obstacle_avoidance='好嘞，我要启动自动避障程序了' 
        word_stop='停下来'
        word_okay='好嘞'
        word_face_recongnition='人脸识别启动'
        word_you_are='你好，人脸识别后，我判断你是{}'
        word_book_recongnition='图书识别启动'
        word_borrow_book_recongnition='借书'
        word_return_book_recongnition='还书'
        word_book_is='你好，图书识别后，我判断这本书可能是{}，请问是否识别准确？'
        word_recongnition_false='错误'
        word_recongnition_false_2='不对'
        word_book_true_is='请问这本书正确的名字叫什么'
        word_book_people_capture='为保证拍摄，请稍微远离摄像头，保证人和书在一起'
        word_book_flow_success='已经拍摄完毕，谢谢配合'
        word_book_recommendation='图书推荐'
        word_book_new_one='新增图书'
        word_book_new_two='添加图书'
        word_book_add_request='请将书本的条形码放到摄像头前面进行识别'
        word_please_turn_on_book_recommendation='请开启图书推荐服务'
        word_recommand_next_boot='推荐下一本书'
        word_move_forward='向前走两步'
        word_moving='好嘞，钢蛋要向前走了'
        word_move_backwards='向后走两步'
        word_moving_back='好嘞，钢弹要向后走了'
        word_jump='跳一下'
        word_cannot_jump_high='好嘞，但我跳的不高哦'
        word_shake_hands='握个手'
        word_lets_shake_hands='好嘞，来握手'
        word_pee='狗狗撒尿'
        word_so_embarrassing='怪不好意思的'
        word_time_now='现在几点'
        word_time_now_is='现在时间是{}年{}月{}日{}点{}分{}秒'
        word_weather_today='今天天气怎么样'
        word_weather_tommorrow='明天天气怎么样'
        word_processor_usage='处理器使用率'
        word_memory_usage='内存使用率'
        word_processor_usage_rate='你好，cpu使用率：{}%'
        word_memory_usage_rate='你好，内存使用率：{}%'
        word_space_walk='太空步'
        word_show_a_piece='我还没完全学会，但我可以给你表演一段'
        word_downward_facing_dog_pose='下犬式'
        word_upward_facing_dog_pose='上犬式'
        word_dance='跳个舞'
        word_king_of_dancing='狗界舞王就是我'
        word_thanks='谢谢'
        word_please_switch_to_english='切换成英语'
        word_please_switch_to_chinese='切换成中文'
        word_request_book_recongnition='请将图书放到靠近摄像头的地方，方便进行识别'
        word_learn_english='口语和听力练习'
        word_book_flow_fail='流程存在问题'
        word_exception_restarted='钢蛋网络异常，已恢复到{}模式'
        word_i_will_talk_to_you_as_interview='好吧，我会像雅思口语面试一样和你说话'
        word_sorry_i_cant_understand_this='抱歉，我没理解你的意思'
        word_goodbye='再见，要再找我玩哦'







