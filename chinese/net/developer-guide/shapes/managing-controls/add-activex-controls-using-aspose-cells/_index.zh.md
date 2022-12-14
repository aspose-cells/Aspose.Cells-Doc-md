---
title: 使用 Aspose.Cells 添加 ActiveX 控件
type: docs
weight: 260
url: /zh/net/add-activex-controls-using-aspose-cells/
---
{{% alert color="primary" %}}

您可以使用 Aspose.Cells 添加 ActiveX 控件[**ShapeCollection.AddActiveXControl()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addactivexcontrol)方法。这个方法接受一个参数[**控件类型**](https://reference.aspose.com/cells/net/aspose.cells.drawing.activexcontrols/controltype)它告诉需要在工作表中添加什么类型的 ActiveX 控件。它具有以下值。

- 控件类型.CheckBox
- 控件类型.ComboBox
- 控件类型.CommandButton
- 控件类型.Image
- 控件类型.标签
- 控件类型.ListBox
- 控件类型.RadioButton
- 控件类型.滚动条
- 控件类型.SpinButton
- 控件类型.TextBox
- 控件类型.ToggleButton
- 控件类型.Unknown

一旦您在形状集合中添加了 ActiveX 控件，您就可以通过以下方式访问 ActiveX 控件对象[**形状.ActiveXControl**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/activexcontrol)属性，然后设置其各种属性。

{{% /alert %}}

以下示例代码使用 Aspose.Cells 添加 Toggle Button ActiveX 控件。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AddActiveXControls-1.cs" >}}
