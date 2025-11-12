def remove_url_anchor(url):
    res = ''
    for i in range(len(url)):
        if url[i] == '#':
            break
        else:
            res += url[i]
    return res
