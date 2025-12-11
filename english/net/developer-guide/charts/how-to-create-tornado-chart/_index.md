---
title: How to create a tornado chart
type: docs
weight: 73
url: /net/create-tornado-chart/
description: Learn how to create a tornado chart with Aspose.Cells for .NET API.
keywords: C# create a tornado chart, add a tornado chart, insert a tornado chart
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Introduction**
A tornado chart, also known as a tornado diagram or tornado graph, is a type of data visualization that is often used for sensitivity analysis in Excel. It helps you understand the impact of changing variables on a particular outcome or result.

## **How to Create a Tornado Chart in Excel**
You can create a tornado chart in Excel by following these steps:
1. Select the data and go to **Insert → Charts → Insert Column or Bar Chart → Stacked Bar Chart**. Click on it.  
<br>
<img src="1.png" width=70% />
2. Change the Y‑axis: Right‑click on the Y‑axis. Click on **Format Axis**. In **Labels**, click on the label position drop‑down and select **Low**.  
<br>
<img src="2.png" width=70% />
3. Select any bar and go to **Formatting**. Set an appropriate gap width.  
<br>
<img src="3.png" width=70% />
4. Let's remove the minus sign (‑) from the tornado chart. Select the X‑axis. Go to **Formatting**. In the axis options, click on **Number**. In **Category**, select **Custom**. In the format code, write `###0,###0`. Click **Add**.  
<br>
<img src="4.png" width=70% />
5. Click on the Y‑axis and go to the axis options. In the **Axis Options**, check **Categories in reverse order**.  
<br>
<img src="5.png" width=70% />

## **How to Add a Tornado Chart in Aspose.Cells**
Please see the following sample code. It loads the [sample Excel file](sample.xlsx) that contains some sample data. It then creates the stacked bar chart based on the initial data and sets relevant properties. Finally, it saves the workbook to [output XLSX format](out.xlsx). The following screenshot shows the tornado chart created by Aspose.Cells in the output Excel file.  
<br>
<img src="6.png" width=70% />

### **Sample Code**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-tornado-chart.cs" >}}
{{< app/cells/assistant language="csharp" >}}
