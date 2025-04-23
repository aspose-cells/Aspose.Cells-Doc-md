---
title: ActiveX Steuerelemente hinzufügen
type: docs
weight: 260
url: /de/python-net/add-activex-controls-using-aspose-cells/
---

{{% alert color="primary" %}}

Sie können ActiveX-Steuerelemente mit Aspose.Cells für Python via .NET mithilfe der [**ShapeCollection.add_active_x_control()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_active_x_control)-Methode hinzufügen. Diese Methode nimmt einen Parameter [**ControlType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.activexcontrols/controltype) entgegen, der angibt, welchen Typ von ActiveX-Steuerelement im Arbeitsblatt hinzugefügt werden soll. Sie hat die folgenden Werte.

- ControlType.COMMAND_BUTTON
- ControlType.COMBO_BOX
- ControlType.CHECK_BOX
- ControlType.LIST_BOX
- ControlType.TEXT_BOX
- ControlType.SPIN_BUTTON
- ControlType.RADIO_BUTTON
- ControlType.LABEL
- ControlType.IMAGE
- ControlType.TOGGLE_BUTTON
- ControlType.SCROLL_BAR
- ControlType.BAR_CODE
- ControlType.UNBEKANNT


Sobald Sie die ActiveX-Steuerung in der Formsammlung hinzugefügt haben, können Sie dann über die [**Shape.active_x_control**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/active_x_control)-Eigenschaft auf das ActiveX-Steuerungselement zugreifen und anschließend seine verschiedenen Eigenschaften festlegen.

{{% /alert %}}

Der folgende Beispielcode fügt eine Umschalt-Schaltfläche (Toggle Button) als ActiveX-Steuerelement mit Aspose.Cells für Python via .NET hinzu.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-AddActiveXControls-1.py" >}}
