#===========================================================
#                       SETUP CODE
#===========================================================
import machine
import ble_repl

ble_repl.start()
machine.freq(240000000)

#===========================================================
#                       STARTUP CODE
#===========================================================
try:
  import bot
  bot.start()
except Exception as e:
  print("Error: ", e)

