---
title: إنشاء نطاق مسمى
type: docs
weight: 70
url: /ar/net/creating-a-named-range/
---

{{% alert color="primary" %}}

يُتيح Aspose.Cells for .NET للمطورين تنفيذ معظم المهام التي يمكن للمستخدمين تنفيذها في Microsoft Excel من خلال تطبيقاتهم. يشرح هذا المقال كيفية تطبيق نطاق مسمى برمجيًا.

نطاق مسمى هو ميزة في Excel تُتيح لك تعيين اسم لخلية أو مجموعة من الخلايا في ورقة بيانات Excel. يمكنك بعد ذلك استخدام الاسم في الصيغ للإشارة إلى الخلية (أو المجموعة). تجعل الأسماء المنطقية للنطاقات الصيغ أسهل فهمًا.

يجب أن يكون لكل نطاق مسمى فريد داخل نطاقه، لذا لا تستخدم نفس الاسم لعدة نطاقات في ورقة عمل. تساعد الأسماء الوصفية للنطاقات في تجنب ذلك: على سبيل المثال، فإن اسم OrderSubTotal هو أكثر وصفية من SubTotal وأقل احتمالاً للتكرار في ورقة بيانات.

{{% /alert %}}

## **إنشاء نطاق مسمى**

لإنشاء نطاق مسمى:

1. إعداد الورقة العمل:
   1. أنشئ كائن تطبيق.
      (فقط VSTO.)
   1. أضف كتاب عمل.
   1. احصل على الورقة الأولى.
1. قم بإنشاء نطاق مسمى:
   1. قم بتعريف نطاق.
   1. أسم النطاق.
4. حفظ الملف.

تُظهر أمثلة الشفرة أدناه كيفية تنفيذ هذه الخطوات باستخدام [VSTO](/cells/ar/net/creating-a-named-range/) بإمكانك استخدام إما C# أو Visual Basic. تُظهر أمثلة الشفرة التي تلي كيفية القيام بنفس الشيء باستخدام [Aspose.Cells for .NET](/cells/ar/net/creating-a-named-range/) مرة أخرى بإمكانك استخدام إما C# أو Visual Basic.
### **إنشاء نطاق مسمى باستخدام VSTO**

**C#**

{{< highlight csharp >}}

 .......

using Microsoft.VisualStudio.Tools.Applications.Runtime;

using Excel = Microsoft.Office.Interop.Excel;

using Office = Microsoft.Office.Core;

using System.Reflection;

.......

//Create Excel Object

Excel.ApplicationClass xl = new Excel.ApplicationClass();

//Create a new Workbook

Excel.Workbook wb = xl.Workbooks.Add(Missing.Value);

//Get Worksheets Collection

Excel.Sheets xlsheets = wb.Sheets;

//Select the first sheet

Excel.Worksheet excelWorksheet = (Excel.Worksheet)xlsheets[1];

//Select a range of cells

Excel.Range range = (Excel.Range)excelWorksheet.get_Range("A1:B4", Type.Missing);

//Add Name to Range

range.Name = "Test_Range";

//Put data in range cells

foreach (Excel.Range cell in range.Cells)

{

    cell.set_Value(Missing.Value, "Test");

}

//Save New Workbook

wb.SaveCopyAs("C:\\Test_Range.xls")

//Quit Excel Object

xl.Quit();



{{< /highlight >}}

### **إنشاء نطاق مسمى باستخدام Aspose.Cells for .NET**

**C#**

{{< highlight csharp >}}

 .......

using Aspose.Cells;

.......


//Instantiating a Workbook object

Workbook workbook = new Workbook();

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Creating a named range

Range range = worksheet.Cells.CreateRange("A1", "B4");

//Setting the name of the named range

range.Name = "Test_Range";

for (int row = 0; row < range.RowCount; row++)

{

    for (int column = 0; column < range.ColumnCount; column++)

    {

        range[row, column].PutValue("Test");

    }

}

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.Save("C:\\Test_Range.xls");



{{< /highlight >}}
