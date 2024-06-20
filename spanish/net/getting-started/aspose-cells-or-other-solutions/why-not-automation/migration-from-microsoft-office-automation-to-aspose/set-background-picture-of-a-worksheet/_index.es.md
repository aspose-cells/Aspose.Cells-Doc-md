---
title: Establecer imagen de fondo de una hoja de cálculo
type: docs
weight: 90
url: /es/net/set-background-picture-of-a-worksheet/
---

{{% alert color="primary" %}}

Las imágenes de fondo se colocan detrás del texto y las líneas en una hoja de cálculo. Se utilizan para proporcionar información sobre un libro de trabajo, por ejemplo, cuando se utilizan como marcas de agua de estado, pero también pueden agregar marca corporativa o decoración. Microsoft Excel permite a los usuarios agregar imágenes de fondo manualmente.

Los desarrolladores también pueden agregar imágenes de fondo a través de sus aplicaciones, utilizando ya sea Aspose.Cells for .NET o VSTO. Este artículo compara los dos enfoques.

{{% /alert %}}

## **Establecer una imagen de fondo en una hoja de cálculo**

Para aplicar una imagen de fondo a una hoja de cálculo:

1. Crear un libro y acceder a la hoja a la que quiere aplicar una imagen de fondo.
1. Aplicar la imagen de fondo.
1. Guardar el libro.

Los ejemplos de código que siguen muestran cómo hacer esto primero con [VSTO](/cells/es/net/set-background-picture-of-a-worksheet/), utilizando ya sea C# o Visual Basic, y luego con [Aspose.Cells for .NET](/cells/es/net/set-background-picture-of-a-worksheet/), nuevamente utilizando ya sea C# o Visual Basic.

Los ejemplos de código en este artículo crean una hoja de cálculo con una imagen de fondo repetida, como la que se muestra a continuación.

**Se ha establecido un fondo para la hoja de cálculo.**

![todo:image_alt_text](set-background-picture-of-a-worksheet_1.png)

### **Configuración de imágenes de fondo con VSTO**

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

### **Configuración de imágenes de fondo con Aspose.Cells for .NET**

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
