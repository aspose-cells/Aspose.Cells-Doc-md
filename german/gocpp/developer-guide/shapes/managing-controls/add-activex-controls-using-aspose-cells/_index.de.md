---
title: ActiveX Steuerelemente mit Aspose.Cells mit Golang via C++ hinzufügen
linktitle: ActiveX Steuerelemente hinzufügen
type: docs
weight: 260
url: /de/go-cpp/add-activex-controls-using-aspose-cells/
description: Erfahren Sie, wie man ActiveX Steuerelemente programmgesteuert zu Excel Arbeitsblättern mit Aspose.Cells for C++ hinzufügt.
---

{{% alert color="primary" %}}

Sie können ActiveX-Steuerelemente mit Aspose.Cells mithilfe der [**ShapeCollection::AddActiveXControl()**](https://reference.aspose.com/cells/go-cpp/shapecollection/addactivexcontrol/)-Methode hinzufügen. Diese Methode nimmt einen Parameter [**ControlType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.activexcontrols/controltype/) entgegen, der den Typ des hinzuzufügenden ActiveX-Steuerelements innerhalb eines Arbeitsblatts angibt. Es hat die folgenden Werte:

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
- ControlType::Unbekannt

Nachdem Sie das ActiveX-Steuerelement in die Shapes-Sammlung eingefügt haben, können Sie das ActiveX-Steuerelement-Objekt mit der [**Shape::get_ActiveXControl()**](https://reference.aspose.com/cells/go-cpp/shape/getactivexcontrol/)-Methode zugreifen und verschiedene Eigenschaften davon setzen.

{{% /alert %}}

Der folgende Beispielcode fügt einen Umschaltknopf ActiveX-Control mit Aspose.Cells for C++ hinzu.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddActivexControlsUsingAsposeCells.go" >}}
