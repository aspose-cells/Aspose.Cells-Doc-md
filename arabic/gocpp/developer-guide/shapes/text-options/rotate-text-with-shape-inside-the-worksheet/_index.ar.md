---
title: تدوير النص مع الشكل داخل ورقة العمل باستخدام Golang عبر C++
linktitle: تدوير النص مع الشكل
type: docs
weight: 1300
url: /ar/go-cpp/rotate-text-with-shape-inside-the-worksheet/
description: تعرف على كيفية التحكم في تدوير النص مع الأشكال في أوراق عمل إكسل باستخدام Aspose.Cells for C++.
---

## **سيناريوهات الاستخدام المحتملة**

يمكنك إضافة نص داخل أي شكل باستخدام Microsoft Excel. إذا قمت بإضافة شكل باستخدام إصدار قديم جداً من Microsoft Excel 2003، فلن يدور النص مع الشكل. ومع ذلك، إذا قمت بإضافة شكل باستخدام إصدارات أحدث من Microsoft Excel، مثل 2007، 2010، 2013، أو 2016، فإن النص سوف يدور مع الشكل. يمكنك التحكم فيما إذا كان النص يجب أن يدور مع الشكل أم لا باستخدام الخاصية [**ShapeTextAlignment.GetRotateTextWithShape()**](https://reference.aspose.com/cells/go-cpp/shapetextalignment/getrotatetextwithshape/). القيمة الافتراضية لهذه الخاصية هي **true**، مما يعني أن النص سيدور مع الشكل. إذا قمت بضبطها على **false**، فلن يدور النص مع الشكل.

## **تدوير النص مع الشكل داخل ورقة العمل**

الكود النموذجي التالي يحمّل ملف إكسل النموذجي الذي يحتوي على شكل مثلث، ويدور النص مع الشكل. إذا قمت بفتح ملف إكسل النموذجي في Microsoft Excel ودوران شكل المثلث، فإن النص سيدور معه أيضاً. ثم يتم ضبط الخاصية [**ShapeTextAlignment.GetRotateTextWithShape()**](https://reference.aspose.com/cells/go-cpp/shapetextalignment/getrotatetextwithshape/) على **false** وحفظه باسم ملف إكسل الناتج. إذا قمت الآن بفتح ملف إكسل الناتج في Microsoft Excel ودوران شكل المثلث، فإن النص لن يدور معه. رجاءً اطلع على الصورة التالية التي تظهر تأثير الكود على ملف إكسل النموذجي للمرجعية.

![todo:image_alt_text](rotate-text-with-shape-inside-the-worksheet_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RotateTextWithShapeInsideTheWorksheet.go" >}}
