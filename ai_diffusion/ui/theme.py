from PyQt5.QtGui import QGuiApplication, QPalette, QIcon
from PyQt5.QtWidgets import QVBoxLayout, QLabel
from pathlib import Path

from ..settings import Setting

is_dark = QGuiApplication.palette().color(QPalette.Window).lightness() < 128

green = "#3b3" if is_dark else "#292"
yellow = "#cc3" if is_dark else "#762"
red = "#c33"
grey = "#888" if is_dark else "#555"
highlight = "#8df" if is_dark else "#346"

background_inactive = "#606060"
background_active = "#53728E"

icon_path = Path(__file__).parent.parent / "icons"


def icon(name: str):
    theme = "dark" if is_dark else "light"
    return QIcon(str(icon_path / f"{name}-{theme}.svg"))


def add_header(layout: QVBoxLayout, setting: Setting):
    title_label = QLabel(setting.name)
    title_label.setStyleSheet("font-weight:bold")
    desc_label = QLabel(setting.desc)
    desc_label.setWordWrap(True)
    layout.addSpacing(6)
    layout.addWidget(title_label)
    layout.addWidget(desc_label)
