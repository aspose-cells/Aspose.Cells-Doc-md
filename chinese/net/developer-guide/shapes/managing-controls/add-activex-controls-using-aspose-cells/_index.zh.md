---
title: 使用Aspose.Cells添加ActiveX控件
type: docs
weight: 260
url: /zh/net/add-activex-controls-using-aspose-cells/
---

{{% alert color="primary" %}}

您可以使用 Aspose.Cells 添加ActiveX控件，使用 [**ShapeCollection.AddActiveXControl()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addactivexcontrol) 方法。此方法需要一个参数 [**ControlType**](https://reference.aspose.com/cells/net/aspose.cells.drawing.activexcontrols/controltype)，告诉需要在工作表内添加什么类型的ActiveX控件。它有以下值。

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

添加了ActiveX控件后，您可以通过 [**Shape.ActiveXControl**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/activexcontrol) 属性访问ActiveX控件对象，然后设置其各种属性。

{{% /alert %}}

以下示例代码添加了 Toggle Button ActiveX 控件使用 Aspose.Cells。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AddActiveXControls-1.cs" >}}
