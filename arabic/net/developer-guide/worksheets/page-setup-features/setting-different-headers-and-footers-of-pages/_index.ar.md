---
title: تعيين رؤوس وتذييلات مختلفة لصفحات مختلفة
type: docs
weight: 35
url: /ar/net/setting-different-headers-and-footers-for-pages-to-Excel/
description: توفر هذه المقالة نموذج التعليمات البرمجية الذي يوضح كيفية تعيين رؤوس وتذييلات مختلفة برمجيًا لإعدادات إعداد صفحة ورقة عمل Excel باستخدام مكتبة C# و .NET API. يمكنك تعيين الرؤوس والتذييلات للصفحة الأولى والصفحات الفردية والزوجية.
keywords: set excel header footer first page c#, set excel header footer odd pages c#, set excel header footer even pages c#
---
{{% alert color="primary" %}}

يدعم MS Excel تعيين رؤوس وتذييلات مختلفة للصفحة الأولى والصفحات الفردية وحتى الصفحات منذ Excel 2007.
Aspose.Cells يدعم نفس الميزة.

{{% /alert %}}

##  **وضع رؤوس وتذييلات مختلفة في MS Excel**

**! [تعيين رؤوس وتذييلات مختلفة] (difpage.png)**

1. انقر فوق * تخطيط الصفحة> عناوين الطباعة> الرأس / التذييل **.
1.  يفحص**مختلف الصفحات الفردية والزوجية** أو * صفحة تنوب مختلفة **.
1. أدخل رؤوس وتذييلات مختلفة.

##  **ضبط رؤوس وتذييلات مختلفة مع Aspose.Cells**

Aspose.Cells يتصرف مثل Excel.
1.  يضبط الأعلام[PageSetup.IsHFDiffOddEven](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/ishfdiffoddeven/) و[PageSetup.SHFDiffFirst](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/IsHFDiffFirst/) 
1. أدخل رؤوس وتذييلات مختلفة.
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "DiffHeaderFooter.cs" >}}
