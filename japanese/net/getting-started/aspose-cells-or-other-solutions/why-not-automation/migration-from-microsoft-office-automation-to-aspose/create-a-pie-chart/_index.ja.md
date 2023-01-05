---
title: 円グラフを作成する
type: docs
weight: 110
url: /ja/net/create-a-pie-chart/
---
{{% alert color="primary" %}}

グラフはデータをわかりやすく表示します。 Microsoft Excel を使用しているユーザーは、さまざまなグラフを作成してカスタマイズできます。 Aspose.Cells for .NET で作業する開発者は、同じ機能を利用できます。

{{% /alert %}}

## **円グラフの作成**

この記事では、Office オートメーションと VSTO を使用して円グラフを作成する方法と、Aspose.Cells for .NET を使用して円グラフを作成する方法を比較します。円グラフを作成する手順は次のとおりです。

1. ワークブックとワークシートの作成。
1. サンプルデータの追加。
1. productsChart の参照。
1. 円グラフを追加し、データ範囲とグラフ タイトルを定義します。
1. スプレッドシートを保存しています。

この記事のコード サンプルは、円グラフを追加する方法を示しています。[VSTO](/cells/ja/net/create-a-pie-chart/) 、C# または Visual Basic を使用して作成する場合と比較して[Aspose.Cells](/cells/ja/net/create-a-pie-chart/)、再び C# または Visual Basic を使用します。

### **VSTO で円グラフを作成する**

次のコード サンプルは、VSTO を使用して円グラフをスプレッドシートに追加する方法を示しています。

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

**VSTO で作成された円グラフ** 

![todo:画像_代替_文章](create-a-pie-chart_1.png)

### **Aspose.Cells for .NET で円グラフを作成する**

次のコード サンプルは、Aspose.Cells を使用して円グラフをスプレッドシートに追加する方法を示しています。

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

**Aspose.Cells for .NET で作成された円グラフ** 

![todo:画像_代替_文章](create-a-pie-chart_2.png)
