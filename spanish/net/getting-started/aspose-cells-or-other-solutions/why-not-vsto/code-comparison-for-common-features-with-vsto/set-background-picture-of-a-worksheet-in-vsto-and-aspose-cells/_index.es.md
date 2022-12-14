---
title: Establecer imagen de fondo de una hoja de trabajo en VSTO y Aspose.Cells
type: docs
weight: 220
url: /es/net/set-background-picture-of-a-worksheet-in-vsto-and-aspose-cells/
---
Para aplicar una imagen de fondo a una hoja de cálculo:

1. Cree un libro de trabajo y acceda a la hoja a la que desea aplicar una imagen de fondo.
1. Aplicar la imagen de fondo.
1. Guarde el libro de trabajo.

Los ejemplos de código que siguen muestran cómo hacer esto primero con VSTO, usando C# o Visual Basic, y luego con Aspose.Cells for .NET, nuevamente usando C# o Visual Basic.

Los ejemplos de código de este artículo crean una hoja de trabajo con una imagen de fondo repetida, como la que se muestra en la siguiente captura de pantalla.

![todo:imagen_alternativa_texto](picture1.png)

Se ha establecido un fondo para la hoja de trabajo.

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

## **Descargar código de muestra**

- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Set.Background.Picture.of.a.Worksheet.Aspose.Cells.zip)
- [forjafuente](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Set%20Background%20Picture%20of%20a%20Worksheet%20\(Aspose.Cells\).zip/descargar)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Set%20Background%20Picture%20of%20a%20Worksheet%20\(Aspose.Cells\).Código Postal)
