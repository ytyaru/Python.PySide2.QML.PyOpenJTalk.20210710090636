#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys
#from sys import exit, argv
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtWidgets import QApplication
#from PySide2.QtGui import QGuiApplication
from PySide2.QtQuick import QQuickView
from PySide2.QtCore import QUrl, QObject, Slot
from PySide2 import QtCore
import pyopenjtalk
import numpy
import simpleaudio as sa

class Connect(QObject):
    def __init__(self, parent=None): super().__init__(parent)
    @QtCore.Slot(str)
    def talk(self, text):
        x, sr = pyopenjtalk.tts(text)
        ply = sa.play_buffer(x.astype(numpy.int16), 1, 2, sr)
        ply.wait_done()

def Main():
#    print(dir(pyopenjtalk))

#    x, sr = pyopenjtalk.tts('なにか喋ります。', weight_f0=0.7)
#    ply = sa.play_buffer(x.astype(numpy.int16), 1, 2, sr)
#    ply.wait_done()
#    pyopenjtalk.tts('おめでとうございます。')
#    pyopenjtalk.synthesize(pyopenjtalk.extract_fullcontext('ありがとうございます。'))

    """
    app = QApplication(sys.argv)
#    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    HERE = os.path.dirname(os.path.abspath(__file__))
    UI = os.path.join(HERE, 'talker.qml')
    print(UI)
    engine.load(UI)
    if not engine.rootObjects(): sys.exit(-1)
    sys.exit(app.exec_())
    """

    app = QApplication(sys.argv)
    connect = Connect()
    engine = QQmlApplicationEngine()
    ctx = engine.rootContext()
    ctx.setContextProperty("Connect", connect)
    HERE = os.path.dirname(os.path.abspath(__file__))
    UI = os.path.join(HERE, 'talker.qml')
#    engine.load(UI)
    engine.load(QUrl(UI))
    if not engine.rootObjects(): sys.exit(-1)
    sys.exit(app.exec_())
    """
    """

    """
    app = QApplication(sys.argv)
    view = QQuickView()
    HERE = os.path.dirname(os.path.abspath(__file__))
    UI = os.path.join(HERE, 'talker.qml')
    url = QUrl(UI)
    view.setSource(url)
    view.show()
    sys.exit(app.exec_())
    """

if __name__ == '__main__':
    Main()
