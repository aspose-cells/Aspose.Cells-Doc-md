---
title: حساب عامل تحجيم إعداد الصفحة
type: docs
weight: 300
url: /ar/python-net/calculate-page-setup-scaling-factor/
description: يقدم هذا المقال رمز نموذج يوضح كيفية استخدام Aspose.Cells لـ Python via .NET APIs لحساب معامل تكبير إعداد الصفحة باستخدام خيار التلاؤم لعرض n صفحة (صفحات) واسعة و m عالية من ورقة عمل إكسل برمجياً.
keywords: مكتبة إكسل بايثون، بايثون التناسب مع n صفحة عرض واسعة و m عالية، حساب معامل تكبير إعداد الصفحة في بايثون.
---

{{% alert color="primary" %}}

عند تعيين تحجيم إعداد الصفحة باستخدام خيار **تناسب عرض صفحة n بارتفاع صفحة m**، يقوم Microsoft Excel بحساب عامل تحجيم إعداد الصفحة. يمكنك حساب نفس الشيء باستخدام خاصية [**SheetRender.page_scale**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/page_scale). تعيد هذه الخاصية قيمة من نوع double يمكن تحويلها إلى قيمة نسبية. على سبيل المثال، إذا عادت 0.5 فهذا يعني أن عامل التحجيم هو 50%.

{{% /alert %}}

الرمز العيني التالي يوضح كيفية حساب عامل تحجيم إعداد الصفحة باستخدام الخاصية [**SheetRender.page_scale**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/page_scale).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-CalculateScalingFactor-CalculatePageSetupScalingFactor.py" >}}
{{< app/cells/assistant language="python-net" >}}
