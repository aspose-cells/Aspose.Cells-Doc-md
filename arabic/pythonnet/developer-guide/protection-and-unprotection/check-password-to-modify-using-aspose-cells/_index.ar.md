---
title: تحقق من كلمة المرور للتحرير باستخدام Aspose.Cells للبايثون via .NET
type: docs
weight: 2400
url: /ar/python-net/check-password-to-modify-using-aspose-cells/
---

{{% alert color="primary" %}}

أحيانًا، تحتاج إلى التحقق مما إذا كانت كلمة المرور المعطاة تتطابق مع **كلمة المرور للتحرير** برمجياً. يوفر Aspose.Cells للبايثون via .NET طريقة WorkbookSettings.write_protection.validate_password() والتي يمكنك استخدامها للتحقق مما إذا كانت كلمة المرور للتحرير صحيحة أم لا.

{{% /alert %}}

## **التحقق من كلمة المرور للتعديل في Microsoft Excel**

يمكنك تعيين **كلمة السر للفتح** و**كلمة السر للتعديل** أثناء إنشاء جداول البيانات الخاصة بك في Microsoft Excel. يُرجى الرجوع إلى هذا اللقط الشاشة الذي يظهر واجهة Microsoft Excel المُقدمة لتحديد هذه الكلمات السرية.

|![todo:image_alt_text](check-password-to-modify-using-aspose-cells_1.png)|
| :- |

## **التحقق من كلمة المرور للتحرير باستخدام Aspose.Cells للبايثون via .NET**

يقوم الأكواد العينة التالية بتحميل ملف الإكسل المصدري. يحتوي على كلمة سر لفتح الملف 1234 وكلمة سر للتعديل 5678. تقوم الكود أولاً بالتحقق مما إذا كانت 567 كلمة سر للتعديل صحيحة ويُعيد القيمة false وبعد ذلك يتحقق مما إذا كانت 5678 كلمة سر للتعديل ويُعيد القيمة true.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-CheckPasswordToModifyUsingAsposeCells.py" >}}

### **مخرجات الوحدة**

إليك مخرجات الكونسول للشيفرة العينة أعلاه بعد تحميل ملف الإكسل المصدري.

{{< highlight java >}}

Is 567 correct Password to modify: False

Is 5678 correct Password to modify: True

{{< /highlight >}}

{{< app/cells/assistant language="python-net" >}}
