+++
title = "Creating New Data sources and Queries" 
description = "" 
weight = 12055 
+++

Aspose.Cells for Reporting Services : Creating New Data sources and Queries  

# Aspose.Cells for Reporting Services : Creating New Data sources and Queries


Aspose.Cells.Report.Designer integrates with MS Query and uses MS Query as a tool for creating data sources and queries. To create a new data source and query in Aspose.Cells.Report.Designer, follow the steps below:.

To create a new data source and query in Aspose.Cells.Report.Designer:

1.  Open Microsoft Excel.
2.  Click **Build DataSet** in the Aspose.Cells.Report.Designer toolbar: ![](https://docs2.aspose.com/cells/reportingservices/attachments/6094945/6193495.png)  
    All the data sources and queries are listed in the dialog box.
    *   A data source node: ![](https://docs2.aspose.com/cells/reportingservices/attachments/6094945/6193496.png)
    *   A data set node: ![](https://docs2.aspose.com/cells/reportingservices/attachments/6094945/6193497.png)
3.  Select the tree's root node.
4.  Click **Add**.  
      
    **Adding data sources and data sets**  
    ![](https://docs2.aspose.com/cells/reportingservices/attachments/6094945/6193490.png)  
      
    
5.  In the dialog box, call the data source **SqlServer** and the data set **EmpsSalesDetail**.
6.  Click **Next**.  
      
    **Adding data sets and data sources**  
    ![](https://docs2.aspose.com/cells/reportingservices/attachments/6094945/6193491.png)  
      
    Aspose.Cells.Report.Designer starts Microsoft Query.
7.  In the Choose Data Source dialog, select **New Data Source**.
8.  Click **OK**.  
    You may also select a existing data source.  
      
    **Choosing a data source**  
    ![](https://docs2.aspose.com/cells/reportingservices/attachments/6094945/6193492.png)  
      
    
9.  Input a data source name and select SQL Server from the drop-down list of database drivers.
10.  Click **Connect**.  
      
    **Creating a new data source**  
    ![](https://docs2.aspose.com/cells/reportingservices/attachments/6094945/6193493.png)  
      
    
11.  In the SQL Server Login dialog, select the appropriate value for each item.  
    For example, set server to local, select the AdventureWorks database and select **Use Trusted Connection**.
12.  Click **OK**.  
      
    **Logging in to the SQL server**  
    ![](https://docs2.aspose.com/cells/reportingservices/attachments/6094945/6193486.png)  
      
    
13.  Click **OK**.  
      
    **Note that we are now logged in to the SQL server**  
    ![](https://docs2.aspose.com/cells/reportingservices/attachments/6094945/6193487.png)  
      
    The new data source appears in the **Choose Data Source** dialog.
14.  Select the new data source.  
      
    **The new data source**  
    ![](https://docs2.aspose.com/cells/reportingservices/attachments/6094945/6193488.png)  
      
    
15.  Click **OK** to open Microsoft Query.
16.  To create a query in Microsoft Query, refer to the Microsoft Query Helper. In the following sample, we create a query with parameters.  
      
    **Building a query**  
    ![](https://docs2.aspose.com/cells/reportingservices/attachments/6094945/6193489.png)  
      
    The SQL is as follows:  
      
    
    **SQL**
    
    SELECT C.FirstName + ' ' + C.LastName AS Employee,DATEPART(Month, SOH.OrderDate) AS OrderMonthNum,PS.Name AS SubCat,SUM(SOD.LineTotal) AS Sales,SOH.SalesOrderNumber,P.Name AS Product,SUM(SOD.OrderQty) AS OrderQty,SOD.UnitPrice,PC.Name AS ProdCatFROM  Sales.SalesOrderHeader SOH ,Sales.SalesOrderDetail SOD ,Sales.SalesPerson SP,HumanResources.Employee E,Person.Contact C,Production.Product P,Production.ProductSubcategory PS ,Production.ProductCategory PCwhere SOH.SalesOrderID = SOD.SalesOrderIDand SOH.SalesPersonID = SP.SalesPersonIDand SP.SalesPersonID = E.EmployeeIDand E.ContactID = C.ContactIDand SOD.ProductID = P.ProductIDand P.ProductSubcategoryID = PS.ProductSubcategoryIDand PS.ProductCategoryID = PC.ProductCategoryIDand  (DATEPART(Year, SOH.OrderDate) =  ?)AND (DATEPART(Month, SOH.OrderDate) =  ?)AND (SOH.SalesPersonID =?)GROUP BY    C.FirstName + ' ' + C.LastName,DATEPART(Month, SOH.OrderDate), SOH.SalesOrderNumber,P.Name, PS.Name, SOD.UnitPrice, PC.Name 
    
      
    The query has three parameters: `ReportYear`, `ReportMonth` and `EmpID`.
17.  From Microsoft Query's **File** menu, select **Return To Aspose.Cells.Report.Designer**.  
      
    **Returning to the report designer**  
    ![](https://docs2.aspose.com/cells/reportingservices/attachments/6094945/6193482.png)  
      
    The data source and query created above are listed in the dialog box.
18.  Click the data source **SqlServer** to view its detailed information.  
      
    **The new data source**  
    ![](https://docs2.aspose.com/cells/reportingservices/attachments/6094945/6193483.png)  
      
    
19.  Click the query EmpSalesDetails to view its detailed information.  
      
    **Click SQL Tab to view the sql for the query**  
    ![](https://docs2.aspose.com/cells/reportingservices/attachments/6094945/6193484.png)  
      
    **Click Columns Tab to view the columns of the query**  
    ![](https://docs2.aspose.com/cells/reportingservices/attachments/6094945/6193485.png)  
      
    **Click Parameters Tab to view the parameters of the query**  
    ![](https://docs2.aspose.com/cells/reportingservices/attachments/6094945/6193479.png)  
      
    

## Attachments:

![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Creating New Data sources and Queries-001.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094945/6193495.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Creating New Data sources and Queries-002.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094945/6193496.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Creating New Data sources and Queries-003.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094945/6193497.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Creating New Data sources and Queries-004.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094945/6193490.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Creating New Data sources and Queries-005.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094945/6193491.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Creating New Data sources and Queries-006.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094945/6193492.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Creating New Data sources and Queries-007.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094945/6193493.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Creating New Data sources and Queries-008.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094945/6193486.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Creating New Data sources and Queries-009.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094945/6193487.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Creating New Data sources and Queries-010.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094945/6193488.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Creating New Data sources and Queries-011.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094945/6193489.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Creating New Data sources and Queries-012.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094945/6193482.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Creating New Data sources and Queries-013.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094945/6193483.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Creating New Data sources and Queries-014.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094945/6193484.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Creating New Data sources and Queries-015.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094945/6193485.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Creating New Data sources and Queries-016.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094945/6193479.png) (image/png)  

