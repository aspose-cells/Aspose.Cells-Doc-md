---
title: تدوير نص الخلية
type: docs
weight: 100
url: /ar/net/rotating-cell-text/
---

{{% alert color="primary" %}}

أحيانًا، يكون رأس العمود أو العنوان أعرض بكثير من البيانات في الخلايا أدناه. يمكن أن يتسبب هذا في وجود فراغات غير ضرورية على الصفحة. أحد الحلول هو تدوير النص عموديًا بحيث يأخذ مساحة أفقية أقل. في Microsoft Excel، يُسهل تدوير النص. لحسن الحظ، يمكن تدوير النص برمجيًا أيضًا، بحيث يمكن للمطوّرين تدوير التسميات في الجداول النصية التي يقومون بإنشائها ضمن تطبيقاتهم.

يتناول هذا المقال كيفية تدوير النص في الخلايا باستخدام [Aspose.Cells for .NET](/cells/ar/net/rotating-cell-text/) مقارنة بفعل نفس الشيء باستخدام [VSTO](/cells/ar/net/rotating-cell-text/).

{{% /alert %}}

## **تدوير النص في الخلايا**

لتدوير النص في خلية على ورقة العمل، اتبع الخطوات التالية:

1. إنشاء دفتر عمل والحصول على ورقة عمل.
2. إضافة نصوص عينات.
3. تنسيق النص: تدوير، إضافة لون خلفية.
4. حفظ الملف.

توضح الأمثلة التالية كيفية تنفيذ هذه الخطوات أولاً في [VSTO](/cells/ar/net/rotating-cell-text/)، باستخدام إما C# أو Visual Basic، ثم في [Aspose.Cells](/cells/ar/net/rotating-cell-text/)، مرة أخرى باستخدام إما C# أو Visual Basic.

تعطي أمثلة الشفرات في هذا المقال الناتج المعروض أدناه.
**خلية بها نص مدوّر.**

![todo:image_alt_text](rotating-cell-text_1.png)

### **تدوير النص باستخدام VSTO**

**C#**

{{< highlight csharp >}}

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

objSheet.Cells[2, 2] = "Aspose Heading";

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

#### **تدوير النص باستخدام Aspose.Cells for .NET**

**C#**

{{< highlight csharp >}}

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
