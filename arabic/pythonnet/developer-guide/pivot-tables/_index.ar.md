---
title: إدراج جدول محوري
linktitle: الجداول المحورية
type: docs
weight: 160
url: /ar/python-net/create-pivot-table/
description: إنشاء وتنسيق الجدول المحوري باستخدام Aspose.Cells for Python via .NET.
keywords: Create Pivot Table, Insert Pivot Table, Format Pivot Table.
---
##  **إنشاء جدول محوري**

من الممكن استخدام Aspose.Cells for Python via .NET لإضافة الجداول المحورية إلى جداول البيانات برمجياً.

###  **نموذج كائن الجدول المحوري**

 Aspose.Cells for Python via .NET يوفر مجموعة خاصة من الفصول في[**aspose.cells.pivot**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/) مساحة الاسم المستخدمة لإنشاء الجداول المحورية والتحكم فيها. يتم استخدام هذه الفئات لإنشاء وتعيين[**جدول محوري**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/)الكائنات، اللبنات الأساسية للجدول المحوري. الكائنات هي:

- [**PivotField**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/) يمثل حقلاً في[**جدول محوري**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/).
- [**PivotFieldCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection) يمثل مجموعة من كل[**PivotField**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield) كائنات في[**جدول محوري**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable).
- [**جدول محوري**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable)يمثل PivotTable في ورقة العمل.
- [**PivotTableCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection) يمثل مجموعة من كل[**جدول محوري**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable)الكائنات في ورقة العمل.

###  **إنشاء جدول محوري بسيط باستخدام Aspose.Cells**

1.  إضافة بيانات إلى ورقة العمل باستخدام[**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) أشياء[**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#str) طريقة.
 سيتم استخدام هذه البيانات كمصدر بيانات الجدول المحوري.
1.  قم بإضافة جدول محوري إلى ورقة العمل عن طريق استدعاء[**الجداول المحورية**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection) المجموعة[**يضيف**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/add/#str-str-str)الطريقة، والتي تم تضمينها في كائن ورقة العمل.
1.  الوصول إلى الجديد[**جدول محوري**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) كائن من[**الجداول المحورية**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection)المجموعة عن طريق تمرير فهرس PivotTable.
1.  استخدم أيًا من[**جدول محوري**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable)الكائنات (الموضحة أعلاه) لإدارة الجدول المحوري.

بعد تنفيذ رمز المثال، تتم إضافة جدول محوري إلى ورقة العمل.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTable-CreatePivotTable-1.py" >}}

{{% alert color="primary" %}}

عند تعيين نطاق من الخلايا كمصدر للبيانات، يجب أن ينتقل النطاق من أعلى اليسار إلى أسفل اليمين. على سبيل المثال، "A1:C3" صالح ولكن "C3:A1" ليس كذلك.

{{% /alert %}}

##  **مواضيع متقدمة**
- [وظيفة التوحيد](/cells/ar/python-net/consolidation-function/)
- [الفرز المخصص في الجدول المحوري](/cells/ar/python-net/custom-sorting-in-pivot-table/)
- [تخصيص إعدادات العولمة للجدول المحوري](/cells/ar/python-net/customize-globalization-settings-for-pivot-table/)
- [تعطيل أشرطة الجدول المحوري](/cells/ar/python-net/disable-pivot-table-ribbons/)
- [ابحث عن الجداول المحورية المتداخلة أو التابعة للجدول المحوري الأصلي وقم بتحديثها](/cells/ar/python-net/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/)
- [تنسيق الجدول المحوري](/cells/ar/python-net/formatting-pivot-table/)
- [احصل على مصدر بيانات الاتصال الخارجي للجدول المحوري](/cells/ar/python-net/get-external-connection-data-source-of-pivot-table/)
- [احصل على تاريخ تحديث Pivot Table وقم بالتحديث حسب معلومات الشخص](/cells/ar/python-net/get-pivot-table-refresh-date-and-refresh-by-who-information/)
- [تجميع الحقول المحورية في الجدول المحوري](/cells/ar/python-net/group-pivot-fields-in-the-pivot-table/)
- [تحليل السجلات المحورية المخزنة مؤقتًا أثناء تحميل ملف Excel](/cells/ar/python-net/parsing-pivot-cached-records-while-loading-excel-file/)
- [الجدول المحوري وبيانات المصدر](/cells/ar/python-net/pivot-table-and-source-data/)
- [إخفاء الجدول المحوري وفرز البيانات](/cells/ar/python-net/pivot-table-hide-and-sort-data/)
- [تحديث وحساب الجدول المحوري الذي يحتوي على العناصر المحسوبة](/cells/ar/python-net/refresh-and-calculate-pivot-table-having-calculated-items/)
- [حفظ الجدول المحوري في ملف ODS](/cells/ar/python-net/save-pivot-table-in-ods-file/)
- [إظهار خيار صفحات تصفية التقرير](/cells/ar/python-net/show-report-filter-pages-option/)
- [العمل مع تنسيقات عرض البيانات في DataField في Pivot Table](/cells/ar/python-net/working-with-data-display-formats-of-datafield-in-pivot-table/)
