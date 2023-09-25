# Space-Shooters-Game
This game is a good simulation of the famous space shooters with a subtle touch of Star Wars. This project was my first project in college in 2019, but really proud of what I acheived with pygame and OOP. In short terms, the only file you need to try it IF you have a python interpreter and the modules already installed is the [main.py](https://github.com/alexjr2001/Space-Shooters-Game/blob/main/main.py) the rest is the configuration to convert it into an exe file for make it available to everyone, all you need if you don´t have a python interpreter is open this [file](https://github.com/alexjr2001/Space-Shooters-Game/blob/main/dist/main.exe). Here a photo of how it has to look like.

<p align="center">
<img width="280" alt="image" src="https://github.com/alexjr2001/Space-Shooters-Game/assets/63054183/48d45947-b990-45bd-863c-49c93f3c976c">
</p>

## Project Files Structure:
- [.gitattributes](https://github.com/alexjr2001/Space-Shooters-Game/blob/main/.gitattributes) file was used just to show the correct language of the project.
- [main.py](https://github.com/alexjr2001/Space-Shooters-Game/blob/main/main.py) in the top-level is to make it visible because the one that actually works is in the dist directory, this one is commented and explained.
- [/dist](https://github.com/alexjr2001/Space-Shooters-Game/tree/main/dist) has all the resources needed (graphics), code source and the executable file.
- [/build](https://github.com/alexjr2001/Space-Shooters-Game/tree/main/build/main) directory can be omitted because it was generated for converting the .py to .exe

The tool used to convert .py to .exe is pyinstaller which bundles a python app and all its dependencies.

## Package installation and run the program
We import pygame, sys, time and random modules, some of them usually have to be installed such as pygame:

```
python3 -m pip install -U pygame --user
```

After having installed all the required resources, we can run the program:

```
python3 main.py
```

