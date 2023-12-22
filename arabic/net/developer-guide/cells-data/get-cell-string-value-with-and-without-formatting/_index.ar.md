---
title: احصل على قيمة سلسلة Cell مع التنسيق وبدونه
type: docs
weight: 240
url: /ar/net/get-cell-string-value-with-and-without-formatting/
description: تعرف على كيفية الحصول على قيمة سلسلة Cell مع التنسيق وبدونه من خلال Aspose.Cells for .NET API.
keywords: Get Cell String Value with and without Formatting, Retrieve Cell String Value with and without Formatting, Obtain Cell String Value with and without Formatting
---
{{% alert color="primary" %}}

 Aspose.Cells يوفر طريقة[**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue)والتي يمكن استخدامها للحصول على قيمة سلسلة الخلية مع أو بدون أي تنسيق. لنفترض أن لديك خلية بقيمة 0.012345 وقمت بتنسيقها لعرض منزلتين عشريتين فقط. سيتم عرضه بعد ذلك كـ 0.01 في Excel. يمكنك استرداد قيم السلسلة كـ 0.01 و0.012345 باستخدام ملف[**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue) طريقة. فإنه يأخذ[**استراتيجية CellValueFormat**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue)enum كمعلمة تحتوي على القيم التالية

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.None

{{% /alert %}}

 يشرح نموذج التعليمات البرمجية التالي استخدام[**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue)طريقة.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-GetStringValue-GetStringValueWithOrWithoutFormatting.cs" >}}
