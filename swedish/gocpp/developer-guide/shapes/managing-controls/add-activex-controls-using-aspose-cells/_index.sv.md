---
title: Lägg till ActiveX kontroller med Aspose.Cells med Golang via C++
linktitle: Lägg till ActiveX kontroller
type: docs
weight: 260
url: /sv/go-cpp/add-activex-controls-using-aspose-cells/
description: Läs hur du lägger till ActiveX kontroller till Excel blad programmässigt med Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Du kan lägga till ActiveX-kontroller med Aspose.Cells med hjälp av [**ShapeCollection::AddActiveXControl()**](https://reference.aspose.com/cells/go-cpp/shapecollection/addactivexcontrol/)-metoden. Denna metod tar en parameter [**ControlType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.activexcontrols/controltype/) som specificerar vilken typ av ActiveX-kontroll som ska läggas till i ett blad. Den har följande värden:

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

När du har lagt till ActiveX-kontrollen i formgruppen kan du komma åt ActiveX-kontrollobjektet via [**Shape::get_ActiveXControl()**](https://reference.aspose.com/cells/go-cpp/shape/getactivexcontrol/)-metoden och ställa in dess olika egenskaper.

{{% /alert %}}

Följande exempel kod lägger till en Toggle Button ActiveX-kontroll med Aspose.Cells for C++.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddActivexControlsUsingAsposeCells.go" >}}
