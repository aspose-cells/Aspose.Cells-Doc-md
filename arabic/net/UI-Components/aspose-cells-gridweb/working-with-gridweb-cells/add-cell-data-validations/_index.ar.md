---
title: إضافة تحقق من صحة البيانات للخلية
type: docs
weight: 90
url: /ar/net/aspose-cells-gridweb/add-cell-data-validations/
keywords: GridWeb ، التحقق من الصحة ، التحقق من البيانات ، GridValidation
description: يقدم هذا المقال كيفية إضافة التحقق من البيانات (GridValidation) في GridWeb.
---

{{% alert color="primary" %}} 

يتيح لك Aspose.Cells.GridWeb إضافة **التحقق من البيانات** باستخدام طريقة GridWorksheet.Validations.Add(). باستخدام هذه الطريقة، يجب عليك تحديد **نطاق الخلية**. ولكن إذا كنت ترغب في إنشاء التحقق من البيانات في خلية واحدة في الشبكة المربعية يمكنك فعل ذلك مباشرة باستخدام طريقة GridCell.CreateValidation(). بالمثل، يمكنك إزالة **التحقق من البيانات** من خلية الشبكة باستخدام طريقة GridCell.RemoveValidation().

{{% /alert %}} 
## **إنشاء التحقق من البيانات في خلية من GridWeb**
الكود النموذجي التالي ينشئ **التحقق من البيانات** في خلية B3. إذا قمت بإدخال أي قيمة ليست بين 20 و 40، ستظهر خلية B3 **خطأ في التحقق** على شكل **XXXX أحمر** كما هو موضح في هذا اللقطة الشاشة.

![todo:image_alt_text](add-cell-data-validations_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddDataValidation.aspx-AddDataValidation.cs" >}}
