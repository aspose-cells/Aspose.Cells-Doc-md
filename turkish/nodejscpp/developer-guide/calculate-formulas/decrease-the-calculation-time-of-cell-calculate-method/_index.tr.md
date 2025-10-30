---  
title: C++ aracılığıyla Node.js kullanarak Hücre.Calculate yönteminin Hesaplama Süresini Azaltma  
linktitle: Hücre.Calculate yönteminin Hesaplama Zamanını Düşürme  
description: Bu makale, Node.js aracılığıyla C++ kullanarak Excel deki hücre hesaplama yöntemleri için hesaplama süresini azaltmak için Aspose.Cells kütüphanesinin nasıl kullanılacağını tanıtmaktadır.  
keywords: Aspose.Cells, Excel, Hücre hesaplama yöntemleri, optimizasyon, performans, hesaplama süresinin azaltılması, Node.js aracılığıyla C++  
type: docs  
weight: 100  
url: /tr/nodejs-cpp/decrease-the-calculation-time-of-cell-calculate-method/  
---  

## **Olası Kullanım Senaryoları**

Normalde, kullanıcıların [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) yöntemini bir kez çağırmasını ve ardından bireysel hücrelerin hesaplanan değerlerini almasını öneririz. Ama bazen kullanıcılar tüm çalışma kitabını hesaplamayı istemezler. Sadece tek bir hücreyi hesaplamak isterler. Aspose.Cells, bu amaçla [**CalculationOptions.getRecursive()**](https://reference.aspose.com/cells/nodejs-cpp/calculationoptions/#getRecursive--) özelliğini sağlar; bu özelliği **false** olarak ayarlayabilirsiniz, böylece bireysel hücrelerin hesaplama süresi önemli ölçüde azalır. Recursive özelliği **true** olarak ayarlandığında, tüm bağlı hücreler her çağrıda yeniden hesaplanır. Ancak, recursive özelliği **false** ise bağlı hücreler yalnızca bir kez hesaplanır ve sonraki çağrılarda yeniden hesaplanmaz.

## **Hücre.calculate() Yönteminin Hesaplama Süresini Azaltma**

Aşağıdaki örnek kod, [**CalculationOptions.getRecursive()**](https://reference.aspose.com/cells/nodejs-cpp/calculationoptions/#getRecursive--) özelliğinin kullanımını göstermektedir. Lütfen bu kodu verilen [örnek excel dosyasıyla](5113710.xlsx) çalıştırın ve konsol çıktısını kontrol edin. Recursive özelliğini **false** yapmanın hesaplama süresini önemli ölçüde azalttığını göreceksiniz. Ayrıca, bu özelliğin daha iyi anlaşılması için yorumları okuyun.

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

## **Konsol Çıktısı**

Yukarıdaki örnek kodun, verilen [örnek excel dosyasını](5113710.xlsx) kullanarak çalıştırıldığında, konsol çıktısı budur. Lütfen unutmayın, sizin çıkışınız farklı olabilir, ancak recursive özelliği **false** yapıldıktan sonra geçen süre daima **true** yapıldığından daha kısa olacaktır.

{{< highlight java >}}  
Recursive True: 96 seconds  

Recursive False: 42 seconds  
{{< /highlight >}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
