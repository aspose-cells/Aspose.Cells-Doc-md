---
title: إنشاء المجاميع الفرعية
type: docs
weight: 800
url: /ar/nodejs-cpp/creating-subtotals/
description: تعلم كيفية إنشاء إجماليات فرعية لأي قيم متكررة في جدول بيانات باستخدام واجهة برمجة التطبيقات Aspose.Cells for Node.js via C++.
keywords: تطبيق المجاميع الفرعية، تعيين المجاميع الفرعية، إضافة المجاميع الفرعية، إنشاء المجاميع الفرعية، كيفية إضافة مجاميع فرعية لجدول بيانات 
---

{{% alert color="primary" %}}

يمكنك إنشاء إجماليات فرعية تلقائيًا لأي قيم متكررة في جدول بيانات. يوفر Aspose.Cells for Node.js via C++ ميزات API التي تساعدك على إضافة الإجماليات الفرعية للمدخلات برمجيًا.

{{% /alert %}}

## **استخدام Microsoft Excel**

لإضافة المجاميع الفرعية في Microsoft Excel:

1. إنشاء قائمة بيانات بسيطة في الورقة العمل الأولى من المفكرة (كما هو مبين في الشكل أدناه) وحفظ الملف كـ Book1.xls.
1. حدد أي خلية ضمن قائمتك.
1. من قائمة **البيانات**, حدد **المجاميع الفرعية**. سيتم عرض مربع حوار المجاميع الفرعية. حدد الوظيفة المطلوب استخدامها ومكان وضع المجاميع الفرعية.

## **باستخدام واجهة برمجة التطبيقات Aspose.Cells for Node.js via C++**

يوفر Aspose.Cells for Node.js via C++ فئة، [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)، تمثل ملف إكسل من مايكروسوفت. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) على [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) مجموعة تتيح الوصول إلى كل ورقة عمل في ملف إكسل.

يُمثل ورقة العمل بواسطة الفئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). توفر الفئة مجموعة واسعة من الخصائص والأساليب لإدارة الأوراق العمل والكائنات الأخرى. تتكون كل ورقة عمل من مجموعة [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). لإضافة المجاميع الفرعية إلى ورقة العمل، استخدم طريقة [**subtotal**](https://reference.aspose.com/cells/nodejs-cpp/cells/#subtotal-cellarea-number-consolidationfunction-numberarray-) لفئة [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). قم بتقديم قيم المعلمات للطريقة لتحديد كيفية حساب المجموعة الفرعية ووضعها.

في الأمثلة أدناه، أضفنا إجماليات فرعية إلى أول ورقة عمل في [ملف القالب](book1.xlsx) باستخدام واجهة برمجة التطبيقات Aspose.Cells for Node.js via C++. عند تنفيذ الكود، يتم إنشاء ورقة عمل مع إجماليات فرعية.

توضح مقاطع الكود التالية كيف يمكنك إضافة الإجماليات الفرعية إلى ورقة عمل باستخدام Aspose.Cells for Node.js via C++.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-CreatingSubtotals-1.js" >}}

