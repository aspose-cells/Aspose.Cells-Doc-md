---  
title: C++ ile Node.js kullanarak Satırları Otomatik Sığdırmayla Oluşturma  
linktitle: Çizim için Satırları Otomatik Sığdır  
type: docs  
weight: 130  
url: /tr/nodejs-cpp/autofit-rows-for-rendering/  
description: Excel de Aspose.Cells for Node.js via C++ kullanarak satırların otomatik sığdırılmasını nasıl yapacağınızı öğrenin. Kaydedilmiş PDF dosyalarında metin kesilmesini önleyin.  
---  

Genellikle, bir hücredeki tüm metni göstermek istediğinizde, Microsoft Excel’de Normal görünümde %100 yakınlaştırma ile satırı otomatik sığdırabilirsiniz. Bu, metnin Normal görünümde tamamen görünmesini sağlar ve hatta dosyayı yazdırırken veya PDF olarak kaydederken metin düzgün gösterilir.

Ancak bazen, satırı otomatik sığdırmak Normal görünümde iyi çalışır, ancak yazdırma görünümüne geçerken veya dosyayı PDF olarak kaydederken, metin kesilir. Lütfen kaynak dosyayı [Book1.xlsx](Book1.xlsx) ve ekran görüntülerini kontrol edin.

![metin yazdırma görünümünde kesilmiş](metin_yazdırma_görünümünde_kesilmiş.png)

Kaydedilmiş PDF dosyasında metnin kesilmesini önlemek istiyorsanız, satırı [AutoFitterOptions.getForRendering()](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions/#getForRendering--) seçeneği ile otomatik sığdırabilirsiniz.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Init workbook instance.
const workbook = new AsposeCells.Workbook(filePath);

// Set autofit options for rendering.
const autoFitterOptions = new AsposeCells.AutoFitterOptions();
autoFitterOptions.setForRendering(true);

// Autofit rows with options.
workbook.getWorksheets().get(0).autoFitRows(autoFitterOptions);

// Save to pdf.
workbook.save("output.pdf", AsposeCells.SaveFormat.Pdf);
```

Şimdi, metin çıktı PDF dosyasında kesilmemiş durumda.

![kaydedilmiş pdf'de metin kesilmemiş](kaydedilmiş_pdfde_metin_kesilmemiş.png)  
