# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 17:36:57 2015

@author: Евгений
"""
path = """
Производство транспортных средств и оборудования  / Manufacture of  transport equipment												
отчетный месяц в % к предыдущему месяцу  / reporting month as percent of previous month												
2002	81,4	101,1	102,6	107,5	94,2	105,2	102,5	102,5	105,8	95,6	89,1	103,3
2003	85,0	107,8	120,7	107,6	91,0	110,8	105,7	95,1	104,3	103,8	90,7	114,7
2004	73,0	109,3	108,4	113,1	82,5	118,1	107,0	88,6	106,0	100,2	100,4	103,2
2005	68,4	120,3	123,6	92,0	93,6	113,1	103,4	96,5	103,6	105,0	100,7	114,7
2006	53,6	141,7	103,2	99,4	102,7	108,9	88,6	109,5	99,8	103,1	110,0	113,1
2007	65,3	111,2	109,6	101,8	101,5	98,1	96,1	100,5	104,4	100,6	123,8	104,4
2008	57,1	123,7	112,2	101,4	98,1	105,7	98,2	97,5	109,0	94,8	96,7	97,4
2009	39,0	145,7	126,3	94,7	90,9	104,2	111,1	80,6	120,8	110,7	112,5	120,2
2010	43,7	141,7	120,8	114,0	85,0	124,7	91,6	91,6	123,9	108,1	113,6	99,1
2011	55,7	124,0	119,8	98,5	94,2	114,4	87,3	109,7	115,0	100,5	110,2	113,9
2012	51,0	128,6	113,3	96,8	105,1	102,0	94,9	101,8	107,9	111,4	102,9	122,5
2013	45,4	120,9	122,8	97,7	88,3	125,2	87,9	114,2	101,8	102,2	122,7	111,3
2014	45,4	131,8	123,9	102,3	88,8	116,3	98,4	84,0	123,4	100,7	112,3	141,6
2015	31,1	126,3	139,8	83,8	94,6	115,8						
отчетный месяц в % к соответствующему месяцу предыдущего года  / reporting month as percent of corresponding month of previous year												
2002	101,4	102,2	89,2	106,9	102,0	106,8	96,8	110,0	105,4	99,4	85,1	87,9
2003	97,2	100,2	111,8	111,4	110,5	117,7	120,5	108,0	106,5	118,4	124,0	141,1
2004	114,9	120,2	114,2	120,4	106,7	111,9	114,1	110,0	111,7	105,7	113,4	99,5
2005	93,2	102,6	117,1	95,2	107,9	103,3	99,9	108,8	106,4	111,5	111,8	124,4
2006	97,6	114,9	95,9	103,6	113,8	109,5	93,8	106,4	102,5	100,6	109,8	108,2
2007	131,7	103,4	109,8	112,4	111,0	100,1	108,5	99,7	104,3	101,8	114,5	105,7
2008	92,4	102,8	105,3	104,9	101,4	109,2	111,5	108,1	112,9	106,4	83,1	77,5
2009	52,9	62,3	70,2	65,5	60,7	59,9	67,8	56,0	62,0	72,4	84,3	104,1
2010	116,7	113,5	108,5	130,6	122,1	146,2	120,5	137,0	140,5	137,2	138,5	114,2
2011	145,7	127,5	126,5	109,3	121,2	111,1	105,9	126,9	117,8	109,5	106,2	122,0
2012	111,6	115,8	109,5	107,7	120,1	107,1	116,5	108,1	101,4	112,4	105,0	112,9
2013	100,5	94,5	102,4	103,3	86,8	106,6	98,7	110,7	104,5	95,8	114,3	103,8
2014	103,8	113,2	114,2	119,6	118,3	111,7	122,0	90,9	111,4	109,8	95,5	91,0
2015	87,2	77,6	94,8	77,8	82,2	80,1						
	Янв. Jan.	Фев. Feb.	Март Mar.	Апр. Apr.	Май May	Июнь June	Июль July	Август Aug.	Сент. Sept.	Окт. Oct.	Нояб. Nov.	Дек. Dec.
