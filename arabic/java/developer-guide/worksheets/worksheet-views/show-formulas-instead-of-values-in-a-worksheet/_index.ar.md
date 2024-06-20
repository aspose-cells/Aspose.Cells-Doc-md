---
title: اظهر الصيغ بدلاً من القيم في ورقة عمل
type: docs
weight: 100
url: /ar/java/show-formulas-instead-of-values-in-a-worksheet/
---

{{% alert color="primary" %}}

من الممكن عرض الصيغ بدلاً من القيم المحسوبة في Microsoft Excel باستخدام خيار *إظهار الصيغ* من شريط **الصيغ**. عند عرض الصيغ، يعرض Microsoft Excel الصيغ في ورقة العمل. يمكنك الوصول إلى نفس الشيء باستخدام Aspose.Cells.

{{% /alert %}} 

يوفر Aspose.Cells خاصية [**Worksheet.setShowFormulas()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ShowFormulas). قم بتعيين هذا إلى **true** لإعداد Microsoft Excel لعرض الصيغ.

الصورة التالية تظهر ورقة العمل التي تحتوي على صيغة في الخلية A3: =Sum(A1:A2).

**ورقة عمل بصيغة في الخلية A3**

![todo:image_alt_text](show-formulas-instead-of-values-in-a-worksheet_1.png)

تُظهر الصورة التالية الصيغة بدلاً من القيمة المحسوبة، بعد تمكين خاصية [**Worksheet.setShowFormulas()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ShowFormulas) بالقيمة **true** باستخدام Aspose.Cells.

**تعرض الورقة الآن الصيغة بدلاً من القيمة المحسوبة**

![todo:image_alt_text](show-formulas-instead-of-values-in-a-worksheet_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ShowFormulas-ShowFormulas.java" >}}
