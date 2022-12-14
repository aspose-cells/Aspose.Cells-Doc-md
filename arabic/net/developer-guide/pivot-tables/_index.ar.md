---
title: إدراج جدول محوري
linktitle: الجداول المحورية
type: docs
weight: 160
url: /ar/net/create-pivot-table/
description: إنشاء وتنسيق الجداول المحورية لملفات جداول بيانات Excel.
---
## **إنشاء جدول محوري**

من الممكن استخدام Aspose.Cells لإضافة جداول محورية إلى جداول البيانات برمجيًا.

### **نموذج كائن الجدول المحوري**

يوفر Aspose.Cells مجموعة خاصة من الفئات في[**Aspose.Cells.Pivot**](https://reference.aspose.com/cells/net/aspose.cells.pivot) مساحة الاسم المستخدمة لإنشاء الجداول المحورية والتحكم فيها. تستخدم هذه الفئات للإنشاء والتعيين[**جدول محوري**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)الكائنات ، اللبنات الأساسية للجدول المحوري. الأشياء هي:

- [**PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) يمثل حقلاً في[**جدول محوري**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable).
- [**مجموعة PivotFieldCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection) يمثل مجموعة من كل[**PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) كائنات في[**جدول محوري**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable).
- [**جدول محوري**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)يمثل PivotTable في ورقة عمل.
- [**مجموعة PivotTableCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection) يمثل مجموعة من كل[**جدول محوري**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)كائنات في ورقة العمل.

### **تكوين جدول محوري بسيط باستخدام Aspose.Cells**

1. أضف بيانات إلى ورقة عمل باستخدام ملحق[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) أشياء[**ضع القيمة**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) طريقة.
 سيتم استخدام هذه البيانات كمصدر بيانات للجدول المحوري.
1.  أضف جدولاً محوريًا إلى ورقة العمل عن طريق استدعاء ملف[**الجداول المحورية**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection) المجموعة[**يضيف**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/add/index)الطريقة ، والتي يتم تغليفها في كائن ورقة العمل.
1.  الوصول إلى ملف[**جدول محوري**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) كائن من[**الجداول المحورية**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection)المجموعة عن طريق تمرير فهرس PivotTable.
1.  استخدم أيًا من ملفات[**جدول محوري**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)كائنات (موضحة أعلاه) لإدارة الجدول المحوري.

بعد تنفيذ رمز المثال ، تتم إضافة جدول محوري إلى ورقة العمل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-CreatePivotTable-1.cs" >}}

{{% alert color="primary" %}}

عند تعيين نطاق من الخلايا كمصدر بيانات ، يجب أن ينتقل النطاق من أعلى اليسار إلى أسفل اليمين. على سبيل المثال ، "A1: C3" صالح ولكن "C3: A1" ليس كذلك.

{{% /alert %}}

## **موضوعات مسبقة**
- [وظيفة التوحيد](/cells/ar/net/consolidation-function/)
- [فرز مخصص في Pivot Table](/cells/ar/net/custom-sorting-in-pivot-table/)
- [تخصيص إعدادات العولمة للجدول المحوري](/cells/ar/net/customize-globalization-settings-for-pivot-table/)
- [تعطيل شرائط الجدول المحوري](/cells/ar/net/disable-pivot-table-ribbons/)
- [ابحث عن الجداول المتداخلة أو الجداول المحورية التابعة للجدول المحوري الأصل وقم بتحديثها](/cells/ar/net/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/)
- [تنسيق الجدول المحوري](/cells/ar/net/formatting-pivot-table/)
- [الحصول على مصدر بيانات الاتصال الخارجي للجدول المحوري](/cells/ar/net/get-external-connection-data-source-of-pivot-table/)
- [احصل على تاريخ تحديث Pivot Table وقم بالتحديث حسب من المعلومات](/cells/ar/net/get-pivot-table-refresh-date-and-refresh-by-who-information/)
- [تجميع الحقول المحورية في الجدول المحوري](/cells/ar/net/group-pivot-fields-in-the-pivot-table/)
- [تحليل السجلات المحورية المخزنة مؤقتًا أثناء تحميل ملف Excel](/cells/ar/net/parsing-pivot-cached-records-while-loading-excel-file/)
- [جدول محوري وبيانات مصدر](/cells/ar/net/pivot-table-and-source-data/)
- [جدول محوري إخفاء البيانات وفرزها](/cells/ar/net/pivot-table-hide-and-sort-data/)
- [تحديث وحساب الجدول المحوري الذي يحتوي على عناصر محسوبة](/cells/ar/net/refresh-and-calculate-pivot-table-having-calculated-items/)
- [حفظ Pivot Table في ملف ODS](/cells/ar/net/save-pivot-table-in-ods-file/)
- [إظهار خيار صفحات تصفية التقرير](/cells/ar/net/show-report-filter-pages-option/)
- [العمل مع تنسيقات عرض البيانات DataField في Pivot Table](/cells/ar/net/working-with-data-display-formats-of-datafield-in-pivot-table/)
