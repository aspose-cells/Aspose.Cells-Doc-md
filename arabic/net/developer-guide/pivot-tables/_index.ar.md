---
title: إدراج جدول محوري
linktitle: جداول الدوران
type: docs
weight: 160
url: /ar/net/create-pivot-table/
description: إنشاء وتنسيق جداول الدوران في ملفات جداول البيانات في Excel.
---

## **إنشاء جدول محوري**

يمكن استخدام Aspose.Cells لإضافة جداول دوران إلى جداول البيانات برمجيًا.

### **نموذج كائن جدول الدوران**

توفر Aspose.Cells مجموعة خاصة من الفئات في مساحة الاسم [**Aspose.Cells.Pivot**](https://reference.aspose.com/cells/net/aspose.cells.pivot) التي تستخدم لإنشاء والتحكم في جداول الدوران. تستخدم هذه الفئات لإنشاء وتعيين كائنات [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)، وهي البنيات الأساسية لجدول الدوران. الكائنات هي:

- [**PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) يمثل حقل في [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable).
- [**PivotFieldCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection) يمثل مجموعة من جميع كائنات [**PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) في [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable).
- [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) يمثل جدول دوران على ورقة العمل.
- [**PivotTableCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection) يمثل مجموعة من جميع كائنات [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) على ورقة العمل.

### **إنشاء جدول دوران بسيط باستخدام Aspose.Cells**

1. إضافة بيانات إلى ورقة العمل باستخدام طريقة [**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) لكائن [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell).
   سيتم استخدام هذه البيانات كمصدر بيانات جدول الدوران.
1. إضافة جدول دوران إلى ورقة العمل عن طريق استدعاء طريقة [**add**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/add/index) للمجموعة [**PivotTables**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection)، التي تم تقنينها في كائن ورقة العمل.
1. الوصول إلى كائن [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) الجديد من مجمع [**PivotTables**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection) عن طريق تمرير فهرس PivotTable.
1. استخدام أي من كائنات [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) (المشرحة أعلاه) لإدارة جدول الدوران.

بعد تنفيذ رمز المثال، يتم إضافة جدول دوران إلى ورقة العمل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-CreatePivotTable-1.cs" >}}

{{% alert color="primary" %}}

عند تعيين مجموعة من الخلايا كمصدر بيانات، يجب أن تكون المجموعة من الزاوية العلوية اليسرى إلى الزاوية السفلى اليمنى. على سبيل المثال، "A1:C3" صالح ولكن "C3:A1" غير صالح.

{{% /alert %}}

## **مواضيع متقدمة**
- [وظيفة التوحيد](/cells/ar/net/consolidation-function/)
- [ترتيب مخصص في جدول محوري](/cells/ar/net/custom-sorting-in-pivot-table/)
- [تخصيص إعدادات العالمية لجدول محوري](/cells/ar/net/customize-globalization-settings-for-pivot-table/)
- [تعطيل شرائط الجدول المحوري](/cells/ar/net/disable-pivot-table-ribbons/)
- [العثور وتحديث جداول الدوران المدمجة أو الفرعية لجدول الدوران الأم](/cells/ar/net/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/)
- [تنسيق جدول الجدول المحوري](/cells/ar/net/formatting-pivot-table/)
- [الحصول على مصدر بيانات الاتصال الخارجي لجدول الدوران](/cells/ar/net/get-external-connection-data-source-of-pivot-table/)
- [الحصول على تاريخ تحديث جدول محوري ومعلومات تحديث من قبل من خلاله](/cells/ar/net/get-pivot-table-refresh-date-and-refresh-by-who-information/)
- [تجميع حقول الجدول المحوري](/cells/ar/net/group-pivot-fields-in-the-pivot-table/)
- [تحليل السجلات المخزنة في حقول Pivot أثناء تحميل ملف Excel](/cells/ar/net/parsing-pivot-cached-records-while-loading-excel-file/)
- [الجدول المحوري وبيانات المصدر](/cells/ar/net/pivot-table-and-source-data/)
- [إخفاء البيانات وفرزها في جدول بيانات محوري](/cells/ar/net/pivot-table-hide-and-sort-data/)
- [تحديث وحساب الجدول الدوري الذي يحتوي على عناصر محسوبة](/cells/ar/net/refresh-and-calculate-pivot-table-having-calculated-items/)
- [حفظ الجدول المحوري في ملف ODS](/cells/ar/net/save-pivot-table-in-ods-file/)
- [خيار إظهار صفحات مرشح التقرير](/cells/ar/net/show-report-filter-pages-option/)
- [العمل مع تنسيقات عرض البيانات لحقل البيانات في الجدول المحوري](/cells/ar/net/working-with-data-display-formats-of-datafield-in-pivot-table/)
