import QtQuick 2.0
import QtQuick.Window 2.0
import QtQuick.Controls 2.0
//import QtQuick 2.13
//import QtQuick.Controls 2.13

ApplicationWindow {
    id: mainWindow
    width: 500
    height: 50
    title: qsTr("Qt + PySide2 + PyOpenJTalk")
    visible: true
    locale:locale

    Rectangle {
      color: "#FFCCDD"
      anchors.fill: parent

      TextInput {
        id: _talkText
        text: "発話したいテキストを入力してからEnterキーを押してください。"
        focus: true
    //    font.pointSize: 20
    //    scale: Math.min(1, parent.width / contentWidth)
//        font.pixelSize: 0.1 * parent.height
//        font.pixelSize: Math.max(16, 0.2 * parent.height, )
        font.pixelSize: Math.max(16, parent.width / 40)
        anchors.fill: parent
        /*
        anchors.top: parent.top
        anchors.bottom: parent.bottom
        anchors.left: parent.left
        anchors.right: parent.right
        onAccepted: {console.debug(_talkText.text);}
        */
        onAccepted: Connect.talk(_talkText.text)
      }
    }
}
