---
title: إنشاء جدول باستخدام خطوط حدود لنطاق
type: docs
weight: 50
url: /ar/java/create-table-by-using-border-lines-for-a-range/
description: كيفية إنشاء جدول مع نطاق باستخدام خطوط حدود. يوفر Aspose.Cells for Java واجهة برمجة تطبيق بسيطة للغاية يمكن استخدامها لإضافة حدود إلى نطاق.
keywords: إنشاء جدول، نطاق إلى جدول، نطاق إلى جدول Excel، عمود Excel إلى جدول، نطاق إلى جدول بحدود، كيفية إنشاء جدول من نطاق، تحول النطاق إلى جدول، تحويل Excel النطاق إلى جدول، إنشاء جدول Excel، نطاق لجدول جافا 
---

{{% alert color="primary" %}}

في بعض الأحيان، ترغب في إنشاء جدول عن طريق إضافة خطوط حدودية لـ **المجال**/**منطقة الخلية** باستناد إلى عنوان الخلايا التي لديك. يمكنك استخدام الطريقة [**Cells.createRange**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange(int,%20int,%20boolean)) لإنشاء مجموعة من الخلايا. تُعيد الطريقة [**Cells.createRange**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange(int,%20int,%20boolean)) كائن [**Range**](https://reference.aspose.com/cells/java/com.aspose.cells/Range). يمكنك إنشاء كائن [**Style**](https://reference.aspose.com/cells/java/com.aspose.cells/Style) وتحديد الحدود (العلوية، اليسرى، السفلية، اليمنى) وفقًا للخيارات. في وقت لاحق، يمكنك الحصول على الخلايا من [**Range**](https://reference.aspose.com/cells/java/com.aspose.cells/Range) وتطبيق التنسيق المطلوب على الخلايا الخاصة بك.

{{% /alert %}}

المثال التالي يوضح كيفية إنشاء [**Range**](https://reference.aspose.com/cells/java/com.aspose.cells/Range) وتحديد حدود الخلايا المدى الزمني.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreateTableforRange-CreateTableforRange.java" >}}

بعد تشغيل الكود أعلاه، يمكننا الحصول على ملف إكسيل المولد الذي يحتوي على الجدول المنسق؛ هنا هو لقطة للملف.

![todo:image_alt_text](create-table-by-using-border-lines-for-a-range_1.png)
