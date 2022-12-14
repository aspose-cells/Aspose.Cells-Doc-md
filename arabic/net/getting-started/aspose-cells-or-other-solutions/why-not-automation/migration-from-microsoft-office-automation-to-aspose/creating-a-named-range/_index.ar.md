---
title: إنشاء نطاق مسمى
type: docs
weight: 70
url: /ar/net/creating-a-named-range/
---
{{% alert color="primary" %}}

Aspose.Cells for .NET يتيح للمطورين أداء معظم المهام التي يمكن للمستخدمين القيام بها في Microsoft Excel من خلال تطبيقاتهم. تشرح هذه المقالة كيفية تطبيق نطاق مسمى برمجياً.

النطاق المسمى هو إحدى ميزات Excel التي تتيح لك تعيين اسم لخلية أو نطاق من الخلايا في جدول بيانات Excel. يمكنك بعد ذلك استخدام الاسم في الصيغ للإشارة إلى الخلية (أو النطاق). تسهل النطاقات ذات الأسماء المعقولة فهم الصيغ.

يجب أن يكون النطاق المسمى فريدًا ضمن نطاقه ، لذا لا تستخدم نفس الاسم لعدة نطاقات في ورقة العمل. تساعد أسماء النطاقات الوصفية في تجنب ذلك: على سبيل المثال ، يعد OrderSubTotal أكثر وصفًا من SubTotal ويقل احتمال تكراره على ورقة.

{{% /alert %}}

## **إنشاء نطاق مسمى**

لإنشاء نطاق مسمى:

1. قم بإعداد ورقة العمل:
 1. إنشاء كائن تطبيق.
 (VSTO فقط.)
 1. إضافة مصنف.
 1. احصل على الورقة الأولى.
1. قم بإنشاء نطاق مسمى:
 1. تحديد نطاق.
 1. اسم النطاق.
1. حفظ الملف.

 توضح أمثلة التعليمات البرمجية أدناه كيفية تنفيذ هذه الخطوات باستخدام[VSTO](/cells/ar/net/creating-a-named-range/) مع C# أو فيجوال بيسك. توضح أمثلة التعليمات البرمجية التالية كيفية القيام بنفس الشيء باستخدام[Aspose.Cells for .NET](/cells/ar/net/creating-a-named-range/)، مرة أخرى مع C# أو Visual Basic.
### **إنشاء نطاق مسمى باستخدام VSTO**

**C#**

{{< highlight "csharp" >}}

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

### **تكوين نطاق مسمى بواسطة Aspose.Cells for .NET**

**C#**

{{< highlight "csharp" >}}

 .......

باستخدام Aspose.Cells ؛

.......


// إنشاء كائن مصنف

مصنف المصنف = مصنف جديد () ؛

// الوصول إلى ورقة العمل الأولى في ملف Excel

ورقة عمل ورقة العمل = workbook.Worksheets [0] ؛

// إنشاء نطاق مسمى

نطاق النطاق = ورقة عمل .Cells.CreateRange ("A1"، "B4") ؛

// تعيين اسم النطاق المسمى

range.Name = "Test_Range" ؛

 لـ (int row = 0 ؛ row< range.RowCount; row++)

{

    for (int column = 0; column < range.ColumnCount; column++)

    {

        range[row, column].PutValue("Test");

    }

}

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.Save("C:\\Test_Range.xls");



{{< /highlight >}}
