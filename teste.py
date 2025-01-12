from os import link
from videos import read_videos, update_video

videos = read_videos()

for video in videos:
    # if video.link.__contains__("?"):
        # video.link = video.link.split("?")[0]
        # update_video(video.id, video.link)
    print(video.link)
# links = [video.link for video in videos]
# print(link)
# print(update_video(7, estado="baixado"))

# create_video(
#     link="https://www.tiktok.com/@energiasigno/video/7457683159463841066?is_from_webapp=1&sender_device=pc&web_id=7452826216727463429",
#     descricao="El año comienza con todo para estos signos.#astrology #states #signs #zodiacsigns #us #usa🇺🇸 #sagittarius #capricorn #aquarius #scorpio",
#     estado="baixado"
# )


# if __name__ == "__main__":
#     link = input()
#     if link.__contains__("?"):
#         link = link.split("?")[0]
#     if link in links:
#         print("contem")
#     else:
#         print("não contem")
