import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "include_files": [
    "1_clubs.png",
    "1_clubs.png",
    "1_diamonds.png",
    "1_hearts.png",
    "1_spades.png",
    "2_clubs.png",
    "2_diamonds.png",
    "2_hearts.png",
    "2_spades.png",
    "3_clubs.png",
    "3_diamonds.png",
    "3_hearts.png",
    "3_spades.png",
    "4_clubs.png",
    "4_diamonds.png",
    "4_hearts.png",
    "4_spades.png",
    "5_clubs.png",
    "5_diamonds.png",
    "5_hearts.png",
    "5_spades.png",
    "6_clubs.png",
    "6_diamonds.png",
    "6_hearts.png",
    "6_spades.png",
    "7_clubs.png",
    "7_diamonds.png",
    "7_hearts.png",
    "7_spades.png",
    "8_clubs.png",
    "8_diamonds.png",
    "8_hearts.png",
    "8_spades.png",
    "9_clubs.png",
    "9_diamonds.png",
    "9_hearts.png",
    "9_spades.png",
    "10_clubs.png",
    "10_diamonds.png",
    "10_hearts.png",
    "10_spades.png",
    "11_clubs.png",
    "11_diamonds.png",
    "11_hearts.png",
    "11_spades.png",
    "12_clubs.png",
    "12_diamonds.png",
    "12_hearts.png",
    "12_spades.png",
    "13_clubs.png",
    "13_diamonds.png",
    "13_hearts.png",
    "13_spades.png",
    "cardback.png",
        (sys.executable, "DLLs/tcl86t.dll"),  # Replace 'tcl86t.dll' with the appropriate file on your system
        (sys.executable, "DLLs/tk86t.dll"),   # Replace 'tk86t.dll' with the appropriate file on your system
    ],
    "includes": ["tkinter", "PIL"],
    "include_msvcr": True  # Include the MSVC runtime DLLs
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"  # Use this option for a GUI application on Windows

setup(
    name="pwsproject casino spell",
    version="1.2",
    description="casino spell gemaakt voor pws",
    options={"build_exe": build_exe_options},
    executables=[Executable("test.py", base=base)],
)