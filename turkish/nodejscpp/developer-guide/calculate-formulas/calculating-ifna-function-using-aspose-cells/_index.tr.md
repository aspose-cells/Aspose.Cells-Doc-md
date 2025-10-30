---
title: IFNA fonksiyonunu Aspose.Cells for Node.js via C++ kullanarak hesaplama
description: Aspose.Cells kullanarak Node.js aracılığıyla C++ da IFNA fonksiyonlarını nasıl hesaplayacağınızı gösterir. Var olan bir Excel dosyasını yükleyin veya yeni oluşturun ve IFNA fonksiyonunu hesaplayın ve sonucu alın. Son olarak, değiştirilmiş Excel dosyasını diske kaydedin.
keywords: Aspose.Cells, Excel, IFNA fonksiyonları, hesaplamalar Node.js C++ aracılığıyla
type: docs
weight: 40
url: /tr/nodejs-cpp/calculating-ifna-function-using-aspose-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells, IFNA Excel fonksiyonunun hesaplamasını destekler. IFNA fonksiyonu, formül #N/A hata değeri döndürdüğünde belirttiğiniz değeri döndürür; aksi takdirde, formülün sonucunu verir.

{{% /alert %}} 
## **IFNA fonksiyonunu Aspose.Cells for Node.js via C++ kullanarak hesaplama**
Aşağıdaki örnek kod, Aspose.Cells for Node.js via C++ kullanarak IFNA fonksiyonunun hesaplamasını gösterir.


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Create new workbook
// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Add data for VLOOKUP
worksheet.getCells().get("A1").putValue("Apple");
worksheet.getCells().get("A2").putValue("Orange");
worksheet.getCells().get("A3").putValue("Banana");

// Access cell A5 and A6
const cellA5 = worksheet.getCells().get("A5");
const cellA6 = worksheet.getCells().get("A6");

// Assign IFNA formula to A5 and A6
cellA5.setFormula('=IFNA(VLOOKUP("Pear",$A$1:$A$3,1,0),"Not found")');
cellA6.setFormula('=IFNA(VLOOKUP("Orange",$A$1:$A$3,1,0),"Not found")');

// Calculate the formula of workbook
workbook.calculateFormula();

// Print the values of A5 and A6
console.log(cellA5.getStringValue());
console.log(cellA6.getStringValue());
```
## **Konsol Çıktısı**
Yukarıdaki örnek kodun konsol çıktısı burada gösterilmektedir.

{{< highlight javascript >}}
 Not found

Orange
{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
