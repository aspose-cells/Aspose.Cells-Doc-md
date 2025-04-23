---
title: إنشاء المجاميع الفرعية
type: docs
weight: 50
url: /ar/java/creating-subtotals/
---

{{% alert color="primary" %}}

يمكنك إنشاء المجاميع الفرعية تلقائيًا لأي قيم متكررة في ورق العمل. توفر Aspose.Cells ميزات واجهة برمجة التطبيقات التي تساعدك في إضافة المجاميع الفرعية إلى أوراق العمل برمجيًا.

{{% /alert %}}

## **استخدام Microsoft Excel**

لإنشاء المجاميع الفرعية في Microsoft Excel:

1. إنشاء قائمة بيانات بسيطة في الورقة العمل الأولى من المفكرة (كما هو مبين في الشكل أدناه) وحفظ الملف كـ Book1.xls.
1. حدد أي خلية ضمن قائمتك.
1. من قائمة **البيانات**, حدد **المجاميع الفرعية**.
   يتم عرض مربع حوار المجاميع الفرعية. حدد الوظيفة لاستخدامها ومكان وضع المجاميع الفرعية.

   **تحديد نطاق بيانات لإضافة المجاميع الفرعية**

![todo:image_alt_text](creating-subtotals_1.png)

**مربع حوار المجموع الفرعي** 

![todo:image_alt_text](creating-subtotals_2.png)

## **استخدام واجهة برمجة تطبيقات Aspose.Cells**

توفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) تمثل ملف Microsoft Excel. تحتوي الفئة [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) على [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel.

تمثل ورقة العمل بواسطة الفئة [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). توفر الفئة مجموعة واسعة من الخصائص والأساليب لإدارة ورقة العمل والكائنات الأخرى. تتكون كل ورقة عمل من مجموعة [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). لإنشاء المجاميع الفرعية في ورقة العمل، استخدم طريقة مجموع الفئة [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). قدم القيم المناسبة لمعلمات الطريقة للحصول على النتيجة التي تريدها.

يظهر المثال أدناه كيفية إنشاء مجاميع فرعية في الورقة العمل الأولى من ملف القالب (Book1.xls) باستخدام واجهة برمجة التطبيقات Aspose.Cells.

عند تنفيذ الكود، يتم إنشاء ورقة عمل تحتوي على مجاميع فرعية.

**تطبيق المجاميع الفرعية** 

![todo:image_alt_text](creating-subtotals_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-CreatingSubtotals-CreatingSubtotals.java" >}}
{{< app/cells/assistant language="java" >}}
