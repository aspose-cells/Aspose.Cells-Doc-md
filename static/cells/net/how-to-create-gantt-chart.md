##How to create a Gantt chart
Learn how to create a Gantt chart with Aspose.Cells for .NET API.
## **What is Gantt chart**
A Gantt chart is a type of bar chart that illustrates a project schedule. It shows the start and finish dates of the various elements of a project. Each task or activity is represented by a bar, with its length corresponding to its duration. Gantt charts also indicate dependencies between tasks, allowing project managers to visualize the sequence in which tasks need to be completed. They are widely used in project management to plan, schedule, and track projects effectively.
## **How to Create a Gantt Chart in Excel**
You can create a Gantt chart in Excel by following these steps:
1. Add some data for Gantt chart.
1. Select the data and and go to Insert --> Charts --> Insert Column or Bar Chart --> Stacked Bar Chart. In our example, that’s B1:B7, and then Insert **Stacked Bar** chart.
1. Selett the chart,**Select Data**->**Add**, set the **Series name** and **Series values** as following.
1. Select the chart, edit the **Horizontal(Category) Axis Labels**.
1. **Format Axis** the Y Axis, select **Categories in reverse order**.
1. Seletct the **Blue Series** and set the **Fill->NO Fill**.
1. **Format Axis** the X Axis, set the **Mininum and Maxinum**(1/5/2019:43470,1/30/2019:43494).
1. **Add Data labels** for the chart, now you will get a gantt chart.
## **How to Add a Gantt Chart in Aspose.Cells**
Please see the following sample code. It loads the [sample Excel file](sample.xlsx) that contains some sample data. It then creates the stacked bar chart based on the initial data and sets relevant properties. Finally, it saves the workbook to [output XLSX format](result.xlsx). The following screenshot shows the Gantt chart created by Aspose.Cells in the output Excel file.
### **Sample Code**
