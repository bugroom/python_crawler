import requests 
import json
def down(content,page):
	aq=[]
	rep=requests.get('http://106.15.195.249:8011/search_new?q={}&p={}'.format(content,page))
	rep.encoding=rep.apparent_encoding
	aa=rep.text
	ab=aa.replace("null","123")
	ac=json.loads(ab)
	for y in ac['list']['data']:
		aq.append('�ļ�����'+y['title']+'���ӣ�'+y['link'])
	return aq

def main():	
	file_name=input('������Ҫ���ص��ļ�����')
	page=str(input('���������ص�ҳ����'))
	print(down(file_name,page))

main()