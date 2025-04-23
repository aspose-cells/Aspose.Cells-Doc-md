---
title: تنسيق جدول الدوران
type: docs
weight: 10
url: /ar/net/formatting-pivot-table/
---

## **مظهر جدول الدوران**

كيفية إنشاء جدول دوران يشرح كيفية إنشاء جدول دوران بسيط. يوضح هذا المقال كيفية تخصيص مظهر جدول الدوران عن طريق تعيين مختلف الخصائص:

- خيارات تنسيق جدول الدوران
- خيارات تنسيق حقول الجدول الدوران
- خيارات تنسيق حقل البيانات

### **تعيين خيارات تنسيق جدول الدوران**

تتحكم فئة [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) في الجدول الدوري الكلي ويمكن تهيئتها بعدة طرق.

#### **تعيين نوع التنسيق التلقائي**

تقدم Microsoft Excel عددًا من تنسيقات التقارير الجاهزة المختلفة. تدعم Aspose.Cells هذه الخيارات التنسيقية أيضًا. للوصول إليها:

1. قم بتعيين [**PivotTable.IsAutoFormat**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isautoformat) إلى **صحيح**.
1. قم بتعيين خيار التنسيق من تعداد [**PivotTableAutoFormatType**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottableautoformattype) .

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingAutoFormat-1.cs" >}}

#### **ضبط خيارات التنسيق**

تُظهر العينة البرمجية أدناه كيفية تنسيق جدول الدوري لإظهار المجاميع الكلية للصفوف والأعمدة، وكيفية تعيين ترتيب حقل التقرير. كما تُظهر العينة أيضًا كيفية تعيين سلسلة مخصصة لقيم خالية.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingFormatOptions-1.cs" >}}

#### **تنسيق المظهر يدويًا**

لتنسيق مظهر تقرير جدول الدوري يدويًا، بدلاً من استخدام تنسيقات التقرير الجاهزة، استخدم الطرق [**PivotTable.Format()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/format) و [**PivotTable.FormatAll()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/formatall). قم بإنشاء كائن نمط لتنسيقك المرغوب، على سبيل المثال:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-FormattingLook-1.cs" >}}

### **ضبط خيارات تنسيق حقل الدوري**

تمثل فئة [**PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) حقلًا في جدول دور ، ويمكن تهيئته بعدة طرق. تُظهر العينة البرمجية أدناه كيفية:

- الوصول إلى حقول الصفوف.
- ضبط المجاميع الفرعية.
- ضبط الترتيب التلقائي.
- ضبط الإظهار التلقائي.

#### **ضبط تنسيق حقول الصف/العمود/الصفحة**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingPageFieldFormat-1.cs" >}}

### **ضبط تنسيق حقول البيانات**

تُظهر العينة البرمجية أدناه كيفية تعيين تنسيقات العرض وتنسيق الأرقام لحقول البيانات.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingDataFieldFormat-1.cs" >}}

### **مسح حقول Pivot**

تحتوي فئة [**PivotFieldCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection) على طريقة تسمى [**Clear()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection/methods/clear) تتيح لك مسح حقول الجدول الدوري. استخدمها عندما ترغب في مسح جميع حقول الجدول الدوري في المناطق، على سبيل المثال، الصفحة، العمود، الصف أو البيانات.
يظهر الكود العيني أدناه كيفية مسح جميع حقول الجدول المفصلي في مجال البيانات.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-ClearPivotFields-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
