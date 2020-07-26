import telepot
from selenium.webdriver import Chrome
from time import sleep

bot = telepot.Bot('coloque a chave da api do telegram')
browser = Chrome()

url = 'https://www.jacotei.com.br/placa-mae-asus-matx-am4-ddr4-prime-b450m-gaming-br/p'

browser.get(url)
sleep(5)
menor_cotacao = browser.find_element_by_xpath("//div[@id='container_topo_produto']/div/div/a/p[2]/strong")
menor_cotacao = str({menor_cotacao.text})
trat_1 = menor_cotacao.replace('{', '').replace('}', '').replace("'", "").replace(",", ".")
sleep(3)
browser.quit()
sleep(1)
menor_preco = float(434.26)

limpar = trat_1.replace('R$ ','')
trat_2 = float(limpar)

variacao = (float(trat_2/menor_preco)-1)*100

if (variacao > 0):
    bot.sendMessage(coloque o id do seu telegram aqui, 'Fala ae compatriota, rapaz aumentou bagarai\n\n\nÚltima cotação da Placa Mae Asus Matx  (Am4) - Ddr4 - Prime B450m-Gaming/Br é de: {} \n\nO menor preço registrado foi de R$ {} \n\nO aumento é de {:.2f}%'.format(trat_1,menor_preco,variacao))
else:
     bot.sendMessage(coloque o id do seu telegram aqui, 'Fala ae compatriota, rapaz caiu bagarai\n\n\nÚltima cotação da Placa Mae Asus Matx  (Am4) - Ddr4 - Prime B450m-Gaming/Br é de: {} \n\nO menor preço registrado foi de R$ {} \n\nA queada é de {:.2f}%'.format(trat_1,menor_preco,variacao))
