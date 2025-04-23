---  
title: ضبط لون علامة تبويب ورقة العمل باستخدام Node.js عبر C++  
linktitle: تعيين لون علامة التبويب للورقة العمل  
type: docs  
weight: 120  
url: /ar/nodejs-cpp/set-worksheet-tab-color/  
description: يوضح هذا المقال رمزًا نموذجيًا لضبط لون علامة تبويب ورقة Excel برمجياً باستخدام Node.js عبر C++.  
keywords: ضبط لون علامة تبويب Excel باستخدام Node.js عبر C++، رمز لضبط لون علامة التبويب باستخدام Node.js عبر C++  
---  

{{% alert color="primary" %}}  

تسمح Aspose.Cells لك بتغيير لون علامات تبويب ورق العمل الفردية لتمييزها عن البقية. على سبيل المثال، يمكنك جعل تكاليف بلون أحمر، ومبيعات بلون أخضر، وأصول بلون أزرق، وما إلى ذلك.

{{% /alert %}}  
## **ضبط لون علامة تبويب ورق العمل باستخدام Microsoft Excel**  
1. انقر بزر الماوس الأيمن فوق علامة تبويب في ورقة العلامات في أسفل ورقة العمل الحالية.  
1. حدد **لون العلامة التبويب**.  
1. حدد لونًا من اللوحة.  
1. انقر على **موافق**.  
## **تعيين لون علامة تبويب الورقة العمل باستخدام Aspose.Cells**  
الشيفرة المثالية أدناه تظهر كيفية تعيين لون علامة تبويب باستخدام Aspose.Cells.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a new Workbook
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Book1.xlsx"));

// Get the first worksheet in the book
const worksheet = workbook.getWorksheets().get(0);

// Set the tab color
worksheet.setTabColor(AsposeCells.Color.Red);

// Save the Excel file
workbook.save(path.join(dataDir, "worksheettabcolor.out.xls"));
```  

