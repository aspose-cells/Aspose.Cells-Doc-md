---
title: تنسيق البيانات في الرسوم البيانية
linktitle: مصدر البيانات
type: docs
weight: 50
url: /ar/java/data-formatting-in-charts/
---

{{% alert color="primary" %}}

في مواضيعنا السابقة، قدمنا ​​بالفعل العديد من الأمثلة لتوضيح كيف يمكنك تعيين مصدر بيانات لرسم بياني ولكن في هذا الموضوع، سنقدم المزيد من التفاصيل حول أنواع البيانات التي يمكن تعيينها للرسم البياني.

{{% /alert %}}

## **ضبط بيانات الرسم البياني**

هناك نوعان من البيانات التي يتعين التعامل معها أثناء العمل على الرسوم البيانية باستخدام Aspose.Cells وهي كما يلي:

- [بيانات الرسم البياني](/cells/ar/java/data-formatting-in-charts/#chart-data).
- [بيانات التصنيف](/cells/ar/java/data-formatting-in-charts/#category-data).

### **بيانات الرسم البياني**

بيانات الرسم البياني هي البيانات التي نستخدمها كمصدر بيانات لإنشاء الرسوم البيانية. يمكننا إضافة نطاق الخلايا (التي تحتوي على بيانات الرسم البياني) عن طريق استدعاء [**Add**](https://reference.aspose.com/cells/java/com.aspose.cells/seriescollection#add(java.lang.Object)) طريقة [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsData-SettingChartsData.java" >}}

### **بيانات الفئة**

تستخدم بيانات التصنيف لوضع العلامات على بيانات الرسم البياني ويمكن إضافتها إلى [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) باستخدام طريقته [**setCategoryData**](https://reference.aspose.com/cells/java/com.aspose.cells/seriescollection#CategoryData).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingCategoryData-SettingCategoryData.java" >}}

**رسم بياني للأعمدة مع بيانات الرسم البياني والتصنيف** 

![todo:image_alt_text](data-formatting-in-charts_1.png)

## **مواضيع متقدمة**
- [إنشاء رسوم بيانية ديناميكية](/cells/ar/java/create-dynamic-charts/)
- [طريقة سهلة لإعداد الرسوم البيانية باستخدام طريقة Chart.setChartDataRange](/cells/ar/java/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [البحث عن نوع قيم X وY لنقاط في سلسلة الرسم البياني](/cells/ar/java/find-type-of-x-and-y-values-of-points-in-chart-series/)
- [تعيين رمز تنسيق القيم لسلاسل الرسم البياني](/cells/ar/java/set-the-values-format-code-of-chart-series/)
