---
title: تنسيق البيانات في الرسوم البيانية
linktitle: مصدر البيانات
type: docs
weight: 50
url: /ar/java/data-formatting-in-charts/
---
{{% alert color="primary" %}}

في موضوعاتنا السابقة ، قدمنا بالفعل العديد من الأمثلة لإثبات كيف يمكنك تعيين مصدر بيانات للمخطط الخاص بك ولكن في هذا الموضوع ، سنقدم المزيد من التفاصيل حول أنواع البيانات التي يمكن تعيينها للمخطط.

{{% /alert %}}

## **ضبط بيانات الرسم البياني**

هناك نوعان من البيانات للتعامل معها أثناء العمل على الرسوم البيانية باستخدام Aspose.Cells على النحو التالي:

- [بيانات الرسم البياني](/cells/ar/java/data-formatting-in-charts/#chart-data).
- [بيانات الفئة](/cells/ar/java/data-formatting-in-charts/#category-data).

### **بيانات الرسم البياني**

 بيانات الرسم البياني هي تلك البيانات التي نستخدمها كمصدر بيانات لبناء مخططاتنا. يمكننا إضافة نطاق من الخلايا (يحتوي على بيانات الرسم البياني) عن طريق استدعاء[**السلسلة**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) أشياء[**يضيف**](https://reference.aspose.com/cells/java/com.aspose.cells/seriescollection#add(java.lang.Object)) طريقة.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsData-SettingChartsData.java" >}}

### **بيانات الفئة**

 تُستخدم بيانات الفئة لتمييز بيانات المخطط ويمكن إضافتها إليها[**السلسلة**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) باستخدام ملف[**setCategoryData**](https://reference.aspose.com/cells/java/com.aspose.cells/seriescollection#CategoryData)طريقة.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingCategoryData-SettingCategoryData.java" >}}

**مخطط عمودي مع بيانات الرسم البياني والفئة** 

![ما يجب القيام به: image_بديل_نص](data-formatting-in-charts_1.png)

## **موضوعات مسبقة**
- [إنشاء مخططات ديناميكية](/cells/ar/java/create-dynamic-charts/)
- [طريقة سهلة لإعداد المخطط باستخدام طريقة Chart.setChartDataRange](/cells/ar/java/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [ابحث عن نوع قيم X و Y للنقاط في سلسلة المخططات](/cells/ar/java/find-type-of-x-and-y-values-of-points-in-chart-series/)
- [قم بتعيين رمز تنسيق القيم لسلسلة التخطيطات](/cells/ar/java/set-the-values-format-code-of-chart-series/)
