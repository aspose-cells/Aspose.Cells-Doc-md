---
title: تحديد فاصل عشري مخصص للأرقام وفاصلات مجموع للورقة العمل
type: docs
weight: 100
url: /ar/java/specify-custom-number-decimal-and-group-separators-for-workbook/
description: يوضح هذا المقال كيفية تغيير فاصلة العشرية وفاصل المجموع في MS Excel وباستخدام رمز Java باستخدام واجهة برمجة التطبيقات Aspose.Cells for Java.
keywords: حدد الفاصل العشري المخصص إكسل، حدد الفاصل العشري المخصص إكسل جافا، حدد الفاصل المجموع المخصص إكسل، حدد الفاصل المجموع المخصص إكسل جافا، حدد الفاصل العشري والفاصل المجموع المخصص إكسل، حدد الفاصل العشري والفاصل المجموع المخصص إكسل جافا، تغيير فاصلة العشرية وفاصل المجموع إكسل جافا، تغيير فاصلة العشرية وفاصل المجموع إكسل، تغيير فاصلة العشرية إكسل، تغيير فاصلة العشرية إكسل جافا، تغيير فاصلة المجموع إكسل، تغيير فاصلة المجموع إكسل جافا
---

{{% alert color="primary" %}}

يمكنك في Microsoft Excel تحديد الفاصل العشري المخصص وفاصل الآلاف بدلاً من استخدام الفواصل النظامية من **خيارات Excel المتقدمة** كما هو موضح في اللقطة أدناه.

توفر Aspose.Cells الخاصية [**WorkbookSettings.setNumberDecimalSeparator()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#NumberDecimalSeparator) و[WorkbookSettings.setNumberGroupSeparator()](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#NumberGroupSeparator) لضبط الفواصل المخصصة لتنسيق/تحليل الأرقام.

{{% /alert %}}

## **تحديد الفواصل المخصصة باستخدام Microsoft Excel**

1. افتح **الخيارات** في علامة التبويب **الملف**.
1. افتح علامة التبويب **المتقدمة**.
1. قم بتغيير الإعدادات في قسم **خيارات التحرير**.

تُظهر اللقطة الشاشية التالية **خيارات Excel المتقدمة** وتبرز القسم الخاص بتحديد **الفواصل المخصصة**.

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)

## **تحديد الفواصل المخصصة باستخدام Aspose.Cells**

يوضح الكود النموذجي التالي كيفية تحديد الفواصل المخصصة باستخدام واجهة برمجة التطبيقات Aspose.Cells. يُحدد الفواصل العشرية وفاصلات المجموع المخصصة كنقطة وفراغ على التوالي. بحيث يتم عرض الرقم **123,456.789** كـ **123 456.789** كما هو موضح في اللقطة الشاشية التي تظهر الناتج PDF الذي تم إنشاؤه بواسطة الكود.

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SpecifyingCustomSeparators-SpecifyingCustomSeparators.java" >}}
{{< app/cells/assistant language="java" >}}
