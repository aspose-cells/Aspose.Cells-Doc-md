---
title: العمل مع جدول الإحصائيات المحوري
type: docs
weight: 100
url: /ar/reportingservices/working-with-pivottable/
---

{{% alert color="primary" %}} 

جدول الإحصائيات المحوري هو جدول تفاعلي يلخص البيانات ويقدمها بطريقة معنوية. لا يمكن لخدمات تقرير SQL Server تصدير تقرير إلى تنسيق Microsoft Excel مع الاحتفاظ بجدول إحصائيات محوري. يضطر مستخدمو التقرير إلى إنشاء جداول إحصائيات محورية يدويًا في كل مرة يقومون فيها بتصدير تقرير الجدول المحوري من خدمات التقرير إلى Microsoft Excel. باستخدام Aspose.Cells for Reporting Services ، يمكنك تصميم جدول محوري مرة واحدة في وقت تصميم التقرير. في كل مرة يقوم فيها التقرير بالتشغيل ، يقوم Aspose.Cells for Reporting Services بتصدير التقرير إلى Microsoft Excel وتحديث البيانات في الجدول المحوري.

{{% /alert %}} 

لإنشاء تقرير جدول إحصائيات محوري:

1. أنشئ مجموعة بيانات كمصدر بيانات لجدول الإحصائيات المحوري.
   أدناه، نستخدم قاعدة البيانات العينية AdventureWorks المرفقة مع خدمات تقرير SQL Server 2005 وننشئ مجموعة بيانات بالاسم "المبيعات".
   SQL لمجموعة البيانات هو كما يلي: 

**SQL**

{{< highlight csharp >}}

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

يرجى الرجوع إلى [مصادر البيانات والاستعلامات](/cells/ar/reportingservices/data-sources-and-queries/) لمعرفة المزيد حول كيفية إنشاء مصدر بيانات ومجموعة بيانات باستخدام Aspose.Cells.Report.Designer.

{{% /alert %}} 

1. أنشئ تقرير جدول وفقًا للتعليمات في [إنشاء تقرير جدولي](/cells/ar/reportingservices/creating-tabular-report/)، كما هو موضح أدناه.
   الجدول سيكون مصدر البيانات للجدول المحوري. 

![todo:image_alt_text](working-with-pivottable_1.png)




1. في Microsoft Excel، من القائمة **إدراج**، حدد **اسم** ثم **تعريف**.
1. حدد اسمًا مثل 'مبيعات'.
   نطاق الاسم يبدأ من الخلية الأولى لعنوان الرأس وينتهي في آخر خلية صف بيانات الجدول كما هو موضح أدناه. 

![todo:image_alt_text](working-with-pivottable_2.png)




1. انقر على **موافق** لإنهاء.
1. إنشاء ورقة جديدة للجدول المحوري.
1. من القائمة **بيانات**، حدد **تقرير الجدول المحوري والرسوم البيانية المحورية** لإضافة جدول محوري.
   يتم عرض مربع حوار.
1. حدد **قائمة Excel لأوفيس مايكروسوفت أو قاعدة بيانات** كمصدر بيانات و**جدول محوري** كنوع تقرير.
1. انقر على **التالي** للمتابعة. 

![todo:image_alt_text](working-with-pivottable_3.png)




1. في مربع الحوار، أدخل 'مبيعات'، الاسم الذي قمت بتعريفه أعلاه.
1. انقر على **التالي** للمتابعة. 

![todo:image_alt_text](working-with-pivottable_4.png)




1. انقر على **إنهاء**. 

![todo:image_alt_text](working-with-pivottable_5.png)




1. تصميم الجدول المحوري في Excel. 

![todo:image_alt_text](working-with-pivottable_6.png)



يتم عرض الجدول المحوري المصمم أدناه. 

![todo:image_alt_text](working-with-pivottable_7.png)




1. انقر بزر الماوس الأيمن على الجدول المحوري وحدد **خيارات الجدول**.
1. تأكد من اختيار **تحديث على الفتح**. 

![todo:image_alt_text](working-with-pivottable_8.png)




1. حفظ التقرير ونشره إلى خادم التقارير.
1. تصدير التقرير من خادم التقارير.
   يتم عرض النتيجة أدناه. 

![todo:image_alt_text](working-with-pivottable_9.png)
