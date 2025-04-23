---
title: ضبط رؤوس وأسافل مختلفة لصفحات مختلفة
type: docs
weight: 35
url: /ar/net/setting-different-headers-and-footers-for-pages-to-Excel/
description: يقدم هذا المقال رمزًا عينيًا يُظهر كيفية ضبط رؤوس وأسافل مختلفة لإعدادات تخطيط الصفحة في ورقة Excel بشكل برمجي باستخدام مكتبة C# وواجهة برمجة التطبيقات .NET. يمكنك ضبط رؤوس وأسافل الصفحة الأولى والصفحات الزوجية والفردية.
keywords: ضبط رأس وتسفل إكسل الصفحة الأولى c#، ضبط رأس وتسفل إكسل الصفحات الفردية c#، ضبط رأس وتسفل إكسل الصفحات الزوجية c#
---

{{% alert color="primary" %}}

تدعم MS Excel ضبط رؤوس وأسافل مختلفة للصفحة الأولى والصفحات الفردية والصفحات الزوجية منذ Excel 2007.
يدعم Aspose.Cells نفس الميزة.

{{% /alert %}}

## **ضبط رؤوس وأسافل مختلفة في MS Excel**

**![ضبط رؤوس وأسافل مختلفة](difpage.png)**

1. انقر على **تخطيط الصفحة > عناوين الطباعة > رأس/تسفل**.
1. تفقد **صفحات فردية وزوجية مختلفة** أو **صفحة أولى مختلفة**.
1. أدخل رؤوس وأسافل مختلفة.

## **ضبط رؤوس وأسافل مختلفة باستخدام Aspose.Cells**

تتصرف Aspose.Cells بنفس الطريقة كما تفعل Excel.
1. يقوم بتعيين العلامات [PageSetup.IsHFDiffOddEven](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/ishfdiffoddeven/) و [PageSetup.IsHFDiffFirst](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/IsHFDiffFirst/) 
1. أدخل رؤوس وأسافل مختلفة.
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "DiffHeaderFooter.cs" >}}
{{< app/cells/assistant language="csharp" >}}
