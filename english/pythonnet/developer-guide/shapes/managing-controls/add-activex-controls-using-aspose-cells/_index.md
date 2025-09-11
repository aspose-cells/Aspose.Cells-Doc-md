---
title: Add ActiveX Controls
type: docs
weight: 260
url: /python-net/add-activex-controls-using-aspose-cells/
---

{{% alert color="primary" %}}

You can add ActiveX controls with Aspose.Cells for Python via .NET using the [**ShapeCollection.add_active_x_control()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_active_x_control) method. This method takes a parameter [**ControlType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.activexcontrols/controltype) which tells what type of ActiveX control needs to be added inside a worksheet. It has the following values.

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


Once, you have added the ActiveX control inside the shape collection, you can then access the ActiveX control object via [**Shape.active_x_control**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/active_x_control) property and then set its various properties.

{{% /alert %}}

The following sample code adds Toggle Button ActiveX Control using Aspose.Cells for Python via .NET.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-AddActiveXControls-1.py" >}}
{{< app/cells/assistant language="python-net" >}}