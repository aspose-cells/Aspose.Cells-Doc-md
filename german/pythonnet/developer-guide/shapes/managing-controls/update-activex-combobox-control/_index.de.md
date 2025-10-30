---
title: Aktualisieren Sie die ActiveX ComboBox Steuerelemente
type: docs
weight: 170
url: /de/python-net/update-activex-combobox-control/
---

## **Mögliche Verwendungsszenarien**
Sie können die Werte eines ActiveX-ComboBox-Steuerelements mit Aspose.Cells für Python via .NET lesen oder schreiben. Greifen Sie auf das ActiveX-Steuerelement über die [Shape.active_x_control](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/active_x_control)-Eigenschaft zu und überprüfen Sie den Typ über die [ActiveXControl.type](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.activexcontrols/activexcontrolbase/type/)-Eigenschaft. Diese sollte den Wert [ControlType.COMBO_BOX](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.activexcontrols/controltype) zurückgeben. Casten Sie es dann in ein [ComboBoxActiveXControl](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.activexcontrols/comboboxactivexcontrol)-Objekt, um die verschiedenen Eigenschaften zu lesen oder zu ändern.

Bitte laden Sie die im folgenden Beispielcode verwendete [Beispieldatei](5115124.xlsx) herunter.
## **Aktualisieren Sie das ActiveX-ComboBox-Steuerelement**
Der folgende Screenshot zeigt die Auswirkung des Beispielcodes auf die [Beispieldatei](5115124.xlsx). Wie Sie sehen können, wurde der Wert der ActiveX-ComboBox auf "Dies ist die Kombinationsfeldsteuerung" aktualisiert.

|![todo:image_alt_text](update-activex-combobox-control_1.png)|
| :- |
## **Beispielcode**
Der folgende Beispielcode aktualisiert den Wert des ActiveX-ComboBox-Steuerungselements, das sich in der [Beispieldatei Excel](5115124.xlsx) befindet.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-UpdateActiveXComboBoxControl.py" >}}
{{< app/cells/assistant language="python-net" >}}
