#Using the results csv from beautiful.py to read each link

import pandas as pd
import requests
from bs4 import BeautifulSoup
import string
import re
from urllib.request import urlopen
 
all_results = pd.read_csv('C:/Users/J-Why/Desktop/Projects/Python/KLSE_Trade/Results/All_Bursa.csv')

print(list(all_results))
print(all_results['LINK'][0])

"""Market Capital (RM) : MainContent_lbFinancialInfo_Capital
Number of Share : MainContent_lbNumberOfShare
EPS (cent) : MainContent_lbFinancialInfo_EPS
P/E Ratio : MainContent_lbFinancialInfo_PE
ROE (%) : MainContent_lbFinancialInfo_ROE"""
"""
Dividend (cent) : MainContent_lbFinancialInfo_Div
Dividend Yield (%) : MainContent_lbFinancialInfo_DY
Dividend Policy (%) : MainContent_lbFinancialInfo_Policy
NTA (RM) : MainContent_lbFinancialInfo_NTA
Par Value (RM) : MainContent_lbFinancialInfo_ParValue"""

web_main_link ="http://www.malaysiastock.biz"
labels_left = {"Market_Cap":"MainContent_lbFinancialInfo_Capital",
               "Num_of_Share":"MainContent_lbNumberOfShare",
               "EPS":"MainContent_lbFinancialInfo_EPS",
               "P/E":"MainContent_lbFinancialInfo_PE",
               "ROE":"MainContent_lbFinancialInfo_ROE"}
labels_right = {"Dividend":"MainContent_lbFinancialInfo_Div",
                "Dividend_Yield":"MainContent_lbFinancialInfo_DY",
                "Dividend_Policy":"MainContent_lbFinancialInfo_Policy",
                "NTA":"MainContent_lbFinancialInfo_NTA",
                "Par_Value":"MainContent_lbFinancialInfo_ParValue"}


def find_string_id(string, id_find = "corporateInfoLeft2"):
    find_string_corp = string.find(id=id_find)
    if find_string_corp:
        return find_string_corp
    
def find_label_id(string, label_id_find):
    find_label = string.find(id=label_id_find)
    if find_label:
        return find_label

all_return=[]    
characters_remove = ':*(){}" '    
for ind, link_ in enumerate(all_results["LINK"]):#[:6]):#.head(1):
    full_link = web_main_link + "/" + link_
    _return_row_ = {}
    _return_row_["EQUITY"]=all_results["EQUITY"][ind]
    page = urlopen(full_link).read()
    soup = BeautifulSoup(page, 'html.parser')
    #corpinfo = soup.find_all('div',class_="corporateInfoField")
    corpinfo = soup.find_all(class_="corporateInfo")
    for co in corpinfo:
        corporateInfoLeft2 = find_string_id(co, "corporateInfoLeft2")
        if corporateInfoLeft2:
            break
    for co in corpinfo:
        corporateInfoRight2 = find_string_id(co,"corporateInfoRight2")
        if corporateInfoRight2:
            break
             
    for ll, llval in labels_left.items():
        _return_row_[ll]=find_label_id(corporateInfoLeft2, llval).get_text().strip(':* ')
        if _return_row_[ll]:
                next
    for lr,lrval in labels_right.items():
        _return_row_[lr]=find_label_id(corporateInfoRight2, lrval).get_text().strip(':* ')
        if _return_row_[lr]:
                next
    
    all_return.append(copy.deepcopy(_return_row_))
    _return_row_ = None
                
print(all_return)  
pd.DataFrame(all_return).to_csv('C:/Users/J-Why/Desktop/Projects/Python/KLSE_Trade/Results/Equity_today.csv')
                
    #corp_info_left2 = corporateInfoLeft2.find_all(class_="corporateInfoField")
    #corp_info_right2 = corporateInfoRight2.find_all(class_="corporateInfoField")
    