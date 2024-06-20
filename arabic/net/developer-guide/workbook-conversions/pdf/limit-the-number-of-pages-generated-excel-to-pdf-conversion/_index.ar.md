---
title: تحديد عدد الصفحات المولدة  تحويل Excel إلى PDF
type: docs
weight: 180
url: /ar/net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
---

{{% alert color="primary" %}}

في بعض الأحيان، ترغب في طباعة مجموعة من الصفحات إلى ملف PDF الناتج. تحتوي Aspose.Cells على القدرة على تحديد الحد الأقصى لعدد الصفحات التي يتم توليدها عند تحويل جدول بيانات Excel إلى صيغة ملف PDF.

{{% /alert %}}

## **تحديد الحد الأقصى لعدد الصفحات المولدة**

المثال التالي يظهر كيفية عرض مجموعة من الصفحات (3 و 4) في ملف Microsoft Excel إلى صيغة PDF.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LimitNumberOfPagesGenerated-1.cs" >}}

{{% alert color="primary" %}}

إذا كان جدول البيانات يحتوي على صيغ، فمن الأفضل استدعاء [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) قبل عرضه إلى صيغة PDF. القيام بذلك يضمن إعادة حساب القيم التي تعتمد على الصيغ، وتقديم القيم الصحيحة في ملف الإخراج.

{{% /alert %}}
