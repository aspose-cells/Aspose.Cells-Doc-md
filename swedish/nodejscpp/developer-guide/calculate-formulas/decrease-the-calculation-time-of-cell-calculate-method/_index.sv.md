---  
title: Minska beräkningstiden för Cell.Calculate metoden med Node.js via C++  
linktitle: Minska beräkningstiden för Cell.Calculate metoden  
description: Denna artikel introducerar hur man använder Aspose.Cells biblioteket för att minska beräkningstiden för cellberäkningsmetoder i Excel med Node.js via C++.   
keywords: Aspose.Cells, Excel, Cellberäkningsmetoder, optimering, prestanda, minskning av beräkningstid, Node.js via C++  
type: docs  
weight: 100  
url: /sv/nodejs-cpp/decrease-the-calculation-time-of-cell-calculate-method/  
---  

## **Möjliga användningsscenario**

Vanligtvis rekommenderar vi användare att anropa [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) metod en gång och sedan få de beräknade värdena för enskilda celler. Men ibland vill användare inte beräkna hela arbetsboken. De vill bara beräkna en enskild cell. Aspose.Cells erbjuder egenskapen [**CalculationOptions.getRecursive()**](https://reference.aspose.com/cells/nodejs-cpp/calculationoptions/#getRecursive--), som du kan ställa in till **false** för att avsevärt minska beräkningstiden för enskilda celler. När den rekursiva egenskapen är inställd på **true**, så omberäknas alla beroende celler vid varje anrop. När den är **false** beräknas beroende celler endast en gång och beräknas inte på nyare anrop.

## **Minska beräkningstiden för Cell.calculate() metod**

Följande exempelkod visar användningen av egenskapen [**CalculationOptions.getRecursive()**](https://reference.aspose.com/cells/nodejs-cpp/calculationoptions/#getRecursive--). Kör denna kod med den givna [exempel excelfilen](5113710.xlsx) och kontrollera dess konsolutmatning. Du kommer att se att inställningen av egenskapen för rekursion till **false** minskar beräkningstiden avsevärt. Läs också kommentarerna för bättre förståelse av denna egenskap.

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

## **Konsoloutput**

Detta är utdata från konsolen för ovanstående exempel när det körs med den givna [exempel excelfilen](5113710.xlsx) på vår maskin. Observera att din utdata kan skilja sig, men den förflutna tiden efter att egenskapen för rekursion ställts in till **false** kommer alltid att vara mindre än att den ställs in till **true**.

{{< highlight java >}}  
Recursive True: 96 seconds  

Recursive False: 42 seconds  
{{< /highlight >}}  

