---  
title: تجميد أجزاء من ورقة عمل إكسل باستخدام Node.js عبر C++  
linktitle: تجميد الأجزاء  
type: docs  
weight: 190  
url: /ar/nodejs-cpp/how-to-freeze-panes-of-excel-worksheet  
description: في هذه المقالة، ستتعلم كيفية تجميد أجزاء من أوراق عمل إكسل برمجياً باستخدام Aspose.Cells for Node.js via C++.  
keywords: تجميد الأجزاء، تجميد النافذة.  
---  

## **مقدمة**  

في هذه المقالة، سنتعلم كيف نجمّد الأجزاء. عندما يكون لديك كمية كبيرة من البيانات تحت عنوان مشترك، لا يمكنك رؤية العنوان عند التمرير لأسفل ورقة العمل. ويحتوي كل سجل على العديد من البيانات. يمكنك تجميد الأجزاء بحيث يمكنك رؤية الجزء المجمد حتى عند تمرير باقي البيانات. يمكنك بسهولة رؤية الرؤوس في الصفوف العليا أو الأعمدة الأولى. التجميد وفك التجميد للأجزاء يغير فقط عرض البيانات بدون تغيير البيانات نفسها.  

## **في إكسل**  

**![تجميد الأجزاء في إكسل](Freeze-panes.png)**  

1. إذا كنت تريد تجميد الأجزاء، وتجميد الصفوف والأعمدة، فحدد أولاً خلية (مثل B2).  
2. انقر على عرض > تجميد الأجزاء.  
3. في القائمة المنسدلة، انقر على تجميد الأجزاء.  
4. إذا قمت بالتمرير لأسفل أو لليمين، فإن الصف الأول والعمود يظل معلقًا.  

**![الأجزاء المجمدة](Frozen-Panes.png)**  

كما ترى، تم تجميد الصف الأول والعمود A، والصف الثاني هو 32 والعمود المرئي الثاني هو D.  

تمكنك ميزة تجميد الأجزاء من عرض بياناتك الكبيرة بدون الحاجة إلى تتبع علامات الصف أو العمود.  

## **تجميد الأجزاء مع Aspose.Cells for Node.js via C++**  
من السهل تجميد الأجزاء باستخدام Aspose.Cells for Node.js via C++. يرجى استخدام طريقة [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#freezePanes-number-number-number-number-) لتجميد الأجزاء عند الخلية المحددة.  
1. إنشاء دفتر العمل لفتح الملف أو إنشاء ملف فارغ.  
2. تجميد الأجزاء باستخدام طريقة Worksheet.freezePanes()  
3. حفظ الملف.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Freeze.xlsx")); 
// Freezing panes at the cell B2
workbook.getWorksheets().get(0).freezePanes("B2", 1, 1);
// Saving the file
workbook.save("frozen.xlsx");
```  

المرفق [ملف الإكسيل عينة](Freeze.xlsx).  

