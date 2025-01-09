from flask import Flask, render_template, request, jsonify

from videos import create_video, read_videos, read_video_by_id, \
    update_video, delete_video
app = Flask(__name__, static_folder="src", template_folder="pages")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/videos", methods=["POST"])
def create():
    data = request.json
    if not data or "link" not in data or "estado" not in data:
        return jsonify({"error": "Link e estado são obrigatórios!"}), 400
    video = create_video(data["link"], data.get("descricao", ""),
                         data["estado"])
    return jsonify({
        "id": video.id,
        "link": video.link,
        "descricao": video.descricao,
        "estado": video.estado
    }), 201


@app.route("/videos", methods=["GET"])
def read():
    videos = read_videos()
    return jsonify([{
        "id": video.id,
        "link": video.link,
        "descricao": video.descricao,
        "estado": video.estado
    } for video in videos])


@app.route("/videos/<int:video_id>", methods=["GET"])
def read_by_id(video_id):
    video = read_video_by_id(video_id)
    if not video:
        return jsonify({"error": "Vídeo não encontrado"}), 404
    return jsonify({
        "id": video.id,
        "link": video.link,
        "descricao": video.descricao,
        "estado": video.estado
    })


@app.route("/videos/<int:video_id>", methods=["PUT"])
def update(video_id):
    data = request.json
    video = update_video(video_id, data.get("link"), data.get("descricao"),
                         data.get("estado"))
    if not video:
        return jsonify({"error": "Vídeo não encontrado"}), 404
    return jsonify({
        "id": video.id,
        "link": video.link,
        "descricao": video.descricao,
        "estado": video.estado
    })


@app.route("/videos/<int:video_id>", methods=["DELETE"])
def delete(video_id):
    video = delete_video(video_id)
    if not video:
        return jsonify({"error": "Vídeo não encontrado"}), 404
    return jsonify({"message": "Vídeo deletado com sucesso"})


if __name__ == "__main__":
    app.run(debug=True)
