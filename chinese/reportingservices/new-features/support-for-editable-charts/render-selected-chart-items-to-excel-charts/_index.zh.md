---
title: 将选定的图表项呈现为 Excel 图表
type: docs
weight: 30
url: /zh/reportingservices/render-selected-chart-items-to-excel-charts/
---
{{% alert color="primary" %}} 

要仅将报表中的某些图表呈现为 Excel 图表：

1. 打开**Aspose.Cells.ReportingServices.xml**文件。
1. 修改配置参数**Aspose.Cells.ReportingServices.xml**文件。
1. 添加所需的报告配置信息。
1. 添加您不想导出为可编辑图表的图表项目的信息。这些项目导出为静态图像。

例如：

{{< highlight "java" >}}

 <Chart >

<Report name= "Employee Sales Summary 2008">

<ChartItem name="Chart1" type="image"/>

</Report >

</Chart> 

{{< /highlight >}}

**导出为图像的图表** 

![待办事项：图片_替代_文本](render-selected-chart-items-to-excel-charts_1.png)

**导出为可编辑 Excel 图表的图表** 

![待办事项：图片_替代_文本](render-selected-chart-items-to-excel-charts_2.png)

{{% /alert %}}
