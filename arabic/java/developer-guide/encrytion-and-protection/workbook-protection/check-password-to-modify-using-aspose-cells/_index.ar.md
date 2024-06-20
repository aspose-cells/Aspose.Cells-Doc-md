---
title: تحقق من كلمة المرور للتعديل باستخدام Aspose.Cells
type: docs
weight: 190
url: /ar/java/check-password-to-modify-using-aspose-cells/
---

{{% alert color="primary" %}}

يمكنك تعيين **كلمة مرور للفتح** و **كلمة مرور للتعديل** أثناء إنشاء مصنفات العمل في Microsoft Excel. يرجى الرجوع إلى لقطة الشاشة هذه التي تظهر واجهة Microsoft Excel التي توفر هذه الكلمات المرور.

![todo:image_alt_text](check-password-to-modify-using-aspose-cells_1.png)

أحيانًا، قد تحتاج إلى التحقق مما إذا كانت كلمة المرور المعطاة تتطابق مع **كلمة مرور التعديل** بصورة برمجية. توفر Aspose.Cells الطريقة [**workbook.getSettings().getWriteProtection().validatePassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/writeprotection#validatePassword(java.lang.String)) التي يمكنك استخدامها للتحقق مما إذا كانت كلمة المرور المعطاة للتعديل صحيحة أم لا.

{{% /alert %}}

## كود Java للتحقق من كلمة المرور للتعديل باستخدام Aspose.Cells

تحمل الأكواد العينية التالية الملف الأصلي [إكسل](5473057.xlsx) . يحتوي على كلمة مرور للفتح كـ 1234 وكلمة مرور للتعديل كـ 5678. يتحقق الكود أولاً مما إذا كانت كلمة مرور 567 صحيحة للتعديل ويرجع **false**، ثم يتحقق مما إذا كانت كلمة مرور 5678 صحيحة للتعديل ويرجع **true**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CheckPassword-CheckPassword.java" >}}

## الناتج الخاص بالوحدة النمطية الذي تم إنشاؤه بواسطة كود Java

إليك الناتج الخاص بالوحدة النمطية الذي تم إنشاؤه بواسطة كود العينة أعلاه بعد تحميل [ملف الإكسل](5473057.xlsx).

{{< highlight java >}}

Is 567 correct Password to modify: false

Is 5678 correct Password to modify: true

{{< /highlight >}}
