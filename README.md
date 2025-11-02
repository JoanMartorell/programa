# CalculoDeCoste - Aplicación macOS

Aplicación para calcular costes basada en minutos y gramos.

## Compilar para macOS desde Windows

Este proyecto está configurado para compilarse automáticamente en la nube usando GitHub Actions.

### Instrucciones:

1. **Sube tu código a GitHub:**
   ```bash
   git init
   git add programa.py .github/workflows/macos-build.yml
   git commit -m "Inicializar proyecto"
   git remote add origin TU_REPOSITORIO_GITHUB
   git push -u origin main
   ```

2. **Activa el workflow:**
   - Ve a tu repositorio en GitHub
   - Click en "Actions"
   - Selecciona el workflow "Compilar para macOS"
   - Click en "Run workflow" → "Run workflow"

3. **Descarga la app:**
   - Una vez completado (verás una marca verde)
   - Click en el workflow completado
   - En "Artifacts" descarga "CalculoDeCoste-macOS"
   - Descomprime el archivo y tendrás `CalculoDeCoste.app`

### Usar la app en macOS:

1. Transfiere `CalculoDeCoste.app` a tu Mac
2. Si macOS muestra un error de seguridad:
   - Clic derecho → "Abrir"
   - Confirma en el diálogo de seguridad

### Compilar localmente (si tienes acceso a un Mac):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install pyinstaller
pyinstaller --clean --noconfirm --windowed --name "CalculoDeCoste" programa.py
```

La app estará en `dist/CalculoDeCoste.app`

