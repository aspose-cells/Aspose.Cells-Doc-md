---
title: Rotación del Texto de la Celda
type: docs
weight: 100
url: /es/net/rotating-cell-text/
---

{{% alert color="primary" %}}

A veces, un encabezado de columna es mucho más ancho que los datos en las celdas below. Esto puede causar espacios en blanco innecesarios en la página. Una solución es rotar el texto verticalmente para que ocupe menos espacio horizontal. En Microsoft Excel, rotar texto es fácil. Por suerte, también es posible rotar el texto programáticamente, de modo que los desarrolladores puedan rotar etiquetas en las hojas de cálculo que crean en sus aplicaciones.

Este artículo analiza cómo rotar texto en celdas usando [Aspose.Cells for .NET](/cells/es/net/rotating-cell-text/) en comparación con hacer lo mismo con [VSTO](/cells/es/net/rotating-cell-text/).

{{% /alert %}}

## **Rotación de Texto en Celdas**

Para rotar el texto en una celda de una hoja de cálculo, siga los siguientes pasos:

1. Cree un libro y obtenga una hoja de cálculo.
1. Agregue texto de muestra.
1. Formatee el texto: rote, agregue color de fondo.
1. Guarde el archivo.

Los ejemplos de código que se muestran a continuación muestran cómo realizar estos pasos primero en [VSTO](/cells/es/net/rotating-cell-text/), utilizando tanto C# como Visual Basic, y luego en [Aspose.Cells](/cells/es/net/rotating-cell-text/), nuevamente utilizando tanto C# como Visual Basic.

Los ejemplos de código en este artículo muestran el siguiente resultado.
**Una celda con texto girado.**

![todo:image_alt_text](rotating-cell-text_1.png)

### **Rotación de texto con VSTO**

**C#**

{{< highlight csharp >}}

 using Microsoft.VisualStudio.Tools.Applications.Runtime;

using Excel = Microsoft.Office.Interop.Excel;

using Office = Microsoft.Office.Core;

using System.Reflection;

//Instantiate the Application object.

Excel.ApplicationClass ExcelApp = new Excel.ApplicationClass();

//Add a Workbook.

Excel.Workbook objBook = ExcelApp.Workbooks.Add(System.Reflection.Missing.Value);

//Get the First sheet.

Excel.Worksheet objSheet = (Excel.Worksheet)objBook.Sheets["Sheet1"];

//Put some text into cell B2.

objSheet.Cells[2, 2] = "Aspose Heading";

//Define a range object(B2).

Excel.Range _range;

_range = objSheet.get_Range("B2", "B2");

//Specify the angle of rotation of the text.

_range.Orientation = 45;

//Set the background color.

_range.Interior.Color = System.Drawing.ColorTranslator.ToWin32(Color.FromArgb(0, 51, 105));

//Set the font color of cell text

_range.Font.Color = System.Drawing.ColorTranslator.ToOle(System.Drawing.Color.White);



//Save the excel file.

objBook.SaveCopyAs("c:\\VSTO_RotateText_test.xlsx");

//Quit the Application.

ExcelApp.Quit();



{{< /highlight >}}

#### **Rotación de texto con Aspose.Cells for .NET**

**C#**

{{< highlight csharp >}}

 // Instantiate a new Workbook.

 Workbook objworkbook = new Workbook();

// Get the First sheet.

Worksheet objworksheet = objworkbook.Worksheets[0];

// Get Cells.

Cells objcells = objworksheet.Cells;// Get a particular Cell.

Cell objcell = objcells["B2"];// Put some text value.

objcell.PutValue("Aspose Heading");



// Get associated style object of the cell.

Style objstyle = objcell.GetStyle();

// Specify the angle of rotation of the text.

objstyle.RotationAngle = 45;



// Set the custom fill color of the cells.

objstyle.ForegroundColor = Color.FromArgb(0, 51, 105);



// Set the background pattern for fill color.

objstyle.Pattern = BackgroundType.Solid;

// Set the font color of cell text

objstyle.Font.Color = Color.White;



// Assign the updated style object back to the cell

objcell.SetStyle(objstyle);



// Save the work book

objworkbook.Save("c:\\RotateText_test.xlsx");



{{< /highlight >}}
