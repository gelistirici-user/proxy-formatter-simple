with open('proxies.txt', 'r', encoding='UTF-8') as f:
    for proxy in f.readlines():
        if proxy != '':
            proxy = proxy.strip().split(':')
            proxy = f"{proxy[2]}:{proxy[3]}@{proxy[0]}:{proxy[1]}"
            print(proxy)
            with open('formated_proxies.txt', 'a', encoding='UTF-8') as f:
                f.write(proxy + '\n')


#-- R10: @gelistirici / Discord: User#2948 --#
