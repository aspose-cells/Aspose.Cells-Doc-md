---
title: يمكنك البحث عن الحد الأقصى من الصفوف والأعمدة المدعومة بالتنسيقات XLS و XLSX
type: docs
weight: 60
url: /ar/java/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/
---
## **سيناريوهات الاستخدام الممكنة**
هناك عدد مختلف من الصفوف والأعمدة التي تدعمها تنسيقات Excel. على سبيل المثال ، يدعم XLS 65536 صفاً و 256 عموداً بينما يدعم XLSX 1048576 صفاً و 16384 عموداً. إذا كنت تريد معرفة عدد الصفوف والأعمدة التي يدعمها تنسيق معين ، فيمكنك استخدام[المصنف.الإعدادات. MaxRow](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxRow)و[المصنف.الإعدادات. MaxColumn](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxColumn)الخصائص.
## **يمكنك البحث عن الحد الأقصى من الصفوف والأعمدة المدعومة بالتنسيقات XLS و XLSX**
ينشئ نموذج التعليمات البرمجية التالي المصنف أولاً في XLS ثم بتنسيق XLSX. بعد الخلق ، تطبع قيم[المصنف.الإعدادات. MaxRow](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxRow)و[المصنف.الإعدادات. MaxColumn](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxColumn)الخصائص. يرجى الاطلاع على إخراج وحدة التحكم من الكود الوارد أدناه للرجوع اليها.
## **عينة من الرموز**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "WorkbookSettings-FindMaximumRowsAndColumnsSupportedByXLSAndXLSXFormats.java" >}}

إخراج وحدة التحكم

{{< highlight "java" >}}

 Maximum Rows and Columns supported by XLS format.

Maximum Rows: 65536

Maximum Columns: 256

Maximum Rows and Columns supported by XLSX format.

Maximum Rows: 1048576

Maximum Columns: 16384

{{< /highlight >}}
