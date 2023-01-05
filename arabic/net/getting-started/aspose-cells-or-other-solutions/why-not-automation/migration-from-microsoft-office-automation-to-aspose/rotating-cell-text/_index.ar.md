---
title: تدوير نص Cell
type: docs
weight: 100
url: /ar/net/rotating-cell-text/
---
{{% alert color="primary" %}}

في بعض الأحيان ، يكون رأس العمود أوسع بكثير من البيانات الموجودة في الخلايا أدناه. يمكن أن يتسبب هذا في وجود مسافات بيضاء غير ضرورية على الصفحة. يتمثل أحد الحلول في تدوير النص رأسيًا بحيث يأخذ مساحة أفقية أقل. في Microsoft Excel ، يكون تدوير النص أمرًا سهلاً. لحسن الحظ ، من الممكن تدوير النص برمجيًا أيضًا ، بحيث يمكن للمطورين تدوير الملصقات في جداول البيانات التي ينشئونها داخل تطبيقاتهم.

 تتناول هذه المقالة كيفية تدوير النص في الخلايا باستخدام[Aspose.Cells for .NET](/cells/ar/net/rotating-cell-text/) مقارنة بفعل الشيء نفسه مع[VSTO](/cells/ar/net/rotating-cell-text/).

{{% /alert %}}

## **تدوير النص في Cells**

لتدوير نص في خلية في ورقة عمل ، اتبع الخطوات التالية:

1. قم بإنشاء مصنف واحصل على ورقة عمل.
1. أضف عينات نصية.
1. تنسيق النص: تدوير وإضافة لون الخلفية.
1. حفظ الملف.

 توضح نماذج التعليمات البرمجية التالية كيفية تنفيذ هذه الخطوات أولاً في[VSTO](/cells/ar/net/rotating-cell-text/) ، باستخدام C# أو Visual Basic ، ثم في[Aspose.Cells](/cells/ar/net/rotating-cell-text/)، مرة أخرى باستخدام إما C# أو Visual Basic.

تعطي أمثلة التعليمات البرمجية في هذه المقالة الإخراج الموضح أدناه.
**خلية بها نص تم تدويره.**

![ما يجب القيام به: image_بديل_نص](rotating-cell-text_1.png)

### **تدوير النص باستخدام VSTO**

**C#**

{{< highlight "csharp" >}}

 using Microsoft.VisualStudio.Tools.Applications.Runtime;

using Excel = Microsoft.Office.Interop.Excel;

using Office = Microsoft.Office.Core;

using System.Reflection;

//Instantiate the Application object.

Excel.ApplicationClass ExcelApp = new Excel.ApplicationClass();

//Add a Workbook.

Excel.Workbook objBook = ExcelApp.Workbooks.Add(System.Reflection.Missing.Value);

//Get the First sheet.

Excel.Worksheet objSheet = (Excel.Worksheet)objBook.Sheets["Sheet1"];

//Put some text into cell B2.

objSheet.Cells[2, 2]= "Aspose Heading";

//Define a range object(B2).

Excel.Range _range;

_range = objSheet.get_Range("B2", "B2");

//Specify the angle of rotation of the text.

_range.Orientation = 45;

//Set the background color.

_range.Interior.Color = System.Drawing.ColorTranslator.ToWin32(Color.FromArgb(0, 51, 105));

//Set the font color of cell text

_range.Font.Color = System.Drawing.ColorTranslator.ToOle(System.Drawing.Color.White);



//Save the excel file.

objBook.SaveCopyAs("c:\\VSTO_RotateText_test.xlsx");

//Quit the Application.

ExcelApp.Quit();



{{< /highlight >}}

#### **تدوير النص مع Aspose.Cells for .NET**

**C#**

{{< highlight "csharp" >}}

 // Instantiate a new Workbook.
 
 Workbook objworkbook = new Workbook();

// Get the First sheet.

Worksheet objworksheet = objworkbook.Worksheets[0];

// Get Cells.

Cells objcells = objworksheet.Cells;// Get a particular Cell.

Cell objcell = objcells["B2"];// Put some text value.

objcell.PutValue("Aspose Heading");



// Get associated style object of the cell.

Style objstyle = objcell.GetStyle();

// Specify the angle of rotation of the text.

objstyle.RotationAngle = 45;



// Set the custom fill color of the cells.

objstyle.ForegroundColor = Color.FromArgb(0, 51, 105);



// Set the background pattern for fill color.

objstyle.Pattern = BackgroundType.Solid;

// Set the font color of cell text

objstyle.Font.Color = Color.White;



// Assign the updated style object back to the cell

objcell.SetStyle(objstyle);



// Save the work book

objworkbook.Save("c:\\RotateText_test.xlsx");



{{< /highlight >}}
