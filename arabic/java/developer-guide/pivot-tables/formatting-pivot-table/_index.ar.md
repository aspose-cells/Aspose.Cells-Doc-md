---
title: تنسيق الجدول المحوري
type: docs
weight: 60
url: /ar/java/formatting-pivot-table/
---
## **مظهر الجدول المحوري**

[كيفية إنشاء جدول محوري](/cells/ar/java/create-pivot-table/) أظهر كيفية إنشاء جدول محوري بسيط. تذهب هذه المقالة إلى أبعد من ذلك وتناقش كيفية تخصيص مظهر الجدول المحوري عن طريق تعيين الخصائص.

### **تعيين خيارات تنسيق الجدول المحوري**

 ال[**جدول محوري**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable) تتيح لك class تعيين خيارات تنسيق متنوعة لجدول محوري.

#### **تعيين التنسيق التلقائي وأنواع PivotTableStyle**

 يوضح مثال الرمز التالي كيفية تعيين نوع التنسيق التلقائي ونوع نمط الجدول المحوري باستخدام ملف[**نوع التنسيق التلقائي**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#AutoFormatType) و[**PivotTableStyleType**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#PivotTableStyleType) الخصائص.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SetAutoFormatandPivotTableStyleTypes-SetAutoFormatandPivotTableStyleTypes.java" >}}

#### **ضبط خيارات التنسيق**

يوضح نموذج التعليمات البرمجية التالي كيفية تعيين عدد من خيارات التنسيق لتقرير الجدول المحوري ، بما في ذلك إضافة الإجماليات الكلية للصفوف والأعمدة.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SettingFormatOptions-SettingFormatOptions.java" >}}

### **تعيين خيارات تنسيق PivotFields**

بالإضافة إلى التحكم في تنسيق الجدول المحوري الكلي ، يسمح Aspose.Cells for Java بالتحكم الدقيق في تنسيق حقول الصفوف وحقول الأعمدة وحقول الصفحة.

#### **تعيين تنسيق حقول الصف والعمود والصفحة**

يوضح مثال الكود التالي كيفية الوصول إلى حقول الصف ، والوصول إلى صف معين ، وتعيين الإجماليات الفرعية ، وتطبيق الفرز التلقائي ، واستخدام خيار AutoShow.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SetRowColumnPageFieldsFormat-SetRowColumnPageFieldsFormat.java" >}}

### **ضبط تنسيق حقول البيانات**

توضح سطور التعليمات البرمجية التالية كيفية تنسيق حقول البيانات.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SettingDataFieldFormat-SettingDataFieldFormat.java" >}}

### **تعديل النمط السريع للجدول المحوري**

توضح أمثلة التعليمات البرمجية التالية كيفية تعديل النمط السريع المطبق على الجدول المحوري.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ModifyPivotTableQuickStyle-ModifyPivotTableQuickStyle.java" >}}

### **مسح الحقول المحورية**

[**مجموعة PivotFieldCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotFieldCollection) طريقة اسمه[**صافي()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotfieldcollection#clear()يمسح الحقول المحورية. استخدمه لمسح الحقول المحورية في جميع المناطق على سبيل المثال ، الصفحة أو العمود أو الصف أو البيانات.
يوضح نموذج التعليمات البرمجية أدناه كيفية مسح كافة الحقول المحورية في منطقة البيانات.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ClearPivotFields-ClearPivotFields.java" >}}

## **وظيفة التوحيد**

### **تطبيق ConsolidationFunction على حقول البيانات في Pivot Table**

 يمكن استخدام Aspose.Cells لتطبيق ConsolidationFunction على حقول البيانات (أو حقول القيمة) للجدول المحوري. في Microsoft Excel ، يمكنك النقر بزر الماوس الأيمن فوق حقل القيمة ثم تحديد**إعدادات حقل القيمة ...** الخيار ثم حدد علامة التبويب**تلخيص القيم حسب**. من هناك ، يمكنك تحديد أي دالة توحيد من اختيارك مثل المجموع ، العدد ، المتوسط ، الحد الأقصى ، الحد الأدنى ، المنتج ، العدد المميز وما إلى ذلك.

 يوفر Aspose.Cells[**التوحيد**](https://reference.aspose.com/cells/java/com.aspose.cells/ConsolidationFunction) التعداد لدعم وظائف التوحيد التالية.

- [**ConsolidationFunction.AVERAGE**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#AVERAGE)
- [**التوحيد وظيفة. العد**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#COUNT)
- [**التوحيد. COUNT_NUMS**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#COUNT_NUMS)
- [**عملية التوحيد. DISTINCT_COUNT**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#DISTINCT_COUNT)
- [**التوحيد**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#MAX)
- [**التوحيد**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#MIN)
- [**التوحيد. المنتج**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#PRODUCT)
- [**التوحيد. STD_DEV**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#STD_DEV)
- [**التوحيد. STD_DEVP**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#STD_DEVP)
- [**التوحيد SUM**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#SUM)
- [**التوحيد. VAR**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#VAR)
- [**التوحيد. VARP**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#VARP)

 الكود التالي ينطبق**متوسط** وظيفة التوحيد إلى حقل البيانات الأول (أو حقل القيمة) و**متميز** وظيفة التوحيد في حقل البيانات الثاني (أو حقل القيمة).

{{% alert color="primary" %}}

يتم دعم وظيفة دمج DistinctCount بواسطة Microsoft Excel 2013 فقط.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ConsolidationFunctions-ConsolidationFunctions.java" >}}
