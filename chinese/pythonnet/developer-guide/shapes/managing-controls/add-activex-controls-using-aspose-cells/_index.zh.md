---
title: 添加 ActiveX 控件
type: docs
weight: 260
url: /zh/python-net/add-activex-controls-using-aspose-cells/
---

{{% alert color="primary" %}}

你可以使用 [**ShapeCollection.add_active_x_control()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_active_x_control) 方法与Aspose.Cells for Python via .NET添加ActiveX控件。该方法接受一个参数 [**ControlType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.activexcontrols/controltype)，告诉你需要在工作表中添加的ActiveX控件类型。它具有以下值。

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
- ControlType.UNKNOWN


添加 ActiveX 控件到形状集合后，您可以通过 [**Shape.active_x_control**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/active_x_control) 属性访问 ActiveX 控件对象，然后设置其各种属性。

{{% /alert %}}

以下示例代码使用 Aspose.Cells for Python via .NET 添加切换按钮 ActiveX 控件。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-AddActiveXControls-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
