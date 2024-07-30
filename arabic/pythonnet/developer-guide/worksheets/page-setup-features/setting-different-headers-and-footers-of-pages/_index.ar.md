---
title: ضبط رؤوس وأسافل مختلفة لصفحات مختلفة
type: docs
weight: 35
url: /ar/python-net/setting-different-headers-and-footers-for-pages-to-Excel/
description: يوفر هذا المقال رمز عينة يوضح كيفية تعيين رءوس و أقدام مختلفة لإعدادات صفحة جدول العمل في Excel برمجياً باستخدام واجهة برمجة التطبيقات من Aspose.Cells لبيثون. يمكنك تعيين رءوس و أقدام للصفحة الأولى، الصفحات الفردية و الزوجية.
keywords: مكتبة Excel الخاصة ببيثون، بيثون تعيين رءوس و أقدام Excel للصفحة الأولى، تعيين رءوس و أقدام Excel للصفحات الفردية في بيثون، تعيين رءوس و أقدام Excel للصفحات الزوجية باستخدام بيثون.
---

{{% alert color="primary" %}}

تدعم MS Excel ضبط رؤوس وأسافل مختلفة للصفحة الأولى والصفحات الفردية والصفحات الزوجية منذ Excel 2007.
Aspose.Cells لـ Python via .NET يدعم نفس الميزة.

{{% /alert %}}

## **كيفية تعيين رؤوس وأسافل مختلفة في MS Excel**

**![ضبط رؤوس وأسافل مختلفة](difpage.png)**

1. انقر على **تخطيط الصفحة > عناوين الطباعة > رأس/تسفل**.
1. تفقد **صفحات فردية وزوجية مختلفة** أو **صفحة أولى مختلفة**.
1. أدخل رؤوس وأسافل مختلفة.

## **كيفية تعيين رؤوس وأسافل مختلفة باستخدام مكتبة Aspose.Cells لـ Python Excel**

Aspose.Cells لـ Python via .NET يتصرف بنفس طريقة Excel.
1. يضبط العلامات [PageSetup.is_hf_diff_odd_even](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/is_hf_diff_odd_even/) و [PageSetup.is_hf_diff_first](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/is_hf_diff_first/) 
1. أدخل رؤوس وأسافل مختلفة.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-DiffHeaderFooter.py" >}}
