---
title: Envolver texto de celda
type: docs
weight: 130
url: /es/net/wrapping-cell-text/
---

{{% alert color="primary" %}}

Envolver texto hace que sea más fácil de leer: una celda con texto envuelto se expande para ajustarse al texto, de manera que el texto no se muestra sobre otras celdas.

Con Aspose.Cells for .NET, los desarrolladores pueden realizar la mayoría de las tareas en sus aplicaciones que los usuarios pueden realizar con Microsoft Excel, incluyendo envolver texto en celdas. Este artículo explica cómo, y compara la tarea usando VSTO y Aspose.Cells. Aspose.Cells está optimizado para una codificación eficiente y funciona sin Automatización de Microsoft.

{{% /alert %}}

## **Envolver texto de celda**

Para crear una hoja de cálculo con dos celdas, una con texto envuelto y otra sin:

1. Configurar la hoja de cálculo:
   1. Crear un libro de trabajo.
   1. Acceder a la primera hoja de cálculo.
1. Agregar texto:
   1. Agregar texto a la celda A1.
   1. Agregar texto envuelto a la celda A5.
1. Guardar la hoja de cálculo.

Los ejemplos de código a continuación muestran cómo realizar estos pasos usando [VSTO](/cells/es/net/wrapping-cell-text/) con C# o Visual Basic. Los ejemplos de código que muestran cómo hacer lo mismo usando [Aspose.Cells for .NET](/cells/es/net/wrapping-cell-text/), nuevamente usando C# o Visual Basic, siguen inmediatamente después.

Al ejecutar el código se obtiene una hoja de cálculo con dos celdas, una con texto que no ha sido envuelto y otra con:

|<p>**Output wrapping cell text with VSTO** </p><p>![todo:image_alt_text](wrapping-cell-text_1.png)</p>|<p>**Output wrapping cell text with Aspose.Cells for .NET** </p><p>![todo:image_alt_text](wrapping-cell-text_2.png)</p>|
| :- | :- |

### **Envolver texto de celda usando VSTO**

**C#**

{{< highlight csharp >}}

 //Note: To help you better, the code uses full namespacing

void WrappingCellText()

{

    //Access vsto application

    Microsoft.Office.Interop.Excel.Application app = Globals.ThisAddIn.Application;

    //Access workbook 

    Microsoft.Office.Interop.Excel.Workbook workbook = app.ActiveWorkbook;

    //Access worksheet 

    Microsoft.Office.Interop.Excel.Worksheet m_sheet = workbook.Worksheets[1];

    //Access vsto worksheet

    Microsoft.Office.Tools.Excel.Worksheet sheet = Globals.Factory.GetVstoObject(m_sheet);

    //Place some text in cell A1 without wrapping

    Microsoft.Office.Interop.Excel.Range cellA1 = sheet.Cells.get_Range("A1");

    cellA1.Value = "Sample Text Unwrapped";

    //Place some text in cell A5 with wrapping

    Microsoft.Office.Interop.Excel.Range cellA5 = sheet.Cells.get_Range("A5");

    cellA5.Value = "Sample Text Wrapped";

    cellA5.WrapText = true;

    //Save the workbook

    workbook.SaveAs("f:\\downloads\\OutputVsto.xlsx");

    //Quit the application

    app.Quit();

}

{{< /highlight >}}

### **Envolver texto de celda usando Aspose.Cells for .NET**

**C#**

{{< highlight csharp >}}

 void WrappingCellText()

{

    //Create workbook

    Workbook workbook = new Workbook();

    //Access worksheet

    Worksheet worksheet = workbook.Worksheets[0];

    //Place some text in cell A1 without wrapping

    Cell cellA1 = worksheet.Cells["A1"];

    cellA1.PutValue("Some Text Unwrapped");

    //Place some text in cell A5 wrapping

    Cell cellA5 = worksheet.Cells["A5"];

    cellA5.PutValue("Some Text Wrapped");

    Style style = cellA5.GetStyle();

    style.IsTextWrapped = true;

    cellA5.SetStyle(style);

    //Autofit rows

    worksheet.AutoFitRows();

    //Save the workbook

    workbook.Save("f:\\downloads\\OutputAspose.xlsx", SaveFormat.Xlsx);

}

{{< /highlight >}}
