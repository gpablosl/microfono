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

# 329.63 Hz E4
# 246.94 Hz B3
# 196.00 Hz G3
# 146.83 Hz D3
# 110.00 Hz A2
# 82.41 Hz E2

if frecuencia_fundamental <= 80:
    print("Apretar cuerda para tecla 6 (E2)")
if frecuencia_fundamental >= 81 and frecuencia_fundamental <= 83:
    print("Tecla 6 (E)")
if frecuencia_fundamental >= 84 and frecuencia_fundamental <= 100:
    print("Aflojar cuerda para tecla 6 (E2)")

if frecuencia_fundamental >= 101 and frecuencia_fundamental <= 108:
    print("Apretar cuerda para tecla 5 (A2)")
if frecuencia_fundamental >= 109 and frecuencia_fundamental <= 111:
    print("Tecla 5 (A)")
if frecuencia_fundamental >= 112 and frecuencia_fundamental <= 120:
    print("Aflojar cuerda para tecla 5 (A2)")

if frecuencia_fundamental >= 121 and frecuencia_fundamental <= 144:
    print("Apretar cuerda para tecla 4 (D3)")
if frecuencia_fundamental >= 145 and frecuencia_fundamental <= 148:
    print("Tecla 4 (D)")
if frecuencia_fundamental >= 149 and frecuencia_fundamental <= 170:
    print("Aflojar cuerda para tecla 4 (D3)")

if frecuencia_fundamental >= 171 and frecuencia_fundamental <= 194:
    print("Apretar cuerda para tecla 3 (G3)")
if frecuencia_fundamental >= 195 and frecuencia_fundamental <= 197:
    print("Tecla 3 (G)")
if frecuencia_fundamental >= 198 and frecuencia_fundamental <= 212:
    print("Aflojar cuerda para tecla 3 (G3)")

if frecuencia_fundamental >= 212 and frecuencia_fundamental <= 244:
    print("Apretar cuerda para tecla 2 (B3)")
if frecuencia_fundamental >= 245 and frecuencia_fundamental <= 247:
    print("Tecla 2 (B)")
if frecuencia_fundamental >= 248 and frecuencia_fundamental <= 300:
    print("Aflojar cuerda para tecla 2 (B3)")

if frecuencia_fundamental >= 301 and frecuencia_fundamental <= 327:
    print("Apretar cuerda para tecla 1 (E4)")
if frecuencia_fundamental >= 328 and frecuencia_fundamental <= 330:
    print("Tecla 1 (E)")
if frecuencia_fundamental >= 331:
    print("Aflojar cuerda para tecla 1 (E4)")
