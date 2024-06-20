---
title: العمل مع الرسوم البيانية
type: docs
weight: 110
url: /ar/reportingservices/working-with-charts/
---

{{% alert color="primary" %}} 

يدعم قالب تقرير Aspose.Cells الرسوم البيانية في Microsoft Excel. في كل مرة تقوم فيها بتشغيل تقرير، يتم ملء الرسم البياني بأحدث البيانات. 

{{% /alert %}} 

لإضافة رسم بياني إلى قالب التقرير:

1. أولاً، قم بإنشاء مجموعة البيانات التي ستكون مصدر بيانات للرسم البياني.
   فيما يلي، نستخدم قاعدة البيانات العينية للمغامرة التي تأتي مع خدمات تقارير خادم SQL 2005 ونقوم بإنشاء مجموعة بيانات باسم المبيعات.
   يحدد هذا ال SQL المجموعة البيانات: 

**SQL**

{{< highlight csharp >}}

 SELECT DATEPART(yy,SOH.OrderDate) 'Year',

'Q'+DATENAME(qq,SOH.OrderDate) 'Quarter',

SUM(SOD.UnitPrice*SOD.OrderQty) 'Sales'

FROMAdventureWorks.Sales.SalesOrderDetail SOD,

AdventureWorks.Sales.SalesOrderHeader SOH

WHERE SOH.SalesOrderID = SOD.SalesOrderID

AND ((DATEPART(yy,SOH.OrderDate)=2002))

GROUP BY DATEPART(yy,SOH.OrderDate), 'Q'+DATENAME(qq,SOH.OrderDate)



{{< /highlight >}}



يرجى الرجوع إلى [مصادر البيانات والاستعلامات](/cells/ar/reportingservices/data-sources-and-queries/) لمعرفة المزيد حول كيفية إنشاء مصدر بيانات ومجموعة بيانات في Aspose.Cells.Report.Designer.

1. إنشاء تقرير جدولي وفقًا للتعليمات في [إنشاء تقرير جدولي](/cells/ar/reportingservices/creating-tabular-report/). الجدولة التي أنشأناها لهذا المثال موجودة أدناه. الجدول هو مصدر بيانات الرسم البياني. 

![todo:image_alt_text](working-with-charts_1.png)




1. في برنامج Microsoft Excel، انقر فوق قائمة **الإدراج** وحدد **الرسم البياني**.
1. انقر فوق **التالي**. 

![todo:image_alt_text](working-with-charts_2.png)




1. انقر على علامة التبويب **السلاسل**. 

![todo:image_alt_text](working-with-charts_3.png)




1. انقر على **إضافة**. 

![todo:image_alt_text](working-with-charts_4.png)




1. في نافذة الحوار، قم بتعيين قيمة Series1 (سلسلة الربع) إلى أول حقل بيانات في الجدول.
   في العينة، هذا هو “CompanySales!$C$3:$C$3”. $C$3 الأول هو فهرس الصف الأول لـ “Quarter” والثاني $C$3 هو علامة نهاية لفهرس “Quarter” وسيتم استبداله بفهرس الصف الحقيقي لبيانات الجدول في وقت التقديم. قم بتعيين علامات محور الفئة(X) إلى “=CompanySales!$C$3:$C$3”. 

![todo:image_alt_text](working-with-charts_5.png)




1. انقر على **إضافة** لإضافة سلسلة أخرى.
   في العينة، قمنا بإضافة سلسلة المبيعات. 
1. قم بتعيين قيمة Series2 (سلسلة المبيعات) إلى حقل البيانات الثاني في الجدول.
   في العينة هو “CompanySales!$D$3:$D$3”. $D$3 الأول هو فهرس الصف الأول لـ “Sales” والثاني $D$3 هو علامة نهاية لفهرس “Sales” وسيتم استبداله بفهرس الصف الحقيقي لبيانات الجدول في وقت التقديم. 
1. انقر على **التالي** للمتابعة. 

![todo:image_alt_text](working-with-charts_6.png)




1. في نافذة الحوار، قم بتعيين عنوان الرسم البياني ومحور الفئة(X).
1. انقر على **إنهاء** لاستكمال العمل. 

![todo:image_alt_text](working-with-charts_7.png)



يبدو النموذج على النحو التالي. 

![todo:image_alt_text](working-with-charts_8.png)




1. حفظ التقرير ونشره إلى خادم التقارير.
1. تصدير التقرير من خادم التقارير.
   النتيجة كما هو موضح أدناه. 

![todo:image_alt_text](working-with-charts_9.png)
