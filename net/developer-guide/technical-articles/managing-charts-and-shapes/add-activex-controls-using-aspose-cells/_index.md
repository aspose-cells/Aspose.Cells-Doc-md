---
title: Add ActiveX Controls using Aspose.Cells
type: docs
weight: 260
url: /net/add-activex-controls-using-aspose-cells/
---

{{% alert color="primary" %}}

You can add ActiveX controls with Aspose.Cells using the [**ShapeCollection.AddActiveXControl()**](https://apireference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addactivexcontrol) method. This method takes a parameter [**ControlType**](https://apireference.aspose.com/cells/net/aspose.cells.drawing.activexcontrols/controltype) which tells what type of ActiveX control needs to be added inside a worksheet. It has the following values.

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

Once, you have added the ActiveX control inside the shape collection, you can then access the ActiveX control object via [**Shape.ActiveXControl**](https://apireference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/activexcontrol) property and then set its various properties.

{{% /alert %}}

The following sample code adds Toggle Button ActiveX Control using Aspose.Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AddActiveXControls-1.cs" >}}
