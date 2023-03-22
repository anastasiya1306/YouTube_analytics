from main import*

if __name__ == '__main__':
    # ch1 = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')   #вДудь
    # ch2 = Channel('UC1eFXmJNkjITxPFWTy6RsWg')   #Редакция
    # ch1.print_info()
    # print(Channel.get_service())
    # # vdud.channel_id = 'Новое название'
    # ch1.to_json('vdud.json')
    # print(ch1.subscriber_count)
    # print(ch2.subscriber_count)
    # print(ch1)
    # print(ch2)
    # print(ch1 + ch2)
    # print(ch1 > ch2)
    # print(ch1 < ch2)

    # video1 = Video('9lO06Zxhu88')
    # video2 = PLVideo('BBotskuyw_M', 'PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD')
    # print(video1)
    # print(video2)

    # pl = PlayList('PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb')
    # print(pl.title)
    # print(pl.url)
    # duration = pl.total_duration
    # print(duration)
    # print(type(duration))
    # print(duration.total_seconds())
    # print(pl.show_best_video())
    broken_video = Video('broken_video_id')
    print(broken_video.video_title)
    print(broken_video.like_count)