import requests
import lxml
from lxml import html
import json

url = 'http://www.expedia.com/Hotel-Search'

queryString = {'responsive': 'true', 'inpAjax': 'false'}
headers = {#"Cookie": "MC1=GUID=f85a8dcbe0e043bd870c42ace7f923cf; tpid=v.1,1; iEAPID=0,; aspp=v.1,0|||||||||||||; WebIQ.API.Debug=false; WarpFirstPartyCookieCheck=1; WebIQWARPSessionID={ea812620-0091-4d6a-b9a9-5976b5daa863}; WebIQWARPReferrer=; ipsnf3=v.3|il|1|0|rosh_haayin; __utma=16308457.1010859874.1412091035.1412524299.1412534645.3; __utmc=16308457; __utmz=16308457.1412091035.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); SSID1=BwAKch2aAAgAAACTzCpU2e4NDZPMKlQHAAAAAADVn1xUzaQ3VAAKiuEDAAP9XwAAqRE1VAMAwgMAAa5YAADNpDdUAQDOAwAB5VoAAM2kN1QBAN8DAAPNXwAACmkxVAYA2wMAA0hfAAAKaTFUBgDSAwADZl0AAJPMKlQHAN4DAAPHXwAACmkxVAYA3QMAAWVfAADNpDdUAQDYAwADt14AAAppMVQGANQDAAP9XQAAk8wqVAcA3AMAAV1fAADNpDdUAQDRAwAA1wMAAA; SSSC1=1.G6064884780159069913.7|962.22702:974.23269:978.23910:980.24061:984.24247:987.24392:988.24413:989.24421:990.24519:991.24525:993.24573; JSESSION=26a5634a-459a-4062-829d-7c0d328c19af; SSRT1=0qU3VAIDAQ; ss_rewards_test=step0; TH=Zq1lI0f9YKT2/TwF8RKlZnX3Ts0SFxsWXUKg+Mkyb6JrWRxFeTTKSw5l65QWbO2r|+ZQHjThw2W9zMI+00ZSPWxQzu2qIxWIrO77bWzD7VnITkReACG3afr0WTOC+QRImjup6uP9f2MQ5tCZW8xcrX7JdXjf5yh87ckJh3rASbkCo5GY7MbcpPC+urYldGCe8eOkMpZUm42UVyPDtNM453+J15pvnwWvO2KYK4rYu51bEfIuUplPtZm2fpvwMgTDoxP78LQ9FUDq08qGSjffOCLzL1qCk/n1anWkwxBe0YlSYkWWwPzYkZtUdSFjaFRtkZ0A4ffMkCsU=|PgcbJYsQBPw0jhq0cz6gMeZl7IEJuINr/AnLE0Xrt1DgshTUX7W5cvkGzIKZ0LawBhik91q/lWA=; lsrc=v.1,10/24/2014; SSOD1=ADEKAAAAkAD4TgAAEgAAAPrMKlTdpTdUyU4AAA4AAAD7zCpU3qU3VJJLAAAHAAAAAc0qVOEZM1QMAAAABQAAAObPKlRvkTFUyzEAAA0AAAA90CpU0qU3VCRLAAABAAAAaGwxVGhsMVQRTgAAAgAAAKFsMVTBbzFUwk8AAAoAAACpbDFU26U3VBhPAAAgAAAAqmwxVNylN1Q; SSLB=1; SSPV1=S9AAAAAAAAsAEwAAAAAAAAAAAAEAAAAAAAA; linfo=v.4,|0|0|255|1|0||||||||1033|0|0||0|0|0|-1|-1; user=v.8,0,EX01D8F0EA62$23$FE$0B01000$82G$C57$A4$2BQ$23$A4$2BQ$23$A4$2BQ$2310009000$1E81!90Po$CD$FC$A9$7FL$E5!i02000; minfo=v.5,EX0182CDC7D03$F5$5Fam$80$9B$BFc$9Bq$82$A1$DF$BB$F8$EF$E4$38$86V$86!2$9A$C30$2E$92$AD$10$FB$DA6$0E$5C$2D$B2$A1$DF$86R$3A$EC$1A$E0$2E$D5ll$DB$A2$7B$22$96$8B$B4$F4$F6$18$D2$BB$FEu$D8$5D$DC$F8d$A5$D8; accttype=v.2,8,1,EX01864F224A3$F5$5Fa$7C$80$83$BFl$9Bq$81$A1$D7$BB$FA$EF$E4$3A$86W$86$90$98$C30$24$92$AD$13$FB$DA$3E; eid=-2; s_cc=true; s_fid=0ABB48427EC0FB39-2264DB9A78097E9A; s_sq=%5B%5BB%5D%5D; s_vi=[CS]v1|2A15664E0530C094-400003068001485F[CE]",
		   "Cookie": "MC1=GUID=f85a8dcbe0e043bd870c42ace7f923cf; iEAPID=0,; aspp=v.1,0|||||||||||||; WebIQ.API.Debug=false; WarpFirstPartyCookieCheck=1; WebIQWARPSessionID={ea812620-0091-4d6a-b9a9-5976b5daa863}; WebIQWARPReferrer=; tpid=v.1,1; isClicked=true; JSESSION=38282eb9-7fa6-4c62-8b1b-90b72074a9ce; ipsnf3=v.3|il|1|0|rosh_haayin; ndcd=wc1.1.w-681606.1.0.nKpzB-9azkuviW4vi-pFHw,,.L0B90O__4qz3QyCET8gLdvlG0c00aE41Tfk2vhuDOU4KarkV7cltm_Mn-Eg7KUdK3fx5b35pcYUU9scD5iHDH_quSQE8VqpKY58qaXKFn0FG314g4r6iiwsLMTjvXaoQKZtgwzBt0PZqZl0GofIYbBsADtOt2P6DbGTYizA3KOPsdHbxINgEcv6ccgC0VOAfMbP02RmeOgmsYynrl1vM-LLa2o56iHthLCAsosQM5Fk,; ss_rewards_test=step0; s_cc=true; __utma=16308457.1010859874.1412091035.1413389896.1413397515.5; __utmc=16308457; __utmz=16308457.1412091035.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); TH=Zq1lI0f9YKT2/TwF8RKlZoAO3SsyQhq6yOAiFAH/uJho/r131K/9pOMcV6w1K7U+uaI2MvXmKFg=|+ZQHjThw2W8/Mxg97b2mKx1MzfhS1gEIIRH+Xq5sRdjDKRwmuR+/c6oxXQ/SxOxQNaEPt/jjEH+lNKsmjgOqTmf1x8+VLyIweIdYOpFWFRS4ow86MJ3gneqzrmeHU0XLjra6FGWsFK/jAL7QPLpJ63ZKGT6tddOKG1dNquKJhxDVlxksNaboq+FzIqTcvg4IPuynCLlxoyC+AKwshtb8AzqtjnH4sx/6nJnneK7ALmu7HxAAT+3/FPZ7qhDcO9T7U73dxm13b+A=|FGPNvk42+FlFilMmm9vD5d5p0kXjlzMApak6fS6MbaTLO78KC0M8p8jMYVszMyUazc9exFGSxQo=; lsrc=v.1,10/29/2014; eid=-2; s_fid=0ABB48427EC0FB39-2264DB9A78097E9A; s_sq=%5B%5BB%5D%5D; s_vi=[CS]v1|2A15664E0530C094-400003068001485F[CE]; SSLB=1; SSID1=BwAOEh1UACAAAACTzCpU2e4NDZPMKlQRAAAAAADVn1xUicg-VAAKiuEDAAP9XwAAqRE1VA0A4AMAAfxfAACJyD5UAQDCAwABrlgAAInIPlQBAM4DAAHpWgAAicg-VAEA3QMAAWZfAACJyD5UAQDcAwABXF8AAInIPlQBANEDAADXAwAA3wMAANIDAADUAwAA2wMAAN4DAADYAwAA; SSSC1=1.G6064884780159069913.17|962.22702:974.23273:988.24412:989.24422:992.24572:993.24573; SSRT1=icg-VAIDAQ; SSOD1=AH0sAAAAoAD4TgAAFwAAAPrMKlTEmz5UyU4AABEAAAD7zCpUrXg9VJJLAAAHAAAAAc0qVOEZM1QMAAAACgAAAObPKlQFvD5UyzEAABkAAAA90CpUicg-VCRLAAAEAAAAaGwxVC28PlQRTgAAAgAAAKFsMVTBbzFUwk8AAA8AAACpbDFUw5s-VBhPAAAyAAAAqmwxVPu_PlQOTgAABAAAAO-dPlT6uz5U; SSPV1=Wg4AAAAAAAEACwAAAAAAAAAAAAEAAAAAAAA; linfo=v.4,|0|0|255|1|0||||||||1033|0|0||0|0|0|-1|-1; user=v.8,0,EX01A81AD5A9$23$FE$0B01000$13X$C67$A4$2BQ$23$A4$2BQ$23$A4$2BQ$2310009000$1E81!90e$E21o$F0$FF2w!i02000; minfo=v.5,EX0190F672E2$95A$3F$15$F2$35$23X$E1$39J$DA$FAp$3A$80kRfq$DDsM$BDG$5Ep$8A$EE$7D$17$36.$7B$E4$2A$EE$34$F6$127$8F$34$89$F8$863$3B$33$30$1C$250$E3v; accttype=v.2,8,1,EX01C69938FA$95A$3F$15$EF$35$3BX$E3$39J$DC$F8p$3A$84cRf$7D$D9zM$8BG",
           "Origin": "http://www.expedia.com",
           "Accept-Encoding": "gzip,deflate",
           "Accept-Language": "en-US,en;q=0.8,he;q=0.6",
           "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36",
           "Content-type": "application/x-www-form-urlencoded",
           "Accept": "application/json, text/javascript",
           "Referer": "http://www.expedia.com/Hotel-Search?",
           "X-Requested-With": "XMLHttpRequest",
           "Connection": "keep-alive",
           "DNT": "1"}

