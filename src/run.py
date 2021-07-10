#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys, numpy, pyopenjtalk
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtWidgets import QApplication
from PySide2.QtQuick import QQuickView
from PySide2.QtCore import QUrl, QObject, Slot
import simpleaudio as sa

class Connect(QObject):
    def __init__(self, parent=None): super().__init__(parent)
    @Slot(str)
    def talk(self, text):
        x, sr = pyopenjtalk.tts(text)
        ply = sa.play_buffer(x.astype(numpy.int16), 1, 2, sr)
        ply.wait_done()

def Main():
    app = QApplication(sys.argv)
    connect = Connect()
    engine = QQmlApplicationEngine()
    ctx = engine.rootContext()
    ctx.setContextProperty("Connect", connect)
    HERE = os.path.dirname(os.path.abspath(__file__))
    UI = os.path.join(HERE, 'talker.qml')
    engine.load(UI)
    if not engine.rootObjects(): sys.exit(-1)
    sys.exit(app.exec_())

if __name__ == '__main__':
    Main()
