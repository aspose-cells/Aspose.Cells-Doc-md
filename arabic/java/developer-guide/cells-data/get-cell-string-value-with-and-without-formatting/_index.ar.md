---
title: الحصول على قيمة سلسلة الخلية مع أو بدون تنسيق
type: docs
weight: 230
url: /ar/java/get-cell-string-value-with-and-without-formatting/
---

{{% alert color="primary" %}} 

يوفر Aspose.Cells طريقة [Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue-int-) التي يمكن استخدامها للحصول على القيمة النصية للخلية مع أو بدون أي تنسيق. على سبيل المثال، لديك خلية بقيمة 0.012345 وقمت بتنسيقها لعرض منزلتين عشريتين فقط. ستظهر كنص 0.01 في Excel. يمكنك استرجاع القيم النصية كـ 0.01 و 0.012345 باستخدام طريقة [Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue-int-). تأخذ هذه الطريقة قائمة على enum تسمى [CellValueFormatStrategy](https://reference.aspose.com/cells/java/com.aspose.cells/CellValueFormatStrategy) والتي تحتوي على القيم التالية

- [CellValueFormatStrategy.CELL_STYLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#CELL-STYLE)
- [CellValueFormatStrategy.DISPLAY_STYLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#DISPLAY-STYLE)
- [CellValueFormatStrategy.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#NONE)

{{% /alert %}} 
## **الحصول على قيمة سلسلة الخلية بتنسيق وبدون تنسيق**
يوضح الشفرة النموذجية التالية استخدام [Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue-int-).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetCellStringValue-GetCellStringValue.java" >}}
## **مخرجات الوحدة**
فيما يلي إخراج وحدة التحكم للرمز العيني أعلاه.

{{< highlight java >}}

 0.01

0.012345

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
