---
title: إرسال الشكل إلى الأمام أو الوراء داخل ورقة العمل
type: docs
weight: 3400
url: /ar/python-net/send-shape-front-or-back-inside-the-worksheet/
---

## **سيناريوهات الاستخدام المحتملة**

عندما تتواجد أشكال متعددة في نفس الموقع، فإن مدى ظهورها يُحدد بمواقع ترتيب z الخاص بها. يوفر Aspose.Cells لبايثون via .NET طريقة [**Shape.to_front_or_back()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/to_front_or_back) والتي تغير من موضع ترتيب z للشكل. إذا أردت إرسال شكل إلى الخلف، ستستخدم رقمًا سالبًا مثل -1، -2، -3، وهكذا، وإذا أردت إرساله إلى الأمام، ستستخدم رقمًا موجَبًا مثل 1، 2، 3، وهكذا.

## **إرسال الشكل إلى الأمام أو الوراء داخل ورقة العمل**

الكود العيني التالي يشرح استخدام الطريقة [**Shape.to_front_or_back()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/to_front_or_back). يرجى الرجوع إلى [ملف الإكسل العيني](50528330.xlsx) المستخدم داخل الكود و[ملف الإكسل الناتج](50528331.xlsx) الذي تم إنشاؤه بواسطته. تظهر اللقطة الملتقطة تأثير الكود على ملف الإكسل العيني عند تنفيذه.

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-SendShapeFrontOrBackInWorksheet.py" >}}
