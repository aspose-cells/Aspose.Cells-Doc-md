---
title: قراءة تسميات المحاور بعد حساب الرسم البياني باستخدام Golang عبر C++
linktitle: قراءة تسميات المحور بعد حساب الرسم البياني
description: تعلم كيفية قراءة تسميات المحور في Aspose.Cells for C++ بعد حساب الرسم البياني. سيرشدك دليلنا إلى كيفية الوصول واسترجاع تسميات المحاور، بما في ذلك تنسيقها وتحديد مواقعها.
keywords: Aspose.Cells for C++، المخطط، تسميات المحاور، الحساب، القراءة، الوصول، الاسترجاع، التنسيق، التوجيه.
type: docs
weight: 90
url: /ar/go-cpp/read-axis-labels-after-calculating-the-chart/
---

## **سيناريوهات الاستخدام المحتملة**

يمكنك قراءة تسميات المحاور لرسم بياني بعد حساب قيمه باستخدام الطريقة [**Chart.Calculate()**](https://reference.aspose.com/cells/go-cpp/chart/calculate/). يرجى استخدام الطريقة [**Axis.GetAxisTexts()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/axis/getaxistexts/) لهذا الغرض التي ستُرجع قائمة تسميات المحاور.

## **قراءة تسميات المحور بعد حساب الرسم البياني**

يرجى الاطلاع على رمز العينة التالي الذي يحمل [ملف Excel عيني](ReadAxisLabels.xlsx) ويقرأ تسميات المحور الفئوي للرسم البياني في الورقة العمل الأولى. ثم يقوم بطباعة قيم تسميات المحور على وحدة التحكم. يرجى الاطلاع على الإخراج على وحدة التحكم من رمز العينة الذي يلي للرجوع إليه.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ReadAxisLabelsAfterCalculatingTheChart.go" >}}
## **مخرجات الوحدة**

{{< highlight cpp >}}

 Category Axis Labels:

\---------------------

Iran

China

USA

Brazil

England

{{< /highlight >}}
