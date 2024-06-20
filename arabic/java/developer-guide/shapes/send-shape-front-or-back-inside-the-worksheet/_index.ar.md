---
title: إرسال الشكل إلى الأمام أو الوراء داخل ورقة العمل
type: docs
weight: 600
url: /ar/java/send-shape-front-or-back-inside-the-worksheet/
---

## **سيناريوهات الاستخدام المحتملة**

عند وجود أشكال متعددة في نفس الموقع، يتم تحديد مدى وضوحها من خلال مواقفها في ترتيب الصف (z-order). يوفر Aspose.Cells الطريقة [**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#toFrontOrBack(int)) التي تغير موقف ترتيب الصف. إذا كنت ترغب في إرسال الشكل إلى الخلف، فسوف تستخدم عددًا سالبًا مثل -1، -2، -3، وما إلى ذلك، وإذا كنت ترغب في إرسال الشكل إلى الأمام، فستستخدم عددًا موجبًا مثل 1، 2، 3، وهلم جرا.

## **إرسال الشكل إلى الأمام أو الوراء داخل ورقة العمل**

يشرح كود العينة التالي استخدام الطريقة [**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#toFrontOrBack(int)). يرجى الاطلاع على [ملف إكسل عينة](50528362.xlsx) المستخدم داخل الكود و [ملف إكسل الناتج](50528361.xlsx) المولد به. تُظهر لقطة الشاشة تأثير الكود على ملف إكسل العينة عند التنفيذ.

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-DrawingObjects-SendShapeFrontOrBackInWorksheet.java" >}}
