---
title: إنشاء مصادر بيانات واستعلامات جديدة
type: docs
weight: 20
url: /ar/reportingservices/creating-new-data-sources-and-queries/
---

{{% alert color="primary" %}} 

يتكامل Aspose.Cells.Report.Designer مع MS Query ويستخدم MS Query كأداة لإنشاء مصادر البيانات والاستعلامات. لإنشاء مصدر بيانات واستعلام جديد في Aspose.Cells.Report.Designer، اتبع الخطوات التالية: 

{{% /alert %}} 

لإنشاء مصدر بيانات واستعلام جديد في Aspose.Cells.Report.Designer:

1. افتح Microsoft Excel.
1. انقر على **بناء مجموعة البيانات** في شريط أدوات Aspose.Cells.Report.Designer: 

![todo:image_alt_text](creating-new-data-sources-and-queries_1.png)


جميع مصادر البيانات والاستعلامات مدرجة في مربع الحوار. 

1. عقدة مصدر البيانات: 

![todo:image_alt_text](creating-new-data-sources-and-queries_2.png)

1. عقدة مجموعة البيانات: 

![todo:image_alt_text](creating-new-data-sources-and-queries_3.png)

1. حدد عقدة الجذر الخاصة بالشجرة.
1. انقر على **إضافة**. 

   **إضافة مصادر البيانات ومجموعات البيانات** 

![todo:image_alt_text](creating-new-data-sources-and-queries_4.png)




1. في مربع الحوار، اسم الاتصال بمصدر البيانات **SqlServer** واسم مجموعة البيانات **EmpsSalesDetail**.
1. انقر فوق **التالي**. 

   **إضافة مجموعات البيانات ومصادر البيانات** 

![todo:image_alt_text](creating-new-data-sources-and-queries_5.png)



يبدأ Aspose.Cells.Report.Designer استعلام Microsoft Query. 

1. في مربع حوار اختيار مصدر البيانات، حدد **مصدر بيانات جديد**.
1. انقر على **موافق**.
   يمكنك أيضًا تحديد مصدر بيانات موجود. 

   **اختيار مصدر البيانات** 

![todo:image_alt_text](creating-new-data-sources-and-queries_6.png)




1. أدخل اسم مصدر البيانات وحدد SQL Server من قائمة السائقين قاعدة البيانات المنسدلة.
1. انقر على **الاتصال**. 

   **إنشاء مصدر بيانات جديد** 

![todo:image_alt_text](creating-new-data-sources-and-queries_7.png)




1. في مربع حوار تسجيل الدخول إلى SQL Server، حدد القيمة المناسبة لكل عنصر.
   على سبيل المثال، قم بتعيين الخادم إلى محلي، حدد قاعدة بيانات AdventureWorks وحدد **استخدام اتصال موثوق**.
1. انقر على **موافق**. 

   **تسجيل الدخول إلى خادم SQL** 

![todo:image_alt_text](creating-new-data-sources-and-queries_8.png)




1. انقر على **موافق**. 

   **يرجى ملاحظة أننا الآن قمنا بتسجيل الدخول إلى خادم SQL** 

![todo:image_alt_text](creating-new-data-sources-and-queries_9.png)



يظهر مصدر البيانات الجديد في مربع حوار **اختيار مصدر البيانات**. 

1. حدد مصدر البيانات الجديد. 

   **مصدر البيانات الجديد** 

![todo:image_alt_text](creating-new-data-sources-and-queries_10.png)




1. انقر على **موافق** لفتح الاستعلامات المايكروسوفت.
1. لإنشاء استعلام في استعلام المايكروسوفت، راجع مساعد الاستعلام المايكروسوفت. في العينة التالية، نقوم بإنشاء استعلام بمعلمات. 

   **بناء استعلام** 

![todo:image_alt_text](creating-new-data-sources-and-queries_11.png)



الاستعلام الخاص بـ ما يلي: 

**SQL**

{{< highlight csharp >}}

 SELECT C.FirstName + ' ' + C.LastName AS Employee,

DATEPART(Month, SOH.OrderDate) AS OrderMonthNum,

PS.Name AS SubCat,

SUM(SOD.LineTotal) AS Sales,

SOH.SalesOrderNumber,

P.Name AS Product,

SUM(SOD.OrderQty) AS OrderQty,

SOD.UnitPrice,

PC.Name AS ProdCat

FROM  Sales.SalesOrderHeader SOH ,

Sales.SalesOrderDetail SOD ,

Sales.SalesPerson SP,

HumanResources.Employee E,

Person.Contact C,

Production.Product P,

Production.ProductSubcategory PS ,

Production.ProductCategory PC

where SOH.SalesOrderID = SOD.SalesOrderID

and SOH.SalesPersonID = SP.SalesPersonID

and SP.SalesPersonID = E.EmployeeID

and E.ContactID = C.ContactID

and SOD.ProductID = P.ProductID

and P.ProductSubcategoryID = PS.ProductSubcategoryID

and PS.ProductCategoryID = PC.ProductCategoryID

and  (DATEPART(Year, SOH.OrderDate) =  ?)

AND (DATEPART(Month, SOH.OrderDate) =  ?)

AND (SOH.SalesPersonID =?)

GROUP BY    C.FirstName + ' ' + C.LastName,

DATEPART(Month, SOH.OrderDate), SOH.SalesOrderNumber,

P.Name, PS.Name, SOD.UnitPrice, PC.Name



{{< /highlight >}}


الاستعلام يحتوي على ثلاث معلمات: سن التقرير، شهر التقرير ومعرف الموظف.

1. من قائمة **ملف** في Microsoft Query، حدد **العودة إلى Aspose.Cells.Report.Designer**. 

   **العودة إلى مصمم التقرير** 

![todo:image_alt_text](creating-new-data-sources-and-queries_12.png)



يتم إدراج مصدر البيانات والاستعلام المنشأ أعلاه في مربع الحوار. 

1. انقر فوق مصدر البيانات **SqlServer** لعرض معلوماته المفصلة. 

   **مصدر البيانات الجديد** 

![todo:image_alt_text](creating-new-data-sources-and-queries_13.png)




1. انقر على استعلام EmpSalesDetails لعرض معلوماته المفصلة. 

   **انقر على علامة التبويب SQL لعرض SQL لللاستعلام** 

![todo:image_alt_text](creating-new-data-sources-and-queries_14.png)



**انقر على علامة التبويب الأعمدة لعرض أعمدة الاستعلام** 

![todo:image_alt_text](creating-new-data-sources-and-queries_15.png)



**انقر فوق علامة تبويب المعلمات لعرض معلمات الاستعلام** 

![todo:image_alt_text](creating-new-data-sources-and-queries_16.png)



