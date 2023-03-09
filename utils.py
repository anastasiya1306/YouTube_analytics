from main import Channel

if __name__ == '__main__':
    ch1 = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')   #вДудь
    ch2 = Channel('UC1eFXmJNkjITxPFWTy6RsWg')   #Редакция
    # ch1.print_info()
    # print(Channel.get_service())
    # # vdud.channel_id = 'Новое название'
    # ch1.to_json('vdud.json')
    print(ch1.subscriber_count)
    print(ch2.subscriber_count)
    print(ch1)
    print(ch2)
    print(ch1 + ch2)
    print(ch1 > ch2)
    print(ch1 < ch2)