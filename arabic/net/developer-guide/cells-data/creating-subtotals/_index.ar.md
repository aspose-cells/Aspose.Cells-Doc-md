---
title: تكوين المجاميع الفرعية
type: docs
weight: 800
url: /ar/net/creating-subtotals/
---
{{% alert color="primary" %}}

يمكنك إنشاء مجاميع فرعية تلقائيًا لأي قيم مكررة في جدول بيانات. يوفر Aspose.Cells ميزات API التي تساعدك على إضافة الإجماليات الفرعية إلى جداول البيانات برمجيًا.

{{% /alert %}}

## **باستخدام Microsoft إكسل**

لإضافة مجاميع فرعية في Microsoft Excel:

1. قم بإنشاء قائمة بيانات بسيطة في ورقة العمل الأولى من المصنف (كما هو موضح في الشكل أدناه) وحفظ الملف باسم Book1.xls.
1. حدد أي خلية داخل قائمتك.
1.  من**بيانات** القائمة ، حدد**المجاميع الجزئية**. سيتم عرض مربع حوار المجاميع الفرعية. حدد الوظيفة التي تريد استخدامها ومكان وضع المجاميع الفرعية.

## **باستخدام Aspose.Cells API**

 Aspose.Cells يوفر فصل دراسي ،[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) ، يمثل ملف Excel Microsoft. ال[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) فئة تحتوي على[**أوراق عمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)مجموعة تسمح بالوصول إلى كل ورقة عمل في ملف Excel.

 يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) صف دراسي. يوفر الفصل مجموعة واسعة من الخصائص والأساليب لإدارة أوراق العمل والكائنات الأخرى. تتكون كل ورقة عمل من ملف[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) مجموعة. لإضافة مجاميع فرعية إلى ورقة عمل ، استخدم ملحق[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) صف دراسي'[**المجموع الفرعي**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/subtotal/index)طريقة. قم بتوفير قيم المعلمات للطريقة لتحديد كيفية حساب الإجمالي الفرعي ووضعه.

في الأمثلة أدناه ، قمنا بإضافة المجاميع الفرعية إلى ورقة العمل الأولى لملف القالب (Book1.xls) باستخدام Aspose.Cells API. عند تنفيذ التعليمات البرمجية ، يتم إنشاء ورقة عمل تحتوي على مجاميع فرعية.

توضح مقتطفات التعليمات البرمجية التالية كيفية إضافة مجاميع فرعية إلى ورقة عمل باستخدام Aspose.Cells for .NET.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-CreatingSubtotals-1.cs" >}}

## **موضوعات مسبقة**
- [تطبيق الإجمالي الفرعي وتغيير اتجاه صفوف ملخص المخطط التفصيلي أسفل التفاصيل](/cells/ar/net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/)
