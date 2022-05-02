import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.io.wavfile import write

#formato de audio
frecuencia_muestreo = 44100
canales = 1
profundidad_bits = 'float64'

duracion = 5.3

grabacion = sd.rec(
    int(duracion * frecuencia_muestreo),  #Total de frames (muestras) a grabar
    samplerate=frecuencia_muestreo,       #Frecuencia de muestreo
    channels=1,                           #Cantidad de canales
    dtype = profundidad_bits)             #Profundidad de bits (Tipo de dato)
print("Comienza grabacion")
sd.wait()
print("Grabacion completa")

tiempos = np.linspace(0.0, duracion, len(grabacion))

print("Shape: " + str(grabacion.shape))
print("dtype: " + str(grabacion.dtype))

sd.play(grabacion, frecuencia_muestreo)
print("Comienza reproducción")
sd.wait()
print("Reproduccion completa")
grabacion_formato = (grabacion * np.iinfo(np.int16).max).astype(np.int16)
write("grabacion.wav", frecuencia_muestreo, grabacion_formato)

transformada = np.fft.rfft(grabacion[:,0])
frecuencias = np.fft.rfftfreq(len(grabacion[:,0]), 1.0/frecuencia_muestreo)

print("Grabacion shape: " + str(grabacion[:,0].shape))
print("Transformada shape: " + str(transformada.shape))
print("Frecuencias shape: "+ str(frecuencias.shape))

frecuencia_fundamental = frecuencias[transformada.argmax()]

print("Frecuencia fundamental: " + str(frecuencia_fundamental))

fig, ejes = plt.subplots(1,2)

ejes[0].plot(tiempos, grabacion)
ejes[1].plot(frecuencias, np.abs(transformada))
plt.show()

#https://en.wikipedia.org/wiki/Piano_key_frequencies

if frecuencia_fundamental >= 27 and frecuencia_fundamental <= 28:
    print("Tecla 1")
if frecuencia_fundamental >= 28.5 and frecuencia_fundamental <= 29.5:
    print("Tecla 2")
if frecuencia_fundamental >= 29.51 and frecuencia_fundamental <= 31.4:
    print("Tecla 3")
if frecuencia_fundamental >= 31.41 and frecuencia_fundamental <= 33.5:
    print("Tecla 4")
if frecuencia_fundamental >= 33.6 and frecuencia_fundamental <= 35:
    print("Tecla 5")
if frecuencia_fundamental >= 35.1 and frecuencia_fundamental <= 37.5:
    print("Tecla 6")
if frecuencia_fundamental >= 37.6 and frecuencia_fundamental <= 39.6:
    print("Tecla 7")
if frecuencia_fundamental >= 39.7 and frecuencia_fundamental <= 42:
    print("Tecla 8")
if frecuencia_fundamental >= 42.1 and frecuencia_fundamental <= 45:
    print("Tecla 9")
if frecuencia_fundamental >= 45.1 and frecuencia_fundamental <= 47.5:
    print("Tecla 10")
if frecuencia_fundamental >= 47.51 and frecuencia_fundamental <= 50:
    print("Tecla 11")
if frecuencia_fundamental >= 50.1 and frecuencia_fundamental <= 52.5:
    print("Tecla 12")
if frecuencia_fundamental >= 52.5 and frecuencia_fundamental <= 57.5:
    print("Tecla 13")
if frecuencia_fundamental >= 57.6 and frecuencia_fundamental <= 60:
    print("Tecla 14")
if frecuencia_fundamental >= 60.1 and frecuencia_fundamental <= 63:
    print("Tecla 15")
if frecuencia_fundamental >= 63.1 and frecuencia_fundamental <= 67:
    print("Tecla 16")
if frecuencia_fundamental >= 67.1 and frecuencia_fundamental <= 71:
    print("Tecla 17")
if frecuencia_fundamental >= 71.1 and frecuencia_fundamental <= 75:
    print("Tecla 18")
if frecuencia_fundamental >= 75.1 and frecuencia_fundamental <= 79.5:
    print("Tecla 19")
if frecuencia_fundamental >= 79.6 and frecuencia_fundamental <= 84:
    print("Tecla 20")
if frecuencia_fundamental >= 84.1 and frecuencia_fundamental <= 90:
    print("Tecla 21")
if frecuencia_fundamental >= 90.1 and frecuencia_fundamental <= 94.9:
    print("Tecla 22")
