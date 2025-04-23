---
title: إدراج وإزالة تعليقات الخلية في ورقة عمل في VSTO و Aspose.Cells
type: docs
weight: 150
url: /ar/net/inserting-and-removing-cell-comments-in-a-worksheet-in-vsto-and-aspose-cells/
---

لإضافة تعليقات إلى الخلايا:

1. افتح ملف Excel موجود.
1. أضف تعليقًا لخلية.
4. حفظ الملف.

لإزالة التعليقات، يكون العملية مماثلة، باستثناء إزالة التعليق.

توضح العينات البرمجية أدناه كيفية إضافة تعليق أولاً ثم كيفية إزالة التعليق باستخدام VSTO أو Aspose.Cells for .NET.
## **إدراج التعليقات**
تُظهر مقاطع الشفرة هذه كيفية إضافة تعليق إلى الخلية أولاً باستخدام VSTO (C#) ومن ثم باستخدام Aspose.Cells for .NET (C#).
### **VSTO**
{{< highlight csharp >}}

 //Instantiate the Application object.

 Excel.Application excelApp = Application;

//Specify the template excel file path.

  string myPath = "Book1.xls";

//Open the excel file.

 excelApp.Workbooks.Open(myPath, Missing.Value, Missing.Value,

            Missing.Value, Missing.Value,

            Missing.Value, Missing.Value,

            Missing.Value, Missing.Value,

            Missing.Value, Missing.Value,

            Missing.Value, Missing.Value,

            Missing.Value, Missing.Value);

//Get the A1 cell.

 Excel.Range rng1 = excelApp.get_Range("A1", Missing.Value);

//Add the comment with text.

 rng1.AddComment("This is my comment");

//Save the file.

  excelApp.ActiveWorkbook.Save();

//Quit the Application.

  excelApp.Quit();

{{< /highlight >}}
### **Aspose.Cells**
{{< highlight csharp >}}

 //Specify the template excel file path.

string myPath = "Book1.xls";

//Instantiate a new Workbook.

//Open the excel file.

 Workbook workbook = new Workbook(myPath);

//Add a Comment to A1 cell.

 int commentIndex = workbook.Worksheets[0].Comments.Add("A1");

//Accessing the newly added comment

 Comment comment = workbook.Worksheets[0].Comments[commentIndex];

//Setting the comment note

 comment.Note = "This is my comment";

//Save As the excel file.

 workbook.Save("Book1.xls");

{{< /highlight >}}
## **إزالة التعليقات**
لإزالة تعليق من الخلية، استخدم الأسطر التالية من الشيفرة لـ VSTO (C#) و Aspose.Cells for .NET (C#).
### **VSTO**
{{< highlight csharp >}}

 //Remove the comment.

  rng1.Comment.Delete();


{{< /highlight >}}
### **Aspose.Cells**
{{< highlight csharp >}}

 //removing comments

 workbook.Worksheets[0].Comments.RemoveAt("A1");

{{< /highlight >}}
## **تحميل رمز عينة**
- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Inserting.and.Removing.Cell.Comments.in.a.Worksheet.Aspose.Cells.zip)
- [Sourceforge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Inserting%20and%20Removing%20Cell%20Comments%20in%20a%20Worksheet%20\(Aspose.Cells\).zip/download)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Inserting%20and%20Removing%20Cell%20Comments%20in%20a%20Worksheet%20\(Aspose.Cells\).zip)
{{< app/cells/assistant language="csharp" >}}