def ea(s):  # encode ascii with throwing stupid errors for unicode characters
	return s.encode('ascii','ignore')

formData = {'sort': ['guestRating'],
            'startDate': ['11/12/2014'],
            'hashParam': ['1ba888436b046f30a2ce8d83e2636ac2ce4b3122'],
            #'regionId': ['179892'],
            #'regionId': ['179992'],
            'endDate': ['11/15/2014'],
            'adults': ['2'],
            'destination': ['Rome (and vicinity), Italy']}

r = requests.post(url, data=formData, params=queryString, headers=headers)
# if r.status_code != 200:
#     print r.raw.headers
#     print r.request.body
#     print "Status Code: " + r.status_code
#     print r.raw.reason
#     exit(1)
pageNum = 1
print "Name\tPrice\tURL"

while r.status_code == 200:

	hotels_json = json.loads(r.text)
	for hotel in hotels_json['resultsBelow']:
		info = hotel['retailHotelInfoModel']
		priceInfo = hotel['retailHotelPricingModel']
		print ea(info['hotelName']) + '\t' + ea(priceInfo['currencySymbol']) + ea(priceInfo['priceFormatted']) + '\t' + \
			  ea(hotel['infositeUrl'])

	pageNum += 1
	formData = {'sort': ['guestRating'],
	            'startDate': ['11/12/2014'],
	            'hashParam': ['1ba888436b046f30a2ce8d83e2636ac2ce4b3122'],
	            #'regionId': ['179892'],
	            #'regionId': ['179992'],
	            'endDate': ['11/15/2014'],
	            'adults': ['2'],
	            'destination': ['Rome (and vicinity), Italy'],
	            'page': [str(pageNum)]}

	r = requests.post(url, data=formData, params=queryString, headers=headers)
