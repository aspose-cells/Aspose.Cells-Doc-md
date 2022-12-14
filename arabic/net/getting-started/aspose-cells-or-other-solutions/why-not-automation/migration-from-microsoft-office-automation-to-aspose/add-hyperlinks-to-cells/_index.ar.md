---
title: أضف ارتباطات تشعبية إلى Cells
type: docs
weight: 60
url: /ar/net/add-hyperlinks-to-cells/
---
{{% alert color="primary" %}}

Aspose.Cells for .NET يسمح لك بأداء أي مهام تقريبًا من خلال التطبيق الخاص بك والتي يمكن للمستخدم تنفيذها في Microsoft Excel. تقارن هذه المقالة كيفية إضافة ارتباط تشعبي إلى خلية في ورقة عمل باستخدام VSTO و Aspose.Cells for .NET.

{{% /alert %}}

## **إضافة ارتباطات تشعبية إلى Cells**

لإضافة ارتباطات تشعبية إلى خلايا في جدول بيانات ، اتبع الخطوات التالية:

1. قم بإعداد ورقة العمل:
 1. إنشاء كائن تطبيق.
 (VSTO فقط.)
 1. إضافة مصنف.
 1. احصل على الورقة الأولى.
 1. أضف نصًا إلى الخلايا التي ستضيف ارتباطًا تشعبيًا إليها.
1. أضف ارتباط تشعبي.
1. احفظ المستند.

 يتم عرض هذه الخطوات في أمثلة التعليمات البرمجية أدناه. توضح الأمثلة الأولى كيفية الاستخدام[VSTO](/cells/ar/net/add-hyperlinks-to-cells/) باستخدام C# أو Visual Basic لإضافة ارتباط تشعبي إلى خلية. توضح الأمثلة التالية كيفية القيام بنفس الشيء باستخدام[Aspose.Cells for .NET](/cells/ar/net/add-hyperlinks-to-cells/)، مرة أخرى باستخدام C# أو Visual Basic.

تنشئ نماذج التعليمات البرمجية ملف Excel يحتوي على ارتباط تشعبي في الخلية A1 في ورقة العمل الأولى.

![ما يجب القيام به: image_بديل_نص](add-hyperlinks-to-cells_1.png)

**تمت إضافة ارتباط تشعبي إلى الخلية A1.**

### **إضافة ارتباطات تشعبية إلى Cells باستخدام VSTO**

**C#**

{{< highlight "csharp" >}}

 .......



using Microsoft.VisualStudio.Tools.Applications.Runtime;

using Excel = Microsoft.Office.Interop.Excel;

using Office = Microsoft.Office.Core;

using System.Reflection;

.......

//Instantiate the Application object.

Excel.ApplicationClass ExcelApp = new Excel.ApplicationClass();

//Add a Workbook.

Excel.Workbook objBook = ExcelApp.Workbooks.Add(System.Reflection.Missing.Value);

//Get the First sheet.

Excel.Worksheet objSheet = (Excel.Worksheet)objBook.Sheets["Sheet1"];



//Define a range object(A1).

Excel.Range _range;

_range = objSheet.get_Range("A1", "A1");

//Add a hyperlink to it.

objSheet.Hyperlinks.Add(_range, "http://www.aspose.com/", Type.Missing, "Click to go to Aspose site", "Aspose Site!");

//Save the excel file.

objBook.SaveCopyAs("c:\\Hyperlink_test.xls"); 

//Quit the Application.

ExcelApp.Quit();



{{< /highlight >}}

### **إضافة ارتباطات تشعبية إلى Cells بواسطة Aspose.Cells for .NET**

**C#**

{{< highlight "csharp" >}}

 .......

using Aspose.Cells;

.......

//Instantiate a new Workbook object.

Workbook workbook = new Workbook();

//Get the First sheet.

Worksheet worksheet = workbook.Worksheets[0];

//Define A1 Cell.

Aspose.Cells.Cell cell = worksheet.Cells["A1"];

//Add a hyperlink to it.

int index = worksheet.Hyperlinks.Add("A1", 1, 1, "http://www.aspose.com/");

worksheet.Hyperlinks[index].TextToDisplay = "Aspose Site!";

worksheet.Hyperlinks[index].ScreenTip = "Click to go to Aspose site";

//Save the excel file.

workbook.Save("c:\\Hyperlink_test.xls");       



{{< /highlight >}}
