import random
import qrcode

def generate_password(n_characters):
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '1234567890'
    symbols = '!@#$%^&*()={}[]'
    all_characters = lower + upper + numbers + symbols
    password = ''.join(random.sample(all_characters, n_characters))
    return password

def image_qr(password):
    filename =input('Alias of the new password: ')
    img= qrcode.make(password)
    img.save(filename + '.png')

def run():
    characters =int(input('Number of characters: '))
    password = generate_password(characters)
    print(f'Your new password is: {password}')
    image_qr(password)
    print('The password was saved as QR code image')

if __name__ == '__main__' :
    run()