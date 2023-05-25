---
title: حساب عامل تحجيم إعداد الصفحة
type: docs
weight: 300
url: /ar/net/calculate-page-setup-scaling-factor/
description: توفر هذه المقالة نموذج التعليمات البرمجية لشرح كيفية استخدام مكتبة C# API أو .NET لحساب عامل تحجيم إعداد الصفحة باستخدام خيار Fit to n page (s) من حيث العرض في الطول m في ورقة عمل Excel برمجيًا.
keywords: Fit to n page wide by m tall excel c#, calculate page setup scaling factor c#
---
{{% alert color="primary" %}}

 عندما تقوم بتعيين مقياس إعداد الصفحة باستخدام**يصلح ل n صفحة (ق) عرض في متر طول** الخيار ، Microsoft يقوم Excel بحساب عامل قياس إعداد الصفحة. يمكنك حساب نفس الشيء باستخدام[**SheetRender.PageScale**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/properties/pagescale)ملكية. تقوم هذه الخاصية بإرجاع قيمة مزدوجة يمكن تحويلها إلى قيمة النسبة المئوية. على سبيل المثال ، إذا أعاد 0.5 ، فهذا يعني أن عامل القياس هو 50٪.

{{% /alert %}}

 يوضح نموذج التعليمات البرمجية التالي كيفية حساب عامل تحجيم إعداد الصفحة باستخدام[**SheetRender.PageScale**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/properties/pagescale) ملكية.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CalculateScalingFactor-CalculatePageSetupScalingFactor.cs" >}}
