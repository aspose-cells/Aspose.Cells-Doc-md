---
title: إنشاء رسم بياني دائري مع خطوط الريادة
description: تعرف على كيفية استخدام Aspose.Cells for .NET لإنشاء رسم بياني دائري مع خطوط الريادة في Microsoft Excel. سيقدم دليلنا كيفية إضافة خطوط الريادة التي تربط نقاط البيانات بالوسيلة التعليمية وتعزز وضوح الرسم البياني الكلي الخاص بك.
keywords: Aspose.Cells for .NET، رسم بياني دائري، خطوط الريادة، Microsoft Excel، تصور البيانات، تخصيص الرسم البياني.
linktitle: رسم بياني دائري
type: docs
weight: 45
url: /ar/net/creating-pie-chart-with-leader-lines/
---

{{% alert color="primary" %}}

يشرح هذا المقال كيفية إنشاء رسم بياني دائري مع خطوط الريادة من البداية أثناء استخدام واجهة برمجة التطبيق Aspose.Cells for .NET. في Excel، يتم تعيين خيار 'إظهار خطوط الريادة' افتراضيًا لذا عند إنشاء رسم بياني دائري في Excel، يتم عرض خطوط الريادة. ومع ذلك، أثناء إنشاء رسم بياني مماثل باستخدام واجهات Aspose.Cells، يتعين عليك ضبط خاصية [**Series.HasLeaderLines**](https://reference.aspose.com/cells/net/aspose.cells.charts/series/properties/hasleaderlines) بشكل صريح.

{{% /alert %}}

لتوضيح استخدام واجهة Aspose.Cells for .NET لإنشاء رسم بياني دائري مع خطوط الريادة، سنقوم أولاً بإنشاء [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) جديدة وإدخال بعض البيانات التي ستعمل كمصدر بيانات السلسلة. بمجرد اكتمال البيانات، سنضيف [**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) من نوع [**ChartType.Pie**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) إلى مجموعة الرسوم البيانية ونضبط جوانبه المختلفة للحصول على عرض الرسم البياني المرغوب فيه.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-CreateWorkbook.cs" >}}

حتى الآن قمنا بإنشاء رسم بياني دائري وضبط جوانبه المختلفة. الآن سنقوم بتشغيل خطوط الريادة للرسم البياني. يرجى ملاحظة أنه لعرض خطوط الريادة، علينا نقل تسميات البيانات قليلاً.

يقوم الكود التالي بتشغيل خطوط الريادة، يحدث الرسم البياني، ومن ثم يحسب مواقع تسميات البيانات لنقلها وفقًا لذلك.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-TurnOnLeaderLines.cs" >}}

أخيرًا، يقوم الكود التالي بحفظ الرسم البياني بتنسيق الصورة ودفتر العمل بتنسيق XLSX.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-SaveChartInImageAndWorkbookInXLSX.cs" >}}

|**الرسم البياني الناتج**|
| :- |
|![todo:image_alt_text](creating-pie-chart-with-leader-lines_1.png)|

## **مواضيع متقدمة**
- [لون قطاع مخصص أو ألوان في الرسم البياني الدائري](/cells/ar/net/custom-slice-or-sector-colors-in-pie-chart/)
- [العثور على ما إذا كانت نقاط البيانات في الفقاعة الثانية أو العمود على مخطط 'بي of بي' أو 'عمود من بي'](/cells/ar/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/)

## مقالات ذات صلة

- [إنشاء الرسوم البيانية](/cells/ar/net/creating-charts/)
- [تخصيص الرسوم البيانية](/cells/ar/net/customizing-charts/)
- [تنسيق البيانات في الرسوم البيانية](/cells/ar/net/data-formatting-in-charts/)
- [ضبط مظهر الرسم البياني](/cells/ar/net/setting-chart-appearance/)

{{< app/cells/assistant language="csharp" >}}
