---
title: حساب عامل تحجيم إعداد الصفحة
type: docs
weight: 300
url: /ar/net/calculate-page-setup-scaling-factor/
---
{{% alert color="primary" %}}

عندما تقوم بتعيين مقياس إعداد الصفحة باستخدام**يصلح ل n صفحة (ق) عرض في متر طول** الخيار ، Microsoft يقوم Excel بحساب عامل قياس إعداد الصفحة. يمكنك حساب نفس الشيء باستخدام[**SheetRender.PageScale**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/properties/pagescale) خاصية. تقوم هذه الخاصية بإرجاع قيمة مزدوجة يمكن تحويلها إلى قيمة النسبة المئوية. على سبيل المثال ، إذا أعاد 0.5 ، فهذا يعني أن عامل القياس هو 50٪.

{{% /alert %}}

 يوضح نموذج التعليمات البرمجية التالي كيفية حساب عامل تحجيم إعداد الصفحة باستخدام[**SheetRender.PageScale**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/properties/pagescale) خاصية.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CalculateScalingFactor-CalculatePageSetupScalingFactor.cs" >}}
