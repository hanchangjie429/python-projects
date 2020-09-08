from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pyautogui
import time
import requests
import json



browser = webdriver.Chrome()
browser.get('https://login.yahoo.com/')

input_email = pyautogui.prompt(
    text='请输入邮箱', title='邮箱', default='hanchangjie429@outlook.com')
input_password = pyautogui.password(
    text='请输入密码', title='密码', default='', mask='*')
# input_email = 'hanchangjie429@outlook.com'
# input_password = '*********'

email = browser.find_element_by_xpath('//*[@id="login-username"]')
email.send_keys(f'{input_email}')

item1 = browser.find_element_by_xpath('//*[@id="login-signin"]')
item1.click()

time.sleep(2)
password = browser.find_element_by_xpath('//*[@id="login-passwd"]')
password.send_keys(f'{input_password}')

item2 = browser.find_element_by_xpath('//*[@id="login-signin"]')
item2.click()


def wait_until_verified():
    # verify_url = 'https://login.yahoo.com/account/challenge/challenge-selector?src=noSrc&authMechanism=primary&display=login&done=https%3A%2F%2Fwww.yahoo.com%2F&acrumb=BG8n9Zc6&sessionIndex=QQ--'
    # verify_by_phone_url = 'https://login.yahoo.com/account/challenge/phone-verify?src=noSrc&authMechanism=primary&display=login&done=https%3A%2F%2Fwww.yahoo.com%2F&acrumb=BG8n9Zc6&sessionIndex=QQ--'
    # verified_url = 'https://www.yahoo.com/?guccounter=1&guce_referrer=aHR0cHM6Ly9sb2dpbi55YWhvby5jb20v&guce_referrer_sig=AQAAAFCbuR-7Trd9F7chhoRM5UbFfDi2NQQAKfjFirmz5A8nrEx5_Z3I8zp4w2rzSXPx5a6n8xNw50NXQidf_AlgR-0nmqTkuZJ8HmeW8o1cfLIGRc0n7aAj6MNeYN0kBLQAjekk8twY0wtVfqTd5b2LtQQ3wCQ_-NGN2Ml1AH8r-fU2'
    condition = True
    while condition:
        if 'challenge-selector' in browser.current_url:
            time.sleep(2)
            # print(browser.current_url)
        elif 'phone-verify' in browser.current_url:
            time.sleep(2)
            # print(browser.current_url)
        else:
            condition = False


wait_until_verified()


# time.sleep(20)
# url = browser.current_url
# while browser.current_url != url:
# 	time.sleep(1)
browser.get('https://finance.yahoo.com/quote/AAPL/financials?p=AAPL')
# print(browser.execute_script('return document.cookie'))


def get_cookie():
    # 自动获取cookies
    cookies_list = browser.get_cookies()
    cookies_dict = {}
    for cookie in cookies_list:
        cookies_dict[cookie['name']] = cookie['value']
    cookies = cookies_dict
    return cookies

cookies = get_cookie()
# print(cookies)

