---
title: إنشاء جدول معالجة محوري
type: docs
weight: 10
url: /ar/java/create-pivot-table/
---

## **إنشاء جدول محوري**

### **إنشاء جدول محوري باستخدام Aspose.Cells**

{{% alert color="primary" %}}

مع Aspose.Cells، من الممكن إضافة جداول محورية إلى الجداول الإلكترونية. تحتوي Aspose.Cells على عدد من الفصول الخاصة المستخدمة بشكل خاص لإنشاء والتحكم في الجداول المحورية. يتم استخدام هذه الفصول لإنشاء وتعيين خصائص [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable) الكائن، المستخدم ككتل بناء للجدول الدوري.

تكوين كائنات الجدول الدوري:

- [**PivotField**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotField): تمثل مجالًا في جدول دوري.
- [**PivotFieldCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotFieldCollection): تمثل مجموعة من جميع الكائنات [**PivotField**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotField) في الجدول الدوري.
- [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable): تمثل جدول دوري.
- [**PivotTableCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection): تمثل مجموعة من جميع كائنات الجدول الدورية على ورقة العمل.

{{% /alert %}}

### **إنشاء جدول محوري بسيط**

لإنشاء جدول محوري باستخدام Aspose.Cells، يرجى اتباع الخطوات أدناه:

1. إضافة بعض البيانات إلى خلايا ورقة العمل باستخدام [**setValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value) [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell). سيتم استخدام هذه البيانات كمصدر بيانات للجدول الدوري.
1. أضف جدول محوري إلى ورقة العمل عن طريق استدعاء الطريقة [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#add-com.aspose.cells.PivotTable-int-int-java.lang.String-) لفئة [**PivotTableCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection)، المغلفة في الكائن ال [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet).
1. الوصول إلى [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable) الكائن من [**PivotTableCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection) من خلال تمرير فهرس [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable).
1. استخدام أيًا من كائنات الجدول الدوري (المشرحة أعلاه) المغلفة في [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable) لإدارة الجدول الدوري.

{{% alert color="primary" %}}

عند تعيين نطاق خلايا معين كمصدر بيانات، يجب تعيين النطاق من الزاوية العلوية اليسرى إلى الزاوية السفلى اليمنى. على سبيل المثال، "A1:C3" صالح؛ "C3:A1" غير صالح.

{{% /alert %}}

يظهر الكود المثال أدناه كيفية إنشاء جدول محوري بسيط باتباع الخطوات الأساسية المدرجة أعلاه. عند تنفيذ الكود، يتم إضافة جدول محوري إلى ورقة العمل:

** إنشاء جدول محوري استنادًا إلى حقل مقابل **

![todo:image_alt_text](create-pivot-table_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-CreatePivotTable-CreatePivotTable.java" >}}
{{< app/cells/assistant language="java" >}}
