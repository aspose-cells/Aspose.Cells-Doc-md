---
title: اقرأ تسميات المحاور بعد حساب المخطط
description: تعرف على كيفية قراءة تسميات المحاور في Aspose.Cells for .NET بعد حساب الرسم البياني. سيوضح لك دليلنا كيفية الوصول إلى تسميات المحاور واستردادها، بما في ذلك تنسيقها وموضعها.
keywords: Aspose.Cells for .NET, chart, axis labels, calculation, reading, accessing, retrieving, formatting, positioning.
type: docs
weight: 90
url: /ar/net/read-axis-labels-after-calculating-the-chart/
---
##  **سيناريوهات الاستخدام المحتملة**

يمكنك قراءة تسميات محاور المخطط الخاص بك بعد حساب قيمها باستخدام[**الرسم البياني.احسب()**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/calculate/)طريقة. الرجاء استخدام[**المحور.GetAxisTexts()**](https://reference.aspose.com/cells/net/aspose.cells.charts/axis/getaxistexts/) طريقة لهذا الغرض والتي ستعيد قائمة تسميات المحاور.

##  **اقرأ تسميات المحاور بعد حساب المخطط**

الرجاء مراجعة نموذج التعليمات البرمجية التالي الذي يقوم بتحميل ملف[عينة من ملف إكسل](ReadAxisLabels.xlsx)ويقرأ تسميات محور الفئة للمخطط في ورقة العمل الأولى. ثم يقوم بطباعة قيم تسميات المحاور على وحدة التحكم. يرجى الاطلاع على مخرجات وحدة التحكم الخاصة بنموذج التعليمات البرمجية الموضح أدناه للحصول على مرجع.

##  **عينة من الرموز**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Charts-ReadAxisLabelsAfterCalculatingTheChart.cs" >}}

##  **إخراج وحدة التحكم**

{{< highlight "csharp" >}}

 Category Axis Labels:

\---------------------

Iran

China

USA

Brazil

England

{{< /highlight >}}
