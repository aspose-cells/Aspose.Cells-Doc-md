---
title: إظهار الصيغ بدلاً من القيم في ورقة عمل
type: docs
weight: 100
url: /ar/java/show-formulas-instead-of-values-in-a-worksheet/
---
{{% alert color="primary" %}}

من الممكن إظهار الصيغ بدلاً من القيم المحسوبة في Microsoft Excel باستخدام t*إظهار الصيغ* خيار من**الصيغ**شريط. عند عرض الصيغ ، يقوم Microsoft Excel بعرض الصيغ في ورقة العمل. يمكنك تحقيق نفس الشيء باستخدام Aspose.Cells.

{{% /alert %}} 

يوفر Aspose.Cells أ[**Worksheet.setShowFormulas ()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ShowFormulas) خاصية. اضبط هذا على**حقيقي**لتعيين Microsoft Excel لعرض الصيغ.

تُظهر الصورة التالية ورقة العمل التي تحتوي على صيغة في الخلية A3: = Sum (A1: A2).

**ورقة عمل بالصيغة الموجودة في الخلية A3**

![ما يجب القيام به: image_بديل_نص](show-formulas-instead-of-values-in-a-worksheet_1.png)

 تُظهر الصورة التالية الصيغة بدلاً من القيمة المحسوبة ، والتي يتم تمكينها من خلال تعيين[**Worksheet.setShowFormulas ()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ShowFormulas) ملكية ل**حقيقي** مع Aspose.Cells.

**تعرض ورقة العمل الآن الصيغة بدلاً من القيمة المحسوبة**

![ما يجب القيام به: image_بديل_نص](show-formulas-instead-of-values-in-a-worksheet_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ShowFormulas-ShowFormulas.java" >}}
