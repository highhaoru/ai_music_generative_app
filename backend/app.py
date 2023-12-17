from flask import Flask, send_from_directory, render_template

app = Flask(__name__, 
            static_folder='../frontend',  # 设置静态文件夹路径
            template_folder='../frontend' # 设置模板文件夹路径
           )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_music/<composer>')
def get_music(composer):
    # 假设 MIDI 文件存储在 'music_files' 目录下，该目录与 'app.py' 在同一路径
    file_path = 'music_files/' + composer + 'AI' + '.mp3'
    return send_from_directory(directory='.', path=file_path)

if __name__ == '__main__':
    app.run(debug=True)
