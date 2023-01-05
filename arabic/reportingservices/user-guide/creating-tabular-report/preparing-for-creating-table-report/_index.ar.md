---
title: التحضير لإنشاء تقرير الجدول
type: docs
weight: 10
url: /ar/reportingservices/preparing-for-creating-table-report/
---
 قبل إنشاء تقرير جدولي ، يجب على المستخدم أولاً إنشاء مصادر البيانات ومجموعات البيانات ومعلمات التقرير (اختياري) كما هو موضح في[مصادر البيانات والاستعلامات](/cells/ar/reportingservices/data-sources-and-queries/).

أدناه ، نستخدم نموذج قاعدة بيانات AdventureWorks التي تأتي مع SQL Server Reporting Services 2005.

1. قم بإنشاء مجموعة بيانات باسم EmpSalesDetail. سنستخدم هذا كمصدر بيانات الجدول. تحتوي مجموعة البيانات على ثلاث معلمات: ReportYear و ReportMonth و EmpID.
 SQL الذي يعرف EmpSalesDetail هو كما يلي:

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

1. قم بإنشاء مجموعة بيانات باسم SalesEmps. سنستخدم ذلك كقيم صالحة لمعلمة EmpID.
 SQL الذي يعرف SalesEmps هو:

**SQL**

{{< highlight "csharp" >}}

 SELECT  E.EmployeeID,  C.FirstName + N' ' + C.LastName AS Employee

FROM  HumanResources.Employee E INNER JOIN  Sales.SalesPerson SP

ON E.EmployeeID = SP.SalesPersonID INNER JOIN   Person.Contact C

ON E.ContactID = C.ContactID  ORDER BY    C.LastName, C.FirstName



{{< /highlight >}}

1.  قم بإنشاء ثلاثة معلمات للتقرير: ReportYear و ReportMonth و EmpID.
 1. القيم الصالحة لمعلمة ReportYear هي:

![ما يجب القيام به: image_بديل_نص](preparing-for-creating-table-report_1.png)




1. القيم الصالحة للمعلمة ReportMonth هي:

![ما يجب القيام به: image_بديل_نص](preparing-for-creating-table-report_2.png)




1.  القيمة الصالحة للمعلمة EmpID هي:

![ما يجب القيام به: image_بديل_نص](preparing-for-creating-table-report_3.png)




1.  قم بتعيين معلمات مجموعة البيانات لتقرير المعلمات ، على النحو التالي:

![ما يجب القيام به: image_بديل_نص](preparing-for-creating-table-report_4.png)
