---
title: تحقق من كلمة المرور للتعديل باستخدام Aspose.Cells
type: docs
weight: 2400
url: /ar/net/check-password-to-modify-using-aspose-cells/
---
{{% alert color="primary" %}}

 في بعض الأحيان ، تحتاج إلى التحقق مما إذا كانت كلمة المرور المقدمة تتطابق مع**كلمة مرور للتعديل** برمجيا. يوفر Aspose.Cells طريقة WorkbookSettings.WriteProtection.ValidatePassword () التي يمكنك استخدامها للتحقق مما إذا كانت كلمة المرور المعينة للتعديل صحيحة أم لا.

{{% /alert %}}

## **تحقق من كلمة المرور للتعديل في Microsoft Excel**

يمكنك التنازل**كلمة السر لفتح** و**كلمة مرور للتعديل** أثناء إنشاء المصنفات الخاصة بك في Microsoft Excel. يرجى الاطلاع على لقطة الشاشة هذه التي توضح الواجهة Microsoft التي يوفرها Excel لتحديد كلمات المرور هذه.

|![ما يجب القيام به: image_بديل_نص](check-password-to-modify-using-aspose-cells_1.png)|
|:- |

## **تحقق من كلمة المرور للتعديل باستخدام Aspose.Cells**

 تقوم الرموز النموذجية التالية بتحميل ملف[مصدر Excel](5112232.xlsx) ملف. يحتوي على كلمة مرور لفتحها كـ 1234 وكلمة مرور لتعديلها كـ 5678. يتحقق الكود أولاً مما إذا كانت 567 هي كلمة مرور صحيحة لتعديلها ويعيد خطأ ، ثم يتحقق مما إذا كانت 5678 هي كلمة مرور لتعديلها وإرجاعها صحيحة.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CheckPasswordToModify-CheckPasswordToModifyUsingAsposeCells.cs" >}}

### **إخراج وحدة التحكم**

 إليك إخراج وحدة التحكم لعينة التعليمات البرمجية أعلاه بعد تحميل ملف[مصدر Excel](5112232.xlsx) ملف.

{{< highlight "java" >}}

Is 567 correct Password to modify: False

Is 5678 correct Password to modify: True

{{< /highlight >}}
