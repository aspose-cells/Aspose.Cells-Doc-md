---
title: تعيين مصدر البيانات للمخطط
description: تعرف على مصادر البيانات المختلفة المدعومة بواسطة Aspose.Cells for .NET. سيقوم دليلنا بتوجيهك خلال أنواع مختلفة من مصادر البيانات المتاحة وسيظهر لك كيفية الاتصال واسترداد البيانات منها لملء أوراق العمل الخاصة بك.
keywords: Aspose.Cells for .NET, تخطيط، تنسيق البيانات، علامات، ألوان، خطوط، مظهر، سهولة الاستخدام.
linktitle: مصدر البيانات
type: docs
weight: 10
url: /ar/net/data-formatting-in-charts/
---

في مواضيعنا السابقة، قدمنا ​​بالفعل العديد من الأمثلة لتوضيح كيف يمكنك تعيين مصدر بيانات لرسم بياني ولكن في هذا الموضوع، سنقدم المزيد من التفاصيل حول أنواع البيانات التي يمكن تعيينها للرسم البياني.

## **ضبط بيانات الرسم البياني**

هناك نوعان من البيانات التي يتعين التعامل معها أثناء العمل على الرسوم البيانية باستخدام Aspose.Cells وهي كما يلي:

- بيانات الرسم البياني.
- بيانات الفئة.

### **بيانات الرسم البياني**

بيانات الرسم البياني هي البيانات التي نستخدمها كمصدر لبناء الرسوم البيانية الخاصة بنا. يمكننا إضافة مجموعة من الخلايا (تحتوي على بيانات الرسم البياني) عن طريق استدعاء [**SeriesCollection**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) إلى [**Add**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection/methods/add).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsData-1.cs" >}}

### **بيانات الفئة**

تُستخدم بيانات الفئة لوسم بيانات الرسم البياني ويمكن إضافتها إلى [**SeriesCollection**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) باستخدام خاصية [**CategoryData**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection/properties/categorydata). يتم تقديم مثال كامل أدناه لتوضيح استخدام بيانات الرسم البياني والفئة. بعد تنفيذ رمز المثال أعلاه، سيتم إضافة رسم بياني للأعمدة إلى ورقة العمل كما هو موضح أدناه.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingCategoryData-1.cs" >}}

## **مواضيع متقدمة**
- [تغيير مصدر البيانات للرسم البياني إلى ورقة العمل الوجهة أثناء نسخ الصفوف أو النطاق](/cells/ar/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [إنشاء رسوم بيانية ديناميكية](/cells/ar/net/create-dynamic-charts/)
- [طريقة سهلة لضبط الرسوم البيانية باستخدام طريقة Chart.SetChartDataRange](/cells/ar/net/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [البحث عن نوع قيم X وY لنقاط في سلسلة الرسم البياني](/cells/ar/net/find-type-of-x-and-y-values-of-points-in-chart-series/)
