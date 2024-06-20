---
title: Aktualisieren Sie die ActiveX ComboBox Steuerelemente
type: docs
weight: 170
url: /de/net/update-activex-combobox-control/
---

## **Mögliche Verwendungsszenarien**
Sie können die Werte der aktiven ComboBox-Steuerung mit Aspose.Cells lesen oder schreiben. Greifen Sie bitte über die Eigenschaft [Shape.ActiveXControl](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/activexcontrol) auf die ActiveX-Steuerung zu und überprüfen Sie ihren Typ über die Eigenschaft [ActiveXControl.Type](https://reference.aspose.com/cells/net/aspose.cells.drawing/activexcontrols/activexcontrolbase/properties/type), sie sollte den Wert [ControlType.ComboBox](https://reference.aspose.com/cells/net/aspose.cells.drawing/activexcontrols/controltype) zurückgeben, und dann casten Sie sie in ein [ComboBoxActiveXControl](https://reference.aspose.com/cells/net/aspose.cells.drawing/activexcontrols/comboboxactivexcontrol)-Objekt und lesen oder ändern Sie seine verschiedenen Eigenschaften.

Bitte laden Sie die im folgenden Beispielcode verwendete [Beispieldatei](5115124.xlsx) herunter.
## **Aktualisieren Sie das ActiveX-ComboBox-Steuerelement**
Der folgende Screenshot zeigt die Auswirkung des Beispielcodes auf die [Beispieldatei](5115124.xlsx). Wie Sie sehen können, wurde der Wert der ActiveX-ComboBox auf "Dies ist die Kombinationsfeldsteuerung" aktualisiert.

|![todo:image_alt_text](update-activex-combobox-control_1.png)|
| :- |
## **Beispielcode**
Der folgende Beispielcode aktualisiert den Wert des ActiveX-ComboBox-Steuerungselements, das sich in der [Beispieldatei Excel](5115124.xlsx) befindet.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UpdateActiveXComboBoxControl-UpdateActiveXComboBoxControl.cs" >}}
