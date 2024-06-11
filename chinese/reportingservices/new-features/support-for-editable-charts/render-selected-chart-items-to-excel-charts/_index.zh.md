---
title: 将选定的图表项呈现为 Excel 图表
type: docs
weight: 30
url: /zh/reportingservices/render-selected-chart-items-to-excel-charts/
---

{{% alert color="primary" %}} 

要仅将报告中的某些图表呈现为 Excel 图表:

1. 打开 **Aspose.Cells.ReportingServices.xml** 文件。
1. 修改 **Aspose.Cells.ReportingServices.xml** 文件的配置参数。
1. 添加所需的报告配置信息。
1. 添加您不希望以可编辑图表导出的图表项的信息。这些项将作为静态图像导出。

例如:

{{< highlight java >}}

 <Chart >

<Report name= "Employee Sales Summary 2008">

<ChartItem name="Chart1" type="image"/>

</Report >

</Chart> 

{{< /highlight >}}

**作为图像导出的图表** 

![todo:image_alt_text](render-selected-chart-items-to-excel-charts_1.png)

**作为可编辑 Excel 图表导出的图表** 

![todo:image_alt_text](render-selected-chart-items-to-excel-charts_2.png)

{{% /alert %}}
