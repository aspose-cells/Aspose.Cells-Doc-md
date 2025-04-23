---
title: تحديد عدد الصفحات المولدة  تحويل Excel إلى PDF
type: docs
weight: 60
url: /ar/java/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
---

{{% alert color="primary" %}}

في بعض الأحيان، ترغب في طباعة مجموعة من الصفحات إلى ملف PDF الناتج. تمتلك Aspose.Cells القدرة على تحديد حد لعدد الصفحات التي يتم إنشاؤها عند تحويل جدول بيانات Excel إلى PDF.

{{% /alert %}}

## **تحديد الحد الأقصى لعدد الصفحات المولدة**

المثال التالي يظهر كيفية عرض مجموعة من الصفحات (3 و 4) في ملف Microsoft Excel إلى صيغة PDF.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LimitNumberofPagesGenerated-LimitNumberofPagesGenerated.java" >}}

{{% alert color="primary" %}}

إذا كان الجدول الخاص بك يحتوي على صيغ، من الأفضل استدعاء [**Workbook.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) قبل عرضه إلى صيغة PDF. فعل ذلك يضمن إعادة حساب القيم المعتمدة على الصيغ، ويتم عرض القيم الصحيحة في الملف الناتج.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
