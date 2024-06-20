---
title: العثور على الصفوف والأعمدة القصوى المدعومة من قبل تنسيقات XLS و XLSX
type: docs
weight: 20
url: /ar/net/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/
---

## **سيناريوهات الاستخدام المحتملة**

هناك عدد مختلف من الصفوف والأعمدة المدعومة من تنسيقات Excel. على سبيل المثال، يدعم ملف XLS 65536 صف و 256 عمودًا بينما يدعم ملف XLSX 1048576 صف و 16384 عمودًا. إذا كنت ترغب في معرفة كم صف وعمود يتم دعمه في التنسيق المعطى، يمكنك استخدام خصائص [**Workbook.Settings.MaxRow**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxrow) و [**Workbook.Settings.MaxColumn**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxcolumn).

## **العثور على الصفوف والأعمدة القصوى المدعومة من قبل تنسيقات XLS و XLSX**

يقوم الشفرة النموذجية التالية بإنشاء دفتر عمل أولاً في تنسيق XLS ثم في تنسيق XLSX. بعد الإنشاء، تقوم بطباعة قيم خصائص [**Workbook.Settings.MaxRow**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxrow) و [**Workbook.Settings.MaxColumn**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxcolumn). يرجى الرجوع إلى إخراج وحدة التحكم في الشفرة أدناه للرجوع إليه.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "WorkbookSettings-FindMaximumRowsAndColumnsSupportedByXLSAndXLSXFormats.cs" >}}

## **مخرجات الوحدة**

{{< highlight java >}}

Maximum Rows and Columns supported by XLS format.

Maximum Rows: 65536

Maximum Columns: 256

Maximum Rows and Columns supported by XLSX format.

Maximum Rows: 1048576

Maximum Columns: 16384

{{< /highlight >}}
