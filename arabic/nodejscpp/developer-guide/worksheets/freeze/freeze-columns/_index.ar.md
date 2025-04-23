---  
title: تجميد العمود الأول أو الأعمدة الأولى من ورقة عمل Excel باستخدام Node.js عبر C++  
linktitle: تجميد الأعمدة  
type: docs  
weight: 190  
url: /ar/nodejs-cpp/how-to-freeze-columns-of-excel-worksheet  
description: تعلّم كيفية تجميد الأعمدة اليسرى من أوراق عمل Excel برمجيًا باستخدام Aspose.Cells for Node.js via C++.  
keywords: تجميد الأعمدة اليسرى، تجميد الأعمدة الأولى، قفل العمود/الأعمدة  
---  

## **مقدمة**  

في هذه المقالة، سنتعلم كيف نجمّد العمود(الأعمدة) اليسرى. عندما يكون لديك كمية هائلة من البيانات في صف، قد لا تتمكن من رؤية الأعمدة اليسرى عند التمرير الأفقي لورقة العمل. يمكنك تجميد وقفل العمود(الأعمدة) الأولى بحيث يمكنك رؤية الجزء المجمد حتى عند تمرير باقي البيانات. يمكنك بسهولة رؤية رؤوس الأعمدة في الأعمدة اليسرى.  

## **تجميد الأعمدة في Excel**  

**![تجميد الأعمدة اليسرى في Excel](freeze-columns.png)**  

1. إذا أردت تجميد العمود/الأعمدة اليسرى، فابدأ بتحديد العمود تحت العمود الذي يحتاج إلى تجميده.
2. انقر على عرض > تجميد الأجزاء.
3. في القائمة المنسدلة، انقر فوق تجميد العمود الأول.
4. إذا قمت بالتمرير لأسفل، سيكون العمود الأول دائماً في العرض الأيسر.

**![عمود مجمد](frozen-columns.png)**  

كما ترى، العمود الأول مجمد، والعمود الأول دائمًا ثابت في الأعلى عند التمرير أفقيًا.

تتيح لك ميزة تجميد الأعمدة عرض بياناتك الطويلة بدون عناء تتبع العمود الأول.

## **تجميد الأعمدة مع Aspose.Cells for Node.js via C++**  
من السهل تجميد العمود الأول (الأعمدة الأولى) باستخدام Aspose.Cells for Node.js via C++.  
يرجى استخدام طريقة [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#freezePanes-number-number-number-number-) لتجميد الأعمدة عند العمود المحدد.  
1. إنشاء دفتر العمل لفتح الملف أو إنشاء ملف فارغ.
2. تجميد العمود الأول باستخدام طريقة Worksheet.freezePanes()
3. حفظ الملف.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Freeze.xlsx");
// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);
// Freezing panes at the second column
workbook.getWorksheets().get(0).freezePanes("B1", 0, 1);
// Saving the file
workbook.save("frozen.xlsx");
```  

المرفق [ملف الإكسيل عينة](Freeze.xlsx).  

