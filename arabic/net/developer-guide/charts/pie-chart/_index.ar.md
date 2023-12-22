---
title: إنشاء مخطط دائري مع خطوط الزعيم
description: تعرف على كيفية استخدام Aspose.Cells for .NET لإنشاء مخطط دائري بخطوط رئيسية في Microsoft Excel. سيوضح دليلنا كيفية إضافة خطوط رئيسية تربط نقاط البيانات لوسيلة الإيضاح وتعزز الوضوح العام للمخطط الخاص بك.
keywords: Aspose.Cells for .NET, Pie Chart, Leader Lines, Microsoft Excel, Data Visualization, Chart Customization.
linktitle: مخطط دائري
type: docs
weight: 45
url: /ar/net/creating-pie-chart-with-leader-lines/
---
{{% alert color="primary" %}}

تشرح هذه المقالة كيفية إنشاء مخطط دائري بخطوط رئيسية من البداية أثناء استخدام Aspose.Cells for .NET API. في Excel، يتم تعيين خيار "إظهار الخطوط الرئيسية" افتراضيًا، لذلك عندما تقوم بإنشاء مخطط دائري في Excel، يتم عرض الخطوط الرئيسية. ومع ذلك، أثناء إنشاء مخطط مماثل باستخدام واجهات برمجة التطبيقات Aspose.Cells، يجب عليك تعيين صراحة[**سلسلة.HasLeaderLines**](https://reference.aspose.com/cells/net/aspose.cells.charts/series/properties/hasleaderlines) ملكية.

{{% /alert %}}

 لتوضيح استخدام Aspose.Cells for .NET API لإنشاء مخطط دائري بخطوط رئيسية، سنقوم أولاً بإنشاء مخطط جديد[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) وإدخال بعض البيانات التي ستكون بمثابة مصدر بيانات السلسلة. وبمجرد الانتهاء من البيانات، سوف نقوم بإضافة[**جدول**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) من النوع[**ChartType.Pie**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)لمجموعة الرسوم البيانية وضبط جوانبها المختلفة للحصول على عرض الرسم البياني المطلوب.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-CreateWorkbook.cs" >}}

لقد قمنا حتى الآن بإنشاء مخطط دائري وحددنا جوانبه المختلفة. سنقوم الآن بتشغيل الخطوط الرئيسية للمخطط. يرجى ملاحظة أنه لإظهار الخطوط الرئيسية، يتعين علينا تحريك تسميات البيانات قليلاً.

يقوم الجزء التالي من التعليمات البرمجية بتشغيل الأسطر السابقة، وتحديث المخطط، ثم حساب مواضع تسميات البيانات لنقلها وفقًا لذلك.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-TurnOnLeaderLines.cs" >}}

وأخيرًا، يحفظ التعليمة البرمجية التالية المخطط بتنسيق الصورة والمصنف بتنسيق XLSX.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-SaveChartInImageAndWorkbookInXLSX.cs" >}}

|**الرسم البياني الدائري الناتج**|
| :- |
|![ما يجب القيام به:image_alt_text](creating-pie-chart-with-leader-lines_1.png)|

##  **مواضيع متقدمة**
- [شريحة مخصصة أو ألوان القطاع في المخطط الدائري](/cells/ar/net/custom-slice-or-sector-colors-in-pie-chart/)
- [اكتشف ما إذا كانت نقاط البيانات موجودة في الدائرة الثانية أو الشريط على مخطط دائري أو شريط دائري](/cells/ar/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/)

##  مقالات ذات صلة

- [إنشاء الرسوم البيانية](/cells/ar/net/creating-charts/)
- [تخصيص الرسوم البيانية](/cells/ar/net/customizing-charts/)
- [تنسيق البيانات في الرسوم البيانية](/cells/ar/net/data-formatting-in-charts/)
- [ضبط مظهر الرسم البياني](/cells/ar/net/setting-chart-appearance/)

