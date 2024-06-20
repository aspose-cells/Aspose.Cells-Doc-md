---
title: قراءة تسميات المحور بعد حساب الرسم البياني
description: تعلم كيفية قراءة تسميات المحور في Aspose.Cells for Java بعد حساب الرسم البياني. سيعرض دليلنا لك كيفية الوصول إلى تسميات المحور واستردادها، بما في ذلك تنسيقها وموضعها.
keywords: Aspose.Cells for Java، رسم بياني، تسميات المحور، حساب، قراءة، الوصول، استرداد، تنسيق، موضع
type: docs
weight: 90
url: /ar/java/read-axis-labels-after-calculating-the-chart/
---

## **سيناريوهات الاستخدام المحتملة**

يمكنك قراءة تسميات محور الرسم البياني بعد حساب قيمه باستخدام الطريقة [**Chart.calculate()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart/#calculate--). يرجى استخدام الطريقة [**Axis.getAxisTexts()**](https://reference.aspose.com/cells/java/com.aspose.cells/axis/#getAxisTexts--) لهذا الغرض التي ستقوم بإرجاع قائمة تسميات المحور.

## **قراءة تسميات المحور بعد حساب الرسم البياني**

يرجى الاطلاع على الشيفرة المرجعية التالية التي تحمل الملف اكسل المرفق وتقوم بقراءة علامات محور الفئة للرسم البياني في الورقة العمل الأولى. ثم تقوم بطباعة قيم علامات المحور على واجهة الاستخدام. يرجى الاطلاع على الناتج الناتج من الشيفرة المرجعية المرفقة أدناه للإحالة.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Charts-ReadAxisLabelsAfterCalculatingTheChart.java" >}}

## **مخرجات الوحدة**

{{< highlight java >}}

 Category Axis Labels:

\---------------------

Iran

China

USA

Brazil

England

{{< /highlight >}}
