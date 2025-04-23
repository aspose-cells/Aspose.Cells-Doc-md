---
title: حدد ما إذا كان جدول الإحصائيات المحورية متوافقًا مع Excel2003 أثناء تحديث جدول الإحصائيات المحورية
type: docs
weight: 80
url: /ar/net/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
---

{{% alert color="primary" %}}

يوفر Aspose.Cells خاصية [**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible) يمكنك استخدامها لتحديد ما إذا كان الجدول المحوري متوافقًا مع Excel2003 أثناء تحديث الجدول المحوري. إذا كانت قيمة الصحيح، يجب أن يكون السلسلة أقل من أو تساوي 255 حرفًا، لذا إذا كانت السلسلة أكبر من 255 حرفًا، سيتم قصها. إذا كانت **خاطئة**، فلن تكون للسلسلة القيد السابق. القيمة الافتراضية هي **صحيح**.

{{% /alert %}}

## **حدد ما إذا كان جدول الإحصائيات المحورية متوافقًا مع Excel2003 أثناء تحديث جدول الإحصائيات المحورية**

الشيفرة التجريبية التالية تشرح استخدام خاصية [**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible). السلسلة الأصلية طولها 383 حرفًا. ولكن عندما يتم تعيين [**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible) إلى **صحيح** ويتم تحديث الجدول المحوري، يتم قص بيانات الخلية B5 للجدول المحوري ويصبح طولها 255 حرفًا. ومع ذلك، عندما يتم تعيين [**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible) إلى **خاطئة** ويتم تحديث الجدول المحوري مرة أخرى، فإن بيانات الخلية B5 من الجدول المحوري لا تتم قصها وتبقى طولها 383 حرفًا. يرجى قراءة التعليقات داخل الكود لفهم هذه الخاصية بشكل أفضل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTableExamples-SpecifyCompatibility-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
