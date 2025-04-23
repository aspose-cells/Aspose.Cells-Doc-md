---
title: إعدادات الحماية المتقدمة منذ Excel XP في Aspose.Cells
type: docs
weight: 20
url: /ar/net/advanced-protection-settings-since-excel-xp-in-aspose-cells/
---

{{% alert color="primary" %}}

- حذف الصفوف أو الأعمدة.
- تحرير المحتويات أو الكائنات أو السيناريوهات.
- تنسيق الخلايا أو الصفوف أو الأعمدة.
- إدراج الصفوف أو الأعمدة أو الروابط الفرعية.
- تحديد الخلايا المقفلة أو غير المقفلة.
- استخدام الجداول المحورية وأكثر من ذلك بكثير.

تدعم Aspose.Cells جميع إعدادات الحماية المتقدمة المقدمة من Excel XP أو الإصدارات اللاحقة.

{{% /alert %}}

## **إعدادات الحماية المتقدمة باستخدام Excel XP والإصدارات اللاحقة**

لعرض إعدادات الحماية المتاحة في Excel XP:

1. من القائمة **الأدوات**, حدد **الحماية** تلاها **حماية الورقة**.
   يتم عرض مربع حوار.

   **مربع حوار لإظهار خيارات الحماية في Excel XP**

![todo:image_alt_text](advanced-protection-settings-since-excel-xp-in-aspose-cells_1.png)

1. السماح أو تقييد ميزات صفحات العمل أو تطبيق كلمة مرور.

### **إعدادات الحماية المتقدمة باستخدام Aspose.Cells**

تدعم Aspose.Cells جميع إعدادات الحماية المتقدمة.

توفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)، التي تمثل ملف Microsoft Excel. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) على مجموعة [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) التي تتيح الوصول إلى كل ورقة عمل في ملف Excel. تمثل ورقة عمل بفئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet).

تقدم فئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) خاصية [**Protection**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection) التي تُستخدم لتطبيق هذه الإعدادات المتقدمة للحماية. الخاصية [**Protection**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection) هي في الواقع كائن لفئة [**Protection**](https://reference.aspose.com/cells/net/aspose.cells/protection) التي تحتوي على عدة خصائص بوليانية لتعطيل أو تمكين القيود.

فيما يلي مثال تطبيقي صغير. يفتح ملف Excel ويستخدم معظم إعدادات الحماية المتقدمة المدعومة من Excel XP والإصدارات اللاحقة.

**C#**

{{< highlight csharp >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("book1.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook excel = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = excel.Worksheets[0];

//Restricting users to delete columns of the worksheet

worksheet.Protection.AllowDeletingColumn = false;

//Restricting users to delete row of the worksheet

worksheet.Protection.AllowDeletingRow = false;

//Restricting users to edit contents of the worksheet

worksheet.Protection.AllowEditingContent = false;

//Restricting users to edit objects of the worksheet

worksheet.Protection.AllowEditingObject = false;

//Restricting users to edit scenarios of the worksheet

worksheet.Protection.AllowEditingScenario = false;

//Restricting users to filter

worksheet.Protection.AllowFiltering = false;

//Allowing users to format cells of the worksheet

worksheet.Protection.AllowFormattingCell = true;

//Allowing users to format rows of the worksheet

worksheet.Protection.AllowFormattingRow = true;

//Allowing users to insert columns in the worksheet

worksheet.Protection.AllowFormattingColumn = true;

//Allowing users to insert hyperlinks in the worksheet

worksheet.Protection.AllowInsertingHyperlink = true;

//Allowing users to insert rows in the worksheet

worksheet.Protection.AllowInsertingRow = true;

//Allowing users to select locked cells of the worksheet

worksheet.Protection.AllowSelectingLockedCell = true;

//Allowing users to select unlocked cells of the worksheet

worksheet.Protection.AllowSelectingUnlockedCell = true;

//Allowing users to sort

worksheet.Protection.AllowSorting = true;

//Allowing users to use pivot tables in the worksheet

worksheet.Protection.AllowUsingPivotTable = true;

//Saving the modified Excel file

excel.Save("output.xls", SaveFormat.Excel97To2003);

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}

## **تحميل رمز التشغيل**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Advanced%20Protection%20Settings)

## **تحميل رمز عينة**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
{{< app/cells/assistant language="csharp" >}}
