# Making Project Nexus an App (.exe)

Turn your Python script into a standalone Windows application (`.exe`) that you can share with friends or run without Python installed.

## Prerequisites
Open your terminal and make sure `pyinstaller` is installed (it's part of your requirements now via packaging dependency chain usually, but let's be safe):

```powershell
pip install pyinstaller
```

## Build Command
Run this command in the root of your project:

```powershell
pyinstaller --noconfirm --clean --windowed --name "ProjectNexus" --add-data "assets;assets" --icon "assets/images/main.png" main.py
```

### Explanation of flags:
- `--noconfirm`: Replace existing build folders without asking.
- `--clean`: Clean cache.
- `--windowed`: Run without a black console window popping up.
- `--name "ProjectNexus"`: Name of your app.
- `--add-data "assets;assets"`: Important! Copies your images and database templates into the exe.
- `--icon ...`: Sets the app icon (optional, ensure the file exists or remove this flag).

## Finding your App
After the build finishes, look for a `dist` folder.
Inside `dist/ProjectNexus/`, you will find `ProjectNexus.exe`.

**Creation Complete!** 🚀
