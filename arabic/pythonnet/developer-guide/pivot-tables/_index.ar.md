---
title: إدراج جدول محوري
description: إنشاء وتنسيق جدول دوران بواسطة Aspose.Cells for Python via .NET.
linktitle: جداول الدوران
url: /ar/python-net/create-pivot-table/
type: docs
weight: 160
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
keywords: إنشاء جدول دوران، إدراج جدول دوران، تنسيق جدول دوران.
---

## **إنشاء جدول محوري**
من الممكن استخدام Aspose.Cells for Python via .NET لإضافة جداول دوران إلى جداول البيانات برمجياً.

### **نموذج كائن جدول الدوران**
توفر Aspose.Cells for Python via .NET مجموعة خاصة من الفصول في الفضاء الاسمية [**aspose.cells.pivot**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/) التي تستخدم لإنشاء والتحكم في جداول الدوران. يتم استخدام هذه الفصول لإنشاء وضبط كائنات [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/)، والتي تعد مكونات أساسية لجدول الدوران. الكائنات هي:
- [**PivotField**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/) يمثل حقل في [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/).
- [**PivotFieldCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfieldcollection) يمثل مجموعة من جميع كائنات [**PivotField**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield) في [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable).
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

{{< app/cells/assistant language="python-net" >}}