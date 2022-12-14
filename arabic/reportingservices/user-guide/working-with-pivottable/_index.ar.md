---
title: العمل مع PivotTable
type: docs
weight: 100
url: /ar/reportingservices/working-with-pivottable/
---
{{% alert color="primary" %}} 

 أ*جدول محوري* هو جدول تفاعلي يلخص البيانات ويعرضها بطريقة هادفة. لا يمكن لـ SQL Server Reporting Services تصدير تقرير إلى تنسيق Microsft Excel مع الاحتفاظ بالجدول المحوري. يتعين على المستخدمين إنشاء جداول محورية يدويًا في كل مرة يقومون فيها بتصدير تقرير جدول محوري من Reporting Services إلى Microsoft Excel. باستخدام Aspose.Cells لخدمات التقارير ، يمكنك تصميم جدول محوري مرة واحدة في وقت تصميم التقرير. في كل مرة يتم تشغيل التقرير ، يقوم Aspose.Cells الخاص بـ Reporting Services بتصدير التقرير إلى Microsoft Excel وتحديث البيانات في الجدول المحوري.

{{% /alert %}} 

لإنشاء تقرير جدول محوري:

1. أنشئ مجموعة بيانات كمصدر بيانات للجدول المحوري.
أدناه ، نستخدم نموذج قاعدة بيانات AdventureWorks التي تأتي مع SQL Server Reporting Services 2005 وإنشاء مجموعة بيانات باسم "المبيعات".
 يكون SQL لمجموعة البيانات كما يلي:

**SQL**

{{< highlight "csharp" >}}

 SELECT  PC.Name AS ProdCat,

	    PS.Name AS SubCat,

	    DATEPART(yy, SOH.OrderDate) AS OrderYear,

	    'Q' + DATENAME(qq, SOH.OrderDate) AS OrderQtr,

         SUM(SOD.UnitPrice * SOD.OrderQty) AS Sales

FROM    Production.ProductSubcategory PS INNER JOIN

         Sales.SalesOrderHeader SOH INNER JOIN

         Sales.SalesOrderDetail SOD ON SOH.SalesOrderID = SOD.SalesOrderID INNER JOIN

         Production.Product P ON SOD.ProductID = P.ProductID ON PS.ProductSubcategoryID = P.ProductSubcategoryID INNER JOIN

         Production.ProductCategory PC ON PS.ProductCategoryID = PC.ProductCategoryID

WHERE   (SOH.OrderDate BETWEEN '1/1/2002' AND '12/31/2003')

GROUP BY  DATEPART(yy, SOH.OrderDate), PC.Name, PS.Name, 'Q' + DATENAME(qq, SOH.OrderDate), PS.ProductSubcategoryID



{{< /highlight >}}



{{% alert color="primary" %}} 

 يرجى الرجوع إلى[مصادر البيانات والاستعلامات](/cells/ar/reportingservices/data-sources-and-queries/) لمعرفة المزيد حول كيفية إنشاء مصدر بيانات ومجموعة بيانات باستخدام Aspose.Cells.Report.Designer.

{{% /alert %}} 

1.  قم بإنشاء تقرير جدول وفقًا للتعليمات الموجودة في[تكوين تقرير جدولي](/cells/ar/reportingservices/creating-tabular-report/)، كما هو مبين أدناه.
 سيكون الجدول هو مصدر البيانات للجدول المحوري.

![ما يجب القيام به: image_بديل_نص](working-with-pivottable_1.png)




1.  في Microsoft Excel ، من**إدراج** القائمة ، حدد**اسم** وثم**حدد**.
1. حدد اسمًا باسم "المبيعات".
 يبدأ نطاق الاسم بالخلية الأولى من عنوان الرأس وينتهي عند الخلية الأخيرة في صف بيانات الجدول كما هو موضح أدناه.

![ما يجب القيام به: image_بديل_نص](working-with-pivottable_2.png)




1.  انقر**نعم** لانهاء.
1. قم بإنشاء ورقة جديدة للجدول المحوري.
1.  من**بيانات** القائمة ، حدد**تقرير PivotTable و PivotChart** لإضافة جدول محوري.
 يتم عرض مربع حوار.
1.  يختار**Microsoft قائمة أو قاعدة بيانات Office Excel** كمصدر بيانات و**جدول محوري** كنوع التقرير.
1.  انقر**التالي** لاستكمال.

![ما يجب القيام به: image_بديل_نص](working-with-pivottable_3.png)




1. في مربع الحوار ، أدخل "المبيعات" ، الاسم الذي حددته أعلاه.
1.  انقر**التالي** لاستكمال.

![ما يجب القيام به: image_بديل_نص](working-with-pivottable_4.png)




1.  انقر**إنهاء**. 

![ما يجب القيام به: image_بديل_نص](working-with-pivottable_5.png)




1.  صمم الجدول المحوري في Excel.

![ما يجب القيام به: image_بديل_نص](working-with-pivottable_6.png)



يتم عرض الجدول المحوري المصمم أدناه.

![ما يجب القيام به: image_بديل_نص](working-with-pivottable_7.png)




1.  انقر بزر الماوس الأيمن فوق الجدول المحوري وحدد**خيارات الجدول**.
1.  تأكد من أن**التحديث عند الفتح** تم الإختيار.

![ما يجب القيام به: image_بديل_نص](working-with-pivottable_8.png)




1. احفظ التقرير وانشره على خادم التقارير.
1. تصدير التقرير من خادم التقرير.
 النتيجة مبينة أدناه.

![ما يجب القيام به: image_بديل_نص](working-with-pivottable_9.png)
