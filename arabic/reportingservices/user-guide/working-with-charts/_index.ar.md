---
title: العمل مع الرسوم البيانية
type: docs
weight: 110
url: /ar/reportingservices/working-with-charts/
---
{{% alert color="primary" %}} 

 Aspose.Cells يدعم قالب التقرير Microsoft مخططات Excel. في كل مرة تقوم فيها بتنفيذ تقرير ، يتم ملء المخطط بأحدث البيانات.

{{% /alert %}} 

لإضافة مخطط إلى نموذج التقرير:

1. أولاً ، قم بإنشاء مجموعة البيانات التي ستكون مصدر البيانات للمخطط.
 أدناه ، نستخدم نموذج قاعدة بيانات AdventureWorks التي تأتي مع SQL Server Reporting Services 2005 وإنشاء مجموعة بيانات باسم Sales.
 يحدد SQL هذا مجموعة البيانات:

**SQL**

{{< highlight "csharp" >}}

 SELECT DATEPART(yy,SOH.OrderDate) 'Year',

'Q'+DATENAME(qq,SOH.OrderDate) 'Quarter',

SUM(SOD.UnitPrice*SOD.OrderQty) 'Sales'

FROMAdventureWorks.Sales.SalesOrderDetail SOD,

AdventureWorks.Sales.SalesOrderHeader SOH

WHERE SOH.SalesOrderID = SOD.SalesOrderID

AND ((DATEPART(yy,SOH.OrderDate)=2002))

GROUP BY DATEPART(yy,SOH.OrderDate), 'Q'+DATENAME(qq,SOH.OrderDate)



{{< /highlight >}}



 يرجى الرجوع إلى[مصادر البيانات والاستعلامات](/cells/ar/reportingservices/data-sources-and-queries/) لمعرفة المزيد حول كيفية إنشاء مصدر بيانات ومجموعة بيانات في Aspose.Cells.Report.Designer.

1. قم بإنشاء تقرير جدولي وفقًا للتعليمات الموجودة في[تكوين تقرير جدولي](/cells/ar/reportingservices/creating-tabular-report/) . التقرير الذي أنشأناه لهذا المثال أدناه. الجدول هو مصدر بيانات المخطط.

![ما يجب القيام به: image_بديل_نص](working-with-charts_1.png)




1.  في Microsoft Excel ، انقر فوق**إدراج** القائمة وحدد**جدول**.
1.  انقر**التالي**. 

![ما يجب القيام به: image_بديل_نص](working-with-charts_2.png)




1.  انقر على**سلسلة** التبويب.

![ما يجب القيام به: image_بديل_نص](working-with-charts_3.png)




1.  انقر**يضيف**. 

![ما يجب القيام به: image_بديل_نص](working-with-charts_4.png)




1. في مربع الحوار ، قم بتعيين قيمة السلسلة 1 (سلسلة الربع) إلى حقل البيانات الأول بالجدول.
 في العينة ، هذا هو "CompanySales! $ C $ 3: C $ 3". أول 3 دولارات كندية هو مؤشر الصف الأول من "ربع" والثاني دولار كندي 3 هو عنصر نائب لمؤشر الصف الأخير من "ربع" وسيتم استبداله بمؤشر الصف الحقيقي لبيانات الجدول في وقت العرض. عيّن تصنيفات محور الفئة (س) على "= CompanySales! $ C $ 3: $ C $ 3".

![ما يجب القيام به: image_بديل_نص](working-with-charts_5.png)




1.  انقر**يضيف** لإضافة سلسلة أخرى.
 في العينة ، أضفنا سلسلة المبيعات.
1. عيّن قيمة Series2 (سلسلة المبيعات) إلى حقل البيانات الثاني بالجدول.
في العينة "CompanySales! $ D $ 3: $ D $ 3". أول $ D $ 3 هو فهرس الصف الأول من "المبيعات" والثاني $ D $ 3 هو عنصر نائب لمؤشر الصف الأخير من "المبيعات" وسيتم استبداله بمؤشر الصف الحقيقي لبيانات الجدول في وقت العرض.
1.  انقر**التالي** لاستكمال.

![ما يجب القيام به: image_بديل_نص](working-with-charts_6.png)




1. في مربع الحوار ، قم بتعيين عنوان المخطط ومحور الفئة (س).
1.  انقر**إنهاء** لإكمال العمل.

![ما يجب القيام به: image_بديل_نص](working-with-charts_7.png)



 القالب يشبه أدناه.

![ما يجب القيام به: image_بديل_نص](working-with-charts_8.png)




1. احفظ التقرير وانشره على خادم التقارير.
1. تصدير التقرير من خادم التقرير.
 النتيجة على النحو التالي.

![ما يجب القيام به: image_بديل_نص](working-with-charts_9.png)
