---
title: Установить фоновое изображение рабочего листа
type: docs
weight: 90
url: /ru/net/set-background-picture-of-a-worksheet/
---
{{% alert color="primary" %}}

Фоновые изображения размещаются за текстом и строками в электронной таблице. Они используются для предоставления информации о рабочей книге, например, при использовании в качестве водяных знаков статуса, но также могут добавлять фирменный знак или украшение компании. Microsoft Excel позволяет пользователям добавлять фоновые изображения вручную.

Разработчики также могут добавлять фоновые изображения через свои приложения, используя Aspose.Cells for .NET или VSTO. В этой статье сравниваются два подхода.

{{% /alert %}}

## **Установка фонового изображения на рабочем листе**

Чтобы применить фоновое изображение к электронной таблице:

1. Создайте рабочую книгу и откройте лист, к которому вы хотите применить фоновое изображение.
1. Примените фоновое изображение.
1. Сохраните книгу.

 В приведенных ниже примерах кода показано, как это сделать сначала с помощью[ВСТО](/cells/ru/net/set-background-picture-of-a-worksheet/) , используя C# или Visual Basic, а затем с помощью[Aspose.Cells for .NET](/cells/ru/net/set-background-picture-of-a-worksheet/), снова используя либо C#, либо Visual Basic.

Примеры кода в этой статье создают рабочий лист с повторяющимся фоновым изображением, как показано на снимке экрана ниже.

**Для рабочего листа установлен фон.**

![дело:изображение_альтернативный_текст](set-background-picture-of-a-worksheet_1.png)

### **Установка фоновых изображений с помощью VSTO**

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

### **Установка фоновых изображений с помощью Aspose.Cells for .NET**

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
