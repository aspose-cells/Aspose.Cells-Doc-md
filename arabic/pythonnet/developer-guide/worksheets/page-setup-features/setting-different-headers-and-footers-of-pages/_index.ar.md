---
title: ضبط رؤوس وأسافل مختلفة لصفحات مختلفة
type: docs
weight: 35
url: /ar/python-net/setting-different-headers-and-footers-for-pages-to-Excel/
description: توفر هذه المقالة رمز عينة يُظهر كيفية تعيين رؤوس وتذييلات مختلفة لإعداد صفحة ورقة في إكسل برمجياً باستخدام API الخاص بـ Aspose.Cells للبايثون. يمكنك تعيين الرؤوس والتذييلات للصفحة الأولى، الصفحات الفردية والصفحات الزوجية.
keywords: مكتبة إكسل بلغة بايثون، تعيين رأس وتذييل إكسل للصفحة الأولى، تعيين رأس وتذييل إكسل للصفحات الفردية باستخدام بايثون، تعيين رأس وتذييل إكسل للصفحات الزوجية باستخدام بايثون.
---

{{% alert color="primary" %}}

تدعم MS Excel ضبط رؤوس وأسافل مختلفة للصفحة الأولى والصفحات الفردية والصفحات الزوجية منذ Excel 2007.
يدعم Aspose.Cells للبايثون via .NET نفس الميزة.

{{% /alert %}}

## **كيفية تعيين رؤوس وتذييلات مختلفة في MS Excel**

**![ضبط رؤوس وأسافل مختلفة](difpage.png)**

1. انقر على **تخطيط الصفحة > عناوين الطباعة > رأس/تسفل**.
1. تفقد **صفحات فردية وزوجية مختلفة** أو **صفحة أولى مختلفة**.
1. أدخل رؤوس وأسافل مختلفة.

## **كيفية تعيين رؤوس وتذييلات مختلفة باستخدام مكتبة Aspose.Cells للبايثون إكسل**

يتصرف Aspose.Cells للبايثون via .NET بنفس الطريقة التي يتصرف بها إكسل.
1. يحدد أعلام [PageSetup.is_hf_diff_odd_even](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/is_hf_diff_odd_even/) و [PageSetup.is_hf_diff_first](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/is_hf_diff_first/) 
1. أدخل رؤوس وأسافل مختلفة.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-DiffHeaderFooter.py" >}}
{{< app/cells/assistant language="python-net" >}}
