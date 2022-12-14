---
title: احصل على Cell String Value with وبدون التنسيق
type: docs
weight: 230
url: /ar/java/get-cell-string-value-with-and-without-formatting/
---
{{% alert color="primary" %}} 

 يوفر Aspose.Cells طريقة[Cell.getStringValue ()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue\(int\) والتي يمكن استخدامها للحصول على قيمة سلسلة الخلية مع أو بدون أي تنسيق. افترض أن لديك خلية بقيمة 0.012345 وقمت بتنسيقها لعرض منزلتين عشريتين فقط. سيتم عرضه بعد ذلك على أنه 0.01 في Excel. يمكنك استرداد قيم السلسلة مثل 0.01 و 0.012345 باستخدام امتداد[Cell.getStringValue ()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue\(int\) ) طريقة. تستغرق[CellValueFormatStrategy](https://reference.aspose.com/cells/java/com.aspose.cells/CellValueFormatStrategy)تعداد كمعامل يحتوي على القيم التالية

- [CellValueFormatStrategy.CELL_STYLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#CELL_STYLE)
- [CellValueFormatStrategy.DISPLAY_STYLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#DISPLAY_STYLE)
- [CellValueFormatStrategy.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#NONE)

{{% /alert %}} 
## **احصل على Cell String Value with وبدون التنسيق**
 يشرح نموذج التعليمات البرمجية التالي استخدام[Cell.getStringValue ()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue\(int\)) طريقة.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetCellStringValue-GetCellStringValue.java" >}}
## **إخراج وحدة التحكم**
يوجد أدناه إخراج وحدة التحكم لعينة التعليمات البرمجية أعلاه.

{{< highlight "java" >}}

 0.01

0.012345

{{< /highlight >}}
