---
title: 使用 Aspose.Cells 添加 ActiveX 控件
type: docs
weight: 260
url: /zh/net/add-activex-controls-using-aspose-cells/
---

{{% alert color="primary" %}}

您可以使用 Aspose.Cells 的 [**ShapeCollection.AddActiveXControl()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addactivexcontrol) 方法添加 ActiveX 控件。该方法接受一个参数 [**ControlType**](https://reference.aspose.com/cells/net/aspose.cells.drawing.activexcontrols/controltype)，指示需要在工作表内添加何种类型的 ActiveX 控件。它具有以下值。

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

添加 ActiveX 控件到形状集合后，您可以通过 [**Shape.ActiveXControl**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/activexcontrol) 属性访问 ActiveX 控件对象，然后设置其各种属性。

{{% /alert %}}

以下示例代码使用 Aspose.Cells 添加 Toggle Button ActiveX 控件。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AddActiveXControls-1.cs" >}}
