import os


def install() -> None:
    git_url = "https://github.com/mk-samoilov/mtools.git"
    path = str(input("input installing path: "))

    os.system(f"git clone {git_url} \"{path}\"")


if __name__ == "__main__":
    install()
    input("press enter to exit.")
