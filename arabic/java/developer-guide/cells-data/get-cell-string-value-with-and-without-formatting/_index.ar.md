---
title: الحصول على قيمة سلسلة الخلية مع أو بدون تنسيق
type: docs
weight: 230
url: /ar/java/get-cell-string-value-with-and-without-formatting/
---

{{% alert color="primary" %}} 

توفر Aspose.Cells طريقة [Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue\(int\)) الذي يمكن استخدامه للحصول على قيمة السلسلة للخلية مع أو بدون أي تنسيق. فترة ، لديك خلية بقيمة 0.012345 وقمت بتنسيقها لعرض رقمين عشريين فقط. ستعرض بعد ذلك كما 0.01 في Excel. يمكنك استرداد القيم النصية سواء كـ 0.01 وكما 0.012345 باستخدام الطريقة [Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue\(int\)) الأسلوب. يأخذ [CellValueFormatStrategy](https://reference.aspose.com/cells/java/com.aspose.cells/CellValueFormatStrategy) تعتمد على القيم التالية كمعلمة.

- [CellValueFormatStrategy.CELL_STYLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#CELL_STYLE)
- [CellValueFormatStrategy.DISPLAY_STYLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#DISPLAY_STYLE)
- [CellValueFormatStrategy.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#NONE)

{{% /alert %}} 
## **الحصول على قيمة سلسلة الخلية بتنسيق وبدون تنسيق**
يشرح الكود النموذجي التالي استخدام الطريقة [Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue\(int\))

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetCellStringValue-GetCellStringValue.java" >}}
## **مخرجات الوحدة**
فيما يلي إخراج وحدة التحكم للرمز العيني أعلاه.

{{< highlight java >}}

 0.01

0.012345

{{< /highlight >}}
