import subprocess
import sys
from datetime import datetime

REPO_PATH = "/Users/agustinfedericovales/Documents/Claude/Projects/Tabla Haus/tablahaus-netlify"

def run(cmd):
    result = subprocess.run(cmd, cwd=REPO_PATH, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"❌ Error: {result.stderr}")
        sys.exit(1)
    return result.stdout.strip()

# Mensaje de commit: si pasás uno como argumento lo usa, si no genera uno automático
if len(sys.argv) > 1:
    mensaje = " ".join(sys.argv[1:])
else:
    mensaje = f"Actualización {datetime.now().strftime('%d/%m/%Y %H:%M')}"

print("📦 Subiendo cambios a GitHub...")

run(["git", "add", "."])

# Ver si hay algo para commitear
status = run(["git", "status", "--porcelain"])
if not status:
    print("✅ No hay cambios nuevos para subir.")
    sys.exit(0)

run(["git", "commit", "-m", mensaje])
run(["git", "push", "origin", "main"])

print(f"✅ Listo! Cambios subidos con mensaje: '{mensaje}'")
print("🌐 El sitio se actualiza en https://tablahaus.github.io en 1-2 minutos.")
