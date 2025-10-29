---
title: 使用Golang通过C++用Aspose.Cells添加ActiveX控件
linktitle: 添加 ActiveX 控件
type: docs
weight: 260
url: /zh/go-cpp/add-activex-controls-using-aspose-cells/
description: 学习如何使用 Aspose.Cells for C++ 编程方式向 Excel 工作表添加 ActiveX 控件。
---

{{% alert color="primary" %}}

您可以使用 [**ShapeCollection::AddActiveXControl()**](https://reference.aspose.com/cells/go-cpp/shapecollection/addactivexcontrol/) 方法通过 Aspose.Cells 添加 ActiveX 控件。此方法接受一个参数 [**ControlType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.activexcontrols/controltype/) ，指定要在工作表中添加的 ActiveX 控件类型。其值如下：

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

一旦在形状集合中添加了 ActiveX 控件，就可以通过 [**Shape::get_ActiveXControl()**](https://reference.aspose.com/cells/go-cpp/shape/getactivexcontrol/) 方法访问 ActiveX 控件对象，并设置其各种属性。

{{% /alert %}}

以下示例代码使用 Aspose.Cells for C++ 添加了一个切换按钮 ActiveX 控件。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddActivexControlsUsingAsposeCells.go" >}}
