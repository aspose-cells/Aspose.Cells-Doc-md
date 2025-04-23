---  
title: تقليل وقت حساب طريقة Cell.Calculate باستخدام Node.js عبر C++  
linktitle: تقليل وقت حساب أسلوب Cell.Calculate  
description: تقدم هذه المقالة شرحًا لكيفية استخدام مكتبة Aspose.Cells لتقليل زمن حساب طرق حساب الخلايا في Excel باستخدام Node.js عبر C++.  
keywords: Aspose.Cells، Excel، طرق حساب الخلايا، تحسين، الأداء، تقليل وقت الحساب، Node.js عبر C++  
type: docs  
weight: 100  
url: /ar/nodejs-cpp/decrease-the-calculation-time-of-cell-calculate-method/  
---  

## **سيناريوهات الاستخدام المحتملة**

عادةً، نوصي المستخدمين بالاتصال بطريقة [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) مرة واحدة ثم الحصول على القيم المحسوبة للخلايا الفردية. لكن أحيانًا، لا يرغب المستخدمون في حساب كامل دفتر العمل. إنهم يريدون فقط حساب خلية واحدة. توفر Aspose.Cells خاصية [**CalculationOptions.getRecursive()**](https://reference.aspose.com/cells/nodejs-cpp/calculationoptions/#getRecursive--)، والتي يمكنك تعيينها على **false** لتقليل وقت حساب الخلايا بشكل كبير. عندما تكون الخاصية العودية موجوة على **true**، يتم إعادة حساب جميع المعتمدين على الخلايا عند كل استدعاء. ومع ذلك، عندما تكون الخاصية العودية **false**، يتم حساب الخلايا المعتمدة مرة واحدة فقط ولا يتم إعادة حسابها في الاستدعاءات اللاحقة.

## **تقليل وقت الحساب باستخدام طريقة Cell.calculate()**

يوضح الكود التجريبي التالي كيفية استخدام خاصية [**CalculationOptions.getRecursive()**](https://reference.aspose.com/cells/nodejs-cpp/calculationoptions/#getRecursive--). يرجى تنفيذ هذا الكود مع ملف إكسل التجريبي المحدد [ملف إكسل تجريبي](5113710.xlsx) والتحقق من مخرجات وحدة التحكم. ستجد أن تعيين الخاصية العودية على **false** قد قلل بشكل كبير من وقت الحساب. يرجى أيضًا قراءة التعليقات لفهم أفضل لهذه الخاصية.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Test calculation time after setting recursive true
workbook.calculateFormula(); // Call calculateFormula method to initiate calculation

// Test calculation time after setting recursive false
workbook.calculateFormula(false); // Specify ignoreError as false
```  
```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

function testCalcTimeRecursive(rec) {
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load your sample workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Access first worksheet
const ws = workbook.getWorksheets().get(0);

// Set the calculation option, set recursive true or false as per parameter
const opts = new AsposeCells.CalculationOptions();
opts.setRecursive(rec);

// Start stop watch            
const start = process.hrtime();

// Calculate cell A1 one million times
for (let i = 0; i < 1000000; i++) {
ws.getCells().get("A1").calculate(opts);
}

// Stop the watch
const end = process.hrtime(start);

// Calculate elapsed time in seconds
const estimatedTime = end[0] + end[1] / 1e9;

// Print the elapsed time in seconds
console.log(`Recursive ${rec}: ${estimatedTime} seconds`);
}

// Call the function for testing
testCalcTimeRecursive(true);
testCalcTimeRecursive(false);
```

## **مخرجات الوحدة**

هذه هي مخرجات وحدة التحكم للكود التجريبي أعلاه عند تنفيذه مع ملف إكسل التجريبي المحدد [ملف إكسل تجريبي](5113710.xlsx) على جهازنا. يرجى ملاحظة أن المخرجات قد تختلف، لكن الوقت المستغرق بعد تعيين الخاصية العودية على **false** سيكون دائمًا أقل من تعيينها على **true**.

{{< highlight java >}}  
Recursive True: 96 seconds  

Recursive False: 42 seconds  
{{< /highlight >}}  

