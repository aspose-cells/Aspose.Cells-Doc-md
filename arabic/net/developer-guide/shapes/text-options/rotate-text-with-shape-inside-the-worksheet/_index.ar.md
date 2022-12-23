---
title: استدارة النص بالشكل داخل ورقة العمل
type: docs
weight: 1300
url: /ar/net/rotate-text-with-shape-inside-the-worksheet/
---
## **سيناريوهات الاستخدام الممكنة**

يمكنك إضافة نص داخل أي شكل باستخدام Microsoft Excel. إذا أضفت شكلًا باستخدام الإصدار Microsoft Excel 2003 القديم جدًا ، فلن يتم تدوير النص مع الشكل. ولكن إذا أضفت شكلًا باستخدام إصدارات أحدث من Microsoft Excel مثل 2007 أو 2010 أو 2013 أو 2016 ، وما إلى ذلك ، فسيتم تدوير النص بالشكل. يمكنك التحكم في ما إذا كان يجب تدوير النص بالشكل أم لا باستخدام ملف[**ShapeTextAlignment.RotateTextWithShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing.texts/shapetextalignment/properties/rotatetextwithshape) خاصية. القيمة الافتراضية لها هي**حقيقي**مما يعني أن النص سيتم تدويره بالشكل ولكن إذا قمت بتعيينه على هذا النحو**خاطئة**، فلن يتم تدوير النص بالشكل.

## **استدارة النص بالشكل داخل ورقة العمل**

 يقوم نموذج التعليمات البرمجية التالي بتحميل ملف[نموذج لملف Excel](64716896.xlsx) التي لها شكل مثلث ونصها يدور مع الشكل. إذا قمت بفتح نموذج ملف Excel في Microsoft Excel وقمت بتدوير شكل المثلث ، فسيتم تدوير النص معه أيضًا. يقوم الرمز بعد ذلك بتعيين ملف[**ShapeTextAlignment.RotateTextWithShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing.texts/shapetextalignment/properties/rotatetextwithshape) الملكية مثل**خاطئة** ويحفظها باسم[إخراج ملف Excel](64716897.xlsx). إذا قمت الآن بفتح ملف Excel الناتج في Microsoft Excel وقمت بتدوير شكل المثلث ، فلن يتم تدوير النص معه. يرجى الاطلاع على لقطة الشاشة التالية التي توضح تأثير الكود على نموذج ملف Excel كمرجع.

![ما يجب القيام به: image_بديل_نص](rotate-text-with-shape-inside-the-worksheet_1.png)

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "DrawingObjects-RotateTextWithShapeInsideWorksheet.cs" >}}
