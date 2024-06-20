---
title: Creare un grafico a torta
type: docs
weight: 110
url: /it/net/create-a-pie-chart/
---

{{% alert color="primary" %}}

I grafici presentano i dati in modo facile da capire. Gli utenti che lavorano con Microsoft Excel possono creare diverse tipologie di grafici e personalizzarli. Le stesse funzionalità sono disponibili per i developer che lavorano con Aspose.Cells for .NET.

{{% /alert %}}

## **Creazione di un grafico a torta**

Questo articolo confronta come creare un grafico a torta utilizzando l'Automazione Office e VSTO rispetto all'utilizzo del Aspose.Cells for .NET. I passaggi per la creazione di un grafico a torta sono:

1. Creazione di un workbook e di un foglio di lavoro.
1. Aggiunta di dati di esempio.
1. Riferimento a productsChart.
1. Aggiunta di un grafico a torta, definizione dell'intervallo di dati e del titolo del grafico.
1. Salvataggio del foglio di calcolo.

I campioni di codice in questo articolo mostrano come aggiungere un grafico a torta con [VSTO](/cells/it/net/create-a-pie-chart/), utilizzando C# o Visual Basic, rispetto alla creazione di uno con [Aspose.Cells](/cells/it/net/create-a-pie-chart/), ancora utilizzando C# o Visual Basic.

### **Creazione di un grafico a torta con VSTO**

I campioni di codice che seguono mostrano come aggiungere un grafico a torta a un foglio di calcolo utilizzando VSTO.

**C#**

{{< highlight csharp >}}

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

**Un grafico a torta creato con VSTO** 

![todo:image_alt_text](create-a-pie-chart_1.png)

### **Creazione di un grafico a torta con Aspose.Cells for .NET**

I campioni di codice che seguono mostrano come aggiungere un grafico a torta a un foglio di calcolo utilizzando Aspose.Cells.

**C#**

{{< highlight csharp >}}

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

**Grafico a torta creato con Aspose.Cells for .NET** 

![todo:image_alt_text](create-a-pie-chart_2.png)
