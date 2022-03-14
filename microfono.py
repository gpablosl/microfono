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
#frecuencias = np.fft.rfftfreq(len(transformada), 1.0/frecuencia_muestreo)

fig, ejes = plt.subplots(1,2)

ejes[0].plot(tiempos, grabacion)
ejes[1].plot(np.abs(transformada))
plt.show()
