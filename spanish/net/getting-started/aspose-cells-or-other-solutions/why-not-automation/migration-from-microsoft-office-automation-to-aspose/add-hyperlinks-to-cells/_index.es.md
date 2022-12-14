---
title: Agregar hipervínculos a Cells
type: docs
weight: 60
url: /es/net/add-hyperlinks-to-cells/
---
{{% alert color="primary" %}}

Aspose.Cells for .NET le permite realizar casi cualquier tarea a través de su aplicación que un usuario puede realizar en Microsoft Excel. Este artículo compara cómo agregar un hipervínculo a una celda en una hoja de trabajo usando VSTO y Aspose.Cells for .NET.

{{% /alert %}}

## **Adición de hipervínculos a Cells**

Para agregar hipervínculos a las celdas de una hoja de cálculo, siga los siguientes pasos:

1. Configure la hoja de trabajo:
 1. Cree una instancia de un objeto de aplicación.
 (Solo VSTO).
 1. Agregue un libro de trabajo.
 1. Obtenga la primera hoja.
 1. Agregue texto a las celdas a las que agregará un hipervínculo.
1. Añadir hipervínculo.
1. Guarde el documento.

 Estos pasos se muestran en los ejemplos de código a continuación. Los primeros ejemplos muestran cómo usar[VSTO](/cells/es/net/add-hyperlinks-to-cells/) con C# o Visual Basic para agregar un hipervínculo a una celda. Los ejemplos que siguen muestran cómo hacer lo mismo usando[Aspose.Cells for .NET](/cells/es/net/add-hyperlinks-to-cells/), nuevamente usando C# o Visual Basic.

Los ejemplos de código generan un archivo de Excel que tiene un hipervínculo en la celda A1 de la primera hoja de trabajo.

![todo:imagen_alternativa_texto](add-hyperlinks-to-cells_1.png)

**Se agrega un hipervínculo a la celda A1.**

### **Adición de hipervínculos a Cells con VSTO**

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



//Define a range object(A1).

Excel.Range _range;

_range = objSheet.get_Range("A1", "A1");

//Add a hyperlink to it.

objSheet.Hyperlinks.Add(_range, "http://www.aspose.com/", Type.Missing, "Click to go to Aspose site", "Aspose Site!");

//Save the excel file.

objBook.SaveCopyAs("c:\\Hyperlink_test.xls"); 

//Quit the Application.

ExcelApp.Quit();



{{< /highlight >}}

### **Agregar hipervínculos a Cells con Aspose.Cells for .NET**

**C#**

{{< highlight "csharp" >}}

 .......

using Aspose.Cells;

.......

//Instantiate a new Workbook object.

Workbook workbook = new Workbook();

//Get the First sheet.

Worksheet worksheet = workbook.Worksheets[0];

//Define A1 Cell.

Aspose.Cells.Cell cell = worksheet.Cells["A1"];

//Add a hyperlink to it.

int index = worksheet.Hyperlinks.Add("A1", 1, 1, "http://www.aspose.com/");

worksheet.Hyperlinks[index].TextToDisplay = "Aspose Site!";

worksheet.Hyperlinks[index].ScreenTip = "Click to go to Aspose site";

//Save the excel file.

workbook.Save("c:\\Hyperlink_test.xls");       



{{< /highlight >}}
