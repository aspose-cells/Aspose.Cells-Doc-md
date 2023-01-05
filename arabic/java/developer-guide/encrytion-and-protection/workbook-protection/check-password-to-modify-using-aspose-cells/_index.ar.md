---
title: تحقق من كلمة المرور للتعديل باستخدام Aspose.Cells
type: docs
weight: 190
url: /ar/java/check-password-to-modify-using-aspose-cells/
---
{{% alert color="primary" %}}

 يمكنك تعيين ملف**كلمة السر لفتح** و أ**كلمة مرور للتعديل** أثناء إنشاء المصنفات الخاصة بك في Microsoft Excel. يرجى الاطلاع على لقطة الشاشة هذه التي توضح الواجهة Microsoft التي يوفرها Excel لتحديد كلمات المرور هذه.

![ما يجب القيام به: image_بديل_نص](check-password-to-modify-using-aspose-cells_1.png)

 في بعض الأحيان ، تحتاج إلى التحقق مما إذا كانت كلمة المرور المقدمة تتطابق مع**كلمة مرور للتعديل** برمجيا. يوفر Aspose.Cells[**workbook.getSettings (). getWriteProtection (). validatePassword ()**](https://reference.aspose.com/cells/java/com.aspose.cells/writeprotection#validatePassword(java.lang.String)) الطريقة التي يمكنك استخدامها للتحقق مما إذا كانت كلمة المرور المعينة للتعديل صحيحة أم لا.

{{% /alert %}}

## كود Java للتحقق من كلمة المرور للتعديل باستخدام Aspose.Cells

 تقوم الرموز النموذجية التالية بتحميل ملف[مصدر Excel](5473057.xlsx) ملف. يحتوي على كلمة مرور لفتح باسم*1234* وكلمة المرور للتعديل باسم*5678* . يتحقق الرمز أولاً مما إذا كان*567* هي كلمة مرور صحيحة للتعديل وتعود**خاطئة** ثم يتحقق مما إذا كان*5678* هي كلمة مرور للتعديل وتعود**حقيقي**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CheckPassword-CheckPassword.java" >}}

## تم إنشاء خرج وحدة التحكم بواسطة كود Java

 إليك إخراج وحدة التحكم لعينة التعليمات البرمجية أعلاه بعد تحميل ملف[مصدر Excel](5473057.xlsx) ملف.

{{< highlight "java" >}}

Is 567 correct Password to modify: false

Is 5678 correct Password to modify: true

{{< /highlight >}}
