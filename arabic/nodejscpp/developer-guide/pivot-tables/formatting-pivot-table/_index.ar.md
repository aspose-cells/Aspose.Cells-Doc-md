---
title: تنسيق جدول الدوران
type: docs
weight: 10
url: /ar/nodejs-cpp/formatting-pivot-table/
description: كيفية تنسيق الجدول المحوري باستخدام Aspose.Cells for Node.js via C++.
keywords: تنسيق جدول البيانات المحورية.
---

## **مظهر جدول الدوران**

كيفية إنشاء جدول دوران يشرح كيفية إنشاء جدول دوران بسيط. يوضح هذا المقال كيفية تخصيص مظهر جدول الدوران عن طريق تعيين مختلف الخصائص:

- خيارات تنسيق جدول الدوران
- خيارات تنسيق حقول الجدول الدوران
- خيارات تنسيق حقل البيانات

### **كيفية تعيين خيارات تنسيق جدول البيانات المحورية**

تتحكم فئة [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/) في الجدول الدوري الكلي ويمكن تهيئتها بعدة طرق.

#### **كيفية تعيين نوع التنسيق التلقائي**

يقدم Microsoft Excel عددًا من تنسيقات التقارير المسبقة. يدعم Aspose.Cells for Node.js via C++ أيضًا هذه الخيارات التنسيقية. للوصول إليها:

1. قم بتعيين [**PivotTable.setIsAutoFormat(value)**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#setIsAutoFormat-boolean-) إلى **صحيح**.
1. قم بتعيين خيار التنسيق من تعداد [**PivotTableAutoFormatType**](https://reference.aspose.com/cells/nodejs-cpp/pivottableautoformattype/) .

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-SettingAutoFormat-1.js" >}}

#### **كيفية تعيين خيارات التنسيق**

تُظهر العينة البرمجية أدناه كيفية تنسيق جدول الدوري لإظهار المجاميع الكلية للصفوف والأعمدة، وكيفية تعيين ترتيب حقل التقرير. كما تُظهر العينة أيضًا كيفية تعيين سلسلة مخصصة لقيم خالية.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-SettingFormatOptions-1.js" >}}

#### **تنسيق المظهر يدويًا**

لتنسيق كيفية ظهور تقرير الجدول المحوري يدويًا، بدلاً من استخدام تنسيقات التقرير المُعدة مسبقًا، استخدم الأساليب [**PivotTable.formatAll(style)**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#formatAll-style-) و [**PivotTable.format(row, column, style)**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#format-number-number-style-). أنشئ كائن نمط للتنسيق المطلوب، على سبيل المثال:

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-FormattingLook-1.js" >}}

### **كيفية تعيين خيارات تنسيق حقل الجدول المحوري**

تمثل فئة [**PivotField**](https://reference.aspose.com/cells/nodejs-cpp/pivotfield/) حقلًا في جدول دور ، ويمكن تهيئته بعدة طرق. تُظهر العينة البرمجية أدناه كيفية:

- الوصول إلى حقول الصفوف.
- ضبط المجاميع الفرعية.
- ضبط الترتيب التلقائي.
- ضبط الإظهار التلقائي.

#### **كيفية تعيين تنسيق حقول الصف/العمود/الصفحة**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-SettingPageFieldFormat-1.js" >}}

### **كيفية تعيين تنسيق حقول البيانات**

تُظهر العينة البرمجية أدناه كيفية تعيين تنسيقات العرض وتنسيق الأرقام لحقول البيانات.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-SettingDataFieldFormat-1.js" >}}

### **كيفية مسح حقول الجدول المحوري**

تحتوي فئة [**PivotFieldCollection**](https://reference.aspose.com/cells/nodejs-cpp/pivotfieldcollection/) على طريقة تسمى [**clear()**](https://reference.aspose.com/cells/nodejs-cpp/pivotfieldcollection/#clear--) تتيح لك مسح حقول الجدول الدوري. استخدمها عندما ترغب في مسح جميع حقول الجدول الدوري في المناطق، على سبيل المثال، الصفحة، العمود، الصف أو البيانات.
يظهر الكود العيني أدناه كيفية مسح جميع حقول الجدول المفصلي في مجال البيانات.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-ClearPivotFields-1.js" >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
