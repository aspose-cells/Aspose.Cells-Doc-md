---
title: حدد عدد الصفحات الناتجة  تحويل Excel إلى PDF باستخدام Golang عبر C++
linktitle: تحديد عدد الصفحات التي تم إنشاؤها
type: docs
weight: 180
url: /ar/go-cpp/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
description: تعلم كيفية تحديد عدد الصفحات الناتجة عند تحويل Excel إلى PDF باستخدام Aspose.Cells مع Golang عبر C++.
---

{{% alert color="primary" %}}

في بعض الأحيان، ترغب في طباعة مجموعة من الصفحات إلى ملف PDF الناتج. تحتوي Aspose.Cells على القدرة على تحديد الحد الأقصى لعدد الصفحات التي يتم توليدها عند تحويل جدول بيانات Excel إلى صيغة ملف PDF.

{{% /alert %}}

## **تحديد الحد الأقصى لعدد الصفحات المولدة**

المثال التالي يظهر كيفية عرض مجموعة من الصفحات (3 و 4) في ملف Microsoft Excel إلى صيغة PDF.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LimitTheNumberOfPagesGeneratedExcelToPdfConversion.go" >}}
{{% alert color="primary" %}}

إذا كان جدول البيانات يحتوي على صيغ، فمن الأفضل استدعاء [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) قبل عرضه إلى صيغة PDF. القيام بذلك يضمن إعادة حساب القيم التي تعتمد على الصيغ، وتقديم القيم الصحيحة في ملف الإخراج.

{{% /alert %}}
