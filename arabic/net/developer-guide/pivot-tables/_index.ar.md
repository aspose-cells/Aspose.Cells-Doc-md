---
title: إدراج جدول محوري
linktitle: الجداول المحورية
type: docs
weight: 160
url: /ar/net/pivot-tables/
description: إنشاء وتنسيق الجداول المحورية في ملفات جداول البيانات في Excel.
keywords: إنشاء جدول محوري، إدراج جدول محوري، تنسيق جدول محوري.
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **إنشاء جدول محوري**

يمكن استخدام Aspose.Cells لإضافة الجداول المحورية إلى جداول البيانات برمجيًا.

### **نموذج كائن الجدول المحوري**

توفر Aspose.Cells مجموعة خاصة من الفئات في مساحة الاسم [**Aspose.Cells.Pivot**](https://reference.aspose.com/cells/net/aspose.cells.pivot) التي تستخدم لإنشاء والتحكم في الجداول المحورية. تستخدم هذه الفئات لإنشاء وتعيين كائنات [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)، وهي البنيات الأساسية للجدول المحوري. الكائنات هي:

- [**PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) يمثل حقل في [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable).
- [**PivotFieldCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection) يمثل مجموعة من جميع كائنات [**PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) في [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable).
- [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) يمثل جدول محوري على ورقة العمل.
- [**PivotTableCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection) يمثل مجموعة من جميع كائنات [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) على ورقة العمل.

### **إنشاء جدول محوري بسيط باستخدام Aspose.Cells**

1. إضافة بيانات إلى ورقة العمل باستخدام طريقة [**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) لكائن [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell).
   سيتم استخدام هذه البيانات كمصدر بيانات الجدول المحوري.
2. إضافة جدول محوري إلى ورقة العمل عن طريق استدعاء طريقة [**add**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/add/index) للمجموعة [**PivotTables**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection)، المغلفة في كائن ورقة العمل.
3. الوصول إلى كائن [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) الجديد من مجموعة [**PivotTables**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection) عن طريق تمرير فهرس PivotTable.
4. استخدام أي من كائنات [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) (الموضحة أعلاه) لإدارة الجدول المحوري.

بعد تنفيذ رمز المثال، يتم إضافة جدول محوري إلى ورقة العمل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-CreatePivotTable-1.cs" >}}

{{% alert color="primary" %}}

عند تعيين مجموعة من الخلايا كمصدر بيانات، يجب أن تكون المجموعة من الزاوية العلوية اليسرى إلى الزاوية السفلى اليمنى. على سبيل المثال، "A1:C3" صالح ولكن "C3:A1" غير صالح.

{{% /alert %}}

{{< app/cells/assistant language="csharp" >}}
