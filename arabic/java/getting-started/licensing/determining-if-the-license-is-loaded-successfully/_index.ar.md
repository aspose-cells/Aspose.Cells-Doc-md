---
title: تحديد ما إذا تم تحميل الترخيص بنجاح
type: docs
weight: 210
url: /ar/java/determining-if-the-license-is-loaded-successfully/
---
{{% alert color="primary" %}}

 يوفر Aspose.Cells[**Workbook.isLicensed ()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#IsLicensed)الخاصية التي يمكنك استخدامها لتحديد ما إذا تم تحميل الترخيص بنجاح أم لا. إذا قمت باستدعاء هذه الطريقة قبل تعيين الترخيص ، فسيعود خطأ ، وإذا قمت باستدعاء هذه الطريقة بعد تعيين الترخيص ، فسيعود الأمر صحيحًا مشيرًا إلى أنه تم تحميل الترخيص بنجاح.

{{% /alert %}}

## **تحديد ما إذا تم تحميل الترخيص بنجاح**

 الكود التالي يصل إلى[**Workbook.isLicensed ()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#IsLicensed)الطريقة قبل تحديد الترخيص وإرجاع كاذبة. ثم يقوم بتحميل الترخيص والوصول إلى العقار مرة أخرى والذي يعود الآن صحيحًا.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DeterminetheLicenseLoadedSuccessfully-DeterminetheLicenseLoadedSuccessfully.java" >}}

## **إخراج وحدة التحكم**

هنا هو إخراج وحدة التحكم من نموذج التعليمات البرمجية أعلاه

{{< highlight "java" >}}

false

true

{{< /highlight >}}
