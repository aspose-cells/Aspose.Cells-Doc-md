---
title: Resimler veya Grafikler içeren XLS Dosyasını Node.js kullanarak C++ ile PDF ye dönüştürün
linktitle: İmaj veya Grafik İçeren XLS Dosyasını PDF ye Dönüştürme
type: docs
weight: 50
url: /tr/nodejs-cpp/convert-xls-file-with-images-or-charts-to-pdf/
---

{{% alert color="primary" %}} 

Aspose.Cells, resimler ve grafikler içeren XLS dosyalarının PDF belgelerine dönüştürülmesini destekler. Aspose.Cells for Node.js via C++, bir elektronik tablonun PDF'e dönüştürülmesi için bağımsız olarak çalışabilir: Node.js için Aspose.PDF C++ kullanmak gerekmez. İşlem, geçici veya ara XML dosyalarına bağlı olmadığı için bellekte gerçekleştirilebilir. Bu, örneğin, resimler, grafikler ve diğer çizim nesneleri içeren büyük Excel dosyalarının hızlı ve verimli şekilde dönüştürülmesine olanak tanır.

{{% /alert %}} 
## **Örnek Kod**


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
try {
// Get the template excel file path.
const designerFile = path.join(dataDir, "SampleInput.xls");

// Specify the pdf file path.
const pdfFile = path.join(dataDir, "Output.out.pdf");

// Open the template excel file
const wb = new AsposeCells.Workbook(designerFile);

// Save the pdf file.
wb.save(pdfFile, AsposeCells.SaveFormat.Pdf);
} catch (e) {
console.log(e.message);
}
```

{{% alert color="primary" %}} 

Eğer elektronik tablo formüller içeriyorsa, PDF'ye dönüştürmeden hemen önce [Workbook.calculateFormula()](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) metodunu çağırmak en iyisidir. Bu, formüle bağlı değerlerin tekrar hesaplanmasını ve PDF'de doğru değerlerin gösterilmesini sağlar.

{{% /alert %}}
