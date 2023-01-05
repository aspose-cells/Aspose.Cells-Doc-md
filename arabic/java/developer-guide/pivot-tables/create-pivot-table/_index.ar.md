---
title: إنشاء جدول محوري
type: docs
weight: 10
url: /ar/java/create-pivot-table/
---
## **إنشاء جدول محوري**

### **إنشاء جدول محوري باستخدام Aspose.Cells**

{{% alert color="primary" %}}

 مع Aspose.Cells ، من الممكن إضافة جداول محورية إلى جداول البيانات. يحتوي Aspose.Cells على عدد من الفئات الخاصة المستخدمة خصيصًا لإنشاء الجداول المحورية والتحكم فيها. تُستخدم هذه الفئات لإنشاء وتعيين خصائص ملف[**جدول محوري**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable)كائن ، يتم استخدامه ككتل بناء الجدول المحوري.

كائنات الجدول المحوري هي:

- [**PivotField**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotField): يمثل حقلاً في جدول محوري.
- [**مجموعة PivotFieldCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotFieldCollection) إنه يمثل مجموعة من جميع ملفات[**PivotField**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotField)كائنات في الجدول المحوري.
- [**جدول محوري**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable): يمثل جدول محوري.
- [**مجموعة PivotTableCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection): يمثل مجموعة كل كائنات الجدول المحوري في ورقة العمل.

{{% /alert %}}

### **إنشاء جدول محوري بسيط**

لإنشاء جدول محوري باستخدام Aspose.Cells ، يرجى اتباع الخطوات التالية:

1.  أضف بعض البيانات إلى خلايا ورقة العمل باستخدام ملحق[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) أشياء[**setValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value)طريقة. سيتم استخدام هذه البيانات كمصدر بيانات للجدول المحوري.
1. أضف جدولاً محوريًا إلى ورقة العمل عن طريق استدعاء ملف[**يضيف**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#add(com.aspose.cells.PivotTable,%20int,%20int,%20java.lang.String) ) طريقة ال[**مجموعة PivotTableCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection) فئة ، مغلفة في[**ورقة عمل**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)موضوع.
1.  الوصول إلى[**جدول محوري**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable) كائن من[**مجموعة PivotTableCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection) عن طريق تمرير[**جدول محوري**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable)فهرس.
1.  استخدم أيًا من كائنات الجدول المحوري (الموضحة أعلاه) المغلفة في ملف[**جدول محوري**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable)كائن لإدارة الجدول المحوري.

{{% alert color="primary" %}}

عند تعيين نطاق من الخلايا كمصدر بيانات ، يجب تعيين النطاق من أعلى اليسار إلى أسفل اليمين. على سبيل المثال ، "A1: C3" صالح ؛ "C3: A1" غير صالح.

{{% /alert %}}

يوضح مثال الكود أدناه كيفية إنشاء جدول محوري بسيط باتباع الخطوات الأساسية المذكورة أعلاه. عند تنفيذ التعليمات البرمجية ، تتم إضافة جدول محوري إلى ورقة العمل:

**إنشاء جدول محوري بناءً على الحقل المقابل**

![ما يجب القيام به: image_بديل_نص](create-pivot-table_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-CreatePivotTable-CreatePivotTable.java" >}}
