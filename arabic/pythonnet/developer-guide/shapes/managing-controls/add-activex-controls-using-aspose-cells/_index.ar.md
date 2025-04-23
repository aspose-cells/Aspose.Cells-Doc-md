---
title: إضافة عناصر تحكم ActiveX
type: docs
weight: 260
url: /ar/python-net/add-activex-controls-using-aspose-cells/
---

{{% alert color="primary" %}}

يمكنك إضافة عناصر تحكم ActiveX باستخدام Aspose.Cells لبايثون via .NET بواسطة طريقة [**ShapeCollection.add_active_x_control()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_active_x_control). تأخذ هذه الطريقة معلمة [**ControlType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.activexcontrols/controltype) التي تخبر عن نوع عنصر تحكم ActiveX الذي يحتاج إلى إضافته داخل ورقة العمل. لديها القيم التالية.

- نوع_التحكم.زر-أمر
- نوع_التحكم.مربع_اختيار
- نوع_التحكم.مربع_تحقق
- نوع_التحكم.قائمة_صناديق
- نوع_التحكم.مربع_نص
- نوع_التحكم.زر_دوران
- نوع_التحكم.زر_مذياع
- نوع_التحكم.ملصق
- نوع_التحكم.صورة
- نوع_التحكم.زر_التبديل
- نوع_التحكم.شريط_تمرير
- نوع_التحكم.رمز_باركود
- نوع_التحكم.غير_معلوم


بمجردإضافتكلتحكمActiveX داخلمجموعةالشكل، يمكنكمنثمالوصولإلىكائنتحكمActiveXعبرخاصية[**Shape.active_x_control**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/active_x_control)ثمتعيينخصائصه(متغيراته) المختلفة.

{{% /alert %}}

الكود النموذجي التالي يضيف زر تبديل ActiveX باستخدام Aspose.Cells لـ Python via .NET.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-AddActiveXControls-1.py" >}}
