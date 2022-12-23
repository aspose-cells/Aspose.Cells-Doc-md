---
title: Pasta Grafiği Oluşturun
type: docs
weight: 110
url: /tr/net/create-a-pie-chart/
---
{{% alert color="primary" %}}

Grafikler, verileri anlaşılması kolay bir şekilde sunar. Microsoft Excel ile çalışan kullanıcılar, bir dizi farklı grafik oluşturabilir ve bunları özelleştirebilir. Aspose.Cells for .NET ile çalışan geliştiriciler için de aynı özellikler mevcuttur.

{{% /alert %}}

## **Pasta Grafiği Oluşturma**

Bu makale, Office Automation ve VSTO kullanarak pasta grafiğin nasıl oluşturulacağını Aspose.Cells for .NET kullanarak karşılaştırır. Pasta grafiği oluşturmaya yönelik adımlar şunlardır:

1. Çalışma kitabı ve çalışma sayfası oluşturma.
1. Örnek veri ekleme.
1. Başvurulan ürünler Tablosu.
1. Pasta grafik ekleme, veri aralığını ve grafik başlığını tanımlama.
1. E-tablo kaydediliyor.

 Bu makaledeki kod örnekleri, bir pasta grafiğin nasıl ekleneceğini gösterir.[VSTO](/cells/tr/net/create-a-pie-chart/) , C# veya Visual Basic kullanarak, ile bir tane oluşturmaya kıyasla[Aspose.Cells](/cells/tr/net/create-a-pie-chart/), yine C# veya Visual Basic kullanarak.

### **VSTO ile Pasta Grafiği Oluşturma**

Aşağıdaki kod örnekleri, VSTO kullanarak bir elektronik tabloya pasta grafiğin nasıl ekleneceğini gösterir.

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

**VSTO ile oluşturulmuş bir pasta grafiği** 

![yapılacaklar:resim_alternatif_metin](create-a-pie-chart_1.png)

### **Aspose.Cells for .NET ile Pasta Grafik Oluşturma**

Aşağıdaki kod örnekleri, Aspose.Cells kullanarak bir elektronik tabloya pasta grafiğin nasıl ekleneceğini gösterir.

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

**Aspose.Cells for .NET ile oluşturulan pasta grafik** 

![yapılacaklar:resim_alternatif_metin](create-a-pie-chart_2.png)
