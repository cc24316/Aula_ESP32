print("Hello, ESP32!")

# exemplo piscar o pino s

# importando as bibliotecas
from machine import Pin
from time import sleep

# define o led usando uma classe a qual irá controlar os pinos

pinoled = 5
botao1 = 4

btn = Pin(botao1, Pin.IN, Pin.PULL_UP)

ledV = Pin(pinoled, Pin.OUT)
ledA = Pin(17, Pin.OUT)
ledA.value(True)
# loop principal
cor = False
while True:

  if btn.value() == 0:
    cor = not cor
    ledV.value(0)
    ledA.value(0)
  if cor:
    ledV.value(not ledV.value())
  else:
    ledA.value(not ledA.value())
  sleep(0.4)

  '''
  led.value(1)
  sleep(0.5)
  led.value(0)
  sleep(0.5)

  '''
