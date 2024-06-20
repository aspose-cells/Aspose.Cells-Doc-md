---
title: تدوير النص مع الشكل داخل ورقة العمل
type: docs
weight: 110
url: /ar/java/rotate-text-with-shape-inside-the-worksheet/
---

## **سيناريوهات الاستخدام المحتملة**

يمكنك إضافة نص داخل أي شكل باستخدام مايكروسوفت إكسل. إذا قمت بإضافة شكل باستخدام إصدار معين من مايكروسوفت إكسل مثل 2007، 2010، 2013 أو 2016 فإن النص سيتم دورانه مع الشكل. يمكنك التحكم في ما إذا كان النص سيدور مع الشكل أم لا باستخدام الخاصية [**ShapeTextAlignment.RotateTextWithShape**](https://reference.aspose.com/cells/java/com.aspose.cells/shapetextalignment#RotateTextWithShape). القيمة الافتراضية لها هي **true** الذي يعني أن النص سيدور مع الشكل ولكن إذا حددتها كـ **false**، فإن النص لن يدور مع الشكل.

## **تدوير النص مع الشكل داخل ورقة العمل**

الكود العيني التالي يقوم بتحميل [ملف إكسل عيني](64716919.xlsx) الذي يحتوي على شكل مثلث ونصه يدور مع الشكل. إذا فتحت ملف إكسل العيني في مايكروسوفت إكسل وقمت بتدوير شكل المثلث، سيتم دوران النص معه. ثم يضبط الكود الخاصية [**ShapeTextAlignment.RotateTextWithShape**](https://reference.aspose.com/cells/java/com.aspose.cells/shapetextalignment#RotateTextWithShape) كـ **false** ويحفظه كـ [ملف إكسل الناتج](64716917.xlsx). إذا فتحت الآن ملف إكسل الناتج في مايكروسوفت إكسل وقمت بتدوير شكل المثلث، فإن النص لن يدور معه. يرجى الرجوع إلى الصورة العينية التالية التي تظهر تأثير الكود على ملف إكسل العيني للإشارة.

![todo:image_alt_text](rotate-text-with-shape-inside-the-worksheet_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "DrawingObjects-RotateTextWithShapeInsideWorksheet.java" >}}
