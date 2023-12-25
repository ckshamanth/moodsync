from flask import Flask, render_template, Response, jsonify
import gunicorn
from camera import *

app = Flask(__name__)

headings = ("Name","Album","Artist")
df1 = music_rec()
df1 = df1.head(15)
@app.route('/')
def index():
    print(df1.to_json(orient='records'))
    return render_template('index.html', headings=headings, data=df1)

def gen(camera):
    while True:
        global df1
        frame, df1 = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/t')
def gen_table():
    return df1.to_json(orient='records')

@app.route('/captured_image')
def captured_image():
    try:
        ret, jpeg = cv2.imencode('.jpg', camera.captured_frame)
        return Response(jpeg.tobytes(), mimetype='image/jpeg')
    except Exception as e:
        error_message = f"Error: {e}"
        return Response(error_message, status=500)



if __name__ == '__main__':
    app.debug = True
    app.run()