период с начала отчетного года  в % к соответствующему периоду предыдущего года  / period from beginning of reporting year  as percent of corresponding period of previous year												
2002	101,4	101,8	97,1	99,6	100,0	101,2	100,5	101,6	102,1	101,8	100,1	99,0
2003	97,2	98,7	103,1	105,3	106,4	108,4	110,2	109,9	109,5	110,4	111,6	114,0
2004	114,9	117,6	116,4	117,5	115,3	114,6	114,5	113,9	113,7	112,8	112,8	111,5
2005	93,2	98,1	104,9	102,1	103,2	103,3	102,7	103,5	103,8	104,6	105,3	107,1
2006	97,6	107,0	102,5	102,8	105,0	105,9	103,9	104,2	104,0	103,6	104,3	104,7
2007	131,7	115,1	113,1	112,9	112,5	110,1	109,9	108,5	108,0	107,3	108,1	107,8
2008	92,4	97,9	100,6	101,7	101,7	103,0	104,2	104,7	105,7	105,7	103,1	100,4
2009	52,9	58,1	62,7	63,5	62,9	62,4	63,2	62,2	62,2	63,3	65,2	68,5
2010	116,7	114,8	112,1	117,5	118,4	123,4	122,9	124,6	145,4	127,8	129,1	127,2
2011	145,7	135,0	131,5	124,4	123,7	121,1	118,6	119,7	119,4	118,1	116,6	117,2
2012	111,6	113,9	112,2	110,9	112,8	111,7	112,4	111,8	110,4	110,7	110,0	110,3
2013	100,5	97,1	99,2	100,3	97,3	99,0	99,0	100,5	101,0	100,4	101,9	102,2
2014	103,8	108,9	111,0	113,4	114,8	114,2	114,8	111,8	111,8	111,6	110,1	108,5
2015	87,2	82,4	86,5	84,3	83,9	83,3						
"""

headline_dict = {
"Производство транспортных средств и оборудования":  ['PROD_TRANS','bln_rub']
 }
 
support_dict =    {
 "отчетный месяц в % к предыдущему месяцу" : 'rog',
 "отчетный месяц в % к соответствующему месяцу предыдущего года": 'yoy',
 "период с начала отчетного года" : 'from_jan'
 }

def yield_csv_rows(path):
    for row in path.split("\n"):
        yield row.split("\t")
        
from word import is_year


def get_label(text, lab_dict):
    for pat in lab_dict.keys():
        if pat in text: 
            return lab_dict[pat]
    else:
         return None  

def labelled_row_iter(path, full_dict, unit_dict):
    labels = ["unknown_var", "unknown_unit"]
    for row in yield_csv_rows(path):
         text = row[0]
         print("****", headline_dict)
         if len(text) > 0:
             print("****", headline_dict)
             if not is_year(text):
                 labels = [None, None]
                 print("****", headline_dict)
                 if get_label(text, full_dict) is not None:
                     labels[0], labels[1] = get_label(text, full_dict)
                     print("****", headline_dict)
                 elif get_label(text, unit_dict) is not None:
                     labels[1] = get_label(text, unit_dict)
                     print("Changed here?", headline_dict)
                 else:
                     labels = ["unknown_var", "unknown_unit"]
                     print("****", headline_dict)
             else:
                 yield(labels + row)
                 print("****", headline_dict)
         else:
             pass # there is nothing in row[0], len is 0

#for row in yield_csv_rows(path):
#    print (row)

    
print("Local copy")

print("****", headline_dict)
for row in labelled_row_iter(path, headline_dict, support_dict):
    if row[2] =='2015' and row[3] == '87,2':
       print (row) 
print("****", headline_dict)

print("\nFrom file")    
from word import load_spec, change_extension, make_labelled_csv
import os
r = os.path.abspath("data/minitab/minitab2.csv")
src_csv = r
label_dict2, sec_label_dict2 = load_spec(src_csv)

out_csv = change_extension(src_csv,"txt")
gen = labelled_row_iter(r, label_dict2, sec_label_dict2)
for row in gen:
    if row[2] =='2015' and row[3] == '87,2':
       print (row) 

print("\nVars")         
from pprint import pprint
key = [x for x in headline_dict.keys()][0]
pprint(headline_dict [key])
pprint(label_dict2[key])
pprint(support_dict)
pprint(sec_label_dict2)


headline_dict[key] == label_dict2[key] 