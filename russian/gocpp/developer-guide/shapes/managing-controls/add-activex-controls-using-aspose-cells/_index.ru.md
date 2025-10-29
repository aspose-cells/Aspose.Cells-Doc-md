---
title: Добавить элементы ActiveX с помощью Aspose.Cells с Golang через C++
linktitle: Добавить элементы ActiveX
type: docs
weight: 260
url: /ru/go-cpp/add-activex-controls-using-aspose-cells/
description: Узнайте, как программно добавлять элементы ActiveX в листы Excel с помощью Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Вы можете добавлять элементы ActiveX с помощью Aspose.Cells с использованием метода [**ShapeCollection::AddActiveXControl()**](https://reference.aspose.com/cells/go-cpp/shapecollection/addactivexcontrol/). Этот метод принимает параметр [**ControlType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.activexcontrols/controltype/), который задаёт тип элемента ActiveX для вставки в лист. Значения следующего типа:

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

После добавления элемента ActiveX в коллекцию фигур, вы можете получить объект элемента ActiveX через метод [**Shape::get_ActiveXControl()**](https://reference.aspose.com/cells/go-cpp/shape/getactivexcontrol/) и установить его свойства.

{{% /alert %}}

Следующий пример кода добавляет переключатель (Toggle Button) ActiveX с помощью Aspose.Cells for C++.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddActivexControlsUsingAsposeCells.go" >}}
