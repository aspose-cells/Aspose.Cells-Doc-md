---
title: 将选定的图表项目呈现到 Excel 图表中
type: docs
weight: 30
url: /zh/reportingservices/render-selected-chart-items-to-excel-charts/
---

{{% alert color="primary" %}} 

只将报告中的一些图表呈现到 Excel 图表中:

1. 打开 **Aspose.Cells.ReportingServices.xml** 文件。
1. 修改 **Aspose.Cells.ReportingServices.xml** 文件的配置参数。
1. 添加所需的报告配置信息。
1. 添加您不希望导出为可编辑图表的图表项目信息。这些项目将作为静态图像导出。

例如:

{{< highlight java >}}

 <Chart >

<Report name= "Employee Sales Summary 2008">

<ChartItem name="Chart1" type="image"/>

</Report >

</Chart> 

{{< /highlight >}}

**作为图片导出的图表** 

![todo:image_alt_text](render-selected-chart-items-to-excel-charts_1.png)

**作为可编辑 Excel 图表导出的图表** 

![todo:image_alt_text](render-selected-chart-items-to-excel-charts_2.png)

{{% /alert %}}
