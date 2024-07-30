---
title: حساب عامل تحجيم إعداد الصفحة
type: docs
weight: 300
url: /ar/python-net/calculate-page-setup-scaling-factor/
description: يقدم هذا المقال رمزًا عينيًا يشرح كيفية استخدام Aspose.Cells for Python via .NET APIs لحساب عامل تحجيم إعداد الصفحة باستخدام خيار Fit to n page(s) wide by m tall لورقة عمل Excel برمجيًا.
keywords: مكتبة Python Excel، Python Fit to n page wide by m tall excel، حساب عامل تحجيم إعداد الصفحة في Python.
---

{{% alert color="primary" %}}

عند تعيين تحجيم إعداد الصفحة باستخدام خيار **تناسب عرض صفحة n بارتفاع صفحة m**، يقوم Microsoft Excel بحساب عامل تحجيم إعداد الصفحة. يمكنك حساب نفس الشيء باستخدام خاصية [**SheetRender.page_scale**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/page_scale). تعيد هذه الخاصية قيمة من نوع double يمكن تحويلها إلى قيمة نسبية. على سبيل المثال، إذا عادت 0.5 فهذا يعني أن عامل التحجيم هو 50%.

{{% /alert %}}

الرمز العيني التالي يوضح كيفية حساب عامل تحجيم إعداد الصفحة باستخدام الخاصية [**SheetRender.page_scale**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/page_scale).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-CalculateScalingFactor-CalculatePageSetupScalingFactor.py" >}}
