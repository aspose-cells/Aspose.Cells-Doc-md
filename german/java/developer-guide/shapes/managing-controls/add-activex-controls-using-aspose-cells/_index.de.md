---
title: Fügen Sie ActiveX-Steuerelemente mit Aspose.Cells hinzu
type: docs
weight: 720
url: /de/java/add-activex-controls-using-aspose-cells/
---
{{% alert color="primary" %}} 

 Sie können ActiveX-Steuerelemente mit Aspose.Cells hinzufügen, indem Sie die verwenden[ShapeCollection.addActiveXControl()](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addActiveXControl\(int,%20int,%20int,%20int,%20int,%20int,%20int\) ) Methode. Diese Methode akzeptiert einen Parameter[Steuerungstyp](https://reference.aspose.com/cells/java/com.aspose.cells/ControlType)die angibt, welche Art von ActiveX-Steuerelement in einem Arbeitsblatt hinzugefügt werden muss. Es hat die folgenden Werte.

- [CHECK_BOX](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#CHECK_BOX)
- [KOMBINATIONSFELD](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#COMBO_BOX)
- [COMMAND_BUTTON](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#COMMAND_BUTTON)
- [BILD](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#IMAGE)
- [ETIKETT](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#LABEL)
- [LIST_BOX](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#LIST_BOX)
- [RADIO KNOPF](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#RADIO_BUTTON)
- [SCROLLLEISTE](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#SCROLL_BAR)
- [SPIN_BUTTON](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#SPIN_BUTTON)
- [TEXTFELD](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#TEXT_BOX)
- [UMSCHALTKNOPF](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#TOGGLE_BUTTON)
- [UNBEKANNT](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#UNKNOWN)

 Sobald Sie das ActiveX-Steuerelement in der Formensammlung hinzugefügt haben, können Sie über auf das ActiveX-Steuerelementobjekt zugreifen[Shape.ActiveXControl](https://reference.aspose.com/cells/java/com.aspose.cells/shape#ActiveXControl) -Eigenschaft und legen Sie dann ihre verschiedenen Eigenschaften fest.

{{% /alert %}} 
## **Fügen Sie das ActiveX-Steuerelement für die Umschaltfläche mit Aspose.Cells hinzu**
 Der folgende Beispielcode fügt Toggle Button ActiveX Control mit Aspose.Cells hinzu. Bitte laden Sie die[Excel-Datei ausgeben](5473427.xlsx) generiert mit diesem Code für Ihre Referenz.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddActiveXControl-AddActiveXControl.java" >}}
