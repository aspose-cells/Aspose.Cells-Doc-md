---
title: How to create a Gantt chart
linktitle: How to create a Gantt chart
type: docs
weight: 72
url: /net/how-to-create-gantt-chart/
description: Learn how to create a Gantt chart with Aspose.Cells for .NET API.
keywords: C# create a Gantt chart, add a Gantt chart, insert a Gantt chart
---

## **What is Gantt chart**

A Gantt chart is a type of bar chart that illustrates a project schedule. It shows the start and finish dates of the various elements of a project. Each task or activity is represented by a bar, with its length corresponding to its duration. Gantt charts also indicate dependencies between tasks, allowing project managers to visualize the sequence in which tasks need to be completed. They are widely used in project management to plan, schedule, and track projects effectively.

## **How to Create a Gantt Chart in Excel**

You can create a Gantt chart in Excel by following these steps:
1. Add some data for Gantt chart. 
<br>
<img src="00.png" width=50% />
1. Select the data and and go to Insert --> Charts --> Insert Column or Bar Chart --> Stacked Bar Chart. In our example, that’s B1:B7, and then Insert **Stacked Bar** chart.
<br>
<img src="1.png" width=50% />

1. Selett the chart,**Select Data**->**Add**, set the **Series name** and **Series values** as following.
<br>
<img src="2.png" width=50% />

1. Select the chart, edit the **Horizontal(Category) Axis Labels**.
<br>
<img src="3.png" width=50% />

1. **Format Axis** the Y Axis, select **Categories in reverse order**.
1. Seletct the **Blue Series** and set the **Fill->NO Fill**.
1. **Format Axis** the X Axis, set the **Mininum and Maxinum**(1/5/2019:43470,1/30/2019:43494).
<br>
<img src="4.png" width=50% />

1. **Add Data labels** for the chart, now you will get a gantt chart.
<br>
<img src="0.png" width=50% />


## **How to Add a Gantt Chart in Aspose.Cells**
Please see the following sample code. It loads the [sample Excel file](sample.xlsx) that contains some sample data. It then creates the stacked bar chart based on the initial data and sets relevant properties. Finally, it saves the workbook to [output XLSX format](result.xlsx). The following screenshot shows the Gantt chart created by Aspose.Cells in the output Excel file.
<br>
<img src="5.png" width=60% />

### **Sample Code**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-gantt-chart.cs" >}}

{{< app/cells/assistant language="csharp" >}}