---
title: Agregar bordes a Cells en una hoja de trabajo
type: docs
weight: 50
url: /es/net/add-borders-to-cells-in-a-worksheet/
---
{{% alert color="primary" %}}

Aspose.Cells for .NET le permite realizar casi cualquier tarea a través de su aplicación que un usuario puede realizar en Microsoft Excel. Aspose.Cells es potente y robusto y tiene el beneficio adicional de trabajar independientemente de Microsoft Automatización. Este artículo muestra cómo agregar bordes a las celdas de una hoja de cálculo con Aspose.Cells for .NET en comparación con VSTO.

{{% /alert %}}

## **Adición de bordes a Cells**

Para agregar bordes a las celdas de una hoja de cálculo, siga los siguientes pasos:

1. Configure la hoja de trabajo:
 1. Cree una instancia de un objeto de aplicación.
 (Solo VSTO).
 1. Agregue un libro de trabajo.
 1. Obtenga la primera hoja.
 1. Agregue texto a las celdas a las que agregará bordes.
1. Añadir bordes:
 1. Defina un rango.
 1. Aplique un estilo de borde al rango.
Repita para cada rango y cada estilo de borde que desee establecer. Este ejemplo aplica líneas finas, finas, medianas y gruesas.
1. Finalizar:
 1. Ajuste automáticamente la columna en la que se encuentran las celdas para que el texto se ajuste perfectamente.
 1. Guarde el documento.

 Estos pasos se muestran en el código a continuación. Los primeros ejemplos de código muestran cómo implementarlos usando[VSTO](/cells/es/net/add-borders-to-cells-in-a-worksheet/) con C# o Visual Basic. Después de los ejemplos de VSTO, hay ejemplos que muestran cómo realizar los mismos pasos usando[Aspose.Cells for .NET](/cells/es/net/add-borders-to-cells-in-a-worksheet/), nuevamente usando C# o Visual Basic. Los ejemplos de código Aspose.Cells son mucho más cortos porque Aspose.Cells está optimizado para una codificación eficiente.

El código genera un archivo de Excel con un número de celdas en la primera hoja, cada una con un borde diferente:

![todo:imagen_alternativa_texto](add-borders-to-cells-in-a-worksheet_1.png)

**Cells con bordes aplicados.**

### **Agregar bordes usando VSTO**

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



//Put some text into different cells (A2, A4, A6, A8).

objSheet.Cells[2, 1]= "Hair Lines";

objSheet.Cells[4, 1]= "Thin Lines";

objSheet.Cells[6, 1]= "Medium Lines";

objSheet.Cells[8, 1]= "Thick Lines";

//Define a range object(A2).

Excel.Range _range;

_range = objSheet.get_Range("A2", "A2");

//Get the borders collection.

Excel.Borders borders = _range.Borders;

//Set the hair lines style.

borders.LineStyle = Excel.XlLineStyle.xlContinuous;

borders.Weight = 1d;



//Define a range object(A4).

_range = objSheet.get_Range("A4", "A4");

//Get the borders collection.

borders = _range.Borders;

//Set the thin lines style.

borders.LineStyle = Excel.XlLineStyle.xlContinuous;

borders.Weight = 2d;



//Define a range object(A6).

_range = objSheet.get_Range("A6", "A6");

//Get the borders collection.

borders = _range.Borders;

//Set the medium lines style.

borders.LineStyle = Excel.XlLineStyle.xlContinuous;

borders.Weight = 3d;



//Define a range object(A8).

_range = objSheet.get_Range("A8", "A8");

//Get the borders collection.

borders = _range.Borders;

//Set the thick lines style.

borders.LineStyle = Excel.XlLineStyle.xlContinuous;

borders.Weight = 4d;



//Auto-fit Column A.

objSheet.get_Range("A2", "A2").EntireColumn.AutoFit();



//Save the excel file.

objBook.SaveAs("f:\\test\\ApplyBorders.xls",

Microsoft.Office.Interop.Excel.XlFileFormat.xlExcel8,

Type.Missing,

Type.Missing,

Type.Missing,

Type.Missing,

Microsoft.Office.Interop.Excel.XlSaveAsAccessMode.xlNoChange,

Type.Missing,

Type.Missing,

Type.Missing,

Type.Missing,

Type.Missing);



//Quit the Application.

ExcelApp.Quit();



{{< /highlight >}}

### **Agregar bordes usando Aspose.Cells for .NET**

**C#**

{{< highlight "csharp" >}}

 .......

using Aspose.Cells;

.......

//Instantiate a new Workbook.

Workbook objBook = new Workbook();  

//Get the First sheet.

Worksheet objSheet = objBook.Worksheets["Sheet1"];



//Put some text into different cells (A2, A4, A6, A8).

objSheet.Cells[1, 0].PutValue("Hair Lines");

objSheet.Cells[3, 0].PutValue("Thin Lines");

objSheet.Cells[5, 0].PutValue("Medium Lines");

objSheet.Cells[7, 0].PutValue("Thick Lines");

//Define a range object(A2).

Aspose.Cells.Range _range;

_range = objSheet.Cells.CreateRange("A2", "A2");

//Set the borders with hair lines style.

_range.SetOutlineBorders( CellBorderType.Hair, Color.Black);

//Define a range object(A4).

_range = objSheet.Cells.CreateRange("A4", "A4");

//Set the borders with thin lines style.

_range.SetOutlineBorders(CellBorderType.Thin, Color.Black);

//Define a range object(A6).

_range = objSheet.Cells.CreateRange("A6", "A6");

//Set the borders with medium lines style.

_range.SetOutlineBorders(CellBorderType.Medium, Color.Black);

//Define a range object(A8).

_range = objSheet.Cells.CreateRange("A8", "A8");

//Set the borders with thick lines style.

_range.SetOutlineBorders(CellBorderType.Thick, Color.Black);

//Auto-fit Column A.

objSheet.AutoFitColumn(0);

//Save the excel file.

objBook.Save("f:\\test\\ApplyBorders.xls");        



{{< /highlight >}}
