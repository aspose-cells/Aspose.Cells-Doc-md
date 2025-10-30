---
title: Aspose.Cells kullanarak Golang ile C++ kullanarak ActiveX Kontrolleri Ekleme
linktitle: AktifX Kontrolleri Ekle
type: docs
weight: 260
url: /tr/go-cpp/add-activex-controls-using-aspose-cells/
description: Aspose.Cells for C++ kullanarak ActiveX kontrollerini Excel çalışma sayfalarına programatik olarak nasıl ekleyeceğinizi öğrenin.
---

{{% alert color="primary" %}}

Aspose.Cells ile ActiveX kontrollerini [**ShapeCollection::AddActiveXControl()**](https://reference.aspose.com/cells/go-cpp/shapecollection/addactivexcontrol/) yöntemiyle ekleyebilirsiniz. Bu yöntem, bir parametre [**ControlType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.activexcontrols/controltype/) alır ve bu parametre, bir çalışma sayfasına eklenecek ActiveX kontrol türünü belirtir. Aşağıdaki değerleri alır:

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
- ControlType::Bilinmeyen

ActiveX kontrolünü şekil koleksiyonu içine ekledikten sonra, [**Shape::get_ActiveXControl()**](https://reference.aspose.com/cells/go-cpp/shape/getactivexcontrol/) yöntemiyle ActiveX kontrol nesnesine erişebilir ve çeşitli özelliklerini ayarlayabilirsiniz.

{{% /alert %}}

Aşağıdaki örnek kod, Aspose.Cells for C++ kullanarak bir Toggle Button ActiveX Kontrolü ekler.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddActivexControlsUsingAsposeCells.go" >}}
