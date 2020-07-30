---
title : "Working with Charts" 
description : "" 
weight : 8077 
toc : false
type: docs
url: /reportingservices/userguide/working+with+charts/
---

# Aspose.Cells for Reporting Services : Working with Charts


Aspose.Cells Report template supports Microsoft Excel charts. Each time you execute a report, the chart is populated with the most recent data.

To add a chart to report template:

1.  First, create the dataset that will be the data source for the chart.  
    Below, we use the AdventureWorks sample database that ships with SQL Server Reporting Services 2005 and create a dataset named Sales.  
    This SQL defines the dataset:  
      
    
    **SQL**
    
    SELECT DATEPART(yy,SOH.OrderDate) 'Year','Q'+DATENAME(qq,SOH.OrderDate) 'Quarter',SUM(SOD.UnitPrice\*SOD.OrderQty) 'Sales'FROMAdventureWorks.Sales.SalesOrderDetail SOD,AdventureWorks.Sales.SalesOrderHeader SOHWHERE SOH.SalesOrderID = SOD.SalesOrderIDAND ((DATEPART(yy,SOH.OrderDate)=2002))GROUP BY DATEPART(yy,SOH.OrderDate), 'Q'+DATENAME(qq,SOH.OrderDate) 
    
      
      
    Please refer to [Data Sources and Queries](https://docs2.aspose.com/cells/reportingservices/userguide/datasourcesandqueries/) to learn more about how to create a data source and dataset in Aspose.Cells.Report.Designer.  
      
    
2.  Create a tabular report according to the instructions in [Creating Tabular Report](https://docs2.aspose.com/cells/reportingservices/userguide/creatingtabularreport/). The report we've created for this example is below. The table is the chart's data source.  
      
    ![](https://docs2.aspose.com/cells/reportingservices/attachments/6094974/6193183.png)  
      
    
3.  In Microsoft Excel, click the **Insert** menu and select **Chart**.
4.  Click **Next**.  
      
    ![](https://docs2.aspose.com/cells/reportingservices/attachments/6094974/6193182.png)  
      
    
5.  Click the **Series** tab.  
      
    ![](https://docs2.aspose.com/cells/reportingservices/attachments/6094974/6193181.png)  
      
    
6.  Click **Add**.  
      
    ![](https://docs2.aspose.com/cells/reportingservices/attachments/6094974/6193172.png)  
      
    
7.  In the dialog box, set the value of Series1 (Quarter series) to the table's first data field.  
    In the sample, that is “CompanySales!$C$3:$C$3”. The first $C$3 is the first row index of “Quarter” and the second $C$3 is a placeholder for last row index of “Quarter” and will be replaced with the table data's real row index at rendering time. Set the category(X) axis labels to “=CompanySales!$C$3:$C$3”.  
      
    ![](https://docs2.aspose.com/cells/reportingservices/attachments/6094974/6193171.png)  
      
    
8.  Click **Add** to add another series.  
    In the sample, we've added the sales series.
9.  Set the value of Series2 (Sales series) to the table's second data field.  
    In the sample it is “CompanySales!$D$3:$D$3”. The first $D$3 is the first row index of “Sales” and the second $D$3 is a placeholder for last row index of “Sales” and will be replaced with the table data's real row index at rendering time.
10.  Click **Next** to continue.  
      
    ![](https://docs2.aspose.com/cells/reportingservices/attachments/6094974/6193170.png)  
      
    
11.  In the dialog box, set the chart title and category(X) axis.
12.  Click **Finish** to complete the work.  
      
    ![](https://docs2.aspose.com/cells/reportingservices/attachments/6094974/6193169.png)  
      
    The template looks like the below.  
      
    ![](https://docs2.aspose.com/cells/reportingservices/attachments/6094974/6193176.png)  
      
    
13.  Save the report and publish it to Report Server.
14.  Export the report from Report Server.  
    The result is as below.  
      
    ![](https://docs2.aspose.com/cells/reportingservices/attachments/6094974/6193175.png)

## Attachments:

![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Working with Charts-001.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094974/6193183.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Working with Charts-002.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094974/6193182.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Working with Charts-003.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094974/6193181.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Working with Charts-004.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094974/6193172.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Working with Charts-005.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094974/6193171.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Working with Charts-006.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094974/6193170.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Working with Charts-007.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094974/6193169.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Working with Charts-008.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094974/6193176.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Working with Charts-009.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094974/6193175.png) (image/png)  

