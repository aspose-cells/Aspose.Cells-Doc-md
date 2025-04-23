---
title: قراءة تسميات المحور بعد حساب الرسم البياني
description: تعلم كيفية قراءة تسميات المحاور في Aspose.Cells for .NET بعد حساب الرسم البياني. سيوفر دليلنا لك كيفية الوصول إلى تسميات المحاور واسترجاعها، بما في ذلك تنسيقها وتوضيعها.
keywords: Aspose.Cells for .NET ، رسم بياني ، تسميات المحور ، حساب ، قراءة ، الوصول ، استرجاع ، تنسيق ، توضيع.
type: docs
weight: 90
url: /ar/net/read-axis-labels-after-calculating-the-chart/
---

## **سيناريوهات الاستخدام المحتملة**

يمكنك قراءة تسميات المحاور لرسم بياني بعد حساب قيمه باستخدام الطريقة [**Chart.Calculate()**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/calculate/). يرجى استخدام الطريقة [**Axis.GetAxisTexts()**](https://reference.aspose.com/cells/net/aspose.cells.charts/axis/getaxistexts/) لهذا الغرض التي ستُرجع قائمة تسميات المحاور.

## **قراءة تسميات المحور بعد حساب الرسم البياني**

يرجى الاطلاع على رمز العينة التالي الذي يحمل [ملف Excel عيني](ReadAxisLabels.xlsx) ويقرأ تسميات المحور الفئوي للرسم البياني في الورقة العمل الأولى. ثم يقوم بطباعة قيم تسميات المحور على وحدة التحكم. يرجى الاطلاع على الإخراج على وحدة التحكم من رمز العينة الذي يلي للرجوع إليه.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Charts-ReadAxisLabelsAfterCalculatingTheChart.cs" >}}

## **مخرجات الوحدة**

{{< highlight csharp >}}

 Category Axis Labels:

\---------------------

Iran

China

USA

Brazil

England

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
