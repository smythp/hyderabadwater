import mechanicalsoup

url = 'https://www.hyderabadwater.gov.in/en/wlrreport/'


b = mechanicalsoup.StatefulBrowser()
b.open(url)


b.select_form('form')
b['txtdate'] = '27-Aug-2018'

# b.launch_browser()


r = b.submit_selected()

result_html = r.text


