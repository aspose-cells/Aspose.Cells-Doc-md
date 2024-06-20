---
title: تعيين صورة خلفية لورقة عمل
type: docs
weight: 90
url: /ar/net/set-background-picture-of-a-worksheet/
---

{{% alert color="primary" %}}

تقع صور الخلفية خلف النص والخطوط في جدول بيانات. يتم استخدامها لتقديم معلومات حول دفتر العمل، على سبيل المثال عند استخدام علامات المرجعية للحالة، ولكن يمكنها أيضًا إضافة العلامة التجارية للشركة أو الزخرفة. يسمح Microsoft Excel للمستخدمين بإضافة صور الخلفية يدويًا.

يمكن للمطورين أيضًا إضافة صور خلفية من خلال تطبيقاتهم، باستخدام إما Aspose.Cells for .NET أو VSTO. يقارن هذا المقال بين النهجين.

{{% /alert %}}

## **تعيين صورة خلفية على ورقة العمل**

لتطبيق صورة الخلفية على جدول بيانات:

1. إنشاء دفتر عمل والوصول إلى الورقة التي ترغب في تطبيق صورة خلفية عليها.
1. تطبيق صورة الخلفية.
1. حفظ الدفتر.

توضح عينات الشفرات التي تتبع كيفية القيام بذلك أولاً مع [VSTO](/cells/ar/net/set-background-picture-of-a-worksheet/)، باستخدام إما C# أو Visual Basic، وبعد ذلك مع [Aspose.Cells for .NET](/cells/ar/net/set-background-picture-of-a-worksheet/)، مرة أخرى باستخدام إما C# أو Visual Basic.

تقوم أمثلة الشفرات في هذا المقال بإنشاء ورقة عمل بخلفية صورة متكررة، مثل ما هو موضح في لقطة الشاشة أدناه.

**تم تعيين خلفية لورقة العمل.**

![todo:image_alt_text](set-background-picture-of-a-worksheet_1.png)

### **تعيين صور خلفية باستخدام VSTO**

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

//Set a background picture for the sheet.

objSheet.SetBackgroundPicture("e:\\test\\school.jpg");

//Save the excel file.

objBook.SaveCopyAs("c:\\BackgroundPicBook.xls");

//Quit the Application.

ExcelApp.Quit();



{{< /highlight >}}

### **تعيين صور خلفية باستخدام Aspose.Cells for .NET**

**C#**

{{< highlight csharp >}}

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

byte[] imageData = new Byte[fs.Length];

//Obtain the picture into the array of bytes from streams.

fs.Read(imageData, 0, imageData.Length);

//Close the stream.

fs.Close();



//Set the background image for the sheet.

sheet.SetBackground(imageData);



//Save the excel file.

workbook.Save(@"c:\BackgroundPicBook.xls");     



{{< /highlight >}}
