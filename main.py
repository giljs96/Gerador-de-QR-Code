import qrcode

# varável action recebe o link que o qrcode irá direcionar
action = str(input("Digite o link para gerar o QR CODE:\nR:  ")).strip()
action_name = str(input("Qual o nome do site?\nR: "))

#módulo MAKE: para informar o link, mensagem ou ação desejada com o QR CODE
qrCode_image = qrcode.make(action)  #vai direcionar para esse link

qrCode_image.save(f"{action_name}_qrcode.jpg") #nome do arquivo e a extensão que iremos salvar