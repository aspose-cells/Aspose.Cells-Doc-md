---
title: Tablo Raporu Oluşturmaya Hazırlanma
type: docs
weight: 10
url: /tr/reportingservices/preparing-for-creating-table-report/
---
 Tablolu bir rapor oluşturmadan önce, kullanıcı önce veri kaynaklarını, veri kümelerini ve rapor parametrelerini (isteğe bağlı) aşağıda açıklandığı gibi oluşturmalıdır.[Veri Kaynakları ve Sorgular](/cells/tr/reportingservices/data-sources-and-queries/).

Aşağıda, SQL Server Reporting Services 2005 ile birlikte gelen AdventureWorks örnek veritabanını kullanıyoruz.

1. EmpSalesDetail adlı bir veri kümesi oluşturun. Bunu tablonun veri kaynağı olarak kullanacağız. Veri kümesinin üç parametresi vardır: ReportYear, ReportMonth ve EmpID.
 EmpSalesDetail'i tanımlayan SQL aşağıdaki gibidir:

**SQL**

{{< highlight "csharp" >}}

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

1. SalesEmps adlı bir veri kümesi oluşturun. EmpID parametresi için geçerli değerler olarak bunu kullanacağız.
 SalesEmps'i tanımlayan SQL şudur:

**SQL**

{{< highlight "csharp" >}}

 SELECT  E.EmployeeID,  C.FirstName + N' ' + C.LastName AS Employee

FROM  HumanResources.Employee E INNER JOIN  Sales.SalesPerson SP

ON E.EmployeeID = SP.SalesPersonID INNER JOIN   Person.Contact C

ON E.ContactID = C.ContactID  ORDER BY    C.LastName, C.FirstName



{{< /highlight >}}

1.  Üç rapor parametresi oluşturun: ReportYear, ReportMonth ve EmpID.
 1. ReportYear parametresi için geçerli değerler şunlardır:

![yapılacaklar:resim_alternatif_metin](preparing-for-creating-table-report_1.png)




1. ReportMonth parametresi için geçerli değerler:

![yapılacaklar:resim_alternatif_metin](preparing-for-creating-table-report_2.png)




1.  EmpID parametresi için geçerli değerler şunlardır:

![yapılacaklar:resim_alternatif_metin](preparing-for-creating-table-report_3.png)




1.  Veri kümesi parametrelerini aşağıdaki gibi rapor parametreleriyle eşleyin:

![yapılacaklar:resim_alternatif_metin](preparing-for-creating-table-report_4.png)
