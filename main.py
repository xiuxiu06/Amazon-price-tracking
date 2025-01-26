from bs4 import BeautifulSoup
import requests
import smtplib

SMTP_ADDRESS = "smtp.gmail.com"
EMAIL = "lengoctam0106@gmail.com"
PASSWORD = "sees dcxc qcoj tqpw"
header = {
    "headers": {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9",
        "Priority": "u=0, i",
        "Sec-Ch-Ua": "\"Microsoft Edge\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
    }
}
# url = "https://appbrewery.github.io/instant_pot/"
url = ("https://www.amazon.com/AquaSonic-DUO-Whitening-Rechargeable-ToothBrushes/dp/B07HFG93GK/ref=pd_ci_mcx_mh_pe_im_d1_hxwPPE_sspa_dk_det_cao_p_1_0?pd_rd_i=B07HFG93GK&pd_rd_w=hSnWZ&content-id=amzn1.sym.f9934d50-08a9-44c7-8197-748d181c755d&pf_rd_p=f9934d50-08a9-44c7-8197-748d181c755d&pf_rd_r=HA96ED4JEK0XQMCHM484&pd_rd_wg=h3BK1&pd_rd_r=6ecf7d4e-eae3-4b43-918e-71e6b1d9fef3")
response = requests.get(url, header)
soup = BeautifulSoup(response.content, "html.parser")
price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
# ====================== Send an Email ===========================
title = soup.find(id="productTitle").get_text().strip()
print(title)
# Set the price below which you would like to get a notification
BUY_PRICE = 40
if price_as_float < BUY_PRICE:
    message = f"{title} is on sale for {price}!"

    with smtplib.SMTP(SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )
