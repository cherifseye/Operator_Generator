from cx_Freeze import setup, Executable

setup(
    name = "Operator generator",
    version = "0.1",
    description = "Permet de generer des operations de maniere automatique ",
    executables = [Executable("compute.py")]
)
