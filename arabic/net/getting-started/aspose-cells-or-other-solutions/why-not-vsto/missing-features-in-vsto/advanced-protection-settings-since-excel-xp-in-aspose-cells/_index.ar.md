---
title: إعدادات الحماية المتقدمة منذ Excel XP في Aspose.Cells
type: docs
weight: 20
url: /ar/net/advanced-protection-settings-since-excel-xp-in-aspose-cells/
---
{{% alert color="primary" %}}

- احذف الصفوف أو الأعمدة.
- تحرير المحتويات أو الكائنات أو السيناريوهات.
- تنسيق الخلايا أو الصفوف أو الأعمدة.
- قم بإدراج صفوف أو أعمدة أو ارتباطات تشعبية.
- حدد الخلايا المؤمنة أو غير المؤمنة.
- استخدم الجداول المحورية وغير ذلك الكثير.

يدعم Aspose.Cells كافة إعدادات الحماية المتقدمة التي يوفرها Excel XP أو الإصدارات الأحدث.

{{% /alert %}}

## **إعدادات الحماية المتقدمة باستخدام Excel XP والإصدارات الأحدث**

لعرض إعدادات الحماية المتوفرة في Excel XP:

1.  من**أدوات** القائمة ، حدد**حماية** تليها**ورقة حماية**.
 يتم عرض مربع حوار.

   **مربع حوار لإظهار خيارات الحماية في Excel XP**

![ما يجب القيام به: image_بديل_نص](advanced-protection-settings-since-excel-xp-in-aspose-cells_1.png)

1. السماح أو تقييد ميزات أوراق العمل أو تطبيق كلمة مرور.

### **إعدادات الحماية المتقدمة باستخدام Aspose.Cells**

Aspose.Cells يدعم كل إعدادات الحماية المتقدمة.

 Aspose.Cells يوفر فصل دراسي ،[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) ، يمثل ملف Excel Microsoft. ال[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) فئة تحتوي على[**أوراق عمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) مجموعة تسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) صف دراسي.

 ال[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) فئة توفر[**حماية**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection)الخاصية المستخدمة لتطبيق إعدادات الحماية المتقدمة هذه. ال[**حماية**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection) الخاصية هي في الواقع كائن من[**حماية**](https://reference.aspose.com/cells/net/aspose.cells/protection) فئة تضم العديد من الخصائص المنطقية لتعطيل القيود أو تمكينها.

يوجد أدناه مثال صغير للتطبيق. يفتح ملف Excel ويستخدم معظم إعدادات الحماية المتقدمة التي يدعمها Excel XP والإصدارات الأحدث.

**C#**

{{< highlight "csharp" >}}

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

## **تحميل كود الجري**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Advanced%20Protection%20Settings)

## **تنزيل نموذج التعليمات البرمجية**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
