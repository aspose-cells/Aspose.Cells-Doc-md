---
title: تنسيق جدول الدوران
type: docs
weight: 10
url: /ar/python-net/formatting-pivot-table/
description: كيفية تنسيق جدول البيانات المحورية باستخدام Aspose.Cells لـ Python via .NET.
keywords: تنسيق جدول البيانات المحورية.
---

## **مظهر جدول الدوران**

كيفية إنشاء جدول دوران يشرح كيفية إنشاء جدول دوران بسيط. يوضح هذا المقال كيفية تخصيص مظهر جدول الدوران عن طريق تعيين مختلف الخصائص:

- خيارات تنسيق جدول الدوران
- خيارات تنسيق حقول الجدول الدوران
- خيارات تنسيق حقل البيانات

### **كيفية تعيين خيارات تنسيق جدول البيانات المحورية**

تتحكم فئة [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/) في الجدول الدوري الكلي ويمكن تهيئتها بعدة طرق.

#### **كيفية تعيين نوع التنسيق التلقائي**

يقدم Microsoft Excel عددًا من تنسيقات التقارير المُعدة مُسبقًا مختلفة. تدعم Aspose.Cells لـ Python via .NET هذه الخيارات التنسيقية أيضًا. للوصول إليها:

1. قم بتعيين [**PivotTable.is_auto_format**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_auto_format/) إلى **صحيح**.
1. قم بتعيين خيار التنسيق من تعداد [**PivotTableAutoFormatType**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottableautoformattype/) .

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingAutoFormat-1.py" >}}

#### **كيفية تعيين خيارات التنسيق**

تُظهر العينة البرمجية أدناه كيفية تنسيق جدول الدوري لإظهار المجاميع الكلية للصفوف والأعمدة، وكيفية تعيين ترتيب حقل التقرير. كما تُظهر العينة أيضًا كيفية تعيين سلسلة مخصصة لقيم خالية.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingFormatOptions-1.py" >}}

#### **تنسيق المظهر يدويًا**

لتنسيق كيفية ظهور تقرير الجدول المحوري يدويًا، بدلاً من استخدام تنسيقات التقرير المُعدة مسبقًا، استخدم الأساليب [**PivotTable.format_all(style)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/format_all/) و [**PivotTable.format(row, column, style)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/format/). أنشئ كائن نمط للتنسيق المطلوب، على سبيل المثال:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-FormattingLook-1.py" >}}

### **كيفية تعيين خيارات تنسيق حقل الجدول المحوري**

تمثل فئة [**PivotField**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/) حقلًا في جدول دور ، ويمكن تهيئته بعدة طرق. تُظهر العينة البرمجية أدناه كيفية:

- الوصول إلى حقول الصفوف.
- ضبط المجاميع الفرعية.
- ضبط الترتيب التلقائي.
- ضبط الإظهار التلقائي.

#### **كيفية تعيين تنسيق حقول الصف/العمود/الصفحة**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingPageFieldFormat-1.py" >}}

### **كيفية تعيين تنسيق حقول البيانات**

تُظهر العينة البرمجية أدناه كيفية تعيين تنسيقات العرض وتنسيق الأرقام لحقول البيانات.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingDataFieldFormat-1.py" >}}

### **كيفية مسح حقول الجدول المحوري**

تحتوي فئة [**PivotFieldCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfieldcollection/) على طريقة تسمى [**clear()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfieldcollection/clear/#) تتيح لك مسح حقول الجدول الدوري. استخدمها عندما ترغب في مسح جميع حقول الجدول الدوري في المناطق، على سبيل المثال، الصفحة، العمود، الصف أو البيانات.
يظهر الكود العيني أدناه كيفية مسح جميع حقول الجدول المفصلي في مجال البيانات.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-ClearPivotFields-1.py" >}}
