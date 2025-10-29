---
title: تعيين مصدر البيانات للمخطط
description: تعرف على مصادر البيانات المختلفة المدعومة بواسطة Aspose.Cells للبايثون via .NET. سيرشدك دليلنا خلال أنواع مصادر البيانات المختلفة وكيفية الاتصال بها واسترجاع البيانات منها لملء أوراق العمل الخاصة بك.
keywords: Aspose.Cells للبايثون via .NET، رسم بياني، تنسيق البيانات، التسميات، الألوان، الخطوط، المظهر، الاستخدام.
linktitle: مصدر البيانات
type: docs
weight: 10
url: /ar/python-net/data-formatting-in-charts/
---

في مواضيعنا السابقة، قدمنا ​​بالفعل العديد من الأمثلة لتوضيح كيف يمكنك تعيين مصدر بيانات لرسم بياني ولكن في هذا الموضوع، سنقدم المزيد من التفاصيل حول أنواع البيانات التي يمكن تعيينها للرسم البياني.

## **ضبط بيانات الرسم البياني**

هناك نوعان من البيانات التي يجب التعامل معها عند العمل على الرسوم البيانية باستخدام Aspose.Cells للبايثون via .NET على النحو التالي:

- بيانات الرسم البياني.
- بيانات الفئة.

### **بيانات الرسم البياني**

بيانات الرسم البياني هي البيانات التي نستخدمها كمصدر لبناء الرسوم البيانية الخاصة بنا. يمكننا إضافة مجموعة من الخلايا (تحتوي على بيانات الرسم البياني) عن طريق استدعاء [**SeriesCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection) إلى [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection/add).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SettingChartsData-1.py" >}}

### **بيانات الفئة**

تُستخدم بيانات الفئة لوسم بيانات الرسم البياني ويمكن إضافتها إلى [**SeriesCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection) باستخدام خاصية [**category_data**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection/category_data). يتم تقديم مثال كامل أدناه لتوضيح استخدام بيانات الرسم البياني والفئة. بعد تنفيذ رمز المثال أعلاه، سيتم إضافة رسم بياني للأعمدة إلى ورقة العمل كما هو موضح أدناه.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SettingCategoryData-1.py" >}}

## **مواضيع متقدمة**
- [تغيير مصدر البيانات للرسم البياني إلى ورقة العمل الوجهة أثناء نسخ الصفوف أو النطاق](/cells/ar/python-net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [إنشاء رسوم بيانية ديناميكية](/cells/ar/python-net/create-dynamic-charts/)
- [طريقة سهلة لضبط الرسوم البيانية باستخدام طريقة Chart.SetChartDataRange](/cells/ar/python-net/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [البحث عن نوع قيم X وY لنقاط في سلسلة الرسم البياني](/cells/ar/python-net/find-type-of-x-and-y-values-of-points-in-chart-series/)
{{< app/cells/assistant language="python-net" >}}
