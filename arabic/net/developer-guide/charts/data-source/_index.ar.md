---
title: تعيين مصدر البيانات للرسم البياني
linktitle: مصدر البيانات
type: docs
weight: 10
url: /ar/net/data-formatting-in-charts/
---
في موضوعاتنا السابقة ، قدمنا بالفعل العديد من الأمثلة لإثبات كيف يمكنك تعيين مصدر بيانات للمخطط الخاص بك ولكن في هذا الموضوع ، سنقدم المزيد من التفاصيل حول أنواع البيانات التي يمكن تعيينها للمخطط.

## **ضبط بيانات الرسم البياني**

هناك نوعان من البيانات للتعامل معها أثناء العمل على الرسوم البيانية باستخدام Aspose.Cells على النحو التالي:

- بيانات الرسم البياني.
- بيانات الفئة.

### **بيانات الرسم البياني**

بيانات المخطط هي البيانات التي نستخدمها كمصدر بيانات لبناء مخططاتنا. يمكننا إضافة نطاق من الخلايا (يحتوي على بيانات الرسم البياني) عن طريق استدعاء[**السلسلة**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) أشياء[**يضيف**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection/methods/add)طريقة.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsData-1.cs" >}}

### **بيانات الفئة**

 تُستخدم بيانات الفئة لتمييز بيانات المخطط ويمكن إضافتها إليها[**السلسلة**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) باستخدام ملف[**فئة البيانات**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection/properties/categorydata)منشأه. يتم إعطاء مثال كامل أدناه لتوضيح استخدام بيانات الرسم البياني والفئة. بعد تنفيذ رمز المثال أعلاه ، ستتم إضافة مخطط عمودي إلى ورقة العمل كما هو موضح أدناه.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingCategoryData-1.cs" >}}

## **موضوعات مسبقة**
- [قم بتغيير مصدر بيانات المخطط إلى ورقة عمل الوجهة أثناء نسخ الصفوف أو النطاق](/cells/ar/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [إنشاء مخططات ديناميكية](/cells/ar/net/create-dynamic-charts/)
- [طريقة سهلة لإعداد المخطط باستخدام طريقة Chart.SetChartDataRange](/cells/ar/net/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [ابحث عن نوع قيم X و Y للنقاط في سلسلة المخططات](/cells/ar/net/find-type-of-x-and-y-values-of-points-in-chart-series/)
