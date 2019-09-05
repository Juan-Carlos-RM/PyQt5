import QtQuick 2.2
import QtQuick.Window 2.1
import QtQuick.Controls 1.4
import QtQuick.Controls.Styles 1.4
import QtQuick.Extras 1.4

Rectangle {
    id: root
    visible: true

    width: /*1024*/ parent.width
    height: /*480*/ parent.height

    color: "#161616"
    border.width: 5
    property int maxFullScale: 180

    Button {
        id: bt00
        text: "Encender led 13"
        anchors.horizontalCenter: parent.horizontalCenter
        onClicked:{
            if(bt00.text == "Encender led 13"){
                VentanaPrincipal.prenderLed('H')
                text = "Apagar led 13";
            }else
                if(bt00.text == "Apagar led 13"){
                    VentanaPrincipal.prenderLed('L')
                    text = "Encender led 13";
                }
        }
    }

    function actualizarRpm(text) {
        speedometer.value = (maxFullScale*text)/255;
    }

    function actualizarTemperatura(text) {
        temperatura.value = ((100*text)/50);
    }
    
    function actualizarPresion(text) {
        presion.value = (maxFullScale * text) / 250;
    }

    Item {
        id: container
        width: root.width
        height: root.height
        anchors.centerIn: parent

        CircularGauge {
            id: speedometer
            value: 0
            anchors.verticalCenter: parent.verticalCenter
            maximumValue: maxFullScale

            anchors.centerIn: parent

            width: height
            height: container.height * 0.75

            style: DashboardGaugeStyle {txt: "RPM"}

            Behavior on value {
                NumberAnimation { duration: 250 }
            }
        }

        CircularGauge {
            id: temperatura
            value: 0
            x: 74
            y: 212

            width: height
            height: container.height * 0.50

            style: DashboardGaugeStyle {txt: "°C"}
        }

        CircularGauge {
           id: presion
           value: 0
           x: 706
           y: 212

           width: height
           height: container.height * 0.50

           style: DashboardGaugeStyle {txt: "Presión"}
        }
    }
}

