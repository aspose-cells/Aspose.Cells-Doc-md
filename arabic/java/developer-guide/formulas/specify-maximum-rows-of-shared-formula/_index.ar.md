---
title: كما يمكن استخدام الخاصية {0} لتحديد الصفوف القصوى للصيغة المشتركة.
type: docs
weight: 40
url: /ar/java/specify-maximum-rows-of-shared-formula/
---

## **سيناريوهات الاستخدام المحتملة**

الحد الأقصى الافتراضي للصفوف المشتركة من الصيغة هو 64. يمكن أن يكون أي رقم على سبيل المثال، يمكن أن يكون 1000. تتغير أداء الصيغة المشتركة مع عدد مختلف من الصفوف. لذلك، توفر Aspose.Cells الخاصية [**Workbook.Settings.MaxRowsOfSharedFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxRowsOfSharedFormula) التي يمكن استخدامها لتحديد الحد الأقصى للصفوف المشتركة للصيغة. سيتم تقسيم الصيغة المشتركة إلى عدة صيغ مشتركة إذا كان إجمالي الصفوف للصيغة المشتركة أكبر من ذلك كما هو موضح في اللقطة المصورة التالية.

![todo:image_alt_text](specify-maximum-rows-of-shared-formula_1.png)

## **تحديد الصفوف القصوى للصيغة المشتركة**

يوضح الكود المثالي التالي استخدام الخاصية [**Workbook.Settings.MaxRowsOfSharedFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxRowsOfSharedFormula). يقوم بتعيين الحد الأقصى للصفوف المشتركة إلى 5 وإضافة الصيغة المشتركة في الخلية D1 ل 100 صفوف وحفظها في ملف إكسيل الناتج. إذا استخرجت محتويات ملف إكسيل الناتج وفحصت *sheet1.xml*، سترى أن الصيغة المشتركة تنقسم بعد كل 5 صفوف كما هو موضح في اللقطة المصورة أعلاه.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Formulas-SpecifyMaximumRowsOfSharedFormula.java" >}}
{{< app/cells/assistant language="java" >}}
