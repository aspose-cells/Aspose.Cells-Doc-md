---
title: Agregar controles ActiveX usando Aspose.Cells con Golang vía C++
linktitle: Agregar controles ActiveX
type: docs
weight: 260
url: /es/go-cpp/add-activex-controls-using-aspose-cells/
description: Aprenda cómo agregar controles ActiveX en hojas de cálculo de Excel programáticamente usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Puede agregar controles ActiveX con Aspose.Cells usando el método [**ShapeCollection::AddActiveXControl()**](https://reference.aspose.com/cells/go-cpp/shapecollection/addactivexcontrol/). Este método toma un parámetro [**ControlType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.activexcontrols/controltype/) que especifica el tipo de control ActiveX que se agregará dentro de una hoja de cálculo. Tiene los siguientes valores:

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

Una vez que ha agregado el control ActiveX dentro de la colección de formas, puede acceder al objeto control ActiveX a través del método [**Shape::get_ActiveXControl()**](https://reference.aspose.com/cells/go-cpp/shape/getactivexcontrol/) y establecer sus diversas propiedades.

{{% /alert %}}

El siguiente código de ejemplo agrega un control ActiveX de botón de alternancia usando Aspose.Cells for C++.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddActivexControlsUsingAsposeCells.go" >}}
