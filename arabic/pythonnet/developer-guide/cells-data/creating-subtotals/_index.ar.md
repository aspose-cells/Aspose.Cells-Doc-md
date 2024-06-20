---
title: إنشاء المجاميع الفرعية
type: docs
weight: 800
url: /ar/python-net/creating-subtotals/
description: تعلم كيفية إنشاء المجاميع الفرعية لأي قيم متكررة في جدول بيانات باستخدام Aspose.Cells for Python via .NET API.
keywords: مكتبة Excel لـ Python ، تطبيق المجاميع الفرعية ، تعيين المجاميع الفرعية ، إضافة مجاميع فرعية ، إنشاء المجاميع الفرعية ، كيفية إضافة المجاميع الفرعية إلى ورقة العمل 
---

{{% alert color="primary" %}}

يمكنك إنشاء المجاميع الفرعية تلقائيًا لأي قيم متكررة في ورقة بيانات. يوفر Aspose.Cells for Python via .NET ميزات واجهة برمجة التطبيقات التي تساعدك في إضافة المجاميع الفرعية إلى أوراق العمل بشكل برمجي.

{{% /alert %}}

## **استخدام Microsoft Excel**

لإضافة المجاميع الفرعية في Microsoft Excel:

1. إنشاء قائمة بيانات بسيطة في الورقة العمل الأولى من المفكرة (كما هو مبين في الشكل أدناه) وحفظ الملف كـ Book1.xls.
1. حدد أي خلية ضمن قائمتك.
1. من قائمة **البيانات**, حدد **المجاميع الفرعية**. سيتم عرض مربع حوار المجاميع الفرعية. حدد الوظيفة المطلوب استخدامها ومكان وضع المجاميع الفرعية.

## **استخدام Aspose.Cells for Python via .NET API**

توفر Aspose.Cells for Python via .NET فئةً، [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)، التي تمثل ملف Microsoft Excel. تحتوي الفئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) على مجموعة [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel.

يُمثل ورقة العمل بواسطة الفئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). توفر الفئة مجموعة واسعة من الخصائص والأساليب لإدارة الأوراق العمل والكائنات الأخرى. تتكون كل ورقة عمل من مجموعة [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). لإضافة المجاميع الفرعية إلى ورقة العمل، استخدم طريقة [**subtotal**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/subtotal/#aspose.cells.CellArea-int-aspose.cells.ConsolidationFunction-list) لفئة [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). قم بتقديم قيم المعلمات للطريقة لتحديد كيفية حساب المجموعة الفرعية ووضعها.

في الأمثلة أدناه، قمنا بإضافة المجاميع الفرعية إلى الورقة العمل الأولى من ملف القالب (Book1.xls) باستخدام Aspose.Cells for Python via .NET API. عند تنفيذ الكود، يتم إنشاء ورقة عمل بها مجاميع فرعية.

عينات الشفرات التالية توضح كيفية إضافة المجاميع الفرعية إلى ورقة العمل باستخدام Aspose.Cells for Python via .NET.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-CreatingSubtotals-1.py" >}}

## **مواضيع متقدمة**
- [تطبيق المجموع الفرعي وتغيير اتجاه الصفوف القابلة للملخص تحت التفصيل](/cells/ar/python-net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/)
