---
title: إضافة عناصر التحكم ActiveX باستخدام Aspose.Cells
type: docs
weight: 260
url: /ar/net/add-activex-controls-using-aspose-cells/
---

{{% alert color="primary" %}}

يمكنك إضافة أشرطة التحكم ActiveX باستخدام طريقة [**ShapeCollection.AddActiveXControl()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addactivexcontrol). تأخذ هذه الطريقة معلمة [**ControlType**](https://reference.aspose.com/cells/net/aspose.cells.drawing.activexcontrols/controltype) التي تخبر ما نوع أشرطة تحكم ActiveX التي يجب إضافتها داخل ورقة عمل. لديها القيم التالية.

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

بمجردإضافتكلتحكمActiveX داخلمجموعةالشكل، يمكنكمنثمالوصولإلىكائنتحكمActiveXعبرخاصية[**Shape.ActiveXControl**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/activexcontrol)ثمتعيينخصائصه(متغيراته) المختلفة.

{{% /alert %}}

يقومالكودالمصدرالتاليبإضافةزرتبديلتحكمActiveXباستخدامAspose.Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AddActiveXControls-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
