---  
title: Node.js ile C++ kullanarak Excel’i PDF’ye Dönüştürürken Hataları Yoksay  
linktitle: Excel i PDF olarak dönüştürürken Hataları Yoksay  
type: docs  
weight: 80  
url: /tr/nodejs-cpp/ignore-errors-while-rendering-excel-to-pdf/  
description: Aspose.Cells for Node.js via C++ kullanarak Excel dosyalarının PDF’ye dönüştürme sırasında hataları nasıl yoksayacağınızı öğrenin.  
---  

## **Olası Kullanım Senaryoları**  

Bazen, Excel dosyanızı PDF’ye dönüştürürken hatalar veya istisnalar oluşur ve dönüşüm işlemi sona erer. Bu hataları göz ardı etmek için [**PdfSaveOptions.getIgnoreError()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getIgnoreError--) özelliğini kullanabilirsiniz. Bu sayede dönüşüm sorunsuz tamamlanır, herhangi bir hata veya istisna atılmaz, ancak veri kaybı yaşanabilir. Bu nedenle, bu özelliği yalnızca veri kaybı sizin için kritik değilse kullanın.  

## **Excel'den PDF'e Dönüştürme Sırasında Hataları Yoksay**  

Aşağıdaki kod, [örnek Excel dosyasını](55541778.xlsx) yükler, ancak örnek Excel dosyası hatalıdır ve [PDF’ye dönüşüm sırasında](55541779.pdf) bir hata fırlatır; fakat [**PdfSaveOptions.getIgnoreError()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getIgnoreError--) özelliği kullanıldığı için hata ortaya çıkmaz. Ancak, bu ekran görüntüsünde gösterilen *yuvarlak kırmızı ok şeklinde* olan şekil kaybolur.  

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)  

## **Örnek Kod**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleErrorExcel2Pdf.xlsx");
// Load the Sample Workbook that throws Error on Excel2Pdf conversion
const wb = new AsposeCells.Workbook(filePath);

// Specify Pdf Save Options - Ignore Error
const opts = new AsposeCells.PdfSaveOptions();
opts.IgnoreError = true;

// Save the Workbook in Pdf with Pdf Save Options
wb.save("outputErrorExcel2Pdf.pdf", opts);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
