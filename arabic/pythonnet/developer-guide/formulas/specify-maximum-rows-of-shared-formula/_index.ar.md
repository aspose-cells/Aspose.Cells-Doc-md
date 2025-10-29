---
title: كما يمكن استخدام الخاصية {0} لتحديد الصفوف القصوى للصيغة المشتركة.
type: docs
weight: 40
url: /ar/python-net/specify-maximum-rows-of-shared-formula/
---

## **سيناريوهات الاستخدام المحتملة**

الحد الأقصى الافتراضي لصفوف الصيغة المشتركة هو 64. يمكن أن يكون أي رقم، مثلاً 1000. تتغير أداءات الصيغة المشتركة مع عدد الصفوف المختلفة. لذلك، يوفر Aspose.Cells for Python via .NET الخاصية [**Workbook.settings.max_rows_of_shared_formula**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/max_rows_of_shared_formula) التي يمكن استخدامها لتحديد الحد الأقصى لصفوف الصيغة المشتركة. ستتقسم الصيغة المشتركة إلى عدة صيغ مشتركة إذا زاد إجمالي الصفوف عن هذا الحد، كما هو موضح في الصورة التالية.

![todo:image_alt_text](specify-maximum-rows-of-shared-formula_1.png)

## **تحديد الصفوف القصوى للصيغة المشتركة**

يشرح الكود المصدّر التالي استخدام الخاصية [**Workbook.settings.max_rows_of_shared_formula**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/max_rows_of_shared_formula). يقوم بتحديد الصفوف القصوى للصيغة المشتركة بـ 5 ويضيف الصيغة المشتركة في الخلية D1 لعدد 100 صف ويحفظ في [ملف إكسل الناتج](61767856.xlsx). إذا استخرجت محتويات ملف إكسل الناتج وفحصت *sheet1.xml*، سترى أن الصيغ المشتركة تتقسم بعد كل 5 صفوف كما هو موضح في اللقطة المشار إليها أعلاه.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-SpecifyMaximumRowsOfSharedFormula.py" >}}

{{< app/cells/assistant language="python-net" >}}
