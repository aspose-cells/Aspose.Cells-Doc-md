---
title: تعيين رؤوس وتذييلات مختلفة لصفحات مختلفة باستخدام Node.js عبر C++
linktitle: ضبط رؤوس وأسافل مختلفة لصفحات مختلفة
type: docs
weight: 35
url: /ar/nodejs-cpp/setting-different-headers-and-footers-for-pages-to-excel/
description: تقدم هذه المقالة رمزًا نموذجيًا يوضح كيفية تعيين رؤوس وتذييلات إعداد الصفحة لورقة العمل Excel برمجيًا باستخدام Aspose.Cells for Node.js via C++. قم بتعيين رؤوس وتذييلات للصفحات الأولى، والصفحات الفردية، والصفحات الزوجية.
keywords: تعيين رأس وتذييل Excel للصفحة الأولى Node.js عبر C++، تعيين رأس وتذييل Excel للصفحات الفردية Node.js عبر C++، تعيين رأس وتذييل Excel للصفحات الزوجية Node.js عبر C++
---

{{% alert color="primary" %}}

يدعم MS Excel تعيين رؤوس وتذييلات مختلفة للصفحة الأولى والصفحات الفردية والزوجية منذ Excel 2007.
 يدعم Aspose.Cells for Node.js via C++ نفس الميزة.

{{% /alert %}}

## **ضبط رؤوس وأسافل مختلفة في MS Excel**

**![ضبط رؤوس وأسافل مختلفة](difpage.png)**

1. انقر على **تخطيط الصفحة > عناوين الطباعة > رأس/تسفل**.
 1. تحقق من **صفحات فردية ومختلفة** أو **صفحة أولى مختلفة**.
1. أدخل رؤوس وأسافل مختلفة.

## ** تعيين رؤوس وتذييلات مختلفة مع Aspose.Cells for Node.js via C++**

تتصرف Aspose.Cells بنفس الطريقة كما تفعل Excel.
 1. يعين علامات التحقق [PageSetup.isHFDiffOddEven()](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#isHFDiffOddEven--) و [PageSetup.isHFDiffFirst()](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#isHFDiffFirst--) 
1. أدخل رؤوس وأسافل مختلفة.
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const wb = new AsposeCells.Workbook(filePath);

// Gets the setting of page setup.
const pageSetup = wb.getWorksheets().get(0).getPageSetup();
// Sets different odd and even pages
pageSetup.setIsHFDiffOddEven(true);
pageSetup.setHeader(1, "I am the header of the Odd page.");
pageSetup.setEvenHeader(1, "I am the header of the Even page.");
// Sets different first page
pageSetup.setIsHFDiffFirst(true);
pageSetup.setFirstPageHeader(1, "I am the header of the First page.");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
