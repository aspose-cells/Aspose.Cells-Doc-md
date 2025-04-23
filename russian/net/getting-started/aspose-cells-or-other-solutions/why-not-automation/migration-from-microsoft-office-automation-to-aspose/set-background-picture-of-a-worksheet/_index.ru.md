---
title: Установка фонового изображения на листе
type: docs
weight: 90
url: /ru/net/set-background-picture-of-a-worksheet/
---

{{% alert color="primary" %}}

Фоновые изображения находятся за текстом и линиями в электронной таблице. Они используются для отображения информации о книге, например, когда они используются в качестве заставок статуса, но также могут добавлять фирменный стиль компании или украшение. В Microsoft Excel пользователи могут добавлять фоновые изображения вручную.

Разработчики также могут добавлять фоновые изображения через свои приложения, используя Aspose.Cells for .NET или VSTO. В данной статье сравниваются два подхода.

{{% /alert %}}

## **Установка фонового изображения на листе**

Чтобы применить фоновое изображение к электронной таблице:

1. Создайте книгу и получите доступ к листу, на который вы хотите применить фоновое изображение.
1. Примените фоновое изображение.
1. Сохраните книгу.

Приведенные ниже примеры кода показывают, как сделать это сначала с [VSTO](/cells/ru/net/set-background-picture-of-a-worksheet/), используя C# или Visual Basic, а затем с [Aspose.Cells for .NET](/cells/ru/net/set-background-picture-of-a-worksheet/), также используя C# или Visual Basic.

Примеры кода в этой статье создают лист с повторяющимся фоновым изображением, как на скриншоте ниже.

**Фон был установлен для листа.**

![todo:image_alt_text](set-background-picture-of-a-worksheet_1.png)

### **Установка фоновых изображений с помощью VSTO**

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

### **Установка фоновых изображений с Aspose.Cells for .NET**

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
{{< app/cells/assistant language="csharp" >}}
