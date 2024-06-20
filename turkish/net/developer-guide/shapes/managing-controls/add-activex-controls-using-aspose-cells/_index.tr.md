---
title: Aspose.Cells Kullanarak AktifX Kontrolleri Ekleme
type: docs
weight: 260
url: /tr/net/add-activex-controls-using-aspose-cells/
---

{{% alert color="primary" %}}

Aspose.Cells ile AktifX kontrolleri [**ShapeCollection.AddActiveXControl()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addactivexcontrol) yöntemi kullanılarak ekleyebilirsiniz. Bu yöntem, hangi türde AktifX kontrolünün bir çalışma sayfasının içine eklenmesi gerektiğini söyleyen bir parametre olan [**ControlType**](https://reference.aspose.com/cells/net/aspose.cells.drawing.activexcontrols/controltype) alır. Aşağıdaki değerlere sahiptir.

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

Bir kez AktifX kontrolü şekil koleksiyonunun içine ekledikten sonra, daha sonra bu AktifX kontrol nesnesine [**Shape.ActiveXControl**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/activexcontrol) özelliği üzerinden erişebilir ve çeşitli özelliklerini ayarlayabilirsiniz.

{{% /alert %}}

Aşağıdaki örnek kod, Aspose.Cells kullanarak Toggle Button AktifX Kontrolü ekler.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AddActiveXControls-1.cs" >}}
