---
title: إنشاء استعلامات ومصادر بيانات جديدة
type: docs
weight: 20
url: /ar/reportingservices/creating-new-data-sources-and-queries/
---
{{% alert color="primary" %}} 

 Aspose.Cells.Report.Designer يتكامل مع MS Query ويستخدم MS Query كأداة لإنشاء مصادر البيانات والاستعلامات. لإنشاء مصدر بيانات واستعلام جديدين في Aspose.Cells.Report.Designer ، اتبع الخطوات التالية :.

{{% /alert %}} 

لإنشاء مصدر بيانات واستعلام جديدين في Aspose.Cells.Report.Designer:

1. افتح Microsoft Excel.
1.  انقر**بناء مجموعة البيانات** في Aspose.Cells.Report.Designer شريط الأدوات:

![ما يجب القيام به: image_بديل_نص](creating-new-data-sources-and-queries_1.png)


يتم سرد كافة مصادر البيانات والاستعلامات في مربع الحوار.

1.  عقدة مصدر البيانات:

![ما يجب القيام به: image_بديل_نص](creating-new-data-sources-and-queries_2.png)

1.  عقدة مجموعة البيانات:

![ما يجب القيام به: image_بديل_نص](creating-new-data-sources-and-queries_3.png)

1. حدد عقدة جذر الشجرة.
1.  انقر**يضيف**. 

   **إضافة مصادر البيانات ومجموعات البيانات** 

![ما يجب القيام به: image_بديل_نص](creating-new-data-sources-and-queries_4.png)




1.  في مربع الحوار ، اتصل بمصدر البيانات**خادم قاعدة البيانات** ومجموعة البيانات**EmpsSalesDetail**.
1.  انقر**التالي**. 

   **إضافة مجموعات البيانات ومصادرها** 

![ما يجب القيام به: image_بديل_نص](creating-new-data-sources-and-queries_5.png)



 Aspose.Cells. تقرير. المصمم يبدأ Microsoft الاستعلام.

1.  في مربع الحوار اختيار مصدر البيانات ، حدد**مصدر بيانات جديد**.
1.  انقر**نعم**.
 يمكنك أيضًا تحديد مصدر بيانات موجود.

   **اختيار مصدر البيانات** 

![ما يجب القيام به: image_بديل_نص](creating-new-data-sources-and-queries_6.png)




1. أدخل اسم مصدر البيانات وحدد SQL Server من القائمة المنسدلة لبرامج تشغيل قاعدة البيانات.
1.  انقر**الاتصال**. 

   **إنشاء مصدر بيانات جديد** 

![ما يجب القيام به: image_بديل_نص](creating-new-data-sources-and-queries_7.png)




1. في مربع حوار تسجيل الدخول إلى خادم SQL ، حدد القيمة المناسبة لكل عنصر.
 على سبيل المثال ، قم بتعيين الخادم على محلي ، وحدد قاعدة بيانات AdventureWorks وحدد**استخدم اتصال موثوق**.
1.  انقر**نعم**. 

   **تسجيل الدخول إلى خادم SQL** 

![ما يجب القيام به: image_بديل_نص](creating-new-data-sources-and-queries_8.png)




1.  انقر**نعم**. 

   **لاحظ أننا الآن مسجلون الدخول إلى خادم SQL** 

![ما يجب القيام به: image_بديل_نص](creating-new-data-sources-and-queries_9.png)



يظهر مصدر البيانات الجديد في ملف**اختر مصدر البيانات** الحوار.

1.  حدد مصدر البيانات الجديد.

   **مصدر البيانات الجديد** 

![ما يجب القيام به: image_بديل_نص](creating-new-data-sources-and-queries_10.png)




1.  انقر**نعم** لفتح Microsoft الاستعلام.
1.  لتكوين استعلام في Microsoft Query ، ارجع إلى Microsoft Query Helper. في النموذج التالي ، نقوم بإنشاء استعلام مع المعلمات.

   **بناء استعلام** 

![ما يجب القيام به: image_بديل_نص](creating-new-data-sources-and-queries_11.png)



 SQL هي كما يلي:

**SQL**

{{< highlight "csharp" >}}

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


يحتوي الاستعلام على ثلاث معلمات: ReportYear و ReportMonth و EmpID.

1.  من Microsoft Query's**ملف** القائمة ، حدد**العودة إلى Aspose.Cells.Report.Designer**. 

   **العودة إلى مصمم التقرير** 

![ما يجب القيام به: image_بديل_نص](creating-new-data-sources-and-queries_12.png)



 يتم سرد مصدر البيانات والاستعلام اللذين تم إنشاؤهما أعلاه في مربع الحوار.

1.  انقر فوق مصدر البيانات**خادم قاعدة البيانات** لعرض معلوماتها التفصيلية.

   **مصدر البيانات الجديد** 

![ما يجب القيام به: image_بديل_نص](creating-new-data-sources-and-queries_13.png)




1.  انقر فوق الاستعلام EmpSalesDetails لعرض معلوماته التفصيلية.

   **انقر فوق علامة تبويب SQL لعرض SQL للاستعلام** 

![ما يجب القيام به: image_بديل_نص](creating-new-data-sources-and-queries_14.png)



**انقر فوق علامة تبويب الأعمدة لعرض أعمدة الاستعلام** 

![ما يجب القيام به: image_بديل_نص](creating-new-data-sources-and-queries_15.png)



**انقر فوق علامة التبويب المعلمات لعرض معلمات الاستعلام** 

![ما يجب القيام به: image_بديل_نص](creating-new-data-sources-and-queries_16.png)



