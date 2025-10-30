---
title: Aggiungi controlli ActiveX usando Aspose.Cells con Golang tramite C++
linktitle: Aggiungi controlli ActiveX
type: docs
weight: 260
url: /it/go-cpp/add-activex-controls-using-aspose-cells/
description: Impara come aggiungere controlli ActiveX ai fogli di lavoro Excel mediante programmazione usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Puoi aggiungere controlli ActiveX con Aspose.Cells usando il metodo [**ShapeCollection::AddActiveXControl()**](https://reference.aspose.com/cells/go-cpp/shapecollection/addactivexcontrol/). Questo metodo accetta un parametro [**ControlType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.activexcontrols/controltype/) che specifica il tipo di controllo ActiveX da aggiungere all'interno di un foglio di lavoro. Ha i seguenti valori:

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
- ControlType::Sconosciuto

Una volta aggiunto il controllo ActiveX all'interno della raccolta di forme, puoi accedere all'oggetto del controllo ActiveX tramite il metodo [**Shape::get_ActiveXControl()**](https://reference.aspose.com/cells/go-cpp/shape/getactivexcontrol/) e impostarne le varie proprietà.

{{% /alert %}}

Il codice di esempio seguente aggiunge un controllo ActiveX Toggle Button usando Aspose.Cells for C++.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddActivexControlsUsingAsposeCells.go" >}}
