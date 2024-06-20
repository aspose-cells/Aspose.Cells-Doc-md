---
title: إرسال الشكل إلى الأمام أو الوراء داخل ورقة العمل
type: docs
weight: 3400
url: /ar/net/send-shape-front-or-back-inside-the-worksheet/
---

## **سيناريوهات الاستخدام المحتملة**

عند وجود أشكال متعددة في نفس الموقع، يتم تحديد كيفية ظهورها من خلال مواقع ترتيب ال z-order الخاصة بهم. يوفر Aspose.Cells الطريقة [**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/tofrontorback) التي تغير موقع ترتيب ال z-order للشكل. إذا كنت ترغب في إرسال شكل إلى الخلف، ستستخدم رقمًا سالبًا مثل -1، -2، -3، إلخ وإذا كنت تريد إرسال الشكل إلى الأمام، ستستخدم رقمًا موجبًا مثل 1، 2، 3، إلخ.

## **إرسال الشكل إلى الأمام أو الوراء داخل ورقة العمل**

الكود العيني التالي يشرح استخدام الطريقة [**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/tofrontorback). يرجى الرجوع إلى [ملف الإكسل العيني](50528330.xlsx) المستخدم داخل الكود و[ملف الإكسل الناتج](50528331.xlsx) الذي تم إنشاؤه بواسطته. تظهر اللقطة الملتقطة تأثير الكود على ملف الإكسل العيني عند تنفيذه.

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-SendShapeFrontOrBackInWorksheet.cs" >}}
