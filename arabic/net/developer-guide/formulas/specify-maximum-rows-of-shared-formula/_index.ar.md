---
title: كما يمكن استخدام الخاصية {0} لتحديد الصفوف القصوى للصيغة المشتركة.
type: docs
weight: 40
url: /ar/net/specify-maximum-rows-of-shared-formula/
---

## **سيناريوهات الاستخدام المحتملة**

الصفوف المشتركة الافتراضية للصيغة هي 64. يمكن أن يكون أي عدد مثل 1000. تتغير أداء الصيغة المشتركة مع عدد مختلف من الصفوف. لذلك، توفر Aspose.Cells الخاصية [**Workbook.Settings.MaxRowsOfSharedFormula**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxrowsofsharedformula) التي يمكن استخدامها لتحديد الصفوف القصوى للصيغة المشتركة. سيتم تقسيم الصيغة المشتركة إلى عدة صيغ مشتركة إذا كان إجمالي الصفوف للصيغة المشتركة أكبر منه كما هو موضح في لقطة الشاشة التالية.

![todo:image_alt_text](specify-maximum-rows-of-shared-formula_1.png)

## **تحديد الصفوف القصوى للصيغة المشتركة**

يشرح الكود المصدّر التالي استخدام الخاصية [**Workbook.Settings.MaxRowsOfSharedFormula**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxrowsofsharedformula). يقوم بتحديد الصفوف القصوى للصيغة المشتركة بـ 5 ويضيف الصيغة المشتركة في الخلية D1 لعدد 100 صف ويحفظ في [ملف إكسل الناتج](61767856.xlsx). إذا استخرجت محتويات ملف إكسل الناتج وفحصت *sheet1.xml*، سترى أن الصيغ المشتركة تتقسم بعد كل 5 صفوف كما هو موضح في اللقطة المشار إليها أعلاه.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Formulas-SpecifyMaximumRowsOfSharedFormula.cs" >}}
