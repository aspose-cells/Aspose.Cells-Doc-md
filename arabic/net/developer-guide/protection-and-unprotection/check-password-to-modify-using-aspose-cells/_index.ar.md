---
title: تحقق من كلمة المرور للتعديل باستخدام Aspose.Cells
type: docs
weight: 2400
url: /ar/net/check-password-to-modify-using-aspose-cells/
---

{{% alert color="primary" %}}

في بعض الأحيان، تحتاج إلى التحقق مما إذا كانت كلمة المرور المُعطاة تتطابق مع **كلمة السر للتعديل** بشكل برمجي. يوفر Aspose.Cells الطريقة WorkbookSettings.WriteProtection.ValidatePassword() التي يمكنك استخدامها للتحقق مما إذا كانت كلمة السر المعطاة للتعديل صحيحة أم لا.

{{% /alert %}}

## **التحقق من كلمة المرور للتعديل في Microsoft Excel**

يمكنك تعيين **كلمة السر للفتح** و**كلمة السر للتعديل** أثناء إنشاء جداول البيانات الخاصة بك في Microsoft Excel. يُرجى الرجوع إلى هذا اللقط الشاشة الذي يظهر واجهة Microsoft Excel المُقدمة لتحديد هذه الكلمات السرية.

|![todo:image_alt_text](check-password-to-modify-using-aspose-cells_1.png)|
| :- |

## **التحقق من كلمة المرور للتعديل باستخدام Aspose.Cells**

يقوم الأكواد العينة التالية بتحميل ملف الإكسل المصدري. يحتوي على كلمة سر لفتح الملف 1234 وكلمة سر للتعديل 5678. تقوم الكود أولاً بالتحقق مما إذا كانت 567 كلمة سر للتعديل صحيحة ويُعيد القيمة false وبعد ذلك يتحقق مما إذا كانت 5678 كلمة سر للتعديل ويُعيد القيمة true.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CheckPasswordToModify-CheckPasswordToModifyUsingAsposeCells.cs" >}}

### **مخرجات الوحدة**

إليك مخرجات الكونسول للشيفرة العينة أعلاه بعد تحميل ملف الإكسل المصدري.

{{< highlight java >}}

Is 567 correct Password to modify: False

Is 5678 correct Password to modify: True

{{< /highlight >}}
