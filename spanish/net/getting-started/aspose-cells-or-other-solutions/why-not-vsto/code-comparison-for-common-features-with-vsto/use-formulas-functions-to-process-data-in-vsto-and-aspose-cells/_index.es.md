---
title: Usar funciones de fórmulas para procesar datos en VSTO y Aspose.Cells
type: docs
weight: 240
url: /es/net/use-formulas-functions-to-process-data-in-vsto-and-aspose-cells/
---
## **Adición de fórmula Cell**
### **VSTO**
{{< highlight "csharp" >}}

 //Note: To help you better, the code uses full namespacing

private void AddingCellFormula()

{

	//Access vsto application

	Microsoft.Office.Interop.Excel.Application app = Globals.ThisAddIn.Application;

	//Access workbook

	Microsoft.Office.Interop.Excel.Workbook workbook = app.ActiveWorkbook;

	//Access worksheet

	Microsoft.Office.Interop.Excel.Worksheet m_sheet = workbook.Worksheets[1];

	//Access vsto worksheet

	Microsoft.Office.Tools.Excel.Worksheet worksheet = Globals.Factory.GetVstoObject(m_sheet);

	//Access cells A1, A2, A3 , A4

	Microsoft.Office.Interop.Excel.Range cellA1 = worksheet.Range["A1"];

	Microsoft.Office.Interop.Excel.Range cellA2 = worksheet.Range["A2"];

	Microsoft.Office.Interop.Excel.Range cellA3 = worksheet.Range["A3"];

	Microsoft.Office.Interop.Excel.Range cellA4 = worksheet.Range["A4"];

	//Set integer values in cells A1, A2 and A3

	cellA1.Value = 10;

	cellA2.Value = 20;

	cellA3.Value = 30;

	//Add formula in cell A4

	cellA4.Formula = "=Sum(A1:A3)";

	//Set the font bold in cell A4

	cellA4.Font.Bold = true;

	//Set the background color to Yellow in cell A4

	cellA4.Interior.Color = Excel.XlRgbColor.rgbYellow;

	//Save the workbook

	workbook.SaveAs("OutputVsto.xlsx");

	//Quit the application

	app.Quit();

}

{{< /highlight >}}
### **Aspose.Cells**
{{< highlight "csharp" >}}

 private static void AddingCellFormula()

{

	//Create workbook

	Workbook workbook = new Workbook();

	//Access worksheet

	Worksheet worksheet = workbook.Worksheets[0];

	//Access cells A1, A2, A3 , A4

	Cell cellA1 = worksheet.Cells["A1"];

	Cell cellA2 = worksheet.Cells["A2"];

	Cell cellA3 = worksheet.Cells["A3"];

	Cell cellA4 = worksheet.Cells["A4"];

	//Set integer values in cells A1, A2 and A3

	cellA1.Value = 10;

	cellA2.Value = 20;

	cellA3.Value = 30;

	//Add formula in cell A4

	cellA4.Formula = "=Sum(A1:A3)";

	//Set the font bold in cell A4

	//and set the background color to Yellow in cell A4

	Style style = cellA4.GetStyle();

	style.Font.IsBold = true;

	style.Pattern = BackgroundType.Solid;

	style.ForegroundColor = Color.Yellow;

	cellA4.SetStyle(style);

	//Save the workbook

	workbook.Save("OutputAspose.xlsx", SaveFormat.Xlsx);

}

{{< /highlight >}}
## **Descargar código de muestra**
- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Use.Formulas.Functions.to.Process.Data.Aspose.Cells.zip)
- [forjafuente](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Use%20Formulas%20Functions%20to%20Process%20Data%20\(Aspose.Cells\).zip/descargar)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Use%20Formulas%20Functions%20to%20Process%20Data%20\(Aspose.Cells\).Código Postal)
