---
title: حدد رقم عشري مخصص وفواصل المجموعات للمصنف
type: docs
weight: 100
url: /ar/java/specify-custom-number-decimal-and-group-separators-for-workbook/
description: توضح هذه المقالة كيفية تغيير فاصل الأرقام العشري والمجموعات في MS Excel وبرمز Java باستخدام Aspose.Cells for Java API.
keywords: specify custom decimal separator excel, specify custom decimal separator excel java, specify custom group separator excel, specify custom group separator excel java, specify custom decimal and group separator excel, specify custom decimal and group separator excel java, change decimal and group separator excel java, change decimal and group separator excel, change decimal separator excel, change decimal separator excel java, change group separator excel, change group separator excel java
---
{{% alert color="primary" %}}

 في Microsoft Excel ، يمكنك تحديد الفواصل العشرية المخصصة والآلاف بدلاً من استخدام فواصل النظام من**خيارات Excel المتقدمة** كما هو موضح في الصورة أدناه.

 يوفر Aspose.Cells ملف[**WorkbookSettings.setNumberDecimalSeparator ()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#NumberDecimalSeparator) و[WorkbookSettings.setNumberGroupSeparator ()](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#NumberGroupSeparator) خصائص لتعيين الفواصل المخصصة لتنسيق / تحليل الأرقام.

{{% /alert %}}

## **تحديد فواصل مخصصة باستخدام Microsoft Excel**

1.  فتح**خيارات** في ال**ملف** التبويب.
1. افتح ال**متقدم** التبويب.
1.  قم بتغيير الإعدادات في ملف**خيارات التحرير** الجزء.

تُظهر لقطة الشاشة التالية ملف**خيارات Excel المتقدمة** ويسلط الضوء على القسم لتحديد**فواصل مخصصة**.

![ما يجب القيام به: image_بديل_نص](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)

## **تحديد الفواصل المخصصة باستخدام Aspose.Cells**

 يوضح نموذج الكود التالي كيفية تحديد الفواصل المخصصة باستخدام Aspose.Cells API. وهو يحدد الرقم العشري المخصص وفواصل المجموعة كنقطة ومسافة على التوالي. إذن الرقم**123,456.789** سيتم عرضها على شكل**123 456.789** كما هو موضح في لقطة الشاشة التي توضح إخراج PDF الناتج عن الكود.

![ما يجب القيام به: image_بديل_نص](specify-custom-number-decimal-and-group-separators-for-workbook_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SpecifyingCustomSeparators-SpecifyingCustomSeparators.java" >}}
