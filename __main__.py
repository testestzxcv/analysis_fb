import collect
import analyze
import visualize

if __name__ == '__main__':
    items = [
        {'pagename': 'jtbcnews', 'since': '2017-01-01', 'until':'2017-12-31'},
        {'pagename': 'chosun', 'since': '2017-01-01', 'until': '2017-12-31'}
    ]

    # 데이터 수집(collection)
    for item in items:
        resultfile = collect.crawling(**item, fetch=False)
        item['resultfile'] = resultfile



    # 데이터 분석(analyze)
    for item in items:
        data = analyze.json_to_str(item['resultfile'], 'message')
        item['count_wordfreq'] = analyze.count_wordfreq(data)
        print(item['count_wordfreq'])

    # 데이터 시각화(visualize)
    for item in items:
        count = item['count_wordfreq']
        count_m50 = dict(count.most_common(50))

        filename = "%s_%s_%s" % (item['pagename'], item['since'], item['until'])
        visualize.wordcloud(filename, count_m50)
        visualize.graph_bar(
            title='%s 빈도분석' % (item['pagename']),
            xlabel='단어',
            ylabel='빈도',
            values=list(count_m50.values()),
            ticks=list(count_m50.keys()),
            showgrid=False,  # 그리드 그리기
            filename=filename,
            showgraph=False)

