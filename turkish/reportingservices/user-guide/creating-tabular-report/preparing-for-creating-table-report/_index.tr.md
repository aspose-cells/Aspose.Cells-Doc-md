---
title: Tablo Raporu Oluşturulması için Hazırlık
type: docs
weight: 10
url: /tr/reportingservices/preparing-for-creating-table-report/
---

Tablo raporu oluşturmadan önce kullanıcı, ilk olarak [Veri Kaynakları ve Sorgular](/cells/tr/reportingservices/data-sources-and-queries/) bölümünde açıklanan şekilde veri kaynakları, veri setleri ve rapor parametrelerini (isteğe bağlı) oluşturmalıdır.

Aşağıda, SQL Server Raporlama Servisleri 2005 ile birlikte sevk edilen AdventureWorks örnek veritabanını kullanıyoruz.

1. EmpSalesDetail adında bir veri seti oluşturun. Bunu tablonun veri kaynağı olarak kullanacağız. Veri setinde üç parametre bulunmaktadır: RaporYılı, RaporAyı ve EmpID.
   EmpSalesDetail'i tanımlayan SQL şu şekildedir: 

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

1. SalesEmps adında bir veri seti oluşturun. Bunu EmpID parametresi için geçerli değerler olarak kullanacağız.
   SalesEmps'i tanımlayan SQL şudur: 

**SQL**

{{< highlight csharp >}}

 SELECT  E.EmployeeID,  C.FirstName + N' ' + C.LastName AS Employee

FROM  HumanResources.Employee E INNER JOIN  Sales.SalesPerson SP

ON E.EmployeeID = SP.SalesPersonID INNER JOIN   Person.Contact C

ON E.ContactID = C.ContactID  ORDER BY    C.LastName, C.FirstName



{{< /highlight >}}

1. ReportYear, ReportMonth ve EmpID olmak üzere üç rapor parametresi oluşturun. 
   1. ReportYear parametresi için geçerli değerler: 

![todo:image_alt_text](preparing-for-creating-table-report_1.png)




1. ReportMonth parametresi için geçerli değerler: 

![todo:image_alt_text](preparing-for-creating-table-report_2.png)




1. EmpID parametresi için geçerli değer: 

![todo:image_alt_text](preparing-for-creating-table-report_3.png)




1. Veri seti parametrelerini rapor parametrelerine aşağıdaki gibi eşleyin: 

![todo:image_alt_text](preparing-for-creating-table-report_4.png)
