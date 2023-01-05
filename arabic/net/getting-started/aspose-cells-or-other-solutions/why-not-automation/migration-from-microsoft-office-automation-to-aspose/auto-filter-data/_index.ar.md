---
title: تصفية البيانات تلقائيًا
type: docs
weight: 120
url: /ar/net/auto-filter-data/
---
{{% alert color="primary" %}}

لفهم ماهية البيانات الموجودة في النطاق ، غالبًا ما يكون فرز البيانات وتصفيتها أسهل من النظر إلى أعمدة البيانات غير المرتبة. يعمل الفرز على تنظيم البيانات إما بترتيب تصاعدي أو تنازلي ، مما يسهل العثور على قيم معينة. تسمح لك تصفية البيانات بإظهار قيم معينة فقط. يساعد في التركيز على عناصر معينة في سجلات المبيعات ، على سبيل المثال.

يمكن لمستخدمي Microsoft Excel تطبيق التصفية التلقائية للأعمدة. تضيف التصفية التلقائية قائمة في الجزء العلوي من العمود ، يمكنك من خلالها فرز بيانات عمود التصفية. هذه الميزة متاحة أيضًا للمطورين الذين يعملون مع جداول بيانات Excel ، إما من خلال VSTO أو Aspose.Cells for .NET.

{{% /alert %}}

## **تصفية البيانات تلقائيًا**

لتطبيق التصفية التلقائية على عمود:

1. قم بإنشاء مصنف.
1. احصل على ورقة عمل.
1. أضف بيانات العينة.
1. تطبيق مرشح تلقائي.
1. تناسب الأعمدة تلقائيًا لجعل الشاشة جذابة.
1. احفظ جدول البيانات.

 توضح نماذج التعليمات البرمجية في هذه المقالة كيفية تنفيذ هذه الخطوات باستخدام[VSTO](/cells/ar/net/auto-filter-data/) مع C# أو Visual Basic ، أو باستخدام[الغرض Cells](/cells/ar/net/auto-filter-data/)، مرة أخرى مع C# أو Visual Basic.

### **التصفية التلقائية للبيانات باستخدام VSTO**

**C#**

{{< highlight "csharp" >}}

 using Microsoft.VisualStudio.Tools.Applications.Runtime;

using Excel = Microsoft.Office.Interop.Excel;

using Office = Microsoft.Office.Core;

using System.Reflection;.........//Instantiate the Application object.

Excel.ApplicationClass ExcelApp = new Excel.ApplicationClass();



//Add a Workbook.

Excel.Workbook objBook = ExcelApp.Workbooks.Add(System.Reflection.Missing.Value);



//Get the First sheet.

Excel.Worksheet sheet = (Excel.Worksheet)objBook.Sheets["Sheet1"];



//Add data into A1 and B1 Cells as headers.

sheet.Cells[1, 1]= "Product ID";

sheet.Cells[1, 2]= "Product Name";

//Add data into details cells.

sheet.Cells[2, 1]= 1;

sheet.Cells[3, 1]= 2;

sheet.Cells[4, 1]= 3;

sheet.Cells[5, 1]= 4;

sheet.Cells[2, 2]= "Apples";

sheet.Cells[3, 2]= "Bananas";

sheet.Cells[4, 2]= "Grapes";

sheet.Cells[5, 2]= "Oranges";

//Enable Auto-filter.           

sheet.EnableAutoFilter = true;



//Create the range.

Excel.Range range = sheet.get_Range("A1", "B5");



//Auto-filter the range.

range.AutoFilter("1", "<>", Microsoft.Office.Interop.Excel.XlAutoFilterOperator.xlOr, "", true);

//Auto-fit the second column.

sheet.get_Range("B1", "B5").EntireColumn.AutoFit();



//Save the copy of workbook as .xlsx file.

objBook.SaveCopyAs("e:\\test2\\vsto_autofilter.xlsx");



{{< /highlight >}}

**يتم تطبيق التصفية التلقائية مع VSTO** 

![ما يجب القيام به: image_بديل_نص](auto-filter-data_1.png)

### **التصفية التلقائية للبيانات مع Aspose.Cells for .NET**

**C#**

{{< highlight "csharp" >}}

 //Instantiate a new Workbook.

Workbook objBook = new Workbook();



//Get the First sheet.

Worksheet sheet = objBook.Worksheets["Sheet1"];

//Add data into A1 and B1 Cells as headers.

sheet.Cells[0, 0].PutValue("Product ID");

sheet.Cells[0, 1].PutValue("Product Name");

//Add data into details cells.

sheet.Cells[1, 0].PutValue(1);

sheet.Cells[2, 0].PutValue(2);

sheet.Cells[3, 0].PutValue(3);

sheet.Cells[4, 0].PutValue(4);

sheet.Cells[1, 1].PutValue("Apples");

sheet.Cells[2, 1].PutValue("Bananas");

sheet.Cells[3, 1].PutValue("Grapes");

sheet.Cells[4, 1].PutValue("Oranges");

//Auto-filter the range.

sheet.AutoFilter.Range = "A1:B5";

//Auto-fit the second column.

sheet.AutoFitColumn(1,0,4);

//Save the copy of workbook as .xlsx file.

objBook.Save("e:\\test2\\aspose-cells_autofilter.xlsx");



{{< /highlight >}}

**تم تطبيق المرشح التلقائي بالرمز Aspose.Cells for .NET** 

![ما يجب القيام به: image_بديل_نص](auto-filter-data_2.png)
