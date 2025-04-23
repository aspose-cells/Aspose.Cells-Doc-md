---
title: AktiveX Steuerelemente mit Aspose.Cells hinzufügen
type: docs
weight: 720
url: /de/java/add-activex-controls-using-aspose-cells/
---

{{% alert color="primary" %}} 

Sie können ActiveX-Steuerelemente mit Aspose.Cells mithilfe der [ShapeCollection.addActiveXControl()](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addActiveXControl-int-int-int-int-int-int-int-) Methode hinzufügen. Diese Methode akzeptiert einen Parameter [ControlType](https://reference.aspose.com/cells/java/com.aspose.cells/ControlType), der angibt, welchen Typ von ActiveX-Steuerelement innerhalb eines Arbeitsblatts hinzugefügt werden soll. Es hat die folgenden Werte:

- [CHECK_BOX](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#CHECK-BOX)
- [COMBO_BOX](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#COMBO-BOX)
- [COMMAND_BUTTON](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#COMMAND-BUTTON)
- [IMAGE](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#IMAGE)
- [LABEL](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#LABEL)
- [LIST_BOX](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#LIST-BOX)
- [RADIO_BUTTON](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#RADIO-BUTTON)
- [SCROLL_BAR](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#SCROLL-BAR)
- [SPIN_BUTTON](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#SPIN-BUTTON)
- [TEXT_BOX](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#TEXT-BOX)
- [TOGGLE_BUTTON](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#TOGGLE-BUTTON)
- [UNBEKANNT](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#UNKNOWN)

Sobald Sie das ActiveX-Steuerelement in der Shape Collection hinzugefügt haben, können Sie dann auf das ActiveX-Steuerelement-Objekt über die Eigenschaft [Shape.ActiveXControl](https://reference.aspose.com/cells/java/com.aspose.cells/shape#ActiveXControl) zugreifen und anschließend verschiedene Eigenschaften setzen.

{{% /alert %}} 
## **Fügen Sie das Toggle Button ActiveX-Steuerelement mithilfe von Aspose.Cells hinzu**
Der folgende Beispielcode fügt das Toggle Button ActiveX-Steuerelement mit Aspose.Cells hinzu. Laden Sie bitte die mit diesem Code generierte [Ausgabedatei Excel](5473427.xlsx) herunter.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddActiveXControl-AddActiveXControl.java" >}}
{{< app/cells/assistant language="java" >}}
