---
title: Aspose.Cells'i kullanarak ActiveX Denetimleri ekleyin
type: docs
weight: 260
url: /tr/net/add-activex-controls-using-aspose-cells/
---
{{% alert color="primary" %}}

 ActiveX denetimlerini Aspose.Cells ile ekleyebilirsiniz.[**ShapeCollection.AddActiveXControl()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addactivexcontrol) yöntem. Bu metot bir parametre alır.[**Kontrol tipi**](https://reference.aspose.com/cells/net/aspose.cells.drawing.activexcontrols/controltype)bir çalışma sayfasına ne tür ActiveX denetimi eklenmesi gerektiğini söyler. Aşağıdaki değerlere sahiptir.

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
- ControlType.Bilinmeyen

 ActiveX denetimini şekil koleksiyonunun içine ekledikten sonra, ActiveX denetim nesnesine şu şekilde erişebilirsiniz:[**Shape.ActiveXControl**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/activexcontrol) özellik ve ardından çeşitli özelliklerini ayarlayın.

{{% /alert %}}

Aşağıdaki örnek kod, Aspose.Cells kullanarak Geçiş Düğmesi ActiveX Denetimi'ni ekler.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AddActiveXControls-1.cs" >}}
