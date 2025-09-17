##Preparing for Creating Table Report
Before creating a tabular report user must first create data sources, datasets and report parameters (optional) as described in [DataSources and Queries](https://docs.aspose.com/cells/reportingservices/data-sources-and-queries/).
Below, we use the AdventureWorks sample database that ships with SQL Server Reporting Services 2005.
1. Create a dataset named EmpSalesDetail. We'll use this as the table's data source. The dataset has three parameters: ReportYear, ReportMonth and EmpID.
The SQL that defines EmpSalesDetail is as follows:
**SQL**
SELECT C.FirstName+' '+C.LastName 'Employee',
DATEPART(Month,SOH.OrderDate) 'OrderMonthNum',
PS.Name 'SubCat',
Sum(SOD.LineTotal) 'Sales',
SOH.SalesOrderNumber,
P.Name 'Product',
Sum(SOD.OrderQty) 'OrderQty',
SOD.UnitPrice,
PC.Name 'ProdCat'
FROM AdventureWorks.Person.Contact C,
AdventureWorks.HumanResources.Employee E,
AdventureWorks.Production.Product P,
AdventureWorks.Production.ProductCategory PC,
AdventureWorks.Production.ProductSubcategory PS,
AdventureWorks.Sales.SalesOrderDetail SOD,
AdventureWorks.Sales.SalesOrderHeader SOH,
AdventureWorks.Sales.SalesPerson SP
WHERE SOH.SalesOrderID = SOD.SalesOrderID
AND SOH.SalesPersonID = SP.SalesPersonID
AND SP.SalesPersonID = E.EmployeeID
AND E.ContactID = C.ContactID
AND SOD.ProductID = P.ProductID
AND P.ProductSubcategoryID = PS.ProductSubcategoryID
AND PS.ProductCategoryID = PC.ProductCategoryID
AND ((DATEPART(Year,SOH.OrderDate)=?)
AND (DATEPART(Month,SOH.OrderDate)=?) AND (SOH.SalesPersonID=?))
GROUP BY C.FirstName+' '+C.LastName, DATEPART(Month,SOH.OrderDate),
PS.Name,
SOH.SalesOrderNumber,
P.Name,
SOD.UnitPrice,
PC.Name
1. Create a dataset named SalesEmps. We'll use that as the valid values for the EmpID parameter.
The SQL that defines SalesEmps is:
**SQL**
SELECT  E.EmployeeID,  C.FirstName + N' ' + C.LastName AS Employee
FROM  HumanResources.Employee E INNER JOIN  Sales.SalesPerson SP
ON E.EmployeeID = SP.SalesPersonID INNER JOIN   Person.Contact C
ON E.ContactID = C.ContactID  ORDER BY    C.LastName, C.FirstName
1. Create three report parameters: ReportYear, ReportMonth and EmpID.
1. The valid values for the parameter ReportYear are:
![todo:image_alt_text](preparing-for-creating-table-report_1.png)
1. The valid values for the parameter ReportMonth is:
![todo:image_alt_text](preparing-for-creating-table-report_2.png)
1. The valid value for the parameter EmpID are:
![todo:image_alt_text](preparing-for-creating-table-report_3.png)
1. Map the dataset parameters to report parameters, as follow:
![todo:image_alt_text](preparing-for-creating-table-report_4.png)
