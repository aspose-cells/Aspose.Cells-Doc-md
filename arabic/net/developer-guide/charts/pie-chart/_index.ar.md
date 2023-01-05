---
title: إنشاء مخطط دائري بخطوط سابقة
linktitle: مخطط دائري
type: docs
weight: 45
url: /ar/net/creating-pie-chart-with-leader-lines/
---
{{% alert color="primary" %}}

 تشرح هذه المقالة كيفية إنشاء مخطط دائري بخطوط سابقة من البداية أثناء استخدام Aspose.Cells for .NET API. في Excel ، يتم تعيين الخيار "إظهار الخطوط البادئة" افتراضيًا ، لذلك عند إنشاء مخطط دائري في Excel ، تظهر الخطوط البادئة. ومع ذلك ، أثناء إنشاء مخطط مشابه باستخدام واجهات برمجة تطبيقات Aspose.Cells ، يجب عليك تعيين ملف[**السلسلة**](https://reference.aspose.com/cells/net/aspose.cells.charts/series/properties/hasleaderlines) خاصية.

{{% /alert %}}

لتوضيح استخدام Aspose.Cells for .NET API لإنشاء مخطط دائري بخطوط سابقة ، سنقوم أولاً بإنشاء مخطط دائري جديد[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) وإدخال بعض البيانات التي ستكون بمثابة مصدر بيانات السلسلة. بمجرد أن تصبح البيانات في مكانها الصحيح ، سنضيف ملف[**جدول**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) من النوع[**نوع المخطط**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)إلى مجموعة المخططات وتعيين جوانبها المختلفة للحصول على عرض المخطط المطلوب.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-CreateWorkbook.cs" >}}

لقد أنشأنا حتى الآن مخططًا دائريًا وحددنا جوانبه المختلفة. الآن سنقوم بتشغيل الخطوط الرائدة للرسم البياني. يرجى ملاحظة أنه لإظهار الخطوط الرائدة ، يتعين علينا نقل تسميات البيانات قليلاً.

يقوم الجزء التالي من التعليمات البرمجية بتشغيل الخطوط السابقة ، وتحديث المخطط ، ثم حساب مواضع تسميات البيانات لنقلها وفقًا لذلك.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-TurnOnLeaderLines.cs" >}}

أخيرًا ، يحفظ الكود التالي المخطط بتنسيق صورة والمصنف بتنسيق XLSX.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-SaveChartInImageAndWorkbookInXLSX.cs" >}}

|**الناتج التخطيط الدائري**|
|:- |
|![ما يجب القيام به: image_بديل_نص](creating-pie-chart-with-leader-lines_1.png)|

## **موضوعات مسبقة**
- [شريحة مخصصة أو ألوان قطاعية في مخطط دائري](/cells/ar/net/custom-slice-or-sector-colors-in-pie-chart/)
- [اكتشف ما إذا كانت نقاط البيانات موجودة في المخطط الدائري الثاني أو الشريطي في مخطط دائري دائري أو مخطط دائري شريطي](/cells/ar/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/)

## مقالات ذات صلة

- [إنشاء الرسوم البيانية](/cells/ar/net/creating-charts/)
- [الرسوم البيانية Cusomizing](/cells/ar/net/customizing-charts/)
- [تنسيق البيانات في الرسوم البيانية](/cells/ar/net/data-formatting-in-charts/)
- [ضبط مظهر المخطط](/cells/ar/net/setting-chart-appearance/)