income_statement_url = 'https://query2.finance.yahoo.com/ws/fundamentals-timeseries/v1/finance/premium/timeseries/AAPL?lang=en-US&region=US&symbol=AAPL&padTimeSeries=true&type=quarterlyTaxEffectOfUnusualItems%2CtrailingTaxEffectOfUnusualItems%2CquarterlyTaxRateForCalcs%2CtrailingTaxRateForCalcs%2CquarterlyNormalizedEBITDA%2CtrailingNormalizedEBITDA%2CquarterlyNormalizedDilutedEPS%2CtrailingNormalizedDilutedEPS%2CquarterlyNormalizedBasicEPS%2CtrailingNormalizedBasicEPS%2CquarterlyTotalUnusualItems%2CtrailingTotalUnusualItems%2CquarterlyTotalUnusualItemsExcludingGoodwill%2CtrailingTotalUnusualItemsExcludingGoodwill%2CquarterlyNetIncomeFromContinuingOperationNetMinorityInterest%2CtrailingNetIncomeFromContinuingOperationNetMinorityInterest%2CquarterlyReconciledDepreciation%2CtrailingReconciledDepreciation%2CquarterlyReconciledCostOfRevenue%2CtrailingReconciledCostOfRevenue%2CquarterlyEBITDA%2CtrailingEBITDA%2CquarterlyEBIT%2CtrailingEBIT%2CquarterlyNetInterestIncome%2CtrailingNetInterestIncome%2CquarterlyInterestExpense%2CtrailingInterestExpense%2CquarterlyInterestIncome%2CtrailingInterestIncome%2CquarterlyContinuingAndDiscontinuedDilutedEPS%2CtrailingContinuingAndDiscontinuedDilutedEPS%2CquarterlyContinuingAndDiscontinuedBasicEPS%2CtrailingContinuingAndDiscontinuedBasicEPS%2CquarterlyNormalizedIncome%2CtrailingNormalizedIncome%2CquarterlyNetIncomeFromContinuingAndDiscontinuedOperation%2CtrailingNetIncomeFromContinuingAndDiscontinuedOperation%2CquarterlyTotalExpenses%2CtrailingTotalExpenses%2CquarterlyRentExpenseSupplemental%2CtrailingRentExpenseSupplemental%2CquarterlyReportedNormalizedDilutedEPS%2CtrailingReportedNormalizedDilutedEPS%2CquarterlyReportedNormalizedBasicEPS%2CtrailingReportedNormalizedBasicEPS%2CquarterlyTotalOperatingIncomeAsReported%2CtrailingTotalOperatingIncomeAsReported%2CquarterlyDividendPerShare%2CtrailingDividendPerShare%2CquarterlyDilutedAverageShares%2CtrailingDilutedAverageShares%2CquarterlyBasicAverageShares%2CtrailingBasicAverageShares%2CquarterlyDilutedEPS%2CtrailingDilutedEPS%2CquarterlyDilutedEPSOtherGainsLosses%2CtrailingDilutedEPSOtherGainsLosses%2CquarterlyTaxLossCarryforwardDilutedEPS%2CtrailingTaxLossCarryforwardDilutedEPS%2CquarterlyDilutedAccountingChange%2CtrailingDilutedAccountingChange%2CquarterlyDilutedExtraordinary%2CtrailingDilutedExtraordinary%2CquarterlyDilutedDiscontinuousOperations%2CtrailingDilutedDiscontinuousOperations%2CquarterlyDilutedContinuousOperations%2CtrailingDilutedContinuousOperations%2CquarterlyBasicEPS%2CtrailingBasicEPS%2CquarterlyBasicEPSOtherGainsLosses%2CtrailingBasicEPSOtherGainsLosses%2CquarterlyTaxLossCarryforwardBasicEPS%2CtrailingTaxLossCarryforwardBasicEPS%2CquarterlyBasicAccountingChange%2CtrailingBasicAccountingChange%2CquarterlyBasicExtraordinary%2CtrailingBasicExtraordinary%2CquarterlyBasicDiscontinuousOperations%2CtrailingBasicDiscontinuousOperations%2CquarterlyBasicContinuousOperations%2CtrailingBasicContinuousOperations%2CquarterlyDilutedNIAvailtoComStockholders%2CtrailingDilutedNIAvailtoComStockholders%2CquarterlyAverageDilutionEarnings%2CtrailingAverageDilutionEarnings%2CquarterlyNetIncomeCommonStockholders%2CtrailingNetIncomeCommonStockholders%2CquarterlyOtherunderPreferredStockDividend%2CtrailingOtherunderPreferredStockDividend%2CquarterlyPreferredStockDividends%2CtrailingPreferredStockDividends%2CquarterlyNetIncome%2CtrailingNetIncome%2CquarterlyMinorityInterests%2CtrailingMinorityInterests%2CquarterlyNetIncomeIncludingNoncontrollingInterests%2CtrailingNetIncomeIncludingNoncontrollingInterests%2CquarterlyNetIncomeFromTaxLossCarryforward%2CtrailingNetIncomeFromTaxLossCarryforward%2CquarterlyNetIncomeExtraordinary%2CtrailingNetIncomeExtraordinary%2CquarterlyNetIncomeDiscontinuousOperations%2CtrailingNetIncomeDiscontinuousOperations%2CquarterlyNetIncomeContinuousOperations%2CtrailingNetIncomeContinuousOperations%2CquarterlyEarningsFromEquityInterestNetOfTax%2CtrailingEarningsFromEquityInterestNetOfTax%2CquarterlyTaxProvision%2CtrailingTaxProvision%2CquarterlyPretaxIncome%2CtrailingPretaxIncome%2CquarterlyOtherIncomeExpense%2CtrailingOtherIncomeExpense%2CquarterlyOtherNonOperatingIncomeExpenses%2CtrailingOtherNonOperatingIncomeExpenses%2CquarterlySpecialIncomeCharges%2CtrailingSpecialIncomeCharges%2CquarterlyGainOnSaleOfPPE%2CtrailingGainOnSaleOfPPE%2CquarterlyGainOnSaleOfBusiness%2CtrailingGainOnSaleOfBusiness%2CquarterlyOtherSpecialCharges%2CtrailingOtherSpecialCharges%2CquarterlyWriteOff%2CtrailingWriteOff%2CquarterlyImpairmentOfCapitalAssets%2CtrailingImpairmentOfCapitalAssets%2CquarterlyRestructuringAndMergernAcquisition%2CtrailingRestructuringAndMergernAcquisition%2CquarterlySecuritiesAmortization%2CtrailingSecuritiesAmortization%2CquarterlyEarningsFromEquityInterest%2CtrailingEarningsFromEquityInterest%2CquarterlyGainOnSaleOfSecurity%2CtrailingGainOnSaleOfSecurity%2CquarterlyNetNonOperatingInterestIncomeExpense%2CtrailingNetNonOperatingInterestIncomeExpense%2CquarterlyTotalOtherFinanceCost%2CtrailingTotalOtherFinanceCost%2CquarterlyInterestExpenseNonOperating%2CtrailingInterestExpenseNonOperating%2CquarterlyInterestIncomeNonOperating%2CtrailingInterestIncomeNonOperating%2CquarterlyOperatingIncome%2CtrailingOperatingIncome%2CquarterlyOperatingExpense%2CtrailingOperatingExpense%2CquarterlyOtherOperatingExpenses%2CtrailingOtherOperatingExpenses%2CquarterlyOtherTaxes%2CtrailingOtherTaxes%2CquarterlyProvisionForDoubtfulAccounts%2CtrailingProvisionForDoubtfulAccounts%2CquarterlyDepreciationAmortizationDepletionIncomeStatement%2CtrailingDepreciationAmortizationDepletionIncomeStatement%2CquarterlyDepletionIncomeStatement%2CtrailingDepletionIncomeStatement%2CquarterlyDepreciationAndAmortizationInIncomeStatement%2CtrailingDepreciationAndAmortizationInIncomeStatement%2CquarterlyAmortization%2CtrailingAmortization%2CquarterlyAmortizationOfIntangiblesIncomeStatement%2CtrailingAmortizationOfIntangiblesIncomeStatement%2CquarterlyDepreciationIncomeStatement%2CtrailingDepreciationIncomeStatement%2CquarterlyResearchAndDevelopment%2CtrailingResearchAndDevelopment%2CquarterlySellingGeneralAndAdministration%2CtrailingSellingGeneralAndAdministration%2CquarterlySellingAndMarketingExpense%2CtrailingSellingAndMarketingExpense%2CquarterlyGeneralAndAdministrativeExpense%2CtrailingGeneralAndAdministrativeExpense%2CquarterlyOtherGandA%2CtrailingOtherGandA%2CquarterlyInsuranceAndClaims%2CtrailingInsuranceAndClaims%2CquarterlyRentAndLandingFees%2CtrailingRentAndLandingFees%2CquarterlySalariesAndWages%2CtrailingSalariesAndWages%2CquarterlyGrossProfit%2CtrailingGrossProfit%2CquarterlyCostOfRevenue%2CtrailingCostOfRevenue%2CquarterlyTotalRevenue%2CtrailingTotalRevenue%2CquarterlyExciseTaxes%2CtrailingExciseTaxes%2CquarterlyOperatingRevenue%2CtrailingOperatingRevenue&merge=false&period1=493590046&period2=1599240716&corsDomain=finance.yahoo.com'


