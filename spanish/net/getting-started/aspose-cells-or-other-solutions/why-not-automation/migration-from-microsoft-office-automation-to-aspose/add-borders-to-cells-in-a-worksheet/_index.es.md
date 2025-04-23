---
title: Agregar bordes a celdas en una hoja de cálculo
type: docs
weight: 50
url: /es/net/add-borders-to-cells-in-a-worksheet/
---

{{% alert color="primary" %}}

Aspose.Cells for .NET te permite realizar casi todas las tareas a través de tu aplicación que un usuario puede realizar en Microsoft Excel. Aspose.Cells es eficiente y robusto y tiene el beneficio adicional de trabajar de forma independiente de la Automatización de Microsoft. Este artículo muestra cómo agregar bordes a las celdas en una hoja de cálculo usando Aspose.Cells for .NET en comparación con VSTO.

{{% /alert %}}

## **Añadiendo Bordes a las Celdas**

Para agregar bordes a las celdas en una hoja de cálculo, sigue los siguientes pasos:

1. Configurar la hoja de cálculo:
   1. Instancia un objeto de Aplicación.
      (Solo VSTO.)
   1. Agregar un libro.
   1. Obtener la primera hoja.
   1. Agregar texto a las celdas a las que les agregarás bordes.
1. Agregar bordes:
   1. Definir un rango.
   1. Aplicar un estilo de borde al rango.
      Repetir para cada rango y cada estilo de borde que desees establecer. Este ejemplo aplica líneas finas, medianas y gruesas.
1. Terminar:
   1. Ajustar automáticamente el ancho de la columna en la que están las celdas para que el texto encaje correctamente.
   1. Guardar el documento.

Estos pasos se muestran en el código siguiente. Los primeros ejemplos de código muestran cómo implementarlos usando [VSTO](/cells/es/net/add-borders-to-cells-in-a-worksheet/) con C# o Visual Basic. Después de los ejemplos de VSTO, hay ejemplos que muestran cómo realizar los mismos pasos usando [Aspose.Cells for .NET](/cells/es/net/add-borders-to-cells-in-a-worksheet/), nuevamente con C# o Visual Basic. Los ejemplos de código de Aspose.Cells son mucho más breves porque Aspose.Cells está optimizado para una codificación eficiente.

El código genera un archivo de Excel con varias celdas en la primera hoja, cada una con un borde diferente:

![todo:image_alt_text](add-borders-to-cells-in-a-worksheet_1.png)

**Celdas con bordes aplicados.**

### **Añadiendo Bordes usando VSTO**

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



//Put some text into different cells (A2, A4, A6, A8).

objSheet.Cells[2, 1] = "Hair Lines";

objSheet.Cells[4, 1] = "Thin Lines";

objSheet.Cells[6, 1] = "Medium Lines";

objSheet.Cells[8, 1] = "Thick Lines";

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

### **Agregando bordes usando Aspose.Cells for .NET**

**C#**

{{< highlight csharp >}}

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
{{< app/cells/assistant language="csharp" >}}
