---
title: تعيين صورة الخلفية لورقة العمل
type: docs
weight: 90
url: /ar/net/set-background-picture-of-a-worksheet/
---
{{% alert color="primary" %}}

توجد صور الخلفية خلف النص والخطوط في جدول بيانات. يتم استخدامها لإعطاء معلومات حول مصنف ، على سبيل المثال عند استخدامها كعلامات مائية للحالة ، ولكن يمكنها أيضًا إضافة علامة تجارية للشركة أو زخرفة. Microsoft يسمح Excel للمستخدمين بإضافة صور الخلفية يدويًا.

يمكن للمطورين أيضًا إضافة صور الخلفية من خلال تطبيقاتهم ، باستخدام إما Aspose.Cells for .NET أو VSTO. تقارن هذه المقالة بين الطريقتين.

{{% /alert %}}

## **تعيين صورة خلفية في ورقة عمل**

لتطبيق صورة خلفية على جدول بيانات:

1. قم بإنشاء مصنف والوصول إلى الورقة التي تريد تطبيق صورة خلفية عليها.
1. قم بتطبيق صورة الخلفية.
1. احفظ المصنف.

 توضح نماذج التعليمات البرمجية التالية كيفية القيام بذلك أولاً باستخدام[VSTO](/cells/ar/net/set-background-picture-of-a-worksheet/) ، باستخدام C# أو Visual Basic ، ثم مع[Aspose.Cells for .NET](/cells/ar/net/set-background-picture-of-a-worksheet/)، مرة أخرى باستخدام إما C# أو Visual Basic.

تُنشئ أمثلة الكود في هذه المقالة ورقة عمل بها صورة خلفية متكررة ، مثل تلك الموجودة في لقطة الشاشة أدناه.

**تم تعيين خلفية لورقة العمل.**

![ما يجب القيام به: image_بديل_نص](set-background-picture-of-a-worksheet_1.png)

### **ضبط صور الخلفية باستخدام VSTO**

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

//Set a background picture for the sheet.

objSheet.SetBackgroundPicture("e:\\test\\school.jpg");

//Save the excel file.

objBook.SaveCopyAs("c:\\BackgroundPicBook.xls");

//Quit the Application.

ExcelApp.Quit();



{{< /highlight >}}

### **ضبط صور الخلفية مع Aspose.Cells for .NET**

**C#**

{{< highlight "csharp" >}}

 .......

using Aspose.Cells;

.......

//Instantiate a new Workbook.

Workbook workbook = new Workbook();

//Get the first worksheet. 

Worksheet sheet = workbook.Worksheets[0];



//Define a string variable to store the image path.

string ImageUrl = @"e:\test\school.jpg";

//Get the picture into the streams.

FileStream fs = File.OpenRead(ImageUrl);

//Define a byte array.

byte[]imageData = new Byte[fs.Length];

//Obtain the picture into the array of bytes from streams.

fs.Read(imageData, 0, imageData.Length);

//Close the stream.

fs.Close();



//Set the background image for the sheet.

sheet.SetBackground(imageData);



//Save the excel file.

workbook.Save(@"c:\BackgroundPicBook.xls");     



{{< /highlight >}}
