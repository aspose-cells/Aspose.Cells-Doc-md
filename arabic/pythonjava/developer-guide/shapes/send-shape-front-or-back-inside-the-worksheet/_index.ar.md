---
title: جلب الأشكال إلى الأمام أو الخلف في ورقة عمل
type: docs
weight: 3400
url: /ar/python-java/send-shape-front-or-back-inside-the-worksheet/
---

## **سيناريوهات الاستخدام المحتملة**

عند وجود أشكال متعددة في نفس الموقع، يتم تحديد كيفية ظهورها من خلال مواقع ترتيب ال z-order الخاصة بهم. يوفر Aspose.Cells الطريقة [**Shape.toFrontOrBack()**](https://reference.aspose.com/cells/python-java/asposecells.api/shape#toFrontOrBack(int)) التي تغير موقع ترتيب ال z-order للشكل. إذا كنت ترغب في إرسال شكل إلى الخلف، ستستخدم رقمًا سالبًا مثل -1، -2، -3، إلخ وإذا كنت تريد إرسال الشكل إلى الأمام، ستستخدم رقمًا موجبًا مثل 1، 2، 3، إلخ.

## **جلب الشكل إلى الأمام أو الخلف داخل ورقة العمل**

الرمز النموذجي التالي يشرح كيفية استخدام طريقة [**Shape.toFrontOrBack()**](https://reference.aspose.com/cells/python-java/asposecells.api/shape#toFrontOrBack(int)). الرجاء الاطلاع على ملف إكسل [العينة](sampleToFrontOrBack.xlsx) المستخدم داخل الكود وملف إكسل [الإخراج](50528331.xlsx) الذي يتم إنشاؤه بواسطة الكود. يوضح لقطة الشاشة تأثير الكود على الملف التجريبي عند التنفيذ.

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Examples-pythonjava-Shapes-BringShapeFrontOrBackInWorksheet.py" >}}
{{< app/cells/assistant language="csharp" >}}
