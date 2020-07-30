---
title : "Preparing for Creating Table Report" 
description : "" 
weight : 12063 
toc : false
type: docs
url: /reportingservices/userguide/creatingtabularreport/preparing+for+creating+table+report/
---

# Aspose.Cells for Reporting Services : Preparing for Creating Table Report


Before creating a tabular report user must first create data sources, datasets and report parameters (optional) as described in [DataSources and Queries](/pages/createpage.action?spaceKey=cellsreportingservices&title=DataSources+and+Queries&linkCreation=true&fromPageId=6094952).

Below, we use the AdventureWorks sample database that ships with SQL Server Reporting Services 2005.

1.  Create a dataset named EmpSalesDetail. We'll use this as the table's data source. The dataset has three parameters: ReportYear, ReportMonth and EmpID.  
    The SQL that defines EmpSalesDetail is as follows:  
      
    
    **SQL**
    
    SELECT C.FirstName+' '+C.LastName 'Employee',DATEPART(Month,SOH.OrderDate) 'OrderMonthNum',PS.Name 'SubCat',Sum(SOD.LineTotal) 'Sales',SOH.SalesOrderNumber,P.Name 'Product',Sum(SOD.OrderQty) 'OrderQty',SOD.UnitPrice,PC.Name 'ProdCat'FROM AdventureWorks.Person.Contact C,AdventureWorks.HumanResources.Employee E,AdventureWorks.Production.Product P,AdventureWorks.Production.ProductCategory PC,AdventureWorks.Production.ProductSubcategory PS,AdventureWorks.Sales.SalesOrderDetail SOD,AdventureWorks.Sales.SalesOrderHeader SOH,AdventureWorks.Sales.SalesPerson SPWHERE SOH.SalesOrderID = SOD.SalesOrderIDAND SOH.SalesPersonID = SP.SalesPersonIDAND SP.SalesPersonID = E.EmployeeIDAND E.ContactID = C.ContactIDAND SOD.ProductID = P.ProductIDAND P.ProductSubcategoryID = PS.ProductSubcategoryID AND PS.ProductCategoryID = PC.ProductCategoryIDAND ((DATEPART(Year,SOH.OrderDate)=?)AND (DATEPART(Month,SOH.OrderDate)=?) AND (SOH.SalesPersonID=?))GROUP BY C.FirstName+' '+C.LastName, DATEPART(Month,SOH.OrderDate), PS.Name,SOH.SalesOrderNumber,P.Name,SOD.UnitPrice,PC.Name 
    
2.  Create a dataset named SalesEmps. We'll use that as the valid values for the EmpID parameter.  
    The SQL that defines SalesEmps is:  
      
    
    **SQL**
    
    SELECT  E.EmployeeID,  C.FirstName + N' ' + C.LastName AS EmployeeFROM  HumanResources.Employee E INNER JOIN  Sales.SalesPerson SPON E.EmployeeID = SP.SalesPersonID INNER JOIN   Person.Contact CON E.ContactID = C.ContactID  ORDER BY    C.LastName, C.FirstName 
    
3.  Create three report parameters: ReportYear, ReportMonth and EmpID.
    *   The valid values for the parameter ReportYear are:  
          
        ![](https://docs2.aspose.com/cells/reportingservices/attachments/6094952/6193291.png)  
          
        
    *   The valid values for the parameter ReportMonth is:  
          
        ![](https://docs2.aspose.com/cells/reportingservices/attachments/6094952/6193296.png)  
          
        
    *   The valid value for the parameter EmpID are:  
          
        ![](https://docs2.aspose.com/cells/reportingservices/attachments/6094952/6193297.png)  
          
        
4.  Map the dataset parameters to report parameters, as follow:  
      
    ![](https://docs2.aspose.com/cells/reportingservices/attachments/6094952/6193294.png)

## Attachments:

![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Preparing for Creating Table Report-001.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094952/6193291.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Preparing for Creating Table Report-002.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094952/6193296.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Preparing for Creating Table Report-003.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094952/6193297.png) (image/png)  
![](https://docs2.aspose.com/cells/reportingservices/images/icons/bullet_blue.gif) [Preparing for Creating Table Report-004.png](https://docs2.aspose.com/cells/reportingservices/attachments/6094952/6193294.png) (image/png)  