def retrieve_result(income_statement_url):

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
        'origin': 'https://finance.yahoo.com',
        'referer': 'https://finance.yahoo.com'
    }

    # 手动复制cookies
    # cookies = {'cookie':'F=d=IchBWac9vEtuGqOtqq.91WlcLFNJHQK1LtZCwuFqKfzW_fH2CIqwlJKMo.5A3g--; AO=u=1; PRF=t%3DAAPL; OTH=v=1&d=eyJraWQiOiIwMTY0MGY5MDNhMjRlMWMxZjA5N2ViZGEyZDA5YjE5NmM5ZGUzZWQ5IiwiYWxnIjoiUlMyNTYifQ.eyJjdSI6eyJndWlkIjoiUlY3U0RQTjVINlQ0SUdaMlZMNlZSQzZORUEiLCJwZXJzaXN0ZW50Ijp0cnVlLCJzaWQiOiJNZmE4d05tcHVpZWcifX0.jGmwAbwhr7UnIh2R-AJgy4eIXBzXcvVhU1Sfqbl2e5z3Fk2y7rV3CkaimX283uEa2-iIV3zm8R1muZVY72z7AzwAg4kBhUARyfIC3yntsM9bOZsMpZS2b6zIDGczT0tkAdLwfV3dMoloTx4Jhr42-0rIa8tlkNHaQgIqtBB0bBg; T=af=JnRzPTE1OTkyNDE2NTEmcHM9RGZWcFJrNDdwLnExb3l1TXdnSDdjZy0t&d=bnMBeWFob28BZwFSVjdTRFBONUg2VDRJR1oyVkw2VlJDNk5FQQFhYwFBS2Y4WFkubQFhbAFoYW5jaGFuZ2ppZTQyOUBvdXRsb29rLmNvbQFzYwFkZXNrdG9wX3dlYgFmcwFNQm9ZdFdCZlVudUoBenoBejJuVWZCQTdFAWEBUUFFAWxhdAF6Mm5VZkI-&sk=DAAymuPD3RQBRm&ks=EAA7cCZBdCl2W3DRToQudoDDg--~G&kt=EAAF2ES.XGJP2LOlRS051ZnYQ--~I&ku=FAAPZTEPuhlOAuqdHFEgSONCp10_.zz8itfU1uXA2W9oDdpB42ATR0FTJdLUnnAt9mM3AVbIvBgoh_y7esvFZhgFVS.SjJiCI7p584bm65moNixAxTzzj_Xk_6El1UrD94XawTaa_G4QP5VgyKr54IHGxRBBnq3WQRHo71bL_CR.Eg-~D; PH=fn=E0.ZmN7EF_WV6OU1KW9z_kU0tEn84OU-&l=zh-Hans-CN&i=us; Y=v=1&n=2a4dd0n0h66ac&l=hal10ppsxv8novkmd9gvuaf4j7668v661fl3tjf1/o&p=m30000000000000&r=108&intl=us; GUCS=AZ9c-vSk; A1=d=AQABBHd7Ul8CEIcYMtMsslxXJmHujRTTnQEFEgEAAgLBU18-YNxF0iMA_SMAAAcId3tSXxTTnQEIDxd3HCojOMFkEA-t40FtNgkBBwoBlQ&S=AQAAArgo6NhOyul3Su9-ANP33MU; A3=d=AQABBHd7Ul8CEIcYMtMsslxXJmHujRTTnQEFEgEAAgLBU18-YNxF0iMA_SMAAAcId3tSXxTTnQEIDxd3HCojOMFkEA-t40FtNgkBBwoBlQ&S=AQAAArgo6NhOyul3Su9-ANP33MU; A1S=d=AQABBHd7Ul8CEIcYMtMsslxXJmHujRTTnQEFEgEAAgLBU18-YNxF0iMA_SMAAAcId3tSXxTTnQEIDxd3HCojOMFkEA-t40FtNgkBBwoBlQ&S=AQAAArgo6NhOyul3Su9-ANP33MU&j=US; B=037ej2hfl4urn&b=4&d=Ffllbt5tYFrPn8miCffi&s=9f&i=F3ccKiM4wWQQD63jQW02; GUC=AQEAAgJfU8FgPkIbUwRf'}

    response = requests.get(income_statement_url,
                            headers=headers, cookies=cookies)
    result = response.json()
    print(json.dumps(result, indent=4))


def main():
    retrieve_result(income_statement_url)
    

if __name__ == '__main__':
    main()

'''
https://login.yahoo.com/account/challenge/challenge-selector?src=noSrc&authMechanism=primary&display=login&done=https%3A%2F%2Fwww.yahoo.com%2F&acrumb=BG8n9Zc6&sessionIndex=QQ--

https://login.yahoo.com/account/challenge/phone-verify?src=noSrc&authMechanism=primary&display=login&done=https%3A%2F%2Fwww.yahoo.com%2F&acrumb=BG8n9Zc6&sessionIndex=QQ--
'''
