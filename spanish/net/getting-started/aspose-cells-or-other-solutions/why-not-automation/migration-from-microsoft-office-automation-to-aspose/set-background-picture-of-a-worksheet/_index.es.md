---
title: Establecer imagen de fondo de una hoja de cálculo
type: docs
weight: 90
url: /es/net/set-background-picture-of-a-worksheet/
---
{{% alert color="primary" %}}

Las imágenes de fondo se ubican detrás del texto y las líneas en una hoja de cálculo. Se utilizan para proporcionar información sobre un libro de trabajo, por ejemplo, cuando se utilizan como marcas de agua de estado, pero también pueden agregar la marca de la empresa o la decoración. Microsoft Excel permite a los usuarios agregar imágenes de fondo manualmente.

Los desarrolladores también pueden agregar imágenes de fondo a través de sus aplicaciones, usando Aspose.Cells for .NET o VSTO. Este artículo compara los dos enfoques.

{{% /alert %}}

## **Establecer una imagen de fondo en una hoja de cálculo**

Para aplicar una imagen de fondo a una hoja de cálculo:

1. Cree un libro de trabajo y acceda a la hoja a la que desea aplicar una imagen de fondo.
1. Aplicar la imagen de fondo.
1. Guarde el libro de trabajo.

 Los ejemplos de código que siguen muestran cómo hacer esto primero con[VSTO](/cells/es/net/set-background-picture-of-a-worksheet/) , usando C# o Visual Basic, y luego con[Aspose.Cells for .NET](/cells/es/net/set-background-picture-of-a-worksheet/), nuevamente usando C# o Visual Basic.

Los ejemplos de código de este artículo crean una hoja de trabajo con una imagen de fondo repetida, como la de la captura de pantalla a continuación.

**Se ha establecido un fondo para la hoja de trabajo.**

![todo:imagen_alternativa_texto](set-background-picture-of-a-worksheet_1.png)

### **Configuración de imágenes de fondo con VSTO**

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

### **Configuración de imágenes de fondo con Aspose.Cells for .NET**

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
