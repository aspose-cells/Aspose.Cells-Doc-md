---
title: حساب عامل تحجيم إعداد الصفحة
type: docs
weight: 300
url: /ar/net/calculate-page-setup-scaling-factor/
description: توفر هذه المقالة رمزًا عينيًا يشرح كيفية استخدام واجهة برمجة التطبيقات C# أو المكتبة .NET لحساب عامل تحجيم إعداد الصفحة باستخدام خيار Fit to n page(s) wide by m tall في ورقة العمل إكسل برمجياً.
keywords: تناسب واسع لعدد الصفحة والطول إكسل سي شارب، حساب عامل تحجيم إعداد الصفحة سي شارب
---

{{% alert color="primary" %}}

عند تعيين تحجيم إعداد الصفحة باستخدام خيار **تناسب عرض صفحة n بارتفاع صفحة m**، يقوم Microsoft Excel بحساب عامل تحجيم إعداد الصفحة. يمكنك حساب نفس الشيء باستخدام خاصية [**SheetRender.PageScale**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/properties/pagescale). تعيد هذه الخاصية قيمة من نوع double يمكن تحويلها إلى قيمة نسبية. على سبيل المثال، إذا عادت 0.5 فهذا يعني أن عامل التحجيم هو 50%.

{{% /alert %}}

الرمز العيني التالي يوضح كيفية حساب عامل تحجيم إعداد الصفحة باستخدام الخاصية [**SheetRender.PageScale**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/properties/pagescale).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CalculateScalingFactor-CalculatePageSetupScalingFactor.cs" >}}
{{< app/cells/assistant language="csharp" >}}
