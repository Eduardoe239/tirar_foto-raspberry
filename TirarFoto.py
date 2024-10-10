import time
import os
from picamera2 import Picamera2
from picamera2.outputs import FileOutput

picam2 = Picamera2()
picam2.start()

# Defina o diretório de saída para salvar as imagens
output_dir = "Imagens"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)  # Cria o diretório "Imagens" caso não exista

cout = 0
try:
    while True:
        filename = f"image_{cout}.jpg"
        filepath = os.path.join(output_dir, filename)  # Cria o caminho completo para salvar a imagem
        
        # Captura a imagem e salva no caminho completo
        picam2.capture_file(filepath)  # Salva no diretório especificado
        print(f"Foto capturada: {filepath}")
        
        time.sleep(3600)  # Espera 1 hora antes de capturar a próxima foto
        
        cout += 1

except KeyboardInterrupt:
    print("Captura interrompida.")
    picam2.stop()
