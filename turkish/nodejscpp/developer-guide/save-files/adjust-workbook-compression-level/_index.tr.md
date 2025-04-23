---  
title: Node.js ile Çalışma Kitabı Sıkıştırma Seviyesini Ayarla (C++ ile)  
linktitle: Çalışma Kitabı Sıkıştırma Seviyesini Ayarla  
type: docs  
weight: 180  
url: /tr/nodejs-cpp/adjust-workbook-compression-level/  
description: Aspose.Cells for Node.js via C++ kullanarak çalışma kitabının sıkıştırma seviyesini nasıl ayarlayacağınızı öğrenin.  
---  

## **Çalışma kitabının sıkıştırma seviyesini ayarlayın**  

Geliştiriciler, büyük çalışma kitaplarıyla çalışırken sıkıştırma seviyesini ayarlayabilirler. Geliştiriciler, daha küçük dosya boyutlarını işlem süresine tercih edebilir veya tam tersini. Aspose.Cells for Node.js via C++, çalışma kitabının sıkıştırma seviyesini ayarlamak için kullanabileceğiniz [**OoxmlCompressionType**](https://reference.aspose.com/cells/nodejs-cpp/ooxmlcompressiontype) enumerasyonunu sağlar. [**OoxmlCompressionType**](https://reference.aspose.com/cells/nodejs-cpp/ooxmlcompressiontype) enumerasyonu aşağıdaki üyeleri içerir.  

- Level1: En hızlı ama en az etkili sıkıştırma.  
- Level2: Biraz daha yavaş, ama Level 1’den daha iyi.  
- Level3: Biraz daha yavaş, ama Level 2’den daha iyi.  
- Seviye4: Seviye 3'e göre biraz daha yavaş, ama daha iyi.  
- Seviye 5: Seviye 4'ten biraz daha yavaş, ancak daha iyi sıkıştırma ile.  
- Seviye 6: Hız ve sıkıştırma verimliliği için iyi bir denge.  
- Seviye7: Oldukça iyi sıkıştırma!  
- Seviye 8: Seviye 7'den daha iyi sıkıştırma!  
- Seviye9: "En iyi" sıkıştırma, burada en iyi, giriş veri akışının boyutunda en büyük azalmayı ifade eder. Bu aynı zamanda en yavaş sıkıştırmadır.  

Aşağıdaki kod parçacığı, [**OoxmlCompressionType**](https://reference.aspose.com/cells/nodejs-cpp/ooxmlcompressiontype) numaralandırmasının kullanımını gösteriyor ve Düzey1, Düzey6 ve Düzey9 için dönüşüm süresini karşılaştırıyor. Oluşturulan dosyaların boyutlarını da karşılaştırabilirsiniz.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source and output directories
const sourceDir = path.join(__dirname, "data");
const outDir = path.join(__dirname, "output");

const filePath = path.join(sourceDir, "LargeSampleFile.xlsx");
const workbook = new AsposeCells.Workbook(filePath);
const options = new AsposeCells.XlsbSaveOptions();

options.setCompressionType(AsposeCells.OoxmlCompressionType.Level1);
let watch = process.hrtime();
workbook.saveAsync(path.join(outDir, "LargeSampleFile_level_1_out.xlsb"), options);
let elapsedMs = process.hrtime(watch);
console.log("Level 1 Elapsed Time: " + (elapsedMs[0] * 1e3 + elapsedMs[1] / 1e6));

watch = process.hrtime();
options.setCompressionType(AsposeCells.OoxmlCompressionType.Level6);
workbook.saveAsync(path.join(outDir, "LargeSampleFile_level_6_out.xlsb"), options);
elapsedMs = process.hrtime(watch);
console.log("Level 6 Elapsed Time: " + (elapsedMs[0] * 1e3 + elapsedMs[1] / 1e6));

watch = process.hrtime();
options.setCompressionType(AsposeCells.OoxmlCompressionType.Level9);
workbook.saveAsync(path.join(outDir, "LargeSampleFile_level_9_out.xlsb"), options);
elapsedMs = process.hrtime(watch);
console.log("Level 9 Elapsed Time: " + (elapsedMs[0] * 1e3 + elapsedMs[1] / 1e6));
```  

