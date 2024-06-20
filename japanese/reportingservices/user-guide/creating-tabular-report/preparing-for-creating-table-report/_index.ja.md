---
title: テーブルレポートの作成準備
type: docs
weight: 10
url: /ja/reportingservices/preparing-for-creating-table-report/
---

表形式のレポートを作成する前に、ユーザーは最初に[データソースとクエリ](/cells/ja/reportingservices/data-sources-and-queries/)に記載されているように、データソース、データセット、およびレポートパラメータ（オプション）を作成する必要があります。

以下では、SQL Server Reporting Services 2005 に付属の AdventureWorks サンプルデータベースを使用しています。

1. EmpSalesDetail というデータセットを作成します。これをテーブルのデータソースとして使用します。このデータセットには ReportYear、ReportMonth、EmpID の 3 つのパラメータがあります。
   EmpSalesDetail を定義する SQL は次のとおりです。 

**SQL**

{{< highlight csharp >}}

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



{{< /highlight >}}

1. SalesEmps というデータセットを作成します。これを EmpID パラメータの有効な値として使用します。
   SalesEmps を定義する SQL は次のとおりです。 

**SQL**

{{< highlight csharp >}}

 SELECT  E.EmployeeID,  C.FirstName + N' ' + C.LastName AS Employee

FROM  HumanResources.Employee E INNER JOIN  Sales.SalesPerson SP

ON E.EmployeeID = SP.SalesPersonID INNER JOIN   Person.Contact C

ON E.ContactID = C.ContactID  ORDER BY    C.LastName, C.FirstName



{{< /highlight >}}

1. ReportYear、ReportMonth、EmpID の 3 つのレポートパラメータを作成します。 
   1. パラメータ ReportYear の有効な値は次のとおりです。 

![todo:image_alt_text](preparing-for-creating-table-report_1.png)




1. パラメータ ReportMonth の有効な値は次のとおりです。 

![todo:image_alt_text](preparing-for-creating-table-report_2.png)




1. パラメータ EmpID の有効な値は次のとおりです。 

![todo:image_alt_text](preparing-for-creating-table-report_3.png)




データセットのパラメータを次のようにレポートパラメータにマッピングします。 

![todo:image_alt_text](preparing-for-creating-table-report_4.png)
