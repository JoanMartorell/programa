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
   - Descomprime el archivo y tendrás:
     - `CalculoDeCoste.app` - La aplicación (carpeta)
     - `CalculoDeCoste.dmg` - Imagen de disco para instalación fácil

### Usar la app en macOS:

**Opción 1: Usar el DMG (Recomendado)**
1. Transfiere `CalculoDeCoste.dmg` a tu Mac
2. Abre el DMG (doble clic)
3. Arrastra `CalculoDeCoste.app` a la carpeta "Aplicaciones"
4. Expulsa el DMG cuando termines

**Opción 2: Usar el .app directamente**
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

