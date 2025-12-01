---
title: Render Selected Chart Items to Excel Charts
type: docs
weight: 30
url: /reportingservices/render-selected-chart-items-to-excel-charts/
ai_search_scope: cells_reportingservices
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

To render only some charts in a report to Excel charts:

1. Open the **Aspose.Cells.ReportingServices.xml** file.
1. Modify the configuration parameters of the **Aspose.Cells.ReportingServices.xml** file.
1. Add the desired report configuration information.
1. Add the information for the chart items you don’t want to export as editable charts. These items are exported as static images.

For example:

{{< highlight java >}}

 <Chart >

<Report name= "Employee Sales Summary 2008">

<ChartItem name="Chart1" type="image"/>

</Report >

</Chart> 

{{< /highlight >}}

**A chart exported as an image** 

![todo:image_alt_text](render-selected-chart-items-to-excel-charts_1.png)

**A chart exported as an editable Excel chart** 

![todo:image_alt_text](render-selected-chart-items-to-excel-charts_2.png)

{{% /alert %}}
