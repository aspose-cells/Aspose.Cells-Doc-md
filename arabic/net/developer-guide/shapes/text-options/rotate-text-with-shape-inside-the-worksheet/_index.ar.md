---
title: تدوير النص مع الشكل داخل ورقة العمل
type: docs
weight: 1300
url: /ar/net/rotate-text-with-shape-inside-the-worksheet/
---

## **سيناريوهات الاستخدام المحتملة**

يمكنك إضافة نص داخل أي شكل باستخدام Microsoft Excel. إذا قمت بإضافة شكل باستخدام نسخة قديمة من Microsoft Excel مثل 2003، فإن النص لن يتم تدويره مع الشكل. ولكن إذا قمت بإضافة شكل باستخدام الإصدارات الحديثة من Microsoft Excel مثل 2007، 2010، 2013 أو 2016، إلخ، فسيتم تدوير النص مع الشكل. يمكنك التحكم فيما إذا كان يجب أن يتم تدوير النص مع الشكل أم لا باستخدام الخاصية [**ShapeTextAlignment.RotateTextWithShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing.texts/shapetextalignment/properties/rotatetextwithshape). القيمة الافتراضية لها هي **true** مما يعني أن النص سيتم تدويره مع الشكل ولكن إذا قمت بتعيينها على **false**، فلن يتم تدوير النص مع الشكل.

## **تدوير النص مع الشكل داخل ورقة العمل**

الكود المصدري التالي يحمل [ملف إكسل عينة](64716896.xlsx) الذي يحتوي على شكل مثلث ونصه يتدوير مع الشكل. إذا قمت بفتح ملف إكسل العينة في Microsoft Excel وقمت بتدوير شكل المثلث، سيتم تدوير النص أيضًا معه. يقوم الكود ثم بتعيين الخاصية [**ShapeTextAlignment.RotateTextWithShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing.texts/shapetextalignment/properties/rotatetextwithshape) على **false** ثم يحفظه كـ ملف إكسل [الناتج](64716897.xlsx). إذا قمت الآن بفتح ملف إكسل الناتج في Microsoft Excel وقمت بتدوير شكل المثلث، فلن يتم تدوير النص معه. يُرجى الرجوع إلى اللقطة الشاشة التالية التي تُظهر تأثير الكود على ملف إكسل العينة للإحالة.

![todo:image_alt_text](rotate-text-with-shape-inside-the-worksheet_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "DrawingObjects-RotateTextWithShapeInsideWorksheet.cs" >}}
{{< app/cells/assistant language="csharp" >}}
