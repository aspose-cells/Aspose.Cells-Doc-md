---
title: 创建饼图
type: docs
weight: 110
url: /zh/net/create-a-pie-chart/
---
{{% alert color="primary" %}}

图表以易于理解的方式呈现数据。使用 Microsoft Excel 的用户可以创建许多不同的图表并对其进行自定义。使用 Aspose.Cells for .NET 的开发人员可以使用相同的功能。

{{% /alert %}}

## **创建饼图**

本文将如何使用Office Automation和VSTO创建饼图与使用Aspose.Cells for .NET进行了比较，创建饼图的步骤为：

1. 创建工作簿和工作表。
1. 添加示例数据。
1. 参考产品图表。
1. 添加饼图，定义数据范围和图表标题。
1. 保存电子表格。

本文中的代码示例展示了如何添加饼图[VSTO](/cells/zh/net/create-a-pie-chart/)，与创建一个相比，使用 C# 或 Visual Basic[Aspose.Cells](/cells/zh/net/create-a-pie-chart/), 再次使用 C# 或 Visual Basic。

### **使用 VSTO 创建饼图**

下面的代码示例演示如何使用 VSTO 将饼图添加到电子表格。

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

**使用 VSTO 创建的饼图** 

![待办事项：图像_替代_文本](create-a-pie-chart_1.png)

### **使用 Aspose.Cells for .NET 创建饼图**

下面的代码示例显示了如何使用 Aspose.Cells 将饼图添加到电子表格。

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

**使用 Aspose.Cells for .NET 创建的饼图** 

![待办事项：图像_替代_文本](create-a-pie-chart_2.png)
