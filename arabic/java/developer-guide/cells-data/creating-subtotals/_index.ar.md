---
title: تكوين المجاميع الفرعية
type: docs
weight: 50
url: /ar/java/creating-subtotals/
---
{{% alert color="primary" %}}

يمكنك إنشاء مجاميع فرعية تلقائيًا لأي قيم مكررة في جدول بيانات. يوفر Aspose.Cells ميزات API التي تساعدك على إضافة مجاميع فرعية إلى مجموعات البيانات برمجيًا.

{{% /alert %}}

## **باستخدام Microsoft إكسل**

لإنشاء مجاميع فرعية في Microsoft Excel:

1. قم بإنشاء قائمة بيانات بسيطة في ورقة العمل الأولى من المصنف (كما هو موضح في الشكل أدناه) وحفظ الملف باسم Book1.xls.
1. حدد أي خلية داخل قائمتك.
1.  من**بيانات** القائمة ، حدد**المجاميع الجزئية**.
 يتم عرض مربع حوار المجاميع الفرعية. حدد الوظيفة التي تريد استخدامها ومكان وضع المجاميع الفرعية.

   **تحديد نطاق بيانات لإضافة مجاميع فرعية**

![ما يجب القيام به: image_بديل_نص](creating-subtotals_1.png)

**مربع الحوار Subtotal** 

![ما يجب القيام به: image_بديل_نص](creating-subtotals_2.png)

## **باستخدام Aspose.Cells API**

 Aspose.Cells يوفر فصل دراسي ،[**دفتر العمل**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) يمثل ملف Excel Microsoft. ال[**دفتر العمل**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) فئة تحتوي على[**ورقة العمل**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)يسمح بالوصول إلى كل ورقة عمل في ملف Excel.

 يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)صف دراسي. يوفر الفصل مجموعة واسعة من الخصائص والأساليب لإدارة ورقة العمل والكائنات الأخرى. تتكون كل ورقة عمل من ملف[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) مجموعة. لإنشاء مجاميع فرعية في ورقة عمل ، استخدم ملحق[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)طريقة المجموع الفرعي للفئة. قم بتوفير القيم المناسبة لمعلمات الطريقة للحصول على النتيجة التي تريدها.

يوضح المثال أدناه كيفية إنشاء مجاميع فرعية في ورقة العمل الأولى لملف القالب (Book1.xls) باستخدام Aspose.Cells API.

عندما يتم تنفيذ التعليمات البرمجية ، يتم إنشاء ورقة عمل مع المجاميع الفرعية.

**تطبيق المجاميع الفرعية** 

![ما يجب القيام به: image_بديل_نص](creating-subtotals_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-CreatingSubtotals-CreatingSubtotals.java" >}}
