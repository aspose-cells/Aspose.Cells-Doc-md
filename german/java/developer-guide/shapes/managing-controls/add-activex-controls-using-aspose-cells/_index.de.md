---
title: AktiveX Steuerelemente mit Aspose.Cells hinzufügen
type: docs
weight: 720
url: /de/java/add-activex-controls-using-aspose-cells/
---

{{% alert color="primary" %}} 

Sie können ActiveX-Steuerlemente mit Aspose.Cells mithilfe der Methode [ShapeCollection.addActiveXControl()](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addActiveXControl\(int,%20int,%20int,%20int,%20int,%20int,%20int\)) hinzufügen. Diese Methode benötigt den Parameter [ControlType](https://reference.aspose.com/cells/java/com.aspose.cells/ControlType), der angibt, welcher Typ von ActiveX-Steuerelement in einem Arbeitsblatt hinzugefügt werden soll. Es hat die folgenden Werte.

- [CHECK_BOX](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#CHECK_BOX)
- [COMBO_BOX](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#COMBO_BOX)
- [COMMAND_BUTTON](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#COMMAND_BUTTON)
- [IMAGE](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#IMAGE)
- [LABEL](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#LABEL)
- [LIST_BOX](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#LIST_BOX)
- [RADIO_BUTTON](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#RADIO_BUTTON)
- [SCROLL_BAR](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#SCROLL_BAR)
- [SPIN_BUTTON](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#SPIN_BUTTON)
- [TEXT_BOX](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#TEXT_BOX)
- [TOGGLE_BUTTON](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#TOGGLE_BUTTON)
- [UNBEKANNT](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#UNKNOWN)

Sobald Sie das ActiveX-Steuerelement in der Shape Collection hinzugefügt haben, können Sie dann auf das ActiveX-Steuerelement-Objekt über die Eigenschaft [Shape.ActiveXControl](https://reference.aspose.com/cells/java/com.aspose.cells/shape#ActiveXControl) zugreifen und anschließend verschiedene Eigenschaften setzen.

{{% /alert %}} 
## **Fügen Sie das Toggle Button ActiveX-Steuerelement mithilfe von Aspose.Cells hinzu**
Der folgende Beispielcode fügt das Toggle Button ActiveX-Steuerelement mit Aspose.Cells hinzu. Laden Sie bitte die mit diesem Code generierte [Ausgabedatei Excel](5473427.xlsx) herunter.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddActiveXControl-AddActiveXControl.java" >}}
