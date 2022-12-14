---
title: Envolviendo Cell Texto en VSTO y Aspose.Cells
type: docs
weight: 250
url: /es/net/wrapping-cell-text-in-vsto-and-aspose-cells/
---
Para crear una hoja de cálculo con dos celdas, una con texto ajustado y otra sin:

1.  Configure la hoja de trabajo:
 1. Cree un libro de trabajo.
 1. Acceda a la primera hoja de trabajo.
1.  Añadir texto:
 1. Agregue texto a la celda A1.
 1. Agregue texto ajustado a la celda A5.
1. Guarde la hoja de cálculo.
 Los ejemplos de código a continuación muestran cómo realizar estos pasos usando VSTO con C#. Los ejemplos de código que muestran cómo hacer lo mismo usando Aspose.Cells for .NET, nuevamente usando C# siguen inmediatamente después.

Ejecutar el código da como resultado una hoja de cálculo con dos celdas, una que tiene texto que no se ha ajustado y otra que tiene:

## **Salida usando VSTO Excel**

![todo:imagen_alternativa_texto](picture1.png)

## **Salida usando Aspose.Cells for .NET**

![todo:imagen_alternativa_texto](picture2.png)

## **VSTO**

{{< highlight "csharp" >}}

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

workbook.SaveAs("OutputVsto.xlsx");

//Quit the application

app.Quit();

{{< /highlight >}}

## **Aspose.Cells**

{{< highlight "csharp" >}}

 private static void WrappingCellText()

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

	workbook.Save("OutputAspose.xlsx", SaveFormat.Xlsx);

}

{{< /highlight >}}

## **Descargar código de muestra**

- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Wrapping.Cell.Text.Aspose.Cells.zip)
- [forjafuente](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Wrapping%20Cell%20Text%20\(Aspose.Cells\).zip/descargar)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Wrapping%20Cell%20Text%20\(Aspose.Cells\).Código Postal)
