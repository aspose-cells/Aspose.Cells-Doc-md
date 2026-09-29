---
title: حدد ما إذا كان جدول الإحصائيات المحورية متوافقًا مع Excel2003 أثناء تحديث جدول الإحصائيات المحورية
type: docs
weight: 80
url: /ar/nodejs-cpp/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
---

{{% alert color="primary" %}}

يوفر Aspose.Cells for Node.js via C++ خاصية [**PivotTable.setIsExcel2003Compatible**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#setIsExcel2003Compatible-boolean-) والتي يمكن استخدامها لتحديد ما إذا كان جدول Pivot متوافقًا مع Excel2003 أثناء تحديث جدول Pivot. إذا كان صحيحًا، يجب أن يكون النص أقل من أو يساوي 255 حرفًا، وإذا كان النص أكثر من 255 حرفًا، سيتم تقليصه. إذا **خاطئ**، فلن يكون النص مقيدًا كما ذُكر. القيمة الافتراضية هي **صحيح**.

{{% /alert %}}

## **حدد ما إذا كان جدول الإحصائيات المحورية متوافقًا مع Excel2003 أثناء تحديث جدول الإحصائيات المحورية**

الشيفرة التجريبية التالية تشرح استخدام خاصية [**PivotTable.setIsExcel2003Compatible**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#setIsExcel2003Compatible-boolean-). السلسلة الأصلية طولها 383 حرفًا. ولكن عندما يتم تعيين [**PivotTable.setIsExcel2003Compatible**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#setIsExcel2003Compatible-boolean-) إلى **صحيح** ويتم تحديث الجدول المحوري، يتم قص بيانات الخلية B5 للجدول المحوري ويصبح طولها 255 حرفًا. ومع ذلك، عندما يتم تعيين [**PivotTable.setIsExcel2003Compatible**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#setIsExcel2003Compatible-boolean-) إلى **خاطئة** ويتم تحديث الجدول المحوري مرة أخرى، فإن بيانات الخلية B5 من الجدول المحوري لا تتم قصها وتبقى طولها 383 حرفًا. يرجى قراءة التعليقات داخل الكود لفهم هذه الخاصية بشكل أفضل.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-SpecifyCompatibility-1.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
