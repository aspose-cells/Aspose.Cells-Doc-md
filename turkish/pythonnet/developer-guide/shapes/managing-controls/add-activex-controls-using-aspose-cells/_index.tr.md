---
title: AktifX Kontrolleri Ekle
type: docs
weight: 260
url: /tr/python-net/add-activex-controls-using-aspose-cells/
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET kullanarak AktifX kontrollerini [**ShapeCollection.add_active_x_control()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_active_x_control) yöntemiyle ekleyebilirsiniz. Bu yöntem, çalışma sayfasına hangi türde bir AktifX kontrolü eklenmesi gerektiğini belirtir. Aşağıdaki değerler taşır.

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


Bir kez AktifX kontrolü şekil koleksiyonunun içine ekledikten sonra, daha sonra bu AktifX kontrol nesnesine [**Shape.active_x_control**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/active_x_control) özelliği üzerinden erişebilir ve çeşitli özelliklerini ayarlayabilirsiniz.

{{% /alert %}}

Aşağıdaki örnek kod, Aspose.Cells for Python via .NET kullanarak Toggle Button ActiveX Kontrolü ekler.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-AddActiveXControls-1.py" >}}
