---
title: Skapa ett cirkeldiagram
type: docs
weight: 110
url: /sv/net/create-a-pie-chart/
---
{{% alert color="primary" %}}

Diagram presenterar data på ett lättförståeligt sätt. Användare som arbetar med Microsoft Excel kan skapa ett antal olika diagram och anpassa dem. Samma funktioner är tillgängliga för utvecklare som arbetar med Aspose.Cells for .NET.

{{% /alert %}}

## **Skapa ett cirkeldiagram**

Den här artikeln jämför hur man skapar ett cirkeldiagram med Office Automation och VSTO med att använda Aspose.Cells for .NET. Stegen för att skapa ett cirkeldiagram är:

1. Skapa en arbetsbok och ett arbetsblad.
1. Lägger till exempeldata.
1. Hänvisning till produkter Diagram.
1. Lägga till ett cirkeldiagram, definiera dataintervallet och diagrammets titel.
1. Sparar kalkylark.

 Kodexemplen i den här artikeln visar hur man lägger till ett cirkeldiagram med[VSTO](/cells/sv/net/create-a-pie-chart/) , med antingen C# eller Visual Basic, jämfört med att skapa en med[Aspose.Cells](/cells/sv/net/create-a-pie-chart/), återigen med antingen C# eller Visual Basic.

### **Skapa ett cirkeldiagram med VSTO**

Kodexemplen som följer visar hur man lägger till ett cirkeldiagram i ett kalkylblad med VSTO.

**C#**

{{< highlight "csharp" >}}

 void PieChart()

{

    //Access a Vsto Worksheet

    Microsoft.Office.Tools.Excel.Worksheet sheet = this;

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

    Microsoft.Office.Interop.Excel.Workbook workbook= sheet.Application.ActiveWorkbook;

    //Save the copy of workbook as OutputVsto.xlsx

    workbook.SaveCopyAs("C:\\Downloads\\OutputVsto.xlsx");

}



{{< /highlight >}}

**Ett cirkeldiagram skapat med VSTO** 

![todo:image_alt_text](create-a-pie-chart_1.png)

### **Skapa ett cirkeldiagram med Aspose.Cells for .NET**

Kodexemplen som följer visar hur man lägger till ett cirkeldiagram i ett kalkylblad med Aspose.Cells.

**C#**

{{< highlight "csharp" >}}

 private void PieChart()

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

    workbook.Save("C:\\Downloads\\OutputAspose.xlsx");

}

{{< /highlight >}}

**Cirkeldiagram skapat med Aspose.Cells for .NET** 

![todo:image_alt_text](create-a-pie-chart_2.png)
