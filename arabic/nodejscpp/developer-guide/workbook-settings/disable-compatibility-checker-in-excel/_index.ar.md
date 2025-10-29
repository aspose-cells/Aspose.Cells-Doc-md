---  
title: تعطيل مدقق التوافق في Excel باستخدام Node.js عبر C++  
linktitle: تعطيل فاحص التوافق في الإكسيل  
type: docs  
weight: 170  
url: /ar/nodejs-cpp/disable-compatibility-checker-in-excel/  
description: تعلم كيف تعطل مدقق التوافق من خلال واجهة برمجة التطبيقات Aspose.Cells for Node.js via C++.  
keywords: Node.js تعطيل مدقق التوافق، تعطيل مدقق التوافق في Excel باستخدام Node.js عبر C++، تعطيل مدقق التوافق في المصنف.  
---  

## تعطيل مدقق التوافق في أوراق عمل Excel في Node.js  

{{% alert color="primary" %}}  
يُعلق مُدقق التوافق في Microsoft Excel علامة عند حفظ ملف في تنسيق ملف أقدم قد يتسبب في مشكلات الوظائف أو فقدان الصِدق. مُدقق التوافق هو ميزة في Microsoft Office Excel 2007 و Microsoft Excel 2010.  

عند حفظ دفتر عمل في إصدار سابق، Excel 97 من خلال Excel 2003، من Excel 2007 أو Excel 2010، يقوم مُدقق التوافق بفحص الدفتر لمعرفة ما إذا كان يحتوي على ميزات لا تدعمها الإصدار السابق. لمساعدتك في اتخاذ قرارات حول كيفية التعامل مع مشكلات التوافق، يعرض مُدقق التوافق صناديق حوار مع خيارات. يمكن أيضًا استخدامه لإنشاء تقرير عن أي مشكلات في الدفتر، أو تعطيل الميزة.  

أحيانًا، تحتاج إلى تعطيل مدقق التوافق لمصنف معين. مع واجهات برمجة التطبيقات Aspose.Cells، يمكنك فعل ذلك برمجياً بحيث لا يُشعر المستخدمون بالإحباط أو الارتباك عند ظهور مربع حوار مدقق التوافق عند إعادة حفظ الملف في Microsoft Excel يدويًا.  
{{% /alert %}}  

## **كيفية تعطيل مُدقق التوافق باستخدام Microsoft Excel**  

- (Excel 2007) على زر الأوفيس، انقر على **إعداد**, ثم **تشغيل مُدقق التوافق**, ثم قم بمسح خيار **التحقق من التوافق عند حفظ هذا الدفتر**.  

- (Excel 2010) على علامة التبويب الملف، انقر فوق **معلومات**, ثم **البحث عن مشكلات**, انقر على **التحقق من التوافق**, وبصورة نهائية، قم بمسح خيار **التحقق من التوافق عند حفظ هذا الدفتر**.  
كيفية تعطيل مُدقق التوافق باستخدام واجهات برمجة التطبيقات لـ Aspose.Cells  

## **قم بتعيين الخاصية {0} إلى **False** لتعطيل مُدقق التوافق في Microsoft Excel.**  

قم بضبط خاصية [**Workbook.getCheckCompatibility()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getCheckCompatibility--) على **false** لتعطيل مدقق التوافق في Microsoft Excel.  

### **أمثلة على الشفرة**  

يعرض الأمثلة التالية كيفية تعطيل مدقق التوافق باستخدام Aspose.Cells for Node.js via C++.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Open a template file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Disable the compatibility checker
workbook.getSettings().setCheckCompatibility(false);

const outputFilePath = path.join(dataDir, "Output_BK_CompCheck.out.xlsx");
// Saving the Excel file
workbook.save(outputFilePath);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
