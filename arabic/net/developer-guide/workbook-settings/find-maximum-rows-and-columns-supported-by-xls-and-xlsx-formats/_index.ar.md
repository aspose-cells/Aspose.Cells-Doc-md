---
title: ابحث عن الحد الأقصى من الصفوف والأعمدة التي تدعمها تنسيقات XLS و XLSX
type: docs
weight: 20
url: /ar/net/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/
---
## **سيناريوهات الاستخدام الممكنة**

هناك عدد مختلف من الصفوف والأعمدة التي تدعمها تنسيقات Excel. على سبيل المثال ، يدعم XLS 65536 صفاً و 256 عموداً بينما يدعم XLSX 1048576 صفاً و 16384 عموداً. إذا كنت تريد معرفة عدد الصفوف والأعمدة التي يدعمها تنسيق معين ، فيمكنك استخدام[**المصنف.الإعدادات. MaxRow**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxrow) و[**المصنف.الإعدادات. MaxColumn**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxcolumn)الخصائص.

## **ابحث عن الحد الأقصى من الصفوف والأعمدة التي تدعمها تنسيقات XLS و XLSX**

يقوم نموذج التعليمات البرمجية التالي بإنشاء مصنف أولاً في XLS ثم بتنسيق XLSX. بعد الخلق ، تطبع قيم[**المصنف.الإعدادات. MaxRow**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxrow) و[**المصنف.الإعدادات. MaxColumn**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxcolumn)الخصائص. يرجى الاطلاع على إخراج وحدة التحكم من الكود الوارد أدناه للرجوع اليها.

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "WorkbookSettings-FindMaximumRowsAndColumnsSupportedByXLSAndXLSXFormats.cs" >}}

## **إخراج وحدة التحكم**

{{< highlight "java" >}}

Maximum Rows and Columns supported by XLS format.

Maximum Rows: 65536

Maximum Columns: 256

Maximum Rows and Columns supported by XLSX format.

Maximum Rows: 1048576

Maximum Columns: 16384

{{< /highlight >}}
