#%%
# /game/__init__.py

from .graphic.render import render_test

VERSION = 3.5

def print_version_info():
    print(f"The Version of this game is {VERSION}")

# 이곳에 패키지 초기화 코드를 작성한다.
print("Initialize the game...")