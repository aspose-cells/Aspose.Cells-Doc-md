---
title: إنشاء المجاميع الفرعية
type: docs
weight: 800
url: /ar/net/creating-subtotals/
description: تعلم كيفية إنشاء مجاميع فرعية لأي قيم تكرر في جدول بيانات باستخدام Aspose.Cells for .NET API.
keywords: تطبيق المجاميع الفرعية، تعيين المجاميع الفرعية، إضافة المجاميع الفرعية، إنشاء المجاميع الفرعية، كيفية إضافة مجاميع فرعية لجدول بيانات 
---

{{% alert color="primary" %}}

يمكنك إنشاء الإجماليات الفرعية تلقائيًا لأي قيم متكررة في جدول البيانات. توفر Aspose.Cells ميزات واجهة برمجة التطبيقات التي تساعدك في إضافة الإجماليات الفرعية لجداول البيانات بشكل برمجي.

{{% /alert %}}

## **استخدام Microsoft Excel**

لإضافة المجاميع الفرعية في Microsoft Excel:

1. إنشاء قائمة بيانات بسيطة في الورقة العمل الأولى من المفكرة (كما هو مبين في الشكل أدناه) وحفظ الملف كـ Book1.xls.
1. حدد أي خلية ضمن قائمتك.
1. من قائمة **البيانات**, حدد **المجاميع الفرعية**. سيتم عرض مربع حوار المجاميع الفرعية. حدد الوظيفة المطلوب استخدامها ومكان وضع المجاميع الفرعية.

## **استخدام واجهة التطبيقات لـ Aspose.Cells**

توفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)، تمثل ملف Microsoft Excel. تحتوي الفئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) على مجموعة [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) التي تسمح بالوصول إلى كل ورق العمل في ملف Excel.

يُمثل ورقة العمل بواسطة الفئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). توفر الفئة مجموعة واسعة من الخصائص والأساليب لإدارة الأوراق العمل والكائنات الأخرى. تتكون كل ورقة عمل من مجموعة [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). لإضافة المجاميع الفرعية إلى ورقة العمل، استخدم طريقة [**Subtotal**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/subtotal/index) لفئة [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). قم بتقديم قيم المعلمات للطريقة لتحديد كيفية حساب المجموعة الفرعية ووضعها.

في الأمثلة أدناه، قمنا بإضافة إجماليات فرعية إلى الورقة العمل الأولى من ملف القالب (Book1.xls) باستخدام واجهة التطبيقات لـ Aspose.Cells. عند تنفيذ الكود، سيتم إنشاء ورقة عمل بها إجماليات فرعية.

يعرض مقتطفات الشفرة التالية كيفية إضافة الإجماليات الفرعية إلى ورقة عمل بـAspose.Cells for .NET.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-CreatingSubtotals-1.cs" >}}

## **مواضيع متقدمة**
- [تطبيق المجموع الفرعي وتغيير اتجاه الصفوف القابلة للملخص تحت التفصيل](/cells/ar/net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/)
