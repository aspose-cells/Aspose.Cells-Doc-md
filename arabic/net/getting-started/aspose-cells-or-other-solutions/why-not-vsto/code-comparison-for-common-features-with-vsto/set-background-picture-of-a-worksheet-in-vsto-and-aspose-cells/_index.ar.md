---
title: قم بتعيين صورة الخلفية لورقة العمل في VSTO و Aspose.Cells
type: docs
weight: 220
url: /ar/net/set-background-picture-of-a-worksheet-in-vsto-and-aspose-cells/
---
لتطبيق صورة خلفية على جدول بيانات:

1. قم بإنشاء مصنف والوصول إلى الورقة التي تريد تطبيق صورة خلفية عليها.
1. قم بتطبيق صورة الخلفية.
1. احفظ المصنف.

توضح نماذج التعليمات البرمجية التالية كيفية القيام بذلك أولاً باستخدام VSTO ، باستخدام إما C# أو Visual Basic ، ثم باستخدام Aspose.Cells for .NET ، مرة أخرى باستخدام إما C# أو Visual Basic.

تُنشئ أمثلة التعليمات البرمجية في هذه المقالة ورقة عمل تحتوي على صورة خلفية متكررة ، مثل تلك الموجودة في لقطة الشاشة أدناه.

![ما يجب القيام به: image_بديل_نص](picture1.png)

تم تعيين خلفية لورقة العمل.

## **VSTO**

{{< highlight "csharp" >}}

 //Instantiate the Application object.

Excel.Application ExcelApp = Application;

//Add a Workbook.

Excel.Workbook objBook = ExcelApp.Workbooks.Add(System.Reflection.Missing.Value);

//Get the First sheet.

Excel.Worksheet objSheet = (Excel.Worksheet)objBook.Sheets["Sheet1"];

//Set a background picture for the sheet.

objSheet.SetBackgroundPicture("pic.jpeg");

//Save the excel file.

objBook.SaveCopyAs("BackgroundPicBook.xls");

//Quit the Application.

ExcelApp.Quit();

{{< /highlight >}}

## **Aspose.Cells**

{{< highlight "csharp" >}}

 //Instantiate a new Workbook.

Workbook workbook = new Workbook();

//Get the first worksheet.

Worksheet sheet = workbook.Worksheets[0];

//Define a string variable to store the image path.

string ImageUrl = "pic.jpeg";

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

workbook.Save("BackgroundPicBook.xls");

{{< /highlight >}}

## **تنزيل نموذج التعليمات البرمجية**

- [جيثب](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Set.Background.Picture.of.a.Worksheet.Aspose.Cells.zip)
- [سورس فورج](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Set%20Background%20Picture%20of%20a%20Worksheet%20\(Aspose.Cells\).zip / تنزيل)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Set%20Background%20Picture%20of%20a%20Worksheet%20\(Aspose.Cells\).أَزِيز)
