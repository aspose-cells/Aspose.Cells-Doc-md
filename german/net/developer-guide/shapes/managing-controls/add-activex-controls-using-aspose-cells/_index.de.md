---
title: AktiveX Steuerelemente mit Aspose.Cells hinzufügen
type: docs
weight: 260
url: /de/net/add-activex-controls-using-aspose-cells/
---

{{% alert color="primary" %}}

Sie können ActiveX-Steuerelemente mit Aspose.Cells über die [**ShapeCollection.AddActiveXControl()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addactivexcontrol)-Methode hinzufügen. Diese Methode nimmt einen Parameter [**ControlType**](https://reference.aspose.com/cells/net/aspose.cells.drawing.activexcontrols/controltype), der angibt, welche Art von ActiveX-Steuerelement innerhalb eines Arbeitsblatts hinzugefügt werden soll. Es hat die folgenden Werte.

- ControlType.CheckBox
- ControlType.ComboBox
- ControlType.CommandButton
- ControlType.Image
- ControlType.Label
- ControlType.ListBox
- ControlType.RadioButton
- ControlType.ScrollBar
- ControlType.SpinButton
- ControlType.TextBox
- ControlType.ToggleButton
- ControlType.Unknown

Sobald Sie die ActiveX-Steuerung in der Formsammlung hinzugefügt haben, können Sie dann über die [**Shape.ActiveXControl**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/activexcontrol)-Eigenschaft auf das ActiveX-Steuerungselement zugreifen und anschließend seine verschiedenen Eigenschaften festlegen.

{{% /alert %}}

Der folgende Beispielcode fügt eine Umschaltfläche für ActiveX-Steuerungen mithilfe von Aspose.Cells hinzu.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AddActiveXControls-1.cs" >}}
