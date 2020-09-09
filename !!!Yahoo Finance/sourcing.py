from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

import pyautogui
import time
import requests
import json
import csv



def log_in():
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


def get_cookie():
    # 自动获取cookies
    cookies_list = browser.get_cookies()
    cookies_dict = {}
    for cookie in cookies_list:
        cookies_dict[cookie['name']] = cookie['value']
    cookies = cookies_dict
    return cookies

    # cookies = get_cookie()


def retrieve_result(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
        'origin': 'https://finance.yahoo.com',
        'referer': 'https://finance.yahoo.com'
    }
    # 手动复制cookies
    cookies = {'cookie': 'F=d=IchBWac9vEtuGqOtqq.91WlcLFNJHQK1LtZCwuFqKfzW_fH2CIqwlJKMo.5A3g--; AO=u=1; PRF=t%3DAAPL; OTH=v=1&d=eyJraWQiOiIwMTY0MGY5MDNhMjRlMWMxZjA5N2ViZGEyZDA5YjE5NmM5ZGUzZWQ5IiwiYWxnIjoiUlMyNTYifQ.eyJjdSI6eyJndWlkIjoiUlY3U0RQTjVINlQ0SUdaMlZMNlZSQzZORUEiLCJwZXJzaXN0ZW50Ijp0cnVlLCJzaWQiOiJNZmE4d05tcHVpZWcifX0.jGmwAbwhr7UnIh2R-AJgy4eIXBzXcvVhU1Sfqbl2e5z3Fk2y7rV3CkaimX283uEa2-iIV3zm8R1muZVY72z7AzwAg4kBhUARyfIC3yntsM9bOZsMpZS2b6zIDGczT0tkAdLwfV3dMoloTx4Jhr42-0rIa8tlkNHaQgIqtBB0bBg; T=af=JnRzPTE1OTkyNDE2NTEmcHM9RGZWcFJrNDdwLnExb3l1TXdnSDdjZy0t&d=bnMBeWFob28BZwFSVjdTRFBONUg2VDRJR1oyVkw2VlJDNk5FQQFhYwFBS2Y4WFkubQFhbAFoYW5jaGFuZ2ppZTQyOUBvdXRsb29rLmNvbQFzYwFkZXNrdG9wX3dlYgFmcwFNQm9ZdFdCZlVudUoBenoBejJuVWZCQTdFAWEBUUFFAWxhdAF6Mm5VZkI-&sk=DAAymuPD3RQBRm&ks=EAA7cCZBdCl2W3DRToQudoDDg--~G&kt=EAAF2ES.XGJP2LOlRS051ZnYQ--~I&ku=FAAPZTEPuhlOAuqdHFEgSONCp10_.zz8itfU1uXA2W9oDdpB42ATR0FTJdLUnnAt9mM3AVbIvBgoh_y7esvFZhgFVS.SjJiCI7p584bm65moNixAxTzzj_Xk_6El1UrD94XawTaa_G4QP5VgyKr54IHGxRBBnq3WQRHo71bL_CR.Eg-~D; PH=fn=E0.ZmN7EF_WV6OU1KW9z_kU0tEn84OU-&l=zh-Hans-CN&i=us; Y=v=1&n=2a4dd0n0h66ac&l=hal10ppsxv8novkmd9gvuaf4j7668v661fl3tjf1/o&p=m30000000000000&r=108&intl=us; GUCS=AZ9c-vSk; A1=d=AQABBHd7Ul8CEIcYMtMsslxXJmHujRTTnQEFEgEAAgLBU18-YNxF0iMA_SMAAAcId3tSXxTTnQEIDxd3HCojOMFkEA-t40FtNgkBBwoBlQ&S=AQAAArgo6NhOyul3Su9-ANP33MU; A3=d=AQABBHd7Ul8CEIcYMtMsslxXJmHujRTTnQEFEgEAAgLBU18-YNxF0iMA_SMAAAcId3tSXxTTnQEIDxd3HCojOMFkEA-t40FtNgkBBwoBlQ&S=AQAAArgo6NhOyul3Su9-ANP33MU; A1S=d=AQABBHd7Ul8CEIcYMtMsslxXJmHujRTTnQEFEgEAAgLBU18-YNxF0iMA_SMAAAcId3tSXxTTnQEIDxd3HCojOMFkEA-t40FtNgkBBwoBlQ&S=AQAAArgo6NhOyul3Su9-ANP33MU&j=US; B=037ej2hfl4urn&b=4&d=Ffllbt5tYFrPn8miCffi&s=9f&i=F3ccKiM4wWQQD63jQW02; GUC=AQEAAgJfU8FgPkIbUwRf'}

    response = requests.get(url,
                            headers=headers, cookies=cookies)
    result = response.json()

    return result


def structure_data(symbol, result):
    attribute_list = result['timeseries']['result']

    final_list = []

    headers = []

    for attribute_dict in attribute_list:
        attribute_name = attribute_dict['meta']['type'][0]

        if 'timestamp' not in attribute_dict:
            final_list.append([f'{attribute_name}'])

        else:
            timestamp = attribute_dict['timestamp']
            if len(timestamp) >= 10:
                attribute_value_list = attribute_dict[attribute_name]
                raw_data_list = []
                date_list = []

                for each_attribute_value in attribute_value_list:
                    if each_attribute_value == None:
                        raw_data_list.append('null')
                        date_list.append('null')
                    else:
                        date = each_attribute_value['asOfDate']
                        value = each_attribute_value['reportedValue']['raw']
                        raw_data_list.append(value)
                        date_list.append(date)

                ziplist_10 = list(
                    zip(timestamp, date_list, raw_data_list))[-10:]

                list2 = []
                header = [f'{symbol}']
                for i in ziplist_10:
                    list2.append(i[-2])
                if 'null' not in list2:
                    header.extend(list2)
                    headers.append(header)
                else:
                    pass

                list1 = []
                list1.append(attribute_name)
                for i in ziplist_10:
                    list1.append(i[-1])
                final_list.append(list1)
            else:
                final_list.append([attribute_name])

    header = headers[0]
    return header, final_list


