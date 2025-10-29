---
title: إضافة عناصر تحكم ActiveX باستخدام Aspose.Cells مع جولانج عبر C++
linktitle: إضافة عناصر تحكم ActiveX
type: docs
weight: 260
url: /ar/go-cpp/add-activex-controls-using-aspose-cells/
description: تعلم كيف تضيف عناصر تحكم ActiveX إلى أوراق عمل إكسل برمجيًا باستخدام Aspose.Cells for C++.
---

{{% alert color="primary" %}}

يمكنك إضافة عناصر تحكم ActiveX باستخدام Aspose.Cells باستخدام طريقة [**ShapeCollection::AddActiveXControl()**](https://reference.aspose.com/cells/go-cpp/shapecollection/addactivexcontrol/). تأخذ هذه الطريقة معلمة [**ControlType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.activexcontrols/controltype/) التي تحدد نوع عنصر تحكم ActiveX الذي سيتم إضافته داخل ورقة العمل. لها القيم التالية:

- نوع التحكم::مربع اختيار (CheckBox)
- نوع التحكم::مربع تحرير (ComboBox)
- نوع التحكم::زر أمر (CommandButton)
- نوع التحكم::صورة (Image)
- نوع التحكم::تسمية (Label)
- نوع التحكم::قائمة إطار (ListBox)
- نوع التحكم::زر اختيار (RadioButton)
- نوع التحكم::شريط تمرير (ScrollBar)
- نوع التحكم::زر تدوير (SpinButton)
- نوع التحكم::مربع النص (TextBox)
- نوع التحكم::زر تبديل (ToggleButton)
- نوع التحكم::غير معروف (Unknown)

بمجرد إضافة عنصر تحكم ActiveX داخل مجموعة الأشكال، يمكنك الوصول إلى كائن عنصر التحكم ActiveX عبر طريقة [**Shape::get_ActiveXControl()**](https://reference.aspose.com/cells/go-cpp/shape/getactivexcontrol/) وتعيين خصائصه المختلفة.

{{% /alert %}}

الكود النموذجي التالي يضيف عنصر تحكم Toggle Button باستخدام Aspose.Cells for C++.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddActivexControlsUsingAsposeCells.go" >}}
