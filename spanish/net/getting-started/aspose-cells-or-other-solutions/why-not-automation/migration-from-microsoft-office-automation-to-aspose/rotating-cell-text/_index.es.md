---
title: Texto giratorio Cell
type: docs
weight: 100
url: /es/net/rotating-cell-text/
---
{{% alert color="primary" %}}

A veces, el encabezado de una columna es mucho más ancho que los datos de las celdas siguientes. Esto puede generar espacios en blanco innecesarios en la página. Una solución es rotar el texto verticalmente para que ocupe menos espacio horizontal. En Microsoft Excel, rotar texto es fácil. Afortunadamente, también es posible rotar el texto mediante programación, para que los desarrolladores puedan rotar las etiquetas en las hojas de cálculo que crean dentro de sus aplicaciones.

 Este artículo analiza cómo rotar texto en celdas usando[Aspose.Cells for .NET](/cells/es/net/rotating-cell-text/) en comparación con hacer lo mismo con[VSTO](/cells/es/net/rotating-cell-text/).

{{% /alert %}}

## **Texto giratorio en Cells**

Para rotar el texto en una celda de una hoja de trabajo, siga los siguientes pasos:

1. Cree un libro de trabajo y obtenga una hoja de trabajo.
1. Agregue ejemplos de texto.
1. Dar formato al texto: rotar, añadir color de fondo.
1. Guarda el archivo.

 Los ejemplos de código que siguen muestran cómo realizar estos pasos primero en[VSTO](/cells/es/net/rotating-cell-text/) , usando C# o Visual Basic, y luego en[Aspose.Cells](/cells/es/net/rotating-cell-text/), nuevamente usando C# o Visual Basic.

Los ejemplos de código en este artículo dan el resultado que se muestra a continuación.
**Una celda con texto girado.**

![todo:imagen_alternativa_texto](rotating-cell-text_1.png)

### **Texto giratorio con VSTO**

**C#**

{{< highlight "csharp" >}}

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

objSheet.Cells[2, 2]= "Aspose Heading";

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

#### **Texto giratorio con Aspose.Cells for .NET**

**C#**

{{< highlight "csharp" >}}

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
