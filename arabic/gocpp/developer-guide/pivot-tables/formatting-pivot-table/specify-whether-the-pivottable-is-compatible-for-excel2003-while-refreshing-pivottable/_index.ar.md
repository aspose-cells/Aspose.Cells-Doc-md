---
title: تحديد ما إذا كان الجدول المحوري متوافقًا مع Excel2003 أثناء تحديث الجدول المحوري مع Golang عبر C++
linktitle: تحديد التوافق مع Excel2003 في PivotTable
type: docs
weight: 80
url: /ar/go-cpp/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
description: تعلم كيفية تحديد توافق PivotTable مع Excel2003 باستخدام Aspose.Cells for C++ أثناء تحديث PivotTable.
---

{{% alert color="primary" %}}

يوفر Aspose.Cells خاصية [**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/go-cpp/pivottable/isexcel2003compatible/) يمكنك استخدامها لتحديد ما إذا كان الجدول المحوري متوافقًا مع Excel2003 أثناء تحديث الجدول المحوري. إذا كانت قيمة الصحيح، يجب أن يكون السلسلة أقل من أو تساوي 255 حرفًا، لذا إذا كانت السلسلة أكبر من 255 حرفًا، سيتم قصها. إذا كانت **خاطئة**، فلن تكون للسلسلة القيد السابق. القيمة الافتراضية هي **صحيح**.

{{% /alert %}}

## **حدد ما إذا كان جدول الإحصائيات المحورية متوافقًا مع Excel2003 أثناء تحديث جدول الإحصائيات المحورية**

الشيفرة التجريبية التالية تشرح استخدام خاصية [**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/go-cpp/pivottable/isexcel2003compatible/). السلسلة الأصلية طولها 383 حرفًا. ولكن عندما يتم تعيين [**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/go-cpp/pivottable/isexcel2003compatible/) إلى **صحيح** ويتم تحديث الجدول المحوري، يتم قص بيانات الخلية B5 للجدول المحوري ويصبح طولها 255 حرفًا. ومع ذلك، عندما يتم تعيين [**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/go-cpp/pivottable/isexcel2003compatible/) إلى **خاطئة** ويتم تحديث الجدول المحوري مرة أخرى، فإن بيانات الخلية B5 من الجدول المحوري لا تتم قصها وتبقى طولها 383 حرفًا. يرجى قراءة التعليقات داخل الكود لفهم هذه الخاصية بشكل أفضل.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyWhetherThePivottableIsCompatibleForExcel2003WhileRefreshingPivottable.go" >}}