if frecuencia_fundamental >= 95 and frecuencia_fundamental <= 100:
    print("Tecla 23")
if frecuencia_fundamental >= 100.1 and frecuencia_fundamental <= 106:
    print("Tecla 24")
if frecuencia_fundamental >= 106.1 and frecuencia_fundamental <= 113:
    print("Tecla 25")
if frecuencia_fundamental >= 113.1 and frecuencia_fundamental <= 119:
    print("Tecla 26")
if frecuencia_fundamental >= 119.1 and frecuencia_fundamental <= 126:
    print("Tecla 27")
if frecuencia_fundamental >= 126.1 and frecuencia_fundamental <= 134:
    print("Tecla 28")
if frecuencia_fundamental >= 134.1 and frecuencia_fundamental <= 141:
    print("Tecla 29")
if frecuencia_fundamental >= 141.1 and frecuencia_fundamental <= 151:
    print("Tecla 30")
if frecuencia_fundamental >= 151.1 and frecuencia_fundamental <= 160:
    print("Tecla 31")
if frecuencia_fundamental >= 160.1 and frecuencia_fundamental <= 169:
    print("Tecla 32")
if frecuencia_fundamental >= 169.1 and frecuencia_fundamental <= 179:
    print("Tecla 33")
if frecuencia_fundamental >= 179.1 and frecuencia_fundamental <= 190:
    print("Tecla 34")
if frecuencia_fundamental >= 190.1  and frecuencia_fundamental <= 200.9:
    print("Tecla 35")
if frecuencia_fundamental >= 201 and frecuencia_fundamental <= 213.6:
    print("Tecla 36")
if frecuencia_fundamental >= 213.7 and frecuencia_fundamental <= 225.5:
    print("Tecla 37")
if frecuencia_fundamental >= 225.6 and frecuencia_fundamental <= 238.08:
    print("Tecla 38")
if frecuencia_fundamental >= 238.09 and frecuencia_fundamental <= 251.9 :
    print("Tecla 39")
if frecuencia_fundamental >= 252 and frecuencia_fundamental <= 266.6:
    print("Tecla 40")
if frecuencia_fundamental >= 266.7 and frecuencia_fundamental <= 282.2:
    print("Tecla 41")
if frecuencia_fundamental >= 282.3 and frecuencia_fundamental <= 295.6:
    print("Tecla 42")
if frecuencia_fundamental >= 295.7 and frecuencia_fundamental <= 316.2:
    print("Tecla 43")
if frecuencia_fundamental >=316.3  and frecuencia_fundamental <= 334.6:
    print("Tecla 44")
if frecuencia_fundamental >= 334.7 and frecuencia_fundamental <= 354.3:
    print("Tecla 45")
if frecuencia_fundamental >= 354.4 and frecuencia_fundamental <= 375:
    print("Tecla 46")
if frecuencia_fundamental >= 375.1 and frecuencia_fundamental <= 397:
    print("Tecla 47")
if frecuencia_fundamental >= 397.1 and frecuencia_fundamental <= 420.4:
    print("Tecla 48")
if frecuencia_fundamental >= 420.5 and frecuencia_fundamental <= 455:
    print("Tecla 49")
if frecuencia_fundamental >= 455.1 and frecuencia_fundamental <= 476.2:
    print("Tecla 50")
if frecuencia_fundamental >= 476.3 and frecuencia_fundamental <= 504:
    print("Tecla 51")
if frecuencia_fundamental >= 504.1 and frecuencia_fundamental <= 533.3:
    print("Tecla 52")
if frecuencia_fundamental >= 533.4 and frecuencia_fundamental <= 564.4:
    print("Tecla 53")
if frecuencia_fundamental >= 564.5 and frecuencia_fundamental <= 597.4:
    print("Tecla 54")
if frecuencia_fundamental >= 597.5 and frecuencia_fundamental <= 632.3:
    print("Tecla 55")
if frecuencia_fundamental >= 632.4 and frecuencia_fundamental <= 669.3:
    print("Tecla 56")
if frecuencia_fundamental >= 669.4 and frecuencia_fundamental <= 708.5:
    print("Tecla 57")
if frecuencia_fundamental >= 708.6 and frecuencia_fundamental <= 750:
    print("Tecla 58")
if frecuencia_fundamental >= 750.1 and frecuencia_fundamental <= 799:
    print("Tecla 59")
if frecuencia_fundamental >= 799.1 and frecuencia_fundamental <= 845.6:
    print("Tecla 60")
