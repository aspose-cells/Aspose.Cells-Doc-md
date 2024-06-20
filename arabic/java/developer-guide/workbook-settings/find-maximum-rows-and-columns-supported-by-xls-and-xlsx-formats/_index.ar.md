---
title: العثور على الصفوف والأعمدة القصوى المدعومة من قبل تنسيقات XLS و XLSX
type: docs
weight: 60
url: /ar/java/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/
---

## **سيناريوهات الاستخدام المحتملة**
هناك عدد مختلف من الصفوف والأعمدة المدعومة بتنسيقات Excel. على سبيل المثال، يدعم XLS 65536 صفًا و 256 عمودًا بينما يدعم XLSX 1048576 صفًا و 16384 عمودًا. إذا كنت ترغب في معرفة كم عدد الصفوف والأعمدة المدعومة بتنسيق معين، يمكنك استخدام خصائص [Workbook.Settings.MaxRow](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxRow) و [Workbook.Settings.MaxColumn](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxColumn).
## **العثور على الصفوف والأعمدة القصوى المدعومة من قبل تنسيقات XLS و XLSX**
الكود العينة التالي ينشئ المصنف أولًا في تنسيق XLS ثم في تنسيق XLSX. بعد الإنشاء، يقوم بطباعة قيم [Workbook.Settings.MaxRow](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxRow) و [Workbook.Settings.MaxColumn](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxColumn). يرجى رؤية إخراج وحدة التحكم للكود المعطى أدناه للإحالة.
## **الكود المثالي**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "WorkbookSettings-FindMaximumRowsAndColumnsSupportedByXLSAndXLSXFormats.java" >}}

مخرجات الوحدة

{{< highlight java >}}

 Maximum Rows and Columns supported by XLS format.

Maximum Rows: 65536

Maximum Columns: 256

Maximum Rows and Columns supported by XLSX format.

Maximum Rows: 1048576

Maximum Columns: 16384

{{< /highlight >}}
