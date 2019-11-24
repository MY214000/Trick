# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 10:35:13 2019

@author: Lee
"""

# Row by row
from prettytable import PrettyTable


#x.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
#x.add_row(["Adelaide",1295, 1158259, 600.5])
#x.add_row(["Brisbane",5905, 1857594, 1146.4])
#x.add_row(["Darwin", 112, 120900, 1714.7])
#x.add_row(["Hobart", 1357, 205556, 619.5])
#x.add_row(["Sydney", 2058, 4336374, 1214.8])
#x.add_row(["Melbourne", 1566, 3806092, 646.9])
#x.add_row(["Perth", 5386, 1554769, 869.4])
#print(x)
#
## Column by column
#
##x.add_column("City name", 
##["Adelaide","Brisbane","Darwin","Hobart","Sydney","Melbourne","Perth"])
##x.add_column("Area", [1295, 5905, 112, 1357, 2058, 1566, 5386])
##x.add_column("Population", [1158259, 1857594, 120900, 205556, 4336374, 3806092, 
##1554769])
##x.add_column("Annual Rainfall",[600.5, 1146.4, 1714.7, 619.5, 1214.8, 646.9, 
##869.4])
#
## Importing data from a CSV file
#from prettytable import from_csv
#fp = open("file2.csv", "r")
#mytable = from_csv(fp)
#fp.close()
#print(mytable[:10])
#
from prettytable import MSWORD_FRIENDLY,PLAIN_COLUMNS
x = PrettyTable()
#x.set_style(MSWORD_FRIENDLY)
##x.border = False
##x.header = False
##x.padding_width = 5
#print(x)


ulist=[['1', '清华大学', '94.6'], ['2', '北京大学', '76.5'], ['3', '浙江大学', '72.9'], ['4', '上海交通大学', '72.1'], ['5', '复旦大学', '65.6'], ['6', '中国科学技术大学', '60.9'], ['7', '华中科技大学', '58.9'], ['7', '南京大学', '58.9'], ['9', '中山大学', '58.2'], ['10', '哈尔滨工业大学', '56.7'], ['11', '北京航空航天大学', '56.3'], ['12', '武汉大学', '56.2'], ['13', '同济大学', '55.7'], ['14', '西安交通大学', '55.0'], ['15', '四川大学', '54.4'], ['16', '北京理工大学', '54.0'], ['17', '东南大学', '53.6'], ['18', '南开大学', '52.8'], ['19', '天津大学', '52.3'], ['20', '华南理工大学', '52.0'], ['21', '中南大学', '50.3'], ['22', '北京师范大学', '49.7'], ['23', '山东大学', '49.1'], ['23', '厦门大学', '49.1'], ['25', '吉林大学', '48.9'], ['26', '大连理工大学', '48.6'], ['27', '电子科技大学', '48.4'], ['28', '湖南大学', '48.1'], ['29', '苏州大学', '47.3'], ['30', '西北工业大学', '46.7'], ['31', '中国人民大学', '46.1'], ['32', '华东师范大学', '46.0'], ['33', '南京航空航天大学', '44.8'], ['34', '对外经济贸易大学', '44.7'], ['35', '南方科技大学', '44.6'], ['36', '华东理工大学', '44.5'], ['37', '重庆大学', '44.4'], ['38', '南京理工大学', '44.3'], ['39', '北京科技大学', '43.9'], ['40', '东北大学', '43.7'], ['41', '上海大学', '43.4'], ['42', '北京邮电大学', '42.9'], ['42', '上海财经大学', '42.9'], ['42', '中国农业大学', '42.9'], ['45', '武汉理工大学', '42.8'], ['46', '北京交通大学', '42.6'], ['46', '华中师范大学', '42.6'], ['48', '西安电子科技大学', '42.1'], ['49', '中央财经大学', '41.8'], ['50', '北京化工大学', '41.7'], ['51', '暨南大学', '41.5'], ['52', '东华大学', '41.4'], ['52', '兰州大学', '41.4'], ['52', '中南财经政法大学', '41.4'], ['55', '宁波诺丁汉大学', '40.3'], ['56', '哈尔滨工程大学', '40.1'], ['56', '华北电力大学', '40.1'], ['58', '深圳大学', '40.0'], ['59', '江南大学', '39.6'], ['59', '南京师范大学', '39.6'], ['61', '北京工业大学', '39.5'], ['62', '福州大学', '39.4'], ['63', '北京外国语大学', '39.3'], ['63', '北京语言大学', '39.3'], ['63', '中国地质大学（武汉）', '39.3'], ['66', '西南交通大学', '39.2'], ['67', '华中农业大学', '39.1'], ['67', '中国海洋大学', '39.1'], ['69', '南京农业大学', '39.0'], ['70', '上海外国语大学', '38.8'], ['71', '中国矿业大学', '38.6'], ['72', '中国地质大学（北京）', '38.5'], ['73', '东北财经大学', '38.2'], ['73', '西南财经大学', '38.2'], ['73', '西南大学', '38.2'], ['76', '东北师范大学', '38.1'], ['76', '南京邮电大学', '38.1'], ['76', '中国政法大学', '38.1'], ['79', '河海大学', '38.0'], ['80', '南京信息工程大学', '37.9'], ['81', '西北农林科技大学', '37.8'], ['82', '中国石油大学（华东）', '37.4'], ['83', '合肥工业大学', '37.3'], ['84', '陕西师范大学', '37.2'], ['85', '华南师范大学', '37.1'], ['85', '江苏大学', '37.1'], ['87', '南京工业大学', '37.0'], ['87', '中国石油大学（北京）', '37.0'], ['89', '西北大学', '36.9'], ['89', '浙江工业大学', '36.9'], ['91', '北京林业大学', '36.8'], ['91', '湖南师范大学', '36.8'], ['91', '浙江师范大学', '36.8'], ['94', '首都师范大学', '36.4'], ['95', '汕头大学', '36.3'], ['96', '中国传媒大学', '36.2'], ['97', '杭州电子科技大学', '36.1'], ['98', '扬州大学', '36.0'], ['99', '安徽大学', '35.9'], ['100', '华侨大学', '35.7'], ['101', '宁波大学', '35.4'], ['101', '首都经济贸易大学', '35.4'], ['101', '西交利物浦大学', '35.4'], ['104', '燕山大学', '35.3'], ['105', '湖北大学', '35.2'], ['106', '长安大学', '35.1'], ['106', '上海理工大学', '35.1'], ['108', '大连海事大学', '35.0'], ['108', '广东外语外贸大学', '35.0'], ['108', '太原理工大学', '35.0'], ['111', '广东工业大学', '34.8'], ['111', '南京财经大学', '34.8'], ['111', '浙江理工大学', '34.8'], ['114', '河北工业大学', '34.7'], ['115', '华东政法大学', '34.6'], ['115', '湘潭大学', '34.6'], ['115', '浙江财经大学', '34.6'], ['115', '中国矿业大学（北京）', '34.6'], ['119', '青岛大学', '34.5'], ['120', '上海师范大学', '34.2'], ['121', '南京审计大学', '34.1'], ['122', '华南农业大学', '34.0'], ['123', '江西财经大学', '33.9'], ['123', '辽宁大学', '33.9'], ['123', '中央民族大学', '33.9'], ['126', '武汉工程大学', '33.8'], ['126', '郑州大学', '33.8'], ['128', '杭州师范大学', '33.6'], ['128', '上海对外经贸大学', '33.6'], ['130', '上海海事大学', '33.4'], ['131', '山东师范大学', '33.3'], ['131', '武汉科技大学', '33.3'], ['133', '北京第二外国语学院', '33.2'], ['133', '广西大学', '33.2'], ['133', '云南大学', '33.2'], ['133', '浙江工商大学', '33.2'], ['137', '山西大学', '33.1'], ['138', '东北农业大学', '33.0'], ['139', '广州大学', '32.7'], ['139', '黑龙江大学', '32.7'], ['139', '南昌大学', '32.7'], ['139', '天津财经大学', '32.7'], ['143', '东北林业大学', '32.5'], ['143', '河南大学', '32.5'], ['145', '河北大学', '32.4'], ['146', '江苏师范大学', '32.3'], ['147', '济南大学', '32.0'], ['147', '山东财经大学', '32.0'], ['149', '山东科技大学', '31.9'], ['150', '长沙理工大学', '31.7'], ['151', '西南政法大学', '31.4'], ['152', '渤海大学', '31.3'], ['152', '重庆工商大学', '31.3'], ['152', '福建师范大学', '31.3'], ['152', '天津师范大学', '31.3'], ['156', '曲阜师范大学', '31.2'], ['156', '三峡大学', '31.2'], ['158', '北京工商大学', '31.1'], ['158', '西安理工大学', '31.1'], ['158', '浙江农林大学', '31.1'], ['161', '广西师范大学', '31.0'], ['161', '温州大学', '31.0'], ['163', '湖北工业大学', '30.9'], ['163', '四川农业大学', '30.9'], ['165', '重庆邮电大学', '30.8'], ['165', '河北师范大学', '30.8'], ['165', '河南师范大学', '30.8'], ['168', '北京体育大学', '30.7'], ['168', '常州大学', '30.7'], ['168', '天津工业大学', '30.7'], ['171', '石家庄铁道大学', '30.6'], ['172', '中国计量大学', '30.4'], ['173', '海南大学', '30.3'], ['173', '江苏科技大学', '30.3'], ['175', '安徽财经大学', '30.2'], ['175', '北京建筑大学', '30.2'], ['175', '中南民族大学', '30.2'], ['178', '安徽工业大学', '30.1'], ['178', '北京物资学院', '30.1'], ['178', '南通大学', '30.1'], ['178', '内蒙古大学', '30.1'], ['178', '中国人民公安大学', '30.1'], ['183', '青岛科技大学', '30.0'], ['183', '西南石油大学', '30.0'], ['185', '武汉纺织大学', '29.9'], ['185', '中国民航大学', '29.9'], ['187', '华北理工大学', '29.8'], ['187', '南京林业大学', '29.8'], ['187', '西安建筑科技大学', '29.8'], ['190', '北方工业大学', '29.7'], ['190', '河北科技大学', '29.7'], ['190', '上海电力大学', '29.7'], ['193', '安徽师范大学', '29.6'], ['193', '哈尔滨师范大学', '29.6'], ['193', '湖南农业大学', '29.6'], ['193', '上海海洋大学', '29.6'], ['193', '上海立信会计金融学院', '29.6'], ['193', '四川师范大学', '29.6'], ['199', '辽宁工业大学', '29.5'], ['200', '沈阳航空航天大学', '29.4'], ['201', '湖南工业大学', '29.3'], ['202', '江西师范大学', '29.2'], ['202', '西华师范大学', '29.2'], ['204', '福建农林大学', '29.1'], ['204', '天津理工大学', '29.1'], ['206', '安徽农业大学', '29.0'], ['206', '兰州交通大学', '29.0'], ['206', '陕西科技大学', '29.0'], ['209', '集美大学', '28.9'], ['210', '长春理工大学', '28.8'], ['210', '重庆交通大学', '28.8'], ['210', '中南林业科技大学', '28.8'], ['213', '重庆师范大学', '28.7'], ['213', '湖南科技大学', '28.7'], ['213', '江汉大学', '28.7'], ['216', '成都理工大学', '28.6'], ['216', '河南理工大学', '28.6'], ['216', '辽宁师范大学', '28.6'], ['219', '南华大学', '28.5'], ['220', '长江大学', '28.4'], ['220', '重庆理工大学', '28.4'], ['220', '武汉轻工大学', '28.4'], ['220', '云南师范大学', '28.4'], ['224', '闽南师范大学', '28.3'], ['224', '山西财经大学', '28.3'], ['226', '河南工业大学', '28.2'], ['226', '湖州师范学院', '28.2'], ['226', '西安邮电大学', '28.2'], ['229', '广西民族大学', '28.1'], ['229', '湖北经济学院', '28.1'], ['229', '山西师范大学', '28.1'], ['229', '苏州科技大学', '28.1'], ['229', '天津科技大学', '28.1'], ['234', '湖北第二师范学院', '28.0'], ['234', '吉林师范大学', '28.0'], ['234', '郑州师范学院', '28.0'], ['237', '哈尔滨理工大学', '27.9'], ['237', '河北农业大学', '27.9'], ['237', '吉首大学', '27.9'], ['240', '北京信息科技大学', '27.8'], ['240', '西北师范大学', '27.8'], ['240', '浙江外国语学院', '27.8'], ['240', '中北大学', '27.8'], ['244', '贵州大学', '27.7'], ['244', '湖南商学院', '27.7'], ['246', '河南财经政法大学', '27.6'], ['246', '淮北师范大学', '27.6'], ['246', '沈阳农业大学', '27.6'], ['246', '浙江海洋大学', '27.6'], ['250', '东莞理工学院', '27.5'], ['250', '湖北师范大学', '27.5'], ['250', '昆明理工大学', '27.5'], ['250', '西南民族大学', '27.5'], ['254', '上海第二工业大学', '27.4'], ['254', '上海应用技术大学', '27.4'], ['256', '绍兴文理学院', '27.3'], ['257', '东北电力大学', '27.2'], ['257', '桂林电子科技大学', '27.2'], ['257', '浙江传媒学院', '27.2'], ['260', '河北经贸大学', '27.1'], ['260', '河南农业大学', '27.1'], ['262', '东北石油大学', '27.0'], ['262', '石河子大学', '27.0'], ['264', '兰州理工大学', '26.9'], ['265', '广西财经学院', '26.8'], ['265', '西安工业大学', '26.8'], ['265', '浙江科技学院', '26.8'], ['268', '安徽理工大学', '26.7'], ['268', '大连民族大学', '26.7'], ['268', '新疆大学', '26.7'], ['268', '烟台大学', '26.7'], ['268', '延边大学', '26.7'], ['273', '长沙学院', '26.6'], ['273', '大连交通大学', '26.6'], ['275', '吉林财经大学', '26.5'], ['275', '青岛理工大学', '26.5'], ['275', '上海工程技术大学', '26.5'], ['275', '西安科技大学', '26.5'], ['279', '长春工业大学', '26.4'], ['279', '桂林理工大学', '26.4'], ['279', '河南科技大学', '26.4'], ['279', '淮阴师范学院', '26.4'], ['279', '西南科技大学', '26.4'], ['284', '佛山科学技术学院', '26.3'], ['284', '南京工程学院', '26.3'], ['284', '宁夏大学', '26.3'], ['287', '广东技术师范大学', '26.2'], ['287', '河北工程大学', '26.2'], ['287', '黄冈师范学院', '26.2'], ['287', '南京晓庄学院', '26.2'], ['287', '沈阳建筑大学', '26.2'], ['287', '西安工程大学', '26.2'], ['293', '大理大学', '26.1'], ['293', '大连大学', '26.1'], ['295', '湖北民族大学', '25.9'], ['295', '华东交通大学', '25.9'], ['295', '嘉兴学院', '25.9'], ['295', '闽江学院', '25.9'], ['295', '青海大学', '25.9'], ['300', '大连工业大学', '25.8'], ['300', '河北地质大学', '25.8'], ['300', '天津商业大学', '25.8'], ['300', '玉林师范学院', '25.8'], ['300', '中国人民武装警察部队学院', '25.8'], ['305', '北京印刷学院', '25.7'], ['305', '广东金融学院', '25.7'], ['305', '南宁师范大学', '25.7'], ['305', '沈阳师范大学', '25.7'], ['305', '厦门理工学院', '25.7'], ['310', '成都信息工程大学', '25.5'], ['310', '沈阳工业大学', '25.5'], ['310', '云南财经大学', '25.5'], ['313', '安徽建筑大学', '25.4'], ['313', '哈尔滨商业大学', '25.4'], ['313', '黑龙江工程学院', '25.4'], ['313', '湖北工程学院', '25.4'], ['313', '江苏理工学院', '25.4'], ['313', '郑州轻工业大学', '25.4'], ['319', '长春师范大学', '25.3'], ['319', '湖南第一师范学院', '25.3'], ['319', '吉林农业大学', '25.3'], ['319', '太原科技大学', '25.3'], ['319', '太原师范学院', '25.3'], ['324', '常熟理工学院', '25.2'], ['324', '广东石油化工学院', '25.2'], ['324', '海南师范大学', '25.2'], ['324', '华北水利水电大学', '25.2'], ['324', '宁波工程学院', '25.2'], ['324', '西安石油大学', '25.2'], ['324', '西华大学', '25.2'], ['331', '河北科技师范学院', '25.1'], ['331', '湖南城市学院', '25.1'], ['331', '内蒙古工业大学', '25.1'], ['331', '山东农业大学', '25.1'], ['331', '延安大学', '25.1'], ['336', '大连海洋大学', '25.0'], ['336', '广东第二师范学院', '25.0'], ['336', '河北北方学院', '25.0'], ['336', '五邑大学', '25.0'], ['336', '西安财经大学', '25.0'], ['341', '重庆文理学院', '24.9'], ['341', '贵州师范学院', '24.9'], ['343', '宝鸡文理学院', '24.8'], ['343', '南昌航空大学', '24.8'], ['343', '山西大同大学', '24.8'], ['343', '山西农业大学', '24.8'], ['343', '信阳师范学院', '24.8'], ['348', '广东海洋大学', '24.7'], ['349', '湖南工程学院', '24.6'], ['350', '山东理工大学', '24.5'], ['351', '北华航天工业学院', '24.4'], ['351', '湖北汽车工业学院', '24.4'], ['351', '湖南理工学院', '24.4'], ['351', '浙江大学城市学院', '24.4'], ['355', '聊城大学', '24.3'], ['355', '中国民用航空飞行学院', '24.3'], ['357', '安徽工程大学', '24.2'], ['357', '北华大学', '24.2'], ['357', '辽宁工程技术大学', '24.2'], ['357', '南阳师范学院', '24.2'], ['357', '盐城师范学院', '24.2'], ['362', '成都大学', '24.1'], ['362', '福建工程学院', '24.1'], ['362', '陕西理工大学', '24.1'], ['365', '兰州城市学院', '24.0'], ['365', '鲁东大学', '24.0'], ['365', '武汉体育学院', '24.0'], ['365', '徐州工程学院', '24.0'], ['369', '黑龙江科技大学', '23.9'], ['369', '湖北科技学院', '23.9'], ['369', '湖北文理学院', '23.9'], ['372', '北京联合大学', '23.8'], ['372', '江苏第二师范学院', '23.8'], ['372', '江西科技师范大学', '23.8'], ['372', '江西理工大学', '23.8'], ['372', '齐齐哈尔大学', '23.8'], ['372', '韶关学院', '23.8'], ['372', '西安文理学院', '23.8'], ['379', '长春大学', '23.7'], ['379', '洛阳理工学院', '23.7'], ['379', '山东建筑大学', '23.7'], ['382', '沈阳理工大学', '23.6'], ['382', '盐城工学院', '23.6'], ['384', '北京农学院', '23.5'], ['384', '河南科技学院', '23.5'], ['384', '洛阳师范学院', '23.5'], ['384', '内江师范学院', '23.5'], ['384', '沈阳化工大学', '23.5'], ['384', '忻州师范学院', '23.5'], ['384', '运城学院', '23.5'], ['391', '甘肃农业大学', '23.4'], ['391', '广东财经大学', '23.4'], ['391', '湖南财政经济学院', '23.4'], ['391', '湖南文理学院', '23.4'], ['391', '金陵科技学院', '23.4'], ['391', '岭南师范学院', '23.4'], ['391', '内蒙古农业大学', '23.4'], ['391', '齐鲁工业大学', '23.4'], ['391', '上海电机学院', '23.4'], ['391', '上海体育学院', '23.4'], ['401', '辽宁科技大学', '23.3'], ['401', '青岛农业大学', '23.3'], ['401', '新疆师范大学', '23.3'], ['401', '仲恺农业工程学院', '23.3'], ['405', '安康学院', '23.2'], ['405', '赣南师范大学', '23.2'], ['405', '淮海工学院', '23.2'], ['405', '临沂大学', '23.2'], ['405', '泉州师范学院', '23.2'], ['405', '唐山学院', '23.2'], ['405', '通化师范学院', '23.2'], ['412', '北京服装学院', '23.1'], ['412', '合肥学院', '23.1'], ['412', '江西农业大学', '23.1'], ['412', '沈阳大学', '23.1'], ['416', '湖北理工学院', '23.0'], ['416', '淮阴工学院', '23.0'], ['416', '曲靖师范学院', '23.0'], ['419', '安庆师范大学', '22.9'], ['419', '惠州学院', '22.9'], ['419', '佳木斯大学', '22.9'], ['422', '鞍山师范学院', '22.8'], ['422', '衡阳师范学院', '22.8'], ['422', '沈阳工程学院', '22.8'], ['422', '石家庄学院', '22.8'], ['422', '四川轻化工大学', '22.8'], ['422', '肇庆学院', '22.8'], ['428', '黄山学院', '22.7'], ['428', '皖西学院', '22.7'], ['430', '安阳师范学院', '22.6'], ['430', '北京石油化工学院', '22.6'], ['430', '龙岩学院', '22.6'], ['430', '内蒙古科技大学', '22.6'], ['434', '河南工程学院', '22.5'], ['434', '天津城建大学', '22.5'], ['436', '北部湾大学', '22.4'], ['437', '长江师范学院', '22.3'], ['437', '吉林化工学院', '22.3'], ['437', '吉林建筑大学', '22.3'], ['437', '景德镇陶瓷大学', '22.3'], ['437', '云南民族大学', '22.3'], ['442', '辽宁石油化工大学', '22.2'], ['443', '广西科技大学', '22.1'], ['443', '哈尔滨学院', '22.1'], ['443', '山东工商学院', '22.1'], ['443', '太原工业学院', '22.1'], ['443', '郑州航空工业管理学院', '22.1'], ['448', '常州工学院', '22.0'], ['448', '重庆科技学院', '22.0'], ['448', '华北科技学院', '22.0'], ['448', '廊坊师范学院', '22.0'], ['448', '内蒙古民族大学', '22.0'], ['448', '西南林业大学', '22.0'], ['448', '咸阳师范学院', '22.0'], ['448', '湘南学院', '22.0'], ['448', '云南农业大学', '22.0'], ['457', '北方民族大学', '21.9'], ['458', '贵州师范大学', '21.8'], ['458', '天津农学院', '21.8'], ['460', '福建江夏学院', '21.7'], ['460', '合肥师范学院', '21.7'], ['460', '青海师范大学', '21.7'], ['463', '重庆第二师范学院', '21.6'], ['463', '丽水学院', '21.6'], ['463', '南昌工程学院', '21.6'], ['463', '齐鲁师范学院', '21.6'], ['463', '天津职业技术师范大学', '21.6'], ['463', '新乡学院', '21.6'], ['469', '内蒙古师范大学', '21.5'], ['469', '渭南师范学院', '21.5'], ['471', '河南牧业经济学院', '21.4'], ['471', '井冈山大学', '21.4'], ['473', '韩山师范学院', '21.3'], ['473', '河南城建学院', '21.3'], ['473', '贺州学院', '21.3'], ['473', '西北民族大学', '21.3'], ['473', '邢台学院', '21.3'], ['478', '安阳工学院', '21.2'], ['478', '贵州财经大学', '21.2'], ['478', '河西学院', '21.2'], ['478', '昆明学院', '21.2'], ['478', '乐山师范学院', '21.2'], ['483', '山东交通学院', '21.1'], ['483', '玉溪师范学院', '21.1'], ['485', '东华理工大学', '21.0'], ['485', '嘉应学院', '21.0'], ['485', '荆楚理工学院', '21.0'], ['485', '商洛学院', '21.0'], ['489', '贵州民族大学', '20.8'], ['489', '黑龙江八一农垦大学', '20.8'], ['489', '绵阳师范学院', '20.8'], ['489', '牡丹江师范学院', '20.8'], ['489', '浙江万里学院', '20.8'], ['494', '防灾科技学院', '20.6'], ['494', '宜宾学院', '20.6'], ['494', '中原工学院', '20.6'], ['497', '周口师范学院', '20.4'], ['498', '重庆三峡学院', '20.3'], ['498', '济宁学院', '20.3'], ['498', '泰山学院', '20.3'], ['498', '西安航空学院', '20.3'], ['498', '浙江水利水电学院', '20.3'], ['503', '辽东学院', '20.1'], ['503', '新疆农业大学', '20.1'], ['505', '滨州学院', '20.0'], ['506', '长春工程学院', '19.9'], ['507', '赤峰学院', '19.8'], ['507', '南阳理工学院', '19.8'], ['509', '成都工业学院', '19.6'], ['509', '四川文理学院', '19.6'], ['509', '天水师范学院', '19.6'], ['512', '黄淮学院', '19.5'], ['512', '铜陵学院', '19.5'], ['514', '湖南工学院', '19.4'], ['514', '湖南科技学院', '19.4'], ['514', '九江学院', '19.4'], ['514', '邵阳学院', '19.4'], ['514', '许昌学院', '19.4'], ['519', '西藏大学', '19.3'], ['520', '桂林航天工业学院', '19.2'], ['520', '衢州学院', '19.2'], ['520', '商丘师范学院', '19.2'], ['520', '铜仁学院', '19.2'], ['524', '红河学院', '19.0'], ['524', '怀化学院', '19.0'], ['524', '塔里木大学', '19.0'], ['527', '池州学院', '18.9'], ['528', '滁州学院', '18.8'], ['529', '安徽科技学院', '18.7'], ['529', '贵阳学院', '18.7'], ['529', '潍坊学院', '18.7'], ['529', '宜春学院', '18.7'], ['533', '淮南师范学院', '18.6'], ['534', '楚雄师范学院', '18.3'], ['534', '贵州理工学院', '18.3'], ['536', '巢湖学院', '18.2'], ['537', '德州学院', '18.0'], ['538', '攀枝花学院', '17.9'], ['539', '伊犁师范大学', '17.7'], ['539', '榆林学院', '17.7'], ['541', '陇东学院', '17.5'], ['542', '西京学院', '17.3'], ['543', '邯郸学院', '17.2'], ['544', '海南热带海洋学院', '17.1'], ['544', '莆田学院', '17.1'], ['544', '枣庄学院', '17.1'], ['547', '浙江树人学院', '16.7'], ['548', '平顶山学院', '16.0'], ['549', '湖南涉外经济学院', '15.5']]
    

x.field_names=["排名","学校名称","总分"] 
for i in range(10):       
    x.add_row(ulist[i])
print(x)
    
