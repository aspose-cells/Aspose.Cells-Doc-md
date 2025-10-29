---
title: إرسال الشكل للأمام أو للخلف داخل ورقة العمل باستخدام Golang عبر C++
linktitle: إرسال الشكل إلى الأمام أو الوراء داخل ورقة العمل
type: docs
weight: 3400
url: /ar/go-cpp/send-shape-front-or-back-inside-the-worksheet/
description: تعلم كيفية تغيير موضع تتابع z للأشكال في ورقة العمل باستخدام Aspose.Cells for C++.
---

## **سيناريوهات الاستخدام المحتملة**

عندما تكون هناك أشكال متعددة موجودة في نفس الموقع، يتم تحديد مدى رؤيتها من خلال مواقع ترتيب z الخاص بها. توفر Aspose.Cells الطريقة [**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/go-cpp/shape/tofrontorback/)، التي تغير موضع ترتيب z للشكل. إذا كنت ترغب في إرسال شكل إلى الخلف، ستستخدم رقمًا سالبًا مثل -1، -2، -3، وما إلى ذلك. إذا كنت تريد إحضار شكل إلى الأمام، ستستخدم رقمًا موجبًا مثل 1، 2، 3، وما إلى ذلك.

## **إرسال الشكل إلى الأمام أو الوراء داخل ورقة العمل**

يعرض نموذج الكود التالي استخدام الطريقة [**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/go-cpp/shape/tofrontorback/). يرجى الاطلاع على ملف إكسل النموذجي [ملف إكسل عينة](50528330.xlsx) المستخدم في الكود و [ملف إكسل الناتج](50528331.xlsx) الذي تم إنشاؤه بواسطة الكود. تظهر لقطة الشاشة تأثير الكود على ملف إكسل العينة عند التنفيذ.

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SendShapeFrontOrBackInsideTheWorksheet.go" >}}
