---
title: حدد ما إذا كان جدول الإحصائيات المحورية متوافقًا مع Excel2003 أثناء تحديث جدول الإحصائيات المحورية
type: docs
weight: 80
url: /ar/python-net/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
description: يوضح هذا المقال كيفية تحديد ما إذا كانت PivotTable متوافقة مع Excel2003 أثناء تحديث PivotTable باستخدام Aspose.Cells لـ Python via .NET.
keywords: Aspose.Cells for Python Excel، مكتبة Excel Python، حدد ما إذا كانت PivotTable متوافقة مع Excel2003 أثناء تحديث PivotTable
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET يوفر خاصية [**PivotTable.is_excel_2003_compatible**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/) التي يمكنك استخدامها لتحديد ما إذا كانت PivotTable متوافقة مع Excel2003 أثناء تحديث PivotTable. إذا كانت القيمة **صحيحة**، يجب أن تكون السلسلة أقل من أو تساوي 255 حرفًا، لذا إذا كانت السلسلة أكبر من 255 حرفًا، فسيتم قصها. إذا كانت القيمة **خاطئة**، فلن تكون للسلسلة المذكورة القيود السابقة. القيمة الافتراضية هي **صحيحة**.

{{% /alert %}}

## **كيفية تحديد ما إذا كانت PivotTable متوافقة مع Excel2003 أثناء تحديث PivotTable**

الشيفرة التجريبية التالية تشرح استخدام خاصية [**PivotTable.is_excel_2003_compatible**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/). السلسلة الأصلية طولها 383 حرفًا. ولكن عندما يتم تعيين [**PivotTable.is_excel_2003_compatible**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/) إلى **صحيح** ويتم تحديث الجدول المحوري، يتم قص بيانات الخلية B5 للجدول المحوري ويصبح طولها 255 حرفًا. ومع ذلك، عندما يتم تعيين [**PivotTable.is_excel_2003_compatible**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/) إلى **خاطئة** ويتم تحديث الجدول المحوري مرة أخرى، فإن بيانات الخلية B5 من الجدول المحوري لا تتم قصها وتبقى طولها 383 حرفًا. يرجى قراءة التعليقات داخل الكود لفهم هذه الخاصية بشكل أفضل.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SpecifyCompatibility-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
