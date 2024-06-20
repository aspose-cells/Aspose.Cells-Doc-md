---
title: Crear un gráfico circular
type: docs
weight: 110
url: /es/net/create-a-pie-chart/
---

{{% alert color="primary" %}}

Los gráficos presentan datos de una manera fácil de entender. Los usuarios que trabajan con Microsoft Excel pueden crear varios tipos de gráficos diferentes y personalizarlos. Las mismas funciones están disponibles para los desarrolladores que trabajan con Aspose.Cells for .NET.

{{% /alert %}}

## **Crear un gráfico circular**

Este artículo compara cómo crear un gráfico de pie utilizando Automatización de Office y VSTO con el uso de Aspose.Cells for .NET. Los pasos para crear un gráfico de pie son:

1. Crear un libro y una hoja de cálculo.
1. Agregar datos de muestra.
1. Hacer referencia a productsChart.
1. Agregar un gráfico circular, definir el rango de datos y el título del gráfico.
1. Guardar hoja de cálculo.

Los ejemplos de código en este artículo muestran cómo agregar un gráfico circular con [VSTO](/cells/es/net/create-a-pie-chart/), utilizando C# o Visual Basic, en comparación con la creación con [Aspose.Cells](/cells/es/net/create-a-pie-chart/), nuevamente utilizando C# o Visual Basic.

### **Crear un gráfico circular con VSTO**

Los ejemplos de código que siguen muestran cómo agregar un gráfico circular a una hoja de cálculo utilizando VSTO.

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

**Un gráfico circular creado con VSTO** 

![todo:image_alt_text](create-a-pie-chart_1.png)

### **Creando un gráfico circular con Aspose.Cells for .NET**

Los ejemplos de código que siguen muestran cómo agregar un gráfico circular a una hoja de cálculo utilizando Aspose.Cells.

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

**Gráfico circular creado con Aspose.Cells for .NET** 

![todo:image_alt_text](create-a-pie-chart_2.png)
