---  
title: كيفية تعيين خاصية AutoRecover للمصنف باستخدام Node.js عبر C++  
linktitle: كيفية تعيين خاصية AutoRecover للفصل  
type: docs  
weight: 220  
url: /ar/nodejs-cpp/how-to-set-autorecover-property-of-workbook/  
description: تعلم كيفية تعيين خاصية AutoRecover للمصنف باستخدام Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
يمكنك استخدام Aspose.Cells لتعيين خاصية AutoRecover للمصنف. القيمة الافتراضية لهذه الخاصية هي **true**. عند تعيينها على **false** في مصنف، يقوم Microsoft Excel بتعطيل AutoRecover (النسخ التلقائي) على ذلك الملف.  

يوفر Aspose.Cells خاصية [**Workbook.getAutoRecover()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getAutoRecover--) لتمكين أو تعطيل هذا الخيار.  
{{% /alert %}}  

يوضح الكود التالي كيفية استخدام خاصية [**Workbook.getAutoRecover()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getAutoRecover--) للمصنف. يقرأ أولاً القيمة الافتراضية لهذه الخاصية وهي **true**، ثم يعينها إلى **false** ويحفظ المصنف. ثم يفتح المصنف مرة أخرى ويقرأ قيمة الخاصية التي تكون **false** الآن.  

## كود Node.js لتعريف خاصية AutoRecover للمصنف  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const workbook = new AsposeCells.Workbook();

// Read AutoRecover property
console.log("AutoRecover: " + workbook.getSettings().getAutoRecover());

// Set AutoRecover property to false
workbook.getSettings().setAutoRecover(false);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));

// Read the saved workbook again
const workbook2 = new AsposeCells.Workbook(path.join(dataDir, "output_out.xlsx"));

// Read AutoRecover property
console.log("AutoRecover: " + workbook2.getSettings().getAutoRecover());
```  

## **الناتج**  

فيما يلي مخرجات وحدة الإدخال الخاصة بالكود المصدري أعلاه.  

{{< highlight java >}}  
AutoRecover: True  
AutoRecover: False  
{{< /highlight >}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
