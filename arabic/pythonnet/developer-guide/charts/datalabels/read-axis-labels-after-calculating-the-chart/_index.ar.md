---
title: قراءة تسميات المحور بعد حساب الرسم البياني
description: تعرف على كيفية قراءة علامات المحاور في Aspose.Cells for Python via .NET بعد حساب المخطط. سيرينا دليلنا كيفية الوصول إلى علامات المحاور واسترجاعها، بما في ذلك تنسيقها وتحديد موقعها.
keywords: Aspose.Cells for Python via .NET، مخطط، علامات المحاور، الحساب، القراءة، الوصول، الاسترجاع، التنسيق، التحديد بالموقع.
type: docs
weight: 90
url: /ar/python-net/read-axis-labels-after-calculating-the-chart/
---

## **سيناريوهات الاستخدام المحتملة**

يمكنك قراءة تسميات المحاور لرسم بياني بعد حساب قيمه باستخدام الطريقة [**Chart.calculate()**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/calculate/). يرجى استخدام الطريقة [**Axis.get_axis_texts()**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/axis/get_axis_texts) لهذا الغرض التي ستُرجع قائمة تسميات المحاور.

## **قراءة تسميات المحور بعد حساب الرسم البياني**

يرجى الاطلاع على رمز العينة التالي الذي يحمل [ملف Excel عيني](ReadAxisLabels.xlsx) ويقرأ تسميات المحور الفئوي للرسم البياني في الورقة العمل الأولى. ثم يقوم بطباعة قيم تسميات المحور على وحدة التحكم. يرجى الاطلاع على الإخراج على وحدة التحكم من رمز العينة الذي يلي للرجوع إليه.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ReadAxisLabelsAfterCalculatingTheChart.py" >}}

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
