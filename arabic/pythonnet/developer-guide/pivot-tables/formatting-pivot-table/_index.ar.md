---
title: تنسيق الجدول المحوري
type: docs
weight: 10
url: /ar/net/formatting-pivot-table/
description: كيفية تنسيق الجدول المحوري مع Aspose.Cells for Python via .NET.
keywords: Format pivot table.
---
##  **مظهر الجدول المحوري**

كيفية إنشاء جدول محوري يشرح كيفية إنشاء جدول محوري بسيط. توضح هذه المقالة كيفية تخصيص مظهر الجدول المحوري عن طريق تعيين خصائص مختلفة:

- خيارات تنسيق الجدول المحوري
- خيارات تنسيق الحقول المحورية
- خيارات تنسيق حقل البيانات

###  **ضبط خيارات تنسيق الجدول المحوري**

 ال[**جدول محوري**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/)يتحكم الفصل في الجدول المحوري الإجمالي ويمكن تنسيقه بعدة طرق.

####  **ضبط نوع التنسيق التلقائي**

Microsoft يقدم Excel عددًا من تنسيقات التقارير المختلفة المعدة مسبقًا. Aspose.Cells for Python via .NET يدعم خيارات التنسيق هذه أيضًا. للوصول إليهم:

1.  تعيين[**PivotTable.is_auto_format**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_auto_format/)إلى *صحيح**.
1.  قم بتعيين خيار التنسيق من[**PivotTableAutoFormatType**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottableautoformattype/)تعداد.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingAutoFormat-1.py" >}}

####  **ضبط خيارات التنسيق**

يوضح نموذج التعليمات البرمجية أدناه كيفية تنسيق الجدول المحوري لإظهار الإجماليات الكلية للصفوف والأعمدة، وكيفية تعيين ترتيب حقول التقرير. ويوضح أيضًا كيفية تعيين سلسلة العميل للقيم الخالية.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingFormatOptions-1.py" >}}

####  **تنسيق الشكل والمظهر يدويًا**

لتنسيق شكل تقرير الجدول المحوري يدويًا، بدلاً من استخدام تنسيقات التقارير المعدة مسبقًا، استخدم الملف[**PivotTable.format_all(نمط)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/format_all/) و[**PivotTable.format (الصف والعمود والنمط)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/format/)طُرق. قم بإنشاء كائن نمط للتنسيق المطلوب، على سبيل المثال:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-FormattingLook-1.py" >}}

###  **ضبط خيارات تنسيق الحقل المحوري**

 ال[**PivotField**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/)تمثل الفئة حقلاً في جدول محوري ويمكن تنسيقها بعدة طرق. يوضح نموذج التعليمات البرمجية أدناه كيفية:

- الوصول إلى حقول الصف.
- تحديد المجاميع الفرعية.
- إعداد الفرز التلقائي.
- ضبط العرض التلقائي.

####  **ضبط تنسيق حقول الصف/العمود/الصفحة**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingPageFieldFormat-1.py" >}}

###  **ضبط تنسيق حقول البيانات**

يوضح نموذج التعليمات البرمجية أدناه كيفية تعيين تنسيقات العرض وتنسيق الأرقام لحقول البيانات.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingDataFieldFormat-1.py" >}}

###  **مسح الحقول المحورية**

 ال[**PivotFieldCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfieldcollection/) لديه طريقة اسمها[**clear()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfieldcollection/clear/#)الذي يسمح لك بمسح الحقول المحورية. استخدمه عندما تريد مسح كافة الحقول المحورية في المناطق، على سبيل المثال، الصفحة أو العمود أو الصف أو البيانات.
يوضح نموذج التعليمات البرمجية أدناه كيفية مسح كافة الحقول المحورية في منطقة البيانات.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-ClearPivotFields-1.py" >}}
