---
title: إدراج جدول محوري
linktitle: جداول الدوران
type: docs
weight: 160
url: /ar/nodejs-cpp/create-pivot-table/
description: إنشاء وتنسيق جداول الدوران في ملفات جداول البيانات في Excel.
---

## **إنشاء جدول محوري**

من الممكن استخدام Aspose.Cells for Node.js via C++ لإضافة جداول محورية إلى جداول البيانات برمجياً.

### **نموذج كائن جدول الدوران**

يوفر Aspose.Cells for Node.js via C++ مجموعة مميزة من الفصلات التي تُستخدم لإنشاء والتحكم في الجداول المحورية. تُستخدم هذه الفصول لإنشاء وتعيين كائنات [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable)، وهي وحدات البناء الأساسية للجدول المحوري. الكائنات هي:

- [**PivotField**](https://reference.aspose.com/cells/nodejs-cpp/pivotfield) يمثل حقل في [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable).
- [**PivotFieldCollection**](https://reference.aspose.com/cells/nodejs-cpp/pivotfieldcollection) يمثل مجموعة من جميع كائنات [**PivotField**](https://reference.aspose.com/cells/nodejs-cpp/pivotfield) في [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable).
- [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) يمثل جدول دوران على ورقة العمل.
- [**PivotTableCollection**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection) يمثل مجموعة من جميع كائنات [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) على ورقة العمل.

### **إنشاء جدول دوران بسيط باستخدام Aspose.Cells**

1. إضافة بيانات إلى ورقة العمل باستخدام طريقة [**putValue**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-) لكائن [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell).
   سيتم استخدام هذه البيانات كمصدر بيانات جدول الدوران.
1. إضافة جدول دوران إلى ورقة العمل عن طريق استدعاء طريقة [**add**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection/#add-string-string-string-) للمجموعة [**PivotTables**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection)، التي تم تقنينها في كائن ورقة العمل.
1. الوصول إلى كائن [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) الجديد من مجمع [**PivotTables**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection) عن طريق تمرير فهرس PivotTable.
1. استخدام أي من كائنات [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) (المشرحة أعلاه) لإدارة جدول الدوران.

بعد تنفيذ رمز المثال، يتم إضافة جدول دوران إلى ورقة العمل.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-create-pivot-table.js" >}}

{{% alert color="primary" %}}

عند تعيين مجموعة من الخلايا كمصدر بيانات، يجب أن تكون المجموعة من الزاوية العلوية اليسرى إلى الزاوية السفلى اليمنى. على سبيل المثال، "A1:C3" صالح ولكن "C3:A1" غير صالح.

{{% /alert %}}
