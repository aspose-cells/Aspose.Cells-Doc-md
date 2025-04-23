---
title: تحديد ما إذا تم تحميل الترخيص بنجاح
type: docs
weight: 210
url: /ar/java/determining-if-the-license-is-loaded-successfully/
---

{{% alert color="primary" %}}

Aspose.Cells توفر الخاصية [**Workbook.isLicensed()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#IsLicensed) التي يمكنك استخدامها لتحديد ما إذا تم تحميل الترخيص بنجاح أم لا. إذا قمت باستدعاء هذا الأسلوب قبل تعيين الترخيص، سيُرجع قيمة خاطئة، وإذا قمت باستدعاء هذا الأسلوب بعد تعيين الترخيص، سيُرجع القيمة صحيحة مما يشير إلى أن الترخيص تم تحميله بنجاح.

{{% /alert %}}

## **تحديد ما إذا كانت الترخيص قد تم تحميله بنجاح**

الكود التالي يصل إلى الأسلوب [**Workbook.isLicensed()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#IsLicensed) قبل تعيين ترخيص ويُرجع القيمة خاطئة. ثم يحمل الترخيص ويصل إلى الخاصية مرة أخرى التي تُرجع القيمة صحيحة الآن.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DeterminetheLicenseLoadedSuccessfully-DeterminetheLicenseLoadedSuccessfully.java" >}}

## **مخرجات الوحدة**

إليك إخراج الكونسول للكود العيني أعلاه

{{< highlight java >}}

false

true

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
