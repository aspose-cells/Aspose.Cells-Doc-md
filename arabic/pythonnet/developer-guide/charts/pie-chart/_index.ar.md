---
title: إنشاء رسم بياني دائري مع خطوط الريادة
description: تعلم كيفية استخدام Aspose.Cells للبايثون via .NET لإنشاء مخطط دائرة مع خطوط قيادية في Microsoft Excel. سيرينا دليلنا كيف تضيف خطوطًا قيادية تربط نقاط البيانات بالأسطورة وتعزز وضوح الرسم بشكل عام.
keywords: Aspose.Cells للبايثون via .NET، مخطط دائري، خطوط قيادية، Microsoft Excel، تصور البيانات، تخصيص المخططات.
linktitle: رسم بياني دائري
type: docs
weight: 45
url: /ar/python-net/creating-pie-chart-with-leader-lines/
---

{{% alert color="primary" %}}

يشرح هذا المقال كيفية إنشاء مخطط دائري مع خطوط قيادية من الصفر باستخدام API الخاص بـ Aspose.Cells للبايثون via .NET. في Excel، يتم تعيين خيار 'عرض الخطوط القيادية' بشكل افتراضي، لذلك عند إنشاء رسم دائري في Excel، تظهر الخطوط القيادية. ومع ذلك، أثناء إنشاء مخطط مماثل باستخدام API الخاص بـ Aspose.Cells للبايثون via .NET، يجب تعيين الخاصية [**Series.has_leader_lines**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/series/has_leader_lines) بشكل صريح.

{{% /alert %}}

لعرض كيفية استخدام API الخاص بـ Aspose.Cells للبايثون via .NET لإنشاء مخطط دائري مع خطوط قيادية، سنبدأ بإنشاء [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) جديد وإدخال بعض البيانات التي ستعمل كمصدر بيانات السلسلة. بمجرد وضع البيانات، سنضيف [**Chart**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart) من نوع [**ChartType.PIE**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/charttype/) إلى مجموعة الرسوم البيانية ونقوم بضبط خصائصها المختلفة للحصول على العرض المطلوب للرسم.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-CreateWorkbook.py" >}}

حتى الآن قمنا بإنشاء رسم بياني دائري وضبط جوانبه المختلفة. الآن سنقوم بتشغيل خطوط الريادة للرسم البياني. يرجى ملاحظة أنه لعرض خطوط الريادة، علينا نقل تسميات البيانات قليلاً.

يقوم الكود التالي بتشغيل خطوط الريادة، يحدث الرسم البياني، ومن ثم يحسب مواقع تسميات البيانات لنقلها وفقًا لذلك.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-TurnOnLeaderLines.py" >}}

أخيرًا، يقوم الكود التالي بحفظ الرسم البياني بتنسيق الصورة ودفتر العمل بتنسيق XLSX.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SaveChartInImageAndWorkbookInXLSX.py" >}}

|**الرسم البياني الناتج**|
| :- |
|![todo:image_alt_text](creating-pie-chart-with-leader-lines_1.png)|

## **مواضيع متقدمة**
- [لون قطاع مخصص أو ألوان في الرسم البياني الدائري](/cells/ar/python-net/custom-slice-or-sector-colors-in-pie-chart/)
- [العثور على ما إذا كانت نقاط البيانات في الفقاعة الثانية أو العمود على مخطط 'بي of بي' أو 'عمود من بي'](/cells/ar/python-net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/)

## مقالات ذات صلة

- [إنشاء الرسوم البيانية](/cells/ar/python-net/creating-charts/)
- [تخصيص الرسوم البيانية](/cells/ar/python-net/customizing-charts/)
- [تنسيق البيانات في الرسوم البيانية](/cells/ar/python-net/data-formatting-in-charts/)
- [ضبط مظهر الرسم البياني](/cells/ar/python-net/setting-chart-appearance/)

{{< app/cells/assistant language="python-net" >}}
