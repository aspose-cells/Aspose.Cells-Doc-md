---
title: أضف Cell عمليات التحقق من صحة البيانات
type: docs
weight: 90
url: /ar/net/add-cell-data-validations/
---
{{% alert color="primary" %}} 

 Aspose.Cells.GridWeb يسمح لك بإضافة ملفات**تأكيد صحة البيانات** باستخدام طريقة GridWorksheet.Validations.Add (). باستخدام هذه الطريقة ، يجب عليك تحديد**نطاق Cell** ولكن إذا كنت ترغب في إنشاء التحقق من صحة البيانات في GridCell واحدة ، فيمكنك القيام بذلك مباشرةً باستخدام طريقة GridCell.CreateValidation (). وبالمثل ، يمكنك إزالة ملفات**تأكيد صحة البيانات** من GridCell باستخدام طريقة GridCell.RemoveValidation ().

{{% /alert %}} 
## **إنشاء التحقق من صحة البيانات في GridCell من GridWeb**
 يقوم نموذج التعليمات البرمجية التالي بإنشاء ملف**تأكيد صحة البيانات** في الخلية B3. إذا أدخلت أي قيمة ليست بين 20 و 40 ، فستظهر الخلية B3**خطئ في التحقق** في شكل**أحمر XXXX** كما هو موضح في لقطة الشاشة هذه.

![ما يجب القيام به: image_بديل_نص](add-cell-data-validations_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddDataValidation.aspx-AddDataValidation.cs" >}}
