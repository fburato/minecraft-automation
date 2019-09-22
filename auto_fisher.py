from pywinauto import Application
import time


def main():
    minecraft_handle = Application().connect(title_re="Minecraft 1.14.4", class_name="GLFW30")
    main_window = minecraft_handle.top_window()
    while True:
        main_window.right_click()
        time.sleep(0.1)


if __name__ == "__main__":
    main()
