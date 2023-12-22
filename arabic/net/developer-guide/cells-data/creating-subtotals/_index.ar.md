---
title: إنشاء الإجماليات الفرعية
type: docs
weight: 800
url: /ar/net/creating-subtotals/
description: تعرف على كيفية إنشاء إجماليات فرعية لأي قيم متكررة في جدول بيانات باستخدام Aspose.Cells for .NET API.
keywords: Apply Subtotals, Set Subtotals, Add subtotals, Create Subtotals, How to add subtotals to a worksheet 
---
{{% alert color="primary" %}}

يمكنك إنشاء إجماليات فرعية تلقائيًا لأي قيم متكررة في جدول البيانات. يوفر Aspose.Cells ميزات API التي تساعدك على إضافة الإجماليات الفرعية إلى جداول البيانات برمجياً.

{{% /alert %}}

##  **باستخدام Microsoft اكسل**

لإضافة المجاميع الفرعية في Microsoft إكسل:

1. قم بإنشاء قائمة بيانات بسيطة في ورقة العمل الأولى للمصنف (كما هو موضح في الشكل أدناه) واحفظ الملف باسم Book1.xls.
1. حدد أي خلية ضمن قائمتك.
1.  من**بيانات** من القائمة، حدد *الإجماليات الفرعية**. سيتم عرض مربع حوار الإجماليات الفرعية. حدد الوظيفة التي يجب استخدامها ومكان وضع الإجماليات الفرعية.

##  **باستخدام Aspose.Cells API**

 Aspose.Cells يوفر فئة،[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) ، يمثل ملف Excel Microsoft. ال[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) يحتوي الفصل على أ[**أوراق عمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)المجموعة التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel.

يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) فصل. يوفر الفصل نطاقًا واسعًا من الخصائص والأساليب لإدارة أوراق العمل والكائنات الأخرى. تتكون كل ورقة عمل من أ[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)مجموعة. لإضافة الإجماليات الفرعية إلى ورقة العمل، استخدم[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)فصل'[**المجموع الفرعي**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/subtotal/index)طريقة. قم بتوفير قيم المعلمات للطريقة لتحديد كيفية حساب الإجمالي الفرعي ووضعه.

في الأمثلة أدناه، أضفنا الإجماليات الفرعية إلى ورقة العمل الأولى لملف القالب (Book1.xls) باستخدام Aspose.Cells API. عند تنفيذ التعليمات البرمجية، يتم إنشاء ورقة عمل تحتوي على الإجماليات الفرعية.

توضح مقتطفات التعليمات البرمجية التالية كيفية إضافة الإجماليات الفرعية إلى ورقة عمل باستخدام Aspose.Cells for .NET.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-CreatingSubtotals-1.cs" >}}

##  **مواضيع متقدمة**
- [تطبيق الإجمالي الفرعي وتغيير اتجاه صفوف ملخص المخطط التفصيلي أسفل التفاصيل](/cells/ar/net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/)
