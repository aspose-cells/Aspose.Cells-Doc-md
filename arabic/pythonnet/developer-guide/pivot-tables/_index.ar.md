---
title: إدراج جدول محوري
linktitle: جداول الدوران
type: docs
weight: 160
url: /ar/python-net/create-pivot-table/
description: إنشاء وتنسيق جدول دوران بواسطة Aspose.Cells for Python via .NET.
keywords: إنشاء جدول دوران، إدراج جدول دوران، تنسيق جدول دوران.
---

## **إنشاء جدول محوري**

من الممكن استخدام Aspose.Cells for Python via .NET لإضافة جداول دوران إلى جداول البيانات برمجياً.

### **نموذج كائن جدول الدوران**

توفر Aspose.Cells for Python via .NET مجموعة خاصة من الفصول في الفضاء الاسمية [**aspose.cells.pivot**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/) التي تستخدم لإنشاء والتحكم في جداول الدوران. يتم استخدام هذه الفصول لإنشاء وضبط كائنات [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/)، والتي تعد مكونات أساسية لجدول الدوران. الكائنات هي:

- [**PivotField**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/) يمثل حقل في [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/).
- [**PivotFieldCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection) يمثل مجموعة من جميع كائنات [**PivotField**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield) في [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable).
- [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) يمثل جدول دوران على ورقة العمل.
- [**PivotTableCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection) يمثل مجموعة من جميع كائنات [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) على ورقة العمل.

### **إنشاء جدول دوران بسيط باستخدام Aspose.Cells**

1. إضافة بيانات إلى ورقة العمل باستخدام طريقة [**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#str) لكائن [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell).
   سيتم استخدام هذه البيانات كمصدر بيانات جدول الدوران.
1. إضافة جدول دوران إلى ورقة العمل عن طريق استدعاء طريقة [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/add/#str-str-str) للمجموعة [**PivotTables**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection)، التي تم تقنينها في كائن ورقة العمل.
1. الوصول إلى كائن [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) الجديد من مجمع [**PivotTables**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection) عن طريق تمرير فهرس PivotTable.
1. استخدام أي من كائنات [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) (المشرحة أعلاه) لإدارة جدول الدوران.

بعد تنفيذ رمز المثال، يتم إضافة جدول دوران إلى ورقة العمل.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTable-CreatePivotTable-1.py" >}}

{{% alert color="primary" %}}

عند تعيين مجموعة من الخلايا كمصدر بيانات، يجب أن تكون المجموعة من الزاوية العلوية اليسرى إلى الزاوية السفلى اليمنى. على سبيل المثال، "A1:C3" صالح ولكن "C3:A1" غير صالح.

{{% /alert %}}

## **مواضيع متقدمة**
- [وظيفة التوحيد](/cells/ar/python-net/consolidation-function/)
- [ترتيب مخصص في جدول محوري](/cells/ar/python-net/custom-sorting-in-pivot-table/)
- [تخصيص إعدادات العالمية لجدول محوري](/cells/ar/python-net/customize-globalization-settings-for-pivot-table/)
- [تعطيل شرائط الجدول المحوري](/cells/ar/python-net/disable-pivot-table-ribbons/)
- [العثور وتحديث جداول الدوران المدمجة أو الفرعية لجدول الدوران الأم](/cells/ar/python-net/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/)
- [تنسيق جدول الجدول المحوري](/cells/ar/python-net/formatting-pivot-table/)
- [الحصول على مصدر بيانات الاتصال الخارجي لجدول الدوران](/cells/ar/python-net/get-external-connection-data-source-of-pivot-table/)
- [الحصول على تاريخ تحديث جدول محوري ومعلومات تحديث من قبل من خلاله](/cells/ar/python-net/get-pivot-table-refresh-date-and-refresh-by-who-information/)
- [تجميع حقول الجدول المحوري](/cells/ar/python-net/group-pivot-fields-in-the-pivot-table/)
- [تحليل السجلات المخزنة في حقول Pivot أثناء تحميل ملف Excel](/cells/ar/python-net/parsing-pivot-cached-records-while-loading-excel-file/)
- [الجدول المحوري وبيانات المصدر](/cells/ar/python-net/pivot-table-and-source-data/)
- [إخفاء البيانات وفرزها في جدول بيانات محوري](/cells/ar/python-net/pivot-table-hide-and-sort-data/)
- [تحديث وحساب الجدول الدوري الذي يحتوي على عناصر محسوبة](/cells/ar/python-net/refresh-and-calculate-pivot-table-having-calculated-items/)
- [حفظ الجدول المحوري في ملف ODS](/cells/ar/python-net/save-pivot-table-in-ods-file/)
- [خيار إظهار صفحات مرشح التقرير](/cells/ar/python-net/show-report-filter-pages-option/)
- [العمل مع تنسيقات عرض البيانات لحقل البيانات في الجدول المحوري](/cells/ar/python-net/working-with-data-display-formats-of-datafield-in-pivot-table/)
