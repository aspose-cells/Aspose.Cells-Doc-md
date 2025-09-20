---
title: Add ActiveX Controls using Aspose.Cells with Golang via C++
linktitle: Add ActiveX Controls
type: docs
weight: 260
url: /go-cpp/add-activex-controls-using-aspose-cells/
description: Learn how to add ActiveX controls to Excel worksheets programmatically using Aspose.Cells for C++.
---

{{% alert color="primary" %}}

You can add ActiveX controls with Aspose.Cells using the [**ShapeCollection::AddActiveXControl()**](https://reference.aspose.com/cells/go-cpp/shapecollection/addactivexcontrol/) method. This method takes a parameter [**ControlType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.activexcontrols/controltype/) which specifies the type of ActiveX control to be added inside a worksheet. It has the following values:

- ControlType::CheckBox
- ControlType::ComboBox
- ControlType::CommandButton
- ControlType::Image
- ControlType::Label
- ControlType::ListBox
- ControlType::RadioButton
- ControlType::ScrollBar
- ControlType::SpinButton
- ControlType::TextBox
- ControlType::ToggleButton
- ControlType::Unknown

Once you have added the ActiveX control inside the shape collection, you can access the ActiveX control object via the [**Shape::get_ActiveXControl()**](https://reference.aspose.com/cells/go-cpp/shape/getactivexcontrol/) method and set its various properties.

{{% /alert %}}

The following sample code adds a Toggle Button ActiveX Control using Aspose.Cells for C++.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddActivexControlsUsingAsposeCells.go" >}}