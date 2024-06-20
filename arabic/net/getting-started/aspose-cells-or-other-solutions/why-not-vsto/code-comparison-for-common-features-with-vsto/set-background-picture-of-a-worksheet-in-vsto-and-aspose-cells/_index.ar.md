---
title: تعيين صورة الخلفية لورقة عمل في VSTO و Aspose.Cells
type: docs
weight: 220
url: /ar/net/set-background-picture-of-a-worksheet-in-vsto-and-aspose-cells/
---

لتطبيق صورة الخلفية على جدول بيانات:

1. إنشاء دفتر عمل والوصول إلى الورقة التي ترغب في تطبيق صورة خلفية عليها.
1. تطبيق صورة الخلفية.
1. حفظ الدفتر.

تظهر الأمثلة البرمجية التي تلي كيفية القيام بذلك أولاً مع VSTO، باستخدام إما C# أو Visual Basic، ثم مع Aspose.Cells for .NET مرة أخرى باستخدام إما C# أو Visual Basic.

تقوم أمثلة الرمز في هذه المقالة بإنشاء ورقة عمل بها صورة خلفية متكررة ، مثل تلك في الصورة أدناه.

![todo:image_alt_text](picture1.png)

تم تعيين خلفية لورقة العمل.

## **VSTO**

{{< highlight csharp >}}

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

{{< highlight csharp >}}

 //Instantiate a new Workbook.

Workbook workbook = new Workbook();

//Get the first worksheet.

Worksheet sheet = workbook.Worksheets[0];

//Define a string variable to store the image path.

string ImageUrl = "pic.jpeg";

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

workbook.Save("BackgroundPicBook.xls");

{{< /highlight >}}

## **تحميل رمز عينة**

- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Set.Background.Picture.of.a.Worksheet.Aspose.Cells.zip)
- [Sourceforge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Set%20Background%20Picture%20of%20a%20Worksheet%20\(Aspose.Cells\).zip/download)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Set%20Background%20Picture%20of%20a%20Worksheet%20\(Aspose.Cells\).zip)
