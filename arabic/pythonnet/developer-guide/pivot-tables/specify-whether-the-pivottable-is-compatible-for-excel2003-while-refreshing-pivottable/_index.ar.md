---
title: حدد ما إذا كان PivotTable متوافقًا مع Excel2003 أثناء تحديث PivotTable
type: docs
weight: 80
url: /ar/python-net/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
description: توضح هذه المقالة كيفية تحديد ما إذا كان PivotTable متوافقًا مع Excel2003 أثناء تحديث PivotTable باستخدام Aspose.Cells for Python via .NET.
keywords: Specify whether the PivotTable is compatible for Excel2003 while refreshing PivotTable
---
{{% alert color="primary" %}}

 Aspose.Cells for Python via .NET يوفر[**PivotTable.is_excel_2003_compatible**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/) الخاصية التي يمكنك استخدامها لتحديد ما إذا كان PivotTable متوافقًا مع Excel2003 أثناء تحديث PivotTable. إذا كان صحيحًا، فيجب أن تكون السلسلة أقل من أو تساوي 255 حرفًا، لذا إذا كانت السلسلة أكبر من 255 حرفًا، فسيتم اقتطاعها. إذا كانت *خطأ**، فلن تحتوي السلسلة على التقييد المذكور أعلاه. القيمة الافتراضية هي الحقيقية**.

{{% /alert %}}

##  **حدد ما إذا كان PivotTable متوافقًا مع Excel2003 أثناء تحديث PivotTable**

 يشرح نموذج التعليمات البرمجية التالي استخدام[**PivotTable.is_excel_2003_compatible**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/) ملكية. يبلغ طول السلسلة الأصلية 383 حرفًا. لكن عندما[**PivotTable.is_excel_2003_compatible**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/) تم تعيين الملكية**حقيقي** ويتم تحديث الجدول المحوري، ويتم اقتطاع بيانات الخلية B5 من الجدول المحوري ويصبح طولها 255 حرفًا. رغم ذلك، متى[**PivotTable.is_excel_2003_compatible**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/) تم تعيين الملكية**خطأ شنيع**ويتم تحديث الجدول المحوري مرة أخرى، ولا يتم اقتطاع بيانات الخلية B5 من الجدول المحوري وتظل بطول 383 حرفًا. يرجى قراءة التعليقات داخل الكود لفهم هذه الخاصية بشكل أفضل.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SpecifyCompatibility-1.py" >}}
