---
title: احصل على Cell String Value with وبدون التنسيق
type: docs
weight: 240
url: /ar/net/get-cell-string-value-with-and-without-formatting/
---
{{% alert color="primary" %}}

 يوفر Aspose.Cells طريقة[**Cell.GetStringValue ()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue) والتي يمكن استخدامها للحصول على قيمة سلسلة الخلية مع أو بدون أي تنسيق. افترض أن لديك خلية بقيمة 0.012345 وقمت بتنسيقها لعرض منزلتين عشريتين فقط. سيتم عرضه بعد ذلك على أنه 0.01 في Excel. يمكنك استرداد قيم السلسلة مثل 0.01 و 0.012345 باستخدام امتداد[**Cell.GetStringValue ()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue) طريقة. تستغرق[**CellValueFormatStrategy**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue)تعداد كمعامل يحتوي على القيم التالية

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.None

{{% /alert %}}

 يشرح نموذج التعليمات البرمجية التالي استخدام[**Cell.GetStringValue ()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue)طريقة.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-GetStringValue-GetStringValueWithOrWithoutFormatting.cs" >}}
