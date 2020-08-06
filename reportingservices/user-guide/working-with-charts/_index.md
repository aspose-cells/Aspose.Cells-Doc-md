---
title: Working with Charts
type: docs
weight: 110
url: /reportingservices/working-with-charts/
---

{{% alert color="primary" %}} 

Aspose.Cells Report template supports Microsoft Excel charts. Each time you execute a report, the chart is populated with the most recent data. 

{{% /alert %}} 

To add a chart to report template:

1. First, create the dataset that will be the data source for the chart.
   Below, we use the AdventureWorks sample database that ships with SQL Server Reporting Services 2005 and create a dataset named Sales.
   This SQL defines the dataset: 

**SQL**

{{< highlight csharp >}}

 SELECT DATEPART(yy,SOH.OrderDate) 'Year',

'Q'+DATENAME(qq,SOH.OrderDate) 'Quarter',

SUM(SOD.UnitPrice*SOD.OrderQty) 'Sales'

FROMAdventureWorks.Sales.SalesOrderDetail SOD,

AdventureWorks.Sales.SalesOrderHeader SOH

WHERE SOH.SalesOrderID = SOD.SalesOrderID

AND ((DATEPART(yy,SOH.OrderDate)=2002))

GROUP BY DATEPART(yy,SOH.OrderDate), 'Q'+DATENAME(qq,SOH.OrderDate)



{{< /highlight >}}



Please refer to [Data Sources and Queries](/cells/reportingservices/data-sources-and-queries-html/) to learn more about how to create a data source and dataset in Aspose.Cells.Report.Designer.

1. Create a tabular report according to the instructions in [Creating Tabular Report](/cells/reportingservices/creating-tabular-report-html/). The report we've created for this example is below. The table is the chart's data source. 

![todo:image_alt_text](working-with-charts_1.png)




1. In Microsoft Excel, click the **Insert** menu and select **Chart**.
1. Click **Next**. 

![todo:image_alt_text](working-with-charts_2.png)




1. Click the **Series** tab. 

![todo:image_alt_text](working-with-charts_3.png)




1. Click **Add**. 

![todo:image_alt_text](working-with-charts_4.png)




1. In the dialog box, set the value of Series1 (Quarter series) to the table's first data field.
   In the sample, that is “CompanySales!$C$3:$C$3”. The first $C$3 is the first row index of “Quarter” and the second $C$3 is a placeholder for last row index of “Quarter” and will be replaced with the table data's real row index at rendering time. Set the category(X) axis labels to “=CompanySales!$C$3:$C$3”. 

![todo:image_alt_text](working-with-charts_5.png)




1. Click **Add** to add another series.
   In the sample, we've added the sales series. 
1. Set the value of Series2 (Sales series) to the table's second data field.
   In the sample it is “CompanySales!$D$3:$D$3”. The first $D$3 is the first row index of “Sales” and the second $D$3 is a placeholder for last row index of “Sales” and will be replaced with the table data's real row index at rendering time. 
1. Click **Next** to continue. 

![todo:image_alt_text](working-with-charts_6.png)




1. In the dialog box, set the chart title and category(X) axis.
1. Click **Finish** to complete the work. 

![todo:image_alt_text](working-with-charts_7.png)



The template looks like the below. 

![todo:image_alt_text](working-with-charts_8.png)




1. Save the report and publish it to Report Server.
1. Export the report from Report Server.
   The result is as below. 

![todo:image_alt_text](working-with-charts_9.png)
