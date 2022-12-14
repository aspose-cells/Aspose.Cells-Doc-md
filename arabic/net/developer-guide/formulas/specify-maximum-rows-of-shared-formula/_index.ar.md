---
title: حدد الحد الأقصى لصفوف الصيغة المشتركة
type: docs
weight: 40
url: /ar/net/specify-maximum-rows-of-shared-formula/
---
## **سيناريوهات الاستخدام الممكنة**

الحد الأقصى للصفوف الافتراضية للصيغة المشتركة هو 64. يمكن أن يكون أي رقم ، على سبيل المثال يمكن أن يكون 1000. يتغير أداء الصيغة المشتركة بعدد مختلف من الصفوف. لذلك ، يوفر Aspose.Cells الامتداد[**المصنف.الإعدادات. MaxRowsOfSharedFormula**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxrowsofsharedformula)الخاصية التي يمكن استخدامها لتحديد الصفوف القصوى للصيغة المشتركة. سيتم تقسيم الصيغة المشتركة إلى عدة صيغ مشتركة إذا كانت الصفوف الإجمالية للصيغة المشتركة أكبر مما هو موضح في لقطة الشاشة التالية.

![ما يجب القيام به: image_بديل_نص](specify-maximum-rows-of-shared-formula_1.png)

## **حدد الحد الأقصى لصفوف الصيغة المشتركة**

يشرح نموذج التعليمات البرمجية التالي استخدام ملف[**المصنف.الإعدادات. MaxRowsOfSharedFormula**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxrowsofsharedformula) منشأه. يقوم بتعيين الحد الأقصى لصفوف الصيغة المشتركة إلى 5 ويضيف الصيغة المشتركة في الخلية D1 لـ 100 صف ويحفظ في[إخراج ملف Excel](61767856.xlsx). إذا قمت باستخراج محتويات ملف Excel الناتج وتحقق من ملف*ورقة 1.xml*، سترى انقسام الصيغة المشتركة بعد كل 5 صفوف كما هو موضح في لقطة الشاشة أعلاه.

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Formulas-SpecifyMaximumRowsOfSharedFormula.cs" >}}
