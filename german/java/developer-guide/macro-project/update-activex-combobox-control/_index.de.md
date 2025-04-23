---
title: Aktualisieren Sie die ActiveX ComboBox Steuerelemente
type: docs
weight: 900
url: /de/java/update-activex-combobox-control/
---

## **Mögliche Verwendungsszenarien**
Sie können die Werte des ActiveX ComboBox Controls mit Aspose.Cells lesen oder schreiben. Bitte greifen Sie auf das ActiveX Control über die Eigenschaft [Shape.ActiveXControl](https://reference.aspose.com/cells/java/com.aspose.cells/shape#ActiveXControl) zu und überprüfen Sie den Typ über die Eigenschaft [ActiveXControl.Type](https://reference.aspose.com/cells/java/com.aspose.cells/activexcontrol#Type). Es sollte den Wert [ControlType.ComboBox](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#COMBO-BOX) zurückgeben, und danach casten Sie es in ein [ComboBoxActiveXControl](https://reference.aspose.com/cells/java/com.aspose.cells/ComboBoxActiveXControl) Objekt, um die verschiedenen Eigenschaften zu lesen oder zu modifizieren.

Bitte laden Sie die [Beispiel-Excel-Datei](5473374.xlsx), die im folgenden Beispielcode verwendet wird, und die [Ausgabedatei](5473375.xlsx) herunter.
## **Aktualisieren Sie das ActiveX-ComboBox-Steuerelement**
Der folgende Screenshot zeigt die Auswirkung des Beispielcodes auf die [Beispiel-Excel-Datei](5473374.xlsx). Wie Sie sehen können, wurde der Wert des ActiveX-ComboBox-Steuerelements auf "Dies ist ein Kombinationsfeldsteuerelement" aktualisiert.

![todo:image_alt_text](update-activex-combobox-control_1.png)
## **Beispielcode**
Der folgende Beispielcode aktualisiert den Wert des ActiveX-ComboBox-Steuerelements in der [Beispiel-Excel-Datei](5473374.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UpdateActiveXComboBoxControl-UpdateActiveXComboBoxControl.java" >}}
{{< app/cells/assistant language="java" >}}
