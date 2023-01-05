---
title: Envoltura Cell Texto
type: docs
weight: 130
url: /es/net/wrapping-cell-text/
---
{{% alert color="primary" %}}

Ajustar el texto facilita la lectura: una celda con texto ajustado se expande para ajustarse al texto de modo que el texto no se muestre sobre otras celdas.

Con Aspose.Cells for .NET, los desarrolladores pueden realizar la mayoría de las tareas en sus aplicaciones que los usuarios pueden realizar con Microsoft Excel, incluido el ajuste de texto en celdas. Este artículo explica cómo y compara la tarea usando VSTO y Aspose.Cells. Aspose.Cells está optimizado para una codificación eficiente y funciona sin Microsoft Automatización.

{{% /alert %}}

## **Envoltura Cell Texto**

Para crear una hoja de cálculo con dos celdas, una con texto ajustado y otra sin:

1. Configure la hoja de trabajo:
 1. Cree un libro de trabajo.
 1. Acceda a la primera hoja de trabajo.
1. Añadir texto:
 1. Agregue texto a la celda A1.
 1. Agregue texto ajustado a la celda A5.
1. Guarde la hoja de cálculo.

 Los ejemplos de código a continuación muestran cómo realizar estos pasos usando[VSTO](/cells/es/net/wrapping-cell-text/) con C# o Visual Basic. Ejemplos de código que muestran cómo hacer lo mismo usando[Aspose.Cells for .NET](/cells/es/net/wrapping-cell-text/), nuevamente utilizando C# o Visual Basic, siga inmediatamente después.

Ejecutar el código da como resultado una hoja de cálculo con dos celdas, una que tiene texto que no se ha ajustado y otra que tiene:

|<p>**Texto de celda de ajuste de salida con VSTO** </p><p>![todo:imagen_alternativa_texto](wrapping-cell-text_1.png)</p>|<p>**Texto de celda de envoltura de salida con Aspose.Cells for .NET** </p><p>![todo:imagen_alternativa_texto](wrapping-cell-text_2.png)</p>|
|:- |:- |

### **Envolviendo Cell texto usando VSTO**

**C#**

{{< highlight "csharp" >}}

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

### **Envolviendo Cell Texto usando Aspose.Cells for .NET**

**C#**

{{< highlight "csharp" >}}

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
