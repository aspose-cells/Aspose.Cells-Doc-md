---
title: Créer un graphique circulaire dans VSTO et Aspose.Cells
type: docs
weight: 80
url: /fr/net/create-a-pie-chart-in-vsto-and-aspose-cells/
---

Cet article compare comment créer un graphique circulaire à l'aide de l'automatisation Office et de VSTO à l'aide de Aspose.Cells for .NET. Les étapes pour créer un graphique circulaire sont :

1. Créer un classeur et une feuille de calcul.
1. Ajouter des données d'exemple.
1. Référencer productsChart.
1. Ajouter un graphique circulaire, définir la plage de données et le titre du graphique.
1. Enregistrer la feuille de calcul.
   Les exemples de code dans cet article montrent comment ajouter un graphique circulaire avec VSTO, en utilisant soit C#, comparé à la création avec Aspose.Cells, encore une fois en utilisant soit C#.
## **VSTO**
{{< highlight csharp >}}

 private void PieChart()

{

//Instantiate the Application object.

Excel.Application ExcelApp = Application;

//Add a Workbook.

Excel.Workbook objBook = ExcelApp.Workbooks.Add(System.Reflection.Missing.Value);

// Access a Vsto Worksheet

Microsoft.Office.Interop.Excel.Worksheet nativeWorksheet = Globals.ThisAddIn.Application.ActiveWorkbook.ActiveSheet;

Microsoft.Office.Tools.Excel.Worksheet sheet = Globals.Factory.GetVstoObject(nativeWorksheet);

//Add sample data for pie chart

//Add headings in A1 and B1

sheet.Cells[1, 1] = "Products";

sheet.Cells[1, 2] = "Users";

//Add data from A2 till B4

sheet.Cells[2, 1] = "Aspose.Cells";

sheet.Cells[2, 2] = 10000;

sheet.Cells[3, 1] = "Aspose.Slides";

sheet.Cells[3, 2] = 8000;

sheet.Cells[4, 1] = "Aspose.Words";

sheet.Cells[4, 2] = 12000;

//Chart reference

Microsoft.Office.Tools.Excel.Chart productsChart;

//Add a Pie Chart

productsChart = sheet.Controls.AddChart(0, 105, 330, 200, "ProductUsers");

productsChart.ChartType = Microsoft.Office.Interop.Excel.XlChartType.xlPie;

//Set chart title

productsChart.HasTitle = true;

productsChart.ChartTitle.Text = "Users";

//Gets the cells that define the data to be charted.

Microsoft.Office.Interop.Excel.Range chartRange = sheet.get_Range("A2", "B4");

productsChart.SetSourceData(chartRange, missing);

//Access the Active workbook from Vsto sheet

Microsoft.Office.Interop.Excel.Workbook workbook = sheet.Application.ActiveWorkbook;

//Save the copy of workbook as OutputVsto.xlsx

workbook.SaveCopyAs("OutputVsto.xlsx");

}

{{< /highlight >}}
## **Aspose.Cells**
{{< highlight csharp >}}

 private static void PieChart()

{

	//Create Aspose.Cells Workbook

	Workbook workbook = new Workbook();

	//Access Aspose.Cells Worksheet

	Worksheet sheet = workbook.Worksheets[0];

	//Add sample data for pie chart

	//Add headings in A1 and B1

	sheet.Cells["A1"].PutValue("Products");

	sheet.Cells["B1"].PutValue("Users");

	//Add data from A2 till B4

	sheet.Cells["A2"].PutValue("Aspose.Cells");

	sheet.Cells["B2"].PutValue(10000);

	sheet.Cells["A3"].PutValue("Aspose.Slides");

	sheet.Cells["B3"].PutValue(8000);

	sheet.Cells["A4"].PutValue("Aspose.Words");

	sheet.Cells["B4"].PutValue(12000);

	//Chart reference

	Chart productsChart;

	//Add a Pie Chart

	int chartIdx = sheet.Charts.Add(ChartType.Pie, 7, 0, 20, 6);

	productsChart = sheet.Charts[chartIdx];

	//Gets the cells that define the data to be charted

	int seriesIdx = productsChart.NSeries.Add("=Sheet1!$B$2:$B$4", true);

	Series nSeries = productsChart.NSeries[seriesIdx];

	nSeries.XValues = "=Sheet1!$A$2:$A$4";

	//Set chart title

	productsChart.Title.Text = "Users";

	//Autofit first column

	sheet.AutoFitColumn(0);

	//Save the copy of workbook as OutputAspose.xlsx

	workbook.Save("OutputAspose.xlsx");

}


{{< /highlight >}}
## **Télécharger le code source d'exemple**
- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Create.a.Pie.Chart.Aspose.Cells.zip)
- [Sourceforge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Create%20a%20Pie%20Chart%20\(Aspose.Cells\).zip/download)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Create%20a%20Pie%20Chart%20\(Aspose.Cells\).zip)
{{< app/cells/assistant language="csharp" >}}
