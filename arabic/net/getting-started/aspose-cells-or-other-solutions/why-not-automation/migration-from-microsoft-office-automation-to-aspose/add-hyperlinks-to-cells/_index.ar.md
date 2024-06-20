---
title: إضافة ارتباطات تشعبية إلى الخلايا
type: docs
weight: 60
url: /ar/net/add-hyperlinks-to-cells/
---

{{% alert color="primary" %}}

تتيح لك Aspose.Cells for .NET أداء ما يقرب من أي مهام من خلال تطبيقك يمكن للمستخدم أداؤها في Microsoft Excel. وتقارن هذه المقالة كيفية إضافة ارتباط تشعبي إلى خلية في ورقة عمل باستخدام VSTO و Aspose.Cells for .NET.

{{% /alert %}}

## **إضافة الروابط الفائقة إلى الخلايا**

لإضافة ارتباطات تشعبية للخلايا في ورق جدول بيانات، اتبع الخطوات التالية:

1. إعداد الورقة العمل:
   1. أنشئ كائن تطبيق.
      (فقط VSTO.)
   1. أضف كتاب عمل.
   1. احصل على الورقة الأولى.
   1. أضف نصًا إلى الخلايا التي ستضيف ارتباطًا تشعبيًا لها.
1. أضف ارتباطًا تشعبيًا.
1. حفظ المستند.

تظهر هذه الخطوات في أمثلة الشفرة أدناه. تظهر الأمثلة الأولى كيفية استخدام [VSTO](/cells/ar/net/add-hyperlinks-to-cells/) مع كل من C# أو Visual Basic لإضافة رابط فائق إلى خلية. تظهر الأمثلة التالية كيفية القيام بنفس الشيء باستخدام [Aspose.Cells for .NET](/cells/ar/net/add-hyperlinks-to-cells/) مرة أخرى باستخدام C# أو Visual Basic.

تقوم عينات الرمز بإنشاء ملف Excel يحتوي على رابط تشعبي في الخلية A1 على ورقة العمل الأولى.

![todo:image_alt_text](add-hyperlinks-to-cells_1.png)

**يتم إضافة رابط فائق إلى الخلية A1.**

### **إضافة الروابط الفائقة إلى الخلايا مع VSTO**

**C#**

{{< highlight csharp >}}

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

### **إضافة الروابط الفائقة إلى الخلايا مع Aspose.Cells for .NET**

**C#**

{{< highlight csharp >}}

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
