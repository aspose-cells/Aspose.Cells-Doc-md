---  
title: عرض وإخفاء ورقات العمل والتبويبات باستخدام Node.js عبر C++  
linktitle: إظهار وإخفاء الأوراق والألسنة  
type: docs  
weight: 10  
url: /ar/nodejs-cpp/show-and-hide-worksheets-and-tabs/  
description: توفر هذه المقالة رمز نموذجياً لاستخدام واجهة برمجة التطبيقات Node.js أو مكتبة Node.js لعرض وإخفاء ورقة عمل إكسل برمجياً. بالإضافة إلى ذلك، كيفية عرض وإخفاء تبويبات دفتر عمل إكسل.  
---  

{{% alert color="primary" %}}  
تسمح Aspose.Cells للمستخدم بإظهار وإخفاء عناصر دفتر العمل بما في ذلك الأوراق والألسنة.  
{{% /alert %}}  

## **إظهار وإخفاء ورقة عمل**  

يمكن أن يحتوي ملف إكسل على ورقة عمل واحدة أو أكثر. كلما أنشأنا ملف إكسل، نضيف أوراق عمل إلى الملف إكسل الذي نعمل فيه. تكون كل ورقة عمل في ملف إكسل مستقلة عن الورقة العمل الأخرى بوجود بياناتها الخاصة وإعدادات التنسيق وما إلى ذلك. في بعض الأحيان، قد يحتاج المطورون إلى إخفاء بعض الأوراق العمل وجعل البعض الآخر مرئية في ملف إكسل لمصلحتهم الخاصة. لذا، **Aspose.Cells** يتيح للمطورين التحكم في رؤية أوراق العمل في ملفاتهم إكسل.  

توفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)، التي تمثل ملف إكسل. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) على مجموعة [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) تمكن من الوصول إلى كل ورقة عمل في الملف.  

تمثل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). تقدم فئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) مجموعة واسعة من الخصائص والطرق لإدارة أوراق العمل. للتحكم في رؤية ورقة العمل، استخدم خاصية [**Worksheet.isVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isVisible--) من فئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). [**Worksheet.isVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isVisible--) هي خاصية منطقية، مما يعني أنها يمكن أن تخزن فقط قيمة **صحيح** أو **خطأ**.  

### **جعل ورقة العمل مرئية**  

اجعل ورقة عمل مرئية عن طريق تعيين خاصية [**Worksheet.isVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isVisible--) لفئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) إلى **صحيح**.  

### **إخفاء ورقة عمل**  

أخفِ ورقة عمل عن طريق تعيين خاصية [**Worksheet.isVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isVisible--) لفئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) إلى **خطأ**.  

```javascript
try {
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fs = require("fs");
const fstream = fs.createReadStream(filePath);

// Instantiating a Workbook object with opening the Excel file through the file stream
const chunks = [];
fstream.on('data', chunk => chunks.push(chunk));
fstream.on('end', () => {
const workbook = new AsposeCells.Workbook(Buffer.concat(chunks)); // Fixed from stream to Blob

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Hiding the first worksheet of the Excel file
worksheet.setIsVisible(false);

// Saving the modified Excel file in default (that is Excel 2003) format
workbook.save(path.join(dataDir, "output.out.xls"));

// Closing the file stream to free all resources
fstream.close();
```  

## **إظهار وإخفاء الألسنة**  

إذا نظرت عن كثب في أسفل ملف Microsoft Excel، سترى عددًا من الضوابط. تشمل هذه:  

- ألسنة الصفحات.  
- أزرار تمرير الألسنة.  

تمثل ألسنة الصفحات الأوراق العمل في ملف الإكسل. انقر على أي علامة تبويب للانتقال إلى تلك الورقة العمل. كلما زاد عدد الأوراق العمل في الدفتر الحسابي، زادت ألسنة الصفحة. إذا كان لديك عدد جيد من الأوراق العمل في دفتر العمل، يلزمك الأزرار للتنقل خلالها. لذا، يوفر مايكروسوفت إكسل أزرار تمرير الألسنة للتمرير من خلال ألسنة الصفحات.  

باستخدام Aspose.Cells، يمكن للمطورين التحكم في رؤية علامات الجدول وأزرار التمرير في ملفات Excel.  

توفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)، التي تمثل ملف إكسل. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) على مجموعة واسعة من الخصائص والطرق لإدارة ملف إكسل. للتحكم في رؤية علامات التبويب في ملف إكسل، يمكن للمطورين استخدام خاصية [**WorkbookSettings.getShowTabs()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShowTabs--) من فئة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook). [**WorkbookSettings.getShowTabs()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShowTabs--) هي خاصية منطقية، مما يعني أنها يمكن أن تخزن فقط قيمة **صحيح** أو **خطأ**.  

### **جعل علامات التبويب مرئية**  

اجعل علامات التبويب مرئية باستخدام خاصية [**WorkbookSettings.getShowTabs()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShowTabs--) من فئة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) لتكون **صحيح**.  

### **إخفاء علامات التبويب**  

اخفِ علامات التبويب في ملف إكسل عن طريق تعيين خاصية [**WorkbookSettings.getShowTabs()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShowTabs--) من فئة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) إلى **خطأ**.  

فيما يلي مثال كامل يفتح ملف Excel (book1.xls)، يخفي علاماته ويحفظ الملف المعدل بصيغة output.xls. بعد تنفيذ الكود، سترى أن تبويبات الدفتر مخفية.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Opening the Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Hiding the tabs of the Excel file
workbook.getSettings().setShowTabs(false);

// Shows the tabs of the Excel file
// workbook.getSettings().setShowTabs(true);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```  

### **السيطرة على عرض شريط التبويب**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");
// Loading the Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Hiding the tabs of the Excel file
workbook.getSettings().setShowTabs(true);

// Adjusting the sheet tab bar width
workbook.getSettings().setSheetTabBarWidth(800);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
