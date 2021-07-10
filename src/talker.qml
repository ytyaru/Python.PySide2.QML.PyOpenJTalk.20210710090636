import QtQuick 2.0
import QtQuick.Window 2.0
import QtQuick.Controls 2.0

ApplicationWindow {
    id: mainWindow
    width: 500
    height: 50
    title: qsTr("Qt + PySide2 + PyOpenJTalk")
    visible: true
    locale: locale

    Rectangle {
        color: "#FFCCDD"
        anchors.fill: parent

        TextInput {
            id: _talkText
            text: "発話したいテキストを入力してからEnterキーを押してください。"
            focus: true
            font.pixelSize: Math.max(16, parent.width / 40)
            anchors.fill: parent
            onAccepted: Connect.talk(_talkText.text)
        }
    }
}
