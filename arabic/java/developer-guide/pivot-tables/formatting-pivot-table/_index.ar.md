---
title: تنسيق جدول الدوران
type: docs
weight: 60
url: /ar/java/formatting-pivot-table/
---

## **مظهر جدول الدوران**

[كيفية إنشاء جدول دوران](/cells/ar/java/create-pivot-table/) عرض كيفية إنشاء جدول دوران بسيط. يذهب هذا المقال أبعد ويناقش كيفية تخصيص مظهر جدول الدوران عن طريق تعيين الخصائص.

### **تعيين خيارات تنسيق جدول الدوران**

تتيح لك فئة [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable) تعيين خيارات تنسيق مختلفة لجدول الدوران.

#### **ضبط أنواع التنسيق التلقائي وأنماط جدول الإحصائيات**

المثال البرمجي التالي يوضح كيفية ضبط نوع التنسيق التلقائي ونوع أنماط جدول الإحصائيات باستخدام خصائص [**AutoFormatType**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#AutoFormatType) و [**PivotTableStyleType**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#PivotTableStyleType).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SetAutoFormatandPivotTableStyleTypes-SetAutoFormatandPivotTableStyleTypes.java" >}}

#### **ضبط خيارات التنسيق**

المثال البرمجي التالي يوضح كيفية ضبط عدد من خيارات التنسيق لتقرير جدول إحصائيات، بما في ذلك إضافة المجاميع الكبرى للصفوف والأعمدة.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SettingFormatOptions-SettingFormatOptions.java" >}}

### **ضبط خيارات تنسيق PivotFields**

بالإضافة إلى التحكم في تنسيق الجدول الإحصائي الكلي، يسمح Aspose.Cells for Java بالتحكم المكشور في التنسيق لحقول الصف، حقول العمود وحقول الصفحة.

#### **ضبط تنسيق الصفوف والأعمدة وحقول الصفحة**

المثال البرمجي التالي يوضح كيفية الوصول إلى حقول الصف، الوصول إلى صف معين، ضبط المجاميع الفرعية، تطبيق الترتيب التلقائي، واستخدام خيار autoShow.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SetRowColumnPageFieldsFormat-SetRowColumnPageFieldsFormat.java" >}}

### **ضبط تنسيق حقول البيانات**

الأسطر التالية من الكود توضح كيفية تنسيق حقول البيانات.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SettingDataFieldFormat-SettingDataFieldFormat.java" >}}

### **تعديل نمط سريع لجدول إحصائيات**

الأمثلة البرمجية التالية توضح كيفية تعديل النمط السريع المطبق على جدول إحصائيات.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ModifyPivotTableQuickStyle-ModifyPivotTableQuickStyle.java" >}}

### **مسح حقول Pivot**

[**PivotFieldCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotFieldCollection) يحتوي على طريقة تسمى [**clear()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotfieldcollection#clear--) التي تقوم بمسح حقول pivot. استخدمها لمسح حقول pivot في جميع المناطق على سبيل المثال، الصفحة، العمود، الصف، أو البيانات.
المثال البرمجي أدناه يوضح كيفية مسح جميع حقول pivot في منطقة البيانات.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ClearPivotFields-ClearPivotFields.java" >}}

## **وظيفة التوحيد**

### **تطبيق وظيفة التوحيد على حقول البيانات لجدول الإحصائيات**

يمكن استخدام Aspose.Cells لتطبيق وظيفة التوحيد على حقول البيانات (أو حقول القيم) لجدول الإحصائيات. في برنامج Microsoft Excel، يمكنك النقر بزر الماوس الأيمن على حقل القيم ثم تحديد خيار **إعدادات حقل القيم...** ومن ثم تحديد علامة التبويب **تلخيص القيم حسب**. من هناك، يمكنك تحديد أي وظيفة توحيد تفضلها مثل المجموع، العد، المتوسط، الأقصى، الأدنى، الضرب، العد المميز، إلخ.

يوفر Aspose.Cells تعدادًا [**ConsolidationFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ConsolidationFunction) لدعم وظائف التوحيد التالية.

- [**ConsolidationFunction.AVERAGE**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#AVERAGE)
- [**ConsolidationFunction.COUNT**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#COUNT)
- [**ConsolidationFunction.COUNT_NUMS**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#COUNT-NUMS)
- [**ConsolidationFunction.DISTINCT_COUNT**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#DISTINCT-COUNT)
- [**ConsolidationFunction.MAX**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#MAX)
- [**ConsolidationFunction.MIN**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#MIN)
- [**ConsolidationFunction.PRODUCT**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#PRODUCT)
- [**ConsolidationFunction.STD_DEV**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#STD-DEV)
- [**ConsolidationFunction.STD_DEVP**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#STD-DEVP)
- [**ConsolidationFunction.SUM**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#SUM)
- [**ConsolidationFunction.VAR**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#VAR)
- [**ConsolidationFunction.VARP**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#VARP)

الكود التالي يقوم بتطبيق وظيفة **المتوسط** على الحقل الأول للبيانات (أو حقل القيم) ووظيفة **العد المميز** على الحقل الثاني للبيانات (أو حقل القيم).

{{% alert color="primary" %}}

دعم وظيفة تجميع العدد المميز من قبل Microsoft Excel 2013 فقط.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ConsolidationFunctions-ConsolidationFunctions.java" >}}
{{< app/cells/assistant language="java" >}}
