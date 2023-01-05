---
title: Установить фоновое изображение рабочего листа в VSTO и Aspose.Cells
type: docs
weight: 220
url: /ru/net/set-background-picture-of-a-worksheet-in-vsto-and-aspose-cells/
---
Чтобы применить фоновое изображение к электронной таблице:

1. Создайте рабочую книгу и откройте лист, к которому вы хотите применить фоновое изображение.
1. Примените фоновое изображение.
1. Сохраните книгу.

В приведенных ниже примерах кода показано, как это сделать сначала с помощью VSTO, используя либо C#, либо Visual Basic, а затем Aspose.Cells for .NET, снова используя либо C#, либо Visual Basic.

Примеры кода в этой статье создают рабочий лист с повторяющимся фоновым изображением, как показано на снимке экрана ниже.

![дело:изображение_альтернативный_текст](picture1.png)

Для рабочего листа установлен фон.

## **ВСТО**

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

## **Скачать пример кода**

- [Гитхаб](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Set.Background.Picture.of.a.Worksheet.Aspose.Cells.zip)
- [Источникфорж](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Set%20Background%20Picture%20of%20a%20Worksheet%20\(Aspose.Cells\).zip/скачать)
- [Битбакет](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Set%20Background%20Picture%20of%20a%20Worksheet%20\(Aspose.Cells\).zip)
