---
title: وظيفة التوحيد
type: docs
weight: 20
url: /ar/java/consolidation-function/
description: قم بتطبيق وظيفة التوحيد على حقول البيانات في الجدول الدوري Pivot.
---

## **وظيفة التوحيد**

يمكن استخدام Aspose.Cells لتطبيق وظيفة التوحيد على حقول البيانات (أو حقول القيم) لجدول Pivot. في Microsoft Excel، يمكنك نقر بزر الماوس الأيمن على حقل القيم ومن ثم تحديد اختيار **إعدادات حقل القيم...** ثم تحديد علامة **تلخيص القيم بواسطة**. من هناك، يمكنك تحديد أي وظيفة توحيد تفضل مثل Sum، Count، Average، Max، Min، Product، Distinct Count، إلخ.

يوفر Aspose.Cells تعدادًا [**ConsolidationFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ConsolidationFunction) لدعم وظائف التوحيد التالية.

- ConsolidationFunction.SUM
- ConsolidationFunction.COUNT
- ConsolidationFunction.AVERAGE
- ConsolidationFunction.MAX
- ConsolidationFunction.MIN
- ConsolidationFunction.PRODUCT
- ConsolidationFunction.COUNT_NUMS
- ConsolidationFunction.STD_DEV
- ConsolidationFunction.STD_DEVP
- ConsolidationFunction.VAR
- ConsolidationFunction.VARP
- ConsolidationFunction.DISTINCT_COUNT

### **تطبيق وظيفة التوحيد على حقول البيانات لجدول الإحصائيات**

الشيفرة التالية تطبق وظيفة **AVERAGE** للحقل البياني الأول ووظيفة **STD_DEV** للحقل البياني الثاني.

يمكن تنزيل ملف المصدر وملفات الإخراج التجريبية من هنا لاختبار الشيفرة التجريبية:

[ملف إكسل المصدر](source.xlsx)

[ملف إكسل الناتج](output.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-CreatePivotTable-ConsolidationFunction.java" >}}

{{% alert color="primary" %}}

دعم وظيفة تجميع العدد المميز من قبل Microsoft Excel 2013 فقط.

{{% /alert %}}

