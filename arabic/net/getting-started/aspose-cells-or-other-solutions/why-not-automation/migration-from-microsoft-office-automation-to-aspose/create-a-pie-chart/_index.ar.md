---
title: قم بإنشاء مخطط دائري
type: docs
weight: 110
url: /ar/net/create-a-pie-chart/
---
{{% alert color="primary" %}}

تقدم الرسوم البيانية البيانات بطريقة سهلة الفهم. يمكن للمستخدمين الذين يعملون مع Microsoft Excel إنشاء عدد من المخططات المختلفة وتخصيصها. تتوفر نفس الميزات للمطورين الذين يعملون مع Aspose.Cells for .NET.

{{% /alert %}}

## **إنشاء مخطط دائري**

تقارن هذه المقالة كيفية إنشاء مخطط دائري باستخدام Office Automation و VSTO باستخدام Aspose.Cells for .NET. خطوات إنشاء مخطط دائري هي:

1. إنشاء مصنف وورقة عمل.
1. إضافة بيانات العينة.
1. الرجوع إلى المنتجات
1. إضافة مخطط دائري ، وتحديد نطاق البيانات وعنوان المخطط.
1. حفظ جدول البيانات.

 توضح نماذج التعليمات البرمجية في هذه المقالة كيفية إضافة مخطط دائري باستخدام[VSTO](/cells/ar/net/create-a-pie-chart/) ، باستخدام C# أو Visual Basic ، مقارنة بإنشاء واحد بامتداد[Aspose.Cells](/cells/ar/net/create-a-pie-chart/)، مرة أخرى باستخدام إما C# أو Visual Basic.

### **إنشاء مخطط دائري باستخدام VSTO**

توضح نماذج التعليمات البرمجية التالية كيفية إضافة مخطط دائري إلى جدول بيانات باستخدام VSTO.

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

**مخطط دائري تم إنشاؤه باستخدام VSTO** 

![ما يجب القيام به: image_بديل_نص](create-a-pie-chart_1.png)

### **إنشاء مخطط دائري باستخدام Aspose.Cells for .NET**

توضح نماذج التعليمات البرمجية التالية كيفية إضافة مخطط دائري إلى جدول بيانات باستخدام Aspose.Cells.

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

**تم إنشاء المخطط الدائري بالرقم Aspose.Cells for .NET** 

![ما يجب القيام به: image_بديل_نص](create-a-pie-chart_2.png)