def write_to_csv(symbol, header, final_list):
    with open(f'{symbol}.csv', 'w', newline='') as fp:
        wr = csv.writer(fp, dialect='excel')
        wr.writerow(header)
        for i in final_list:
            wr.writerow(i)


def return_symbolist():
	# url = https://www.nyse.com/listings_directory/stock
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
        'origin': 'https://www.nyse.com',
        'referer': 'https://www.nyse.com/listings_directory/stock'
    }

    url = 'https://www.nyse.com/api/quotes/filter'

    data = {
        'filterToken': "",
        'instrumentType': "EQUITY",
        'maxResultsPerPage': 6527,
        'pageNumber': 1,
        'sortColumn': "NORMALIZED_TICKER",
        'sortOrder': "ASC"
    }
    response = requests.post(url, json=data, headers=headers)

    symbol_list = []
    for i in response.json():
        symbol_list.append(i['normalizedTicker'])
    return symbol_list


def main():

    symbolist = return_symbolist()[:50]

    print(symbolist)

    input_data = input('please enter 0 for "income_statement", 1 for "balance_sheet", 2 for "cash_flow" to retrieve data: ')

    for symbol in symbolist:

        try:

            income_statement = f'https://query2.finance.yahoo.com/ws/fundamentals-timeseries/v1/finance/premium/timeseries/{symbol}?lang=en-US&region=US&symbol={symbol}&padTimeSeries=true&type=quarterlyTaxEffectOfUnusualItems%2CtrailingTaxEffectOfUnusualItems%2CquarterlyTaxRateForCalcs%2CtrailingTaxRateForCalcs%2CquarterlyNormalizedEBITDA%2CtrailingNormalizedEBITDA%2CquarterlyNormalizedDilutedEPS%2CtrailingNormalizedDilutedEPS%2CquarterlyNormalizedBasicEPS%2CtrailingNormalizedBasicEPS%2CquarterlyTotalUnusualItems%2CtrailingTotalUnusualItems%2CquarterlyTotalUnusualItemsExcludingGoodwill%2CtrailingTotalUnusualItemsExcludingGoodwill%2CquarterlyNetIncomeFromContinuingOperationNetMinorityInterest%2CtrailingNetIncomeFromContinuingOperationNetMinorityInterest%2CquarterlyReconciledDepreciation%2CtrailingReconciledDepreciation%2CquarterlyReconciledCostOfRevenue%2CtrailingReconciledCostOfRevenue%2CquarterlyEBITDA%2CtrailingEBITDA%2CquarterlyEBIT%2CtrailingEBIT%2CquarterlyNetInterestIncome%2CtrailingNetInterestIncome%2CquarterlyInterestExpense%2CtrailingInterestExpense%2CquarterlyInterestIncome%2CtrailingInterestIncome%2CquarterlyContinuingAndDiscontinuedDilutedEPS%2CtrailingContinuingAndDiscontinuedDilutedEPS%2CquarterlyContinuingAndDiscontinuedBasicEPS%2CtrailingContinuingAndDiscontinuedBasicEPS%2CquarterlyNormalizedIncome%2CtrailingNormalizedIncome%2CquarterlyNetIncomeFromContinuingAndDiscontinuedOperation%2CtrailingNetIncomeFromContinuingAndDiscontinuedOperation%2CquarterlyTotalExpenses%2CtrailingTotalExpenses%2CquarterlyRentExpenseSupplemental%2CtrailingRentExpenseSupplemental%2CquarterlyReportedNormalizedDilutedEPS%2CtrailingReportedNormalizedDilutedEPS%2CquarterlyReportedNormalizedBasicEPS%2CtrailingReportedNormalizedBasicEPS%2CquarterlyTotalOperatingIncomeAsReported%2CtrailingTotalOperatingIncomeAsReported%2CquarterlyDividendPerShare%2CtrailingDividendPerShare%2CquarterlyDilutedAverageShares%2CtrailingDilutedAverageShares%2CquarterlyBasicAverageShares%2CtrailingBasicAverageShares%2CquarterlyDilutedEPS%2CtrailingDilutedEPS%2CquarterlyDilutedEPSOtherGainsLosses%2CtrailingDilutedEPSOtherGainsLosses%2CquarterlyTaxLossCarryforwardDilutedEPS%2CtrailingTaxLossCarryforwardDilutedEPS%2CquarterlyDilutedAccountingChange%2CtrailingDilutedAccountingChange%2CquarterlyDilutedExtraordinary%2CtrailingDilutedExtraordinary%2CquarterlyDilutedDiscontinuousOperations%2CtrailingDilutedDiscontinuousOperations%2CquarterlyDilutedContinuousOperations%2CtrailingDilutedContinuousOperations%2CquarterlyBasicEPS%2CtrailingBasicEPS%2CquarterlyBasicEPSOtherGainsLosses%2CtrailingBasicEPSOtherGainsLosses%2CquarterlyTaxLossCarryforwardBasicEPS%2CtrailingTaxLossCarryforwardBasicEPS%2CquarterlyBasicAccountingChange%2CtrailingBasicAccountingChange%2CquarterlyBasicExtraordinary%2CtrailingBasicExtraordinary%2CquarterlyBasicDiscontinuousOperations%2CtrailingBasicDiscontinuousOperations%2CquarterlyBasicContinuousOperations%2CtrailingBasicContinuousOperations%2CquarterlyDilutedNIAvailtoComStockholders%2CtrailingDilutedNIAvailtoComStockholders%2CquarterlyAverageDilutionEarnings%2CtrailingAverageDilutionEarnings%2CquarterlyNetIncomeCommonStockholders%2CtrailingNetIncomeCommonStockholders%2CquarterlyOtherunderPreferredStockDividend%2CtrailingOtherunderPreferredStockDividend%2CquarterlyPreferredStockDividends%2CtrailingPreferredStockDividends%2CquarterlyNetIncome%2CtrailingNetIncome%2CquarterlyMinorityInterests%2CtrailingMinorityInterests%2CquarterlyNetIncomeIncludingNoncontrollingInterests%2CtrailingNetIncomeIncludingNoncontrollingInterests%2CquarterlyNetIncomeFromTaxLossCarryforward%2CtrailingNetIncomeFromTaxLossCarryforward%2CquarterlyNetIncomeExtraordinary%2CtrailingNetIncomeExtraordinary%2CquarterlyNetIncomeDiscontinuousOperations%2CtrailingNetIncomeDiscontinuousOperations%2CquarterlyNetIncomeContinuousOperations%2CtrailingNetIncomeContinuousOperations%2CquarterlyEarningsFromEquityInterestNetOfTax%2CtrailingEarningsFromEquityInterestNetOfTax%2CquarterlyTaxProvision%2CtrailingTaxProvision%2CquarterlyPretaxIncome%2CtrailingPretaxIncome%2CquarterlyOtherIncomeExpense%2CtrailingOtherIncomeExpense%2CquarterlyOtherNonOperatingIncomeExpenses%2CtrailingOtherNonOperatingIncomeExpenses%2CquarterlySpecialIncomeCharges%2CtrailingSpecialIncomeCharges%2CquarterlyGainOnSaleOfPPE%2CtrailingGainOnSaleOfPPE%2CquarterlyGainOnSaleOfBusiness%2CtrailingGainOnSaleOfBusiness%2CquarterlyOtherSpecialCharges%2CtrailingOtherSpecialCharges%2CquarterlyWriteOff%2CtrailingWriteOff%2CquarterlyImpairmentOfCapitalAssets%2CtrailingImpairmentOfCapitalAssets%2CquarterlyRestructuringAndMergernAcquisition%2CtrailingRestructuringAndMergernAcquisition%2CquarterlySecuritiesAmortization%2CtrailingSecuritiesAmortization%2CquarterlyEarningsFromEquityInterest%2CtrailingEarningsFromEquityInterest%2CquarterlyGainOnSaleOfSecurity%2CtrailingGainOnSaleOfSecurity%2CquarterlyNetNonOperatingInterestIncomeExpense%2CtrailingNetNonOperatingInterestIncomeExpense%2CquarterlyTotalOtherFinanceCost%2CtrailingTotalOtherFinanceCost%2CquarterlyInterestExpenseNonOperating%2CtrailingInterestExpenseNonOperating%2CquarterlyInterestIncomeNonOperating%2CtrailingInterestIncomeNonOperating%2CquarterlyOperatingIncome%2CtrailingOperatingIncome%2CquarterlyOperatingExpense%2CtrailingOperatingExpense%2CquarterlyOtherOperatingExpenses%2CtrailingOtherOperatingExpenses%2CquarterlyOtherTaxes%2CtrailingOtherTaxes%2CquarterlyProvisionForDoubtfulAccounts%2CtrailingProvisionForDoubtfulAccounts%2CquarterlyDepreciationAmortizationDepletionIncomeStatement%2CtrailingDepreciationAmortizationDepletionIncomeStatement%2CquarterlyDepletionIncomeStatement%2CtrailingDepletionIncomeStatement%2CquarterlyDepreciationAndAmortizationInIncomeStatement%2CtrailingDepreciationAndAmortizationInIncomeStatement%2CquarterlyAmortization%2CtrailingAmortization%2CquarterlyAmortizationOfIntangiblesIncomeStatement%2CtrailingAmortizationOfIntangiblesIncomeStatement%2CquarterlyDepreciationIncomeStatement%2CtrailingDepreciationIncomeStatement%2CquarterlyResearchAndDevelopment%2CtrailingResearchAndDevelopment%2CquarterlySellingGeneralAndAdministration%2CtrailingSellingGeneralAndAdministration%2CquarterlySellingAndMarketingExpense%2CtrailingSellingAndMarketingExpense%2CquarterlyGeneralAndAdministrativeExpense%2CtrailingGeneralAndAdministrativeExpense%2CquarterlyOtherGandA%2CtrailingOtherGandA%2CquarterlyInsuranceAndClaims%2CtrailingInsuranceAndClaims%2CquarterlyRentAndLandingFees%2CtrailingRentAndLandingFees%2CquarterlySalariesAndWages%2CtrailingSalariesAndWages%2CquarterlyGrossProfit%2CtrailingGrossProfit%2CquarterlyCostOfRevenue%2CtrailingCostOfRevenue%2CquarterlyTotalRevenue%2CtrailingTotalRevenue%2CquarterlyExciseTaxes%2CtrailingExciseTaxes%2CquarterlyOperatingRevenue%2CtrailingOperatingRevenue&merge=false&period1=493590046&period2=1599240716&corsDomain=finance.yahoo.com'

            balance_sheet = f'https://query1.finance.yahoo.com/ws/fundamentals-timeseries/v1/finance/premium/timeseries/{symbol}?lang=en-US&region=US&symbol={symbol}&padTimeSeries=true&type=quarterlyTreasurySharesNumber%2CtrailingTreasurySharesNumber%2CquarterlyPreferredSharesNumber%2CtrailingPreferredSharesNumber%2CquarterlyOrdinarySharesNumber%2CtrailingOrdinarySharesNumber%2CquarterlyShareIssued%2CtrailingShareIssued%2CquarterlyNetDebt%2CtrailingNetDebt%2CquarterlyTotalDebt%2CtrailingTotalDebt%2CquarterlyTangibleBookValue%2CtrailingTangibleBookValue%2CquarterlyInvestedCapital%2CtrailingInvestedCapital%2CquarterlyWorkingCapital%2CtrailingWorkingCapital%2CquarterlyNetTangibleAssets%2CtrailingNetTangibleAssets%2CquarterlyCapitalLeaseObligations%2CtrailingCapitalLeaseObligations%2CquarterlyCommonStockEquity%2CtrailingCommonStockEquity%2CquarterlyPreferredStockEquity%2CtrailingPreferredStockEquity%2CquarterlyTotalCapitalization%2CtrailingTotalCapitalization%2CquarterlyTotalEquityGrossMinorityInterest%2CtrailingTotalEquityGrossMinorityInterest%2CquarterlyMinorityInterest%2CtrailingMinorityInterest%2CquarterlyStockholdersEquity%2CtrailingStockholdersEquity%2CquarterlyOtherEquityInterest%2CtrailingOtherEquityInterest%2CquarterlyGainsLossesNotAffectingRetainedEarnings%2CtrailingGainsLossesNotAffectingRetainedEarnings%2CquarterlyOtherEquityAdjustments%2CtrailingOtherEquityAdjustments%2CquarterlyFixedAssetsRevaluationReserve%2CtrailingFixedAssetsRevaluationReserve%2CquarterlyForeignCurrencyTranslationAdjustments%2CtrailingForeignCurrencyTranslationAdjustments%2CquarterlyMinimumPensionLiabilities%2CtrailingMinimumPensionLiabilities%2CquarterlyUnrealizedGainLoss%2CtrailingUnrealizedGainLoss%2CquarterlyTreasuryStock%2CtrailingTreasuryStock%2CquarterlyRetainedEarnings%2CtrailingRetainedEarnings%2CquarterlyAdditionalPaidInCapital%2CtrailingAdditionalPaidInCapital%2CquarterlyCapitalStock%2CtrailingCapitalStock%2CquarterlyOtherCapitalStock%2CtrailingOtherCapitalStock%2CquarterlyCommonStock%2CtrailingCommonStock%2CquarterlyPreferredStock%2CtrailingPreferredStock%2CquarterlyTotalPartnershipCapital%2CtrailingTotalPartnershipCapital%2CquarterlyGeneralPartnershipCapital%2CtrailingGeneralPartnershipCapital%2CquarterlyLimitedPartnershipCapital%2CtrailingLimitedPartnershipCapital%2CquarterlyTotalLiabilitiesNetMinorityInterest%2CtrailingTotalLiabilitiesNetMinorityInterest%2CquarterlyTotalNonCurrentLiabilitiesNetMinorityInterest%2CtrailingTotalNonCurrentLiabilitiesNetMinorityInterest%2CquarterlyOtherNonCurrentLiabilities%2CtrailingOtherNonCurrentLiabilities%2CquarterlyLiabilitiesHeldforSaleNonCurrent%2CtrailingLiabilitiesHeldforSaleNonCurrent%2CquarterlyRestrictedCommonStock%2CtrailingRestrictedCommonStock%2CquarterlyPreferredSecuritiesOutsideStockEquity%2CtrailingPreferredSecuritiesOutsideStockEquity%2CquarterlyDerivativeProductLiabilities%2CtrailingDerivativeProductLiabilities%2CquarterlyEmployeeBenefits%2CtrailingEmployeeBenefits%2CquarterlyNonCurrentPensionAndOtherPostretirementBenefitPlans%2CtrailingNonCurrentPensionAndOtherPostretirementBenefitPlans%2CquarterlyNonCurrentAccruedExpenses%2CtrailingNonCurrentAccruedExpenses%2CquarterlyDuetoRelatedPartiesNonCurrent%2CtrailingDuetoRelatedPartiesNonCurrent%2CquarterlyTradeandOtherPayablesNonCurrent%2CtrailingTradeandOtherPayablesNonCurrent%2CquarterlyNonCurrentDeferredLiabilities%2CtrailingNonCurrentDeferredLiabilities%2CquarterlyNonCurrentDeferredRevenue%2CtrailingNonCurrentDeferredRevenue%2CquarterlyNonCurrentDeferredTaxesLiabilities%2CtrailingNonCurrentDeferredTaxesLiabilities%2CquarterlyLongTermDebtAndCapitalLeaseObligation%2CtrailingLongTermDebtAndCapitalLeaseObligation%2CquarterlyLongTermCapitalLeaseObligation%2CtrailingLongTermCapitalLeaseObligation%2CquarterlyLongTermDebt%2CtrailingLongTermDebt%2CquarterlyLongTermProvisions%2CtrailingLongTermProvisions%2CquarterlyCurrentLiabilities%2CtrailingCurrentLiabilities%2CquarterlyOtherCurrentLiabilities%2CtrailingOtherCurrentLiabilities%2CquarterlyCurrentDeferredLiabilities%2CtrailingCurrentDeferredLiabilities%2CquarterlyCurrentDeferredRevenue%2CtrailingCurrentDeferredRevenue%2CquarterlyCurrentDeferredTaxesLiabilities%2CtrailingCurrentDeferredTaxesLiabilities%2CquarterlyCurrentDebtAndCapitalLeaseObligation%2CtrailingCurrentDebtAndCapitalLeaseObligation%2CquarterlyCurrentCapitalLeaseObligation%2CtrailingCurrentCapitalLeaseObligation%2CquarterlyCurrentDebt%2CtrailingCurrentDebt%2CquarterlyOtherCurrentBorrowings%2CtrailingOtherCurrentBorrowings%2CquarterlyLineOfCredit%2CtrailingLineOfCredit%2CquarterlyCommercialPaper%2CtrailingCommercialPaper%2CquarterlyCurrentNotesPayable%2CtrailingCurrentNotesPayable%2CquarterlyPensionandOtherPostRetirementBenefitPlansCurrent%2CtrailingPensionandOtherPostRetirementBenefitPlansCurrent%2CquarterlyCurrentProvisions%2CtrailingCurrentProvisions%2CquarterlyPayablesAndAccruedExpenses%2CtrailingPayablesAndAccruedExpenses%2CquarterlyCurrentAccruedExpenses%2CtrailingCurrentAccruedExpenses%2CquarterlyInterestPayable%2CtrailingInterestPayable%2CquarterlyPayables%2CtrailingPayables%2CquarterlyOtherPayable%2CtrailingOtherPayable%2CquarterlyDuetoRelatedPartiesCurrent%2CtrailingDuetoRelatedPartiesCurrent%2CquarterlyDividendsPayable%2CtrailingDividendsPayable%2CquarterlyTotalTaxPayable%2CtrailingTotalTaxPayable%2CquarterlyIncomeTaxPayable%2CtrailingIncomeTaxPayable%2CquarterlyAccountsPayable%2CtrailingAccountsPayable%2CquarterlyTotalAssets%2CtrailingTotalAssets%2CquarterlyTotalNonCurrentAssets%2CtrailingTotalNonCurrentAssets%2CquarterlyOtherNonCurrentAssets%2CtrailingOtherNonCurrentAssets%2CquarterlyDefinedPensionBenefit%2CtrailingDefinedPensionBenefit%2CquarterlyNonCurrentPrepaidAssets%2CtrailingNonCurrentPrepaidAssets%2CquarterlyNonCurrentDeferredAssets%2CtrailingNonCurrentDeferredAssets%2CquarterlyNonCurrentDeferredTaxesAssets%2CtrailingNonCurrentDeferredTaxesAssets%2CquarterlyDuefromRelatedPartiesNonCurrent%2CtrailingDuefromRelatedPartiesNonCurrent%2CquarterlyNonCurrentNoteReceivables%2CtrailingNonCurrentNoteReceivables%2CquarterlyNonCurrentAccountsReceivable%2CtrailingNonCurrentAccountsReceivable%2CquarterlyFinancialAssets%2CtrailingFinancialAssets%2CquarterlyInvestmentsAndAdvances%2CtrailingInvestmentsAndAdvances%2CquarterlyOtherInvestments%2CtrailingOtherInvestments%2CquarterlyInvestmentinFinancialAssets%2CtrailingInvestmentinFinancialAssets%2CquarterlyHeldToMaturitySecurities%2CtrailingHeldToMaturitySecurities%2CquarterlyAvailableForSaleSecurities%2CtrailingAvailableForSaleSecurities%2CquarterlyFinancialAssetsDesignatedasFairValueThroughProfitorLossTotal%2CtrailingFinancialAssetsDesignatedasFairValueThroughProfitorLossTotal%2CquarterlyTradingSecurities%2CtrailingTradingSecurities%2CquarterlyLongTermEquityInvestment%2CtrailingLongTermEquityInvestment%2CquarterlyInvestmentsinJointVenturesatCost%2CtrailingInvestmentsinJointVenturesatCost%2CquarterlyInvestmentsInOtherVenturesUnderEquityMethod%2CtrailingInvestmentsInOtherVenturesUnderEquityMethod%2CquarterlyInvestmentsinAssociatesatCost%2CtrailingInvestmentsinAssociatesatCost%2CquarterlyInvestmentsinSubsidiariesatCost%2CtrailingInvestmentsinSubsidiariesatCost%2CquarterlyInvestmentProperties%2CtrailingInvestmentProperties%2CquarterlyGoodwillAndOtherIntangibleAssets%2CtrailingGoodwillAndOtherIntangibleAssets%2CquarterlyOtherIntangibleAssets%2CtrailingOtherIntangibleAssets%2CquarterlyGoodwill%2CtrailingGoodwill%2CquarterlyNetPPE%2CtrailingNetPPE%2CquarterlyAccumulatedDepreciation%2CtrailingAccumulatedDepreciation%2CquarterlyGrossPPE%2CtrailingGrossPPE%2CquarterlyLeases%2CtrailingLeases%2CquarterlyConstructionInProgress%2CtrailingConstructionInProgress%2CquarterlyOtherProperties%2CtrailingOtherProperties%2CquarterlyMachineryFurnitureEquipment%2CtrailingMachineryFurnitureEquipment%2CquarterlyBuildingsAndImprovements%2CtrailingBuildingsAndImprovements%2CquarterlyLandAndImprovements%2CtrailingLandAndImprovements%2CquarterlyProperties%2CtrailingProperties%2CquarterlyCurrentAssets%2CtrailingCurrentAssets%2CquarterlyOtherCurrentAssets%2CtrailingOtherCurrentAssets%2CquarterlyHedgingAssetsCurrent%2CtrailingHedgingAssetsCurrent%2CquarterlyAssetsHeldForSaleCurrent%2CtrailingAssetsHeldForSaleCurrent%2CquarterlyCurrentDeferredAssets%2CtrailingCurrentDeferredAssets%2CquarterlyCurrentDeferredTaxesAssets%2CtrailingCurrentDeferredTaxesAssets%2CquarterlyRestrictedCash%2CtrailingRestrictedCash%2CquarterlyPrepaidAssets%2CtrailingPrepaidAssets%2CquarterlyInventory%2CtrailingInventory%2CquarterlyInventoriesAdjustmentsAllowances%2CtrailingInventoriesAdjustmentsAllowances%2CquarterlyOtherInventories%2CtrailingOtherInventories%2CquarterlyFinishedGoods%2CtrailingFinishedGoods%2CquarterlyWorkInProcess%2CtrailingWorkInProcess%2CquarterlyRawMaterials%2CtrailingRawMaterials%2CquarterlyReceivables%2CtrailingReceivables%2CquarterlyReceivablesAdjustmentsAllowances%2CtrailingReceivablesAdjustmentsAllowances%2CquarterlyOtherReceivables%2CtrailingOtherReceivables%2CquarterlyDuefromRelatedPartiesCurrent%2CtrailingDuefromRelatedPartiesCurrent%2CquarterlyTaxesReceivable%2CtrailingTaxesReceivable%2CquarterlyAccruedInterestReceivable%2CtrailingAccruedInterestReceivable%2CquarterlyNotesReceivable%2CtrailingNotesReceivable%2CquarterlyLoansReceivable%2CtrailingLoansReceivable%2CquarterlyAccountsReceivable%2CtrailingAccountsReceivable%2CquarterlyAllowanceForDoubtfulAccountsReceivable%2CtrailingAllowanceForDoubtfulAccountsReceivable%2CquarterlyGrossAccountsReceivable%2CtrailingGrossAccountsReceivable%2CquarterlyCashCashEquivalentsAndShortTermInvestments%2CtrailingCashCashEquivalentsAndShortTermInvestments%2CquarterlyOtherShortTermInvestments%2CtrailingOtherShortTermInvestments%2CquarterlyCashAndCashEquivalents%2CtrailingCashAndCashEquivalents%2CquarterlyCashEquivalents%2CtrailingCashEquivalents%2CquarterlyCashFinancial%2CtrailingCashFinancial&merge=false&period1=493590046&period2=1599677245&corsDomain=finance.yahoo.com'

            cash_flow = f'https://query2.finance.yahoo.com/ws/fundamentals-timeseries/v1/finance/premium/timeseries/{symbol}?lang=en-US&region=US&symbol={symbol}&padTimeSeries=true&type=quarterlyForeignSales%2CtrailingForeignSales%2CquarterlyDomesticSales%2CtrailingDomesticSales%2CquarterlyAdjustedGeographySegmentData%2CtrailingAdjustedGeographySegmentData%2CquarterlyFreeCashFlow%2CtrailingFreeCashFlow%2CquarterlyRepurchaseOfCapitalStock%2CtrailingRepurchaseOfCapitalStock%2CquarterlyRepaymentOfDebt%2CtrailingRepaymentOfDebt%2CquarterlyIssuanceOfDebt%2CtrailingIssuanceOfDebt%2CquarterlyIssuanceOfCapitalStock%2CtrailingIssuanceOfCapitalStock%2CquarterlyCapitalExpenditure%2CtrailingCapitalExpenditure%2CquarterlyInterestPaidSupplementalData%2CtrailingInterestPaidSupplementalData%2CquarterlyIncomeTaxPaidSupplementalData%2CtrailingIncomeTaxPaidSupplementalData%2CquarterlyEndCashPosition%2CtrailingEndCashPosition%2CquarterlyOtherCashAdjustmentOutsideChangeinCash%2CtrailingOtherCashAdjustmentOutsideChangeinCash%2CquarterlyBeginningCashPosition%2CtrailingBeginningCashPosition%2CquarterlyEffectOfExchangeRateChanges%2CtrailingEffectOfExchangeRateChanges%2CquarterlyChangesInCash%2CtrailingChangesInCash%2CquarterlyOtherCashAdjustmentInsideChangeinCash%2CtrailingOtherCashAdjustmentInsideChangeinCash%2CquarterlyCashFlowFromDiscontinuedOperation%2CtrailingCashFlowFromDiscontinuedOperation%2CquarterlyFinancingCashFlow%2CtrailingFinancingCashFlow%2CquarterlyCashFromDiscontinuedFinancingActivities%2CtrailingCashFromDiscontinuedFinancingActivities%2CquarterlyCashFlowFromContinuingFinancingActivities%2CtrailingCashFlowFromContinuingFinancingActivities%2CquarterlyNetOtherFinancingCharges%2CtrailingNetOtherFinancingCharges%2CquarterlyInterestPaidCFF%2CtrailingInterestPaidCFF%2CquarterlyProceedsFromStockOptionExercised%2CtrailingProceedsFromStockOptionExercised%2CquarterlyCashDividendsPaid%2CtrailingCashDividendsPaid%2CquarterlyPreferredStockDividendPaid%2CtrailingPreferredStockDividendPaid%2CquarterlyCommonStockDividendPaid%2CtrailingCommonStockDividendPaid%2CquarterlyNetPreferredStockIssuance%2CtrailingNetPreferredStockIssuance%2CquarterlyPreferredStockPayments%2CtrailingPreferredStockPayments%2CquarterlyPreferredStockIssuance%2CtrailingPreferredStockIssuance%2CquarterlyNetCommonStockIssuance%2CtrailingNetCommonStockIssuance%2CquarterlyCommonStockPayments%2CtrailingCommonStockPayments%2CquarterlyCommonStockIssuance%2CtrailingCommonStockIssuance%2CquarterlyNetIssuancePaymentsOfDebt%2CtrailingNetIssuancePaymentsOfDebt%2CquarterlyNetShortTermDebtIssuance%2CtrailingNetShortTermDebtIssuance%2CquarterlyShortTermDebtPayments%2CtrailingShortTermDebtPayments%2CquarterlyShortTermDebtIssuance%2CtrailingShortTermDebtIssuance%2CquarterlyNetLongTermDebtIssuance%2CtrailingNetLongTermDebtIssuance%2CquarterlyLongTermDebtPayments%2CtrailingLongTermDebtPayments%2CquarterlyLongTermDebtIssuance%2CtrailingLongTermDebtIssuance%2CquarterlyInvestingCashFlow%2CtrailingInvestingCashFlow%2CquarterlyCashFromDiscontinuedInvestingActivities%2CtrailingCashFromDiscontinuedInvestingActivities%2CquarterlyCashFlowFromContinuingInvestingActivities%2CtrailingCashFlowFromContinuingInvestingActivities%2CquarterlyNetOtherInvestingChanges%2CtrailingNetOtherInvestingChanges%2CquarterlyInterestReceivedCFI%2CtrailingInterestReceivedCFI%2CquarterlyDividendsReceivedCFI%2CtrailingDividendsReceivedCFI%2CquarterlyNetInvestmentPurchaseAndSale%2CtrailingNetInvestmentPurchaseAndSale%2CquarterlySaleOfInvestment%2CtrailingSaleOfInvestment%2CquarterlyPurchaseOfInvestment%2CtrailingPurchaseOfInvestment%2CquarterlyNetInvestmentPropertiesPurchaseAndSale%2CtrailingNetInvestmentPropertiesPurchaseAndSale%2CquarterlySaleOfInvestmentProperties%2CtrailingSaleOfInvestmentProperties%2CquarterlyPurchaseOfInvestmentProperties%2CtrailingPurchaseOfInvestmentProperties%2CquarterlyNetBusinessPurchaseAndSale%2CtrailingNetBusinessPurchaseAndSale%2CquarterlySaleOfBusiness%2CtrailingSaleOfBusiness%2CquarterlyPurchaseOfBusiness%2CtrailingPurchaseOfBusiness%2CquarterlyNetIntangiblesPurchaseAndSale%2CtrailingNetIntangiblesPurchaseAndSale%2CquarterlySaleOfIntangibles%2CtrailingSaleOfIntangibles%2CquarterlyPurchaseOfIntangibles%2CtrailingPurchaseOfIntangibles%2CquarterlyNetPPEPurchaseAndSale%2CtrailingNetPPEPurchaseAndSale%2CquarterlySaleOfPPE%2CtrailingSaleOfPPE%2CquarterlyPurchaseOfPPE%2CtrailingPurchaseOfPPE%2CquarterlyCapitalExpenditureReported%2CtrailingCapitalExpenditureReported%2CquarterlyOperatingCashFlow%2CtrailingOperatingCashFlow%2CquarterlyCashFromDiscontinuedOperatingActivities%2CtrailingCashFromDiscontinuedOperatingActivities%2CquarterlyCashFlowFromContinuingOperatingActivities%2CtrailingCashFlowFromContinuingOperatingActivities%2CquarterlyTaxesRefundPaid%2CtrailingTaxesRefundPaid%2CquarterlyInterestReceivedCFO%2CtrailingInterestReceivedCFO%2CquarterlyInterestPaidCFO%2CtrailingInterestPaidCFO%2CquarterlyDividendReceivedCFO%2CtrailingDividendReceivedCFO%2CquarterlyDividendPaidCFO%2CtrailingDividendPaidCFO%2CquarterlyChangeInWorkingCapital%2CtrailingChangeInWorkingCapital%2CquarterlyChangeInOtherWorkingCapital%2CtrailingChangeInOtherWorkingCapital%2CquarterlyChangeInOtherCurrentLiabilities%2CtrailingChangeInOtherCurrentLiabilities%2CquarterlyChangeInOtherCurrentAssets%2CtrailingChangeInOtherCurrentAssets%2CquarterlyChangeInPayablesAndAccruedExpense%2CtrailingChangeInPayablesAndAccruedExpense%2CquarterlyChangeInAccruedExpense%2CtrailingChangeInAccruedExpense%2CquarterlyChangeInInterestPayable%2CtrailingChangeInInterestPayable%2CquarterlyChangeInPayable%2CtrailingChangeInPayable%2CquarterlyChangeInDividendPayable%2CtrailingChangeInDividendPayable%2CquarterlyChangeInAccountPayable%2CtrailingChangeInAccountPayable%2CquarterlyChangeInTaxPayable%2CtrailingChangeInTaxPayable%2CquarterlyChangeInIncomeTaxPayable%2CtrailingChangeInIncomeTaxPayable%2CquarterlyChangeInPrepaidAssets%2CtrailingChangeInPrepaidAssets%2CquarterlyChangeInInventory%2CtrailingChangeInInventory%2CquarterlyChangeInReceivables%2CtrailingChangeInReceivables%2CquarterlyChangesInAccountReceivables%2CtrailingChangesInAccountReceivables%2CquarterlyOtherNonCashItems%2CtrailingOtherNonCashItems%2CquarterlyExcessTaxBenefitFromStockBasedCompensation%2CtrailingExcessTaxBenefitFromStockBasedCompensation%2CquarterlyStockBasedCompensation%2CtrailingStockBasedCompensation%2CquarterlyUnrealizedGainLossOnInvestmentSecurities%2CtrailingUnrealizedGainLossOnInvestmentSecurities%2CquarterlyProvisionandWriteOffofAssets%2CtrailingProvisionandWriteOffofAssets%2CquarterlyAssetImpairmentCharge%2CtrailingAssetImpairmentCharge%2CquarterlyAmortizationOfSecurities%2CtrailingAmortizationOfSecurities%2CquarterlyDeferredTax%2CtrailingDeferredTax%2CquarterlyDeferredIncomeTax%2CtrailingDeferredIncomeTax%2CquarterlyDepreciationAmortizationDepletion%2CtrailingDepreciationAmortizationDepletion%2CquarterlyDepletion%2CtrailingDepletion%2CquarterlyDepreciationAndAmortization%2CtrailingDepreciationAndAmortization%2CquarterlyAmortizationCashFlow%2CtrailingAmortizationCashFlow%2CquarterlyAmortizationOfIntangibles%2CtrailingAmortizationOfIntangibles%2CquarterlyDepreciation%2CtrailingDepreciation%2CquarterlyOperatingGainsLosses%2CtrailingOperatingGainsLosses%2CquarterlyPensionAndEmployeeBenefitExpense%2CtrailingPensionAndEmployeeBenefitExpense%2CquarterlyEarningsLossesFromEquityInvestments%2CtrailingEarningsLossesFromEquityInvestments%2CquarterlyGainLossOnInvestmentSecurities%2CtrailingGainLossOnInvestmentSecurities%2CquarterlyNetForeignCurrencyExchangeGainLoss%2CtrailingNetForeignCurrencyExchangeGainLoss%2CquarterlyGainLossOnSaleOfPPE%2CtrailingGainLossOnSaleOfPPE%2CquarterlyGainLossOnSaleOfBusiness%2CtrailingGainLossOnSaleOfBusiness%2CquarterlyNetIncomeFromContinuingOperations%2CtrailingNetIncomeFromContinuingOperations%2CquarterlyCashFlowsfromusedinOperatingActivitiesDirect%2CtrailingCashFlowsfromusedinOperatingActivitiesDirect%2CquarterlyTaxesRefundPaidDirect%2CtrailingTaxesRefundPaidDirect%2CquarterlyInterestReceivedDirect%2CtrailingInterestReceivedDirect%2CquarterlyInterestPaidDirect%2CtrailingInterestPaidDirect%2CquarterlyDividendsReceivedDirect%2CtrailingDividendsReceivedDirect%2CquarterlyDividendsPaidDirect%2CtrailingDividendsPaidDirect%2CquarterlyClassesofCashPayments%2CtrailingClassesofCashPayments%2CquarterlyOtherCashPaymentsfromOperatingActivities%2CtrailingOtherCashPaymentsfromOperatingActivities%2CquarterlyPaymentsonBehalfofEmployees%2CtrailingPaymentsonBehalfofEmployees%2CquarterlyPaymentstoSuppliersforGoodsandServices%2CtrailingPaymentstoSuppliersforGoodsandServices%2CquarterlyClassesofCashReceiptsfromOperatingActivities%2CtrailingClassesofCashReceiptsfromOperatingActivities%2CquarterlyOtherCashReceiptsfromOperatingActivities%2CtrailingOtherCashReceiptsfromOperatingActivities%2CquarterlyReceiptsfromGovernmentGrants%2CtrailingReceiptsfromGovernmentGrants%2CquarterlyReceiptsfromCustomers%2CtrailingReceiptsfromCustomers&merge=false&period1=493590046&period2=1599677390&corsDomain=finance.yahoo.com'

            financial_list = [income_statement, balance_sheet, cash_flow]

            url = financial_list[int(input_data)]

            result = retrieve_result(url)

            header = structure_data(symbol, result)[0]

            print(header)

            final_list = structure_data(symbol, result)[1]

            write_to_csv(symbol, header, final_list)

            time.sleep(1)

        except Exception as e:

            print('Error', type(e))


if __name__ == '__main__':
    main()
