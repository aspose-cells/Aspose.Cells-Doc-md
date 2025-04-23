---  
title: Node.js ve C++ kullanarak çıktı PDF ve resimlerde metinleri nasıl kırpacağınızı belirtin  
linktitle: Çıktı PDF ve görüntüde dizeyi nasıl geçeceğinizi belirtin  
type: docs  
weight: 120  
url: /tr/nodejs-cpp/specify-how-to-cross-string-in-output-pdf-and-image/  
description: Aspose.Cells for Node.js via C++ kullanarak çıktı PDF / Resim üzerindeki metin taşmalarını kontrol etmeyi öğrenin.  
---  

## **Olası Kullanım Senaryoları**

Bir hücrede metin veya dize bulunuyorsa ve bu hücrenin genişliğinden büyükse, dizge taşar; eğer sonraki sütundaki hücre null veya boşsa. Excel dosyanızı PDF / Resim'e kaydederken, bu taşmayı [**TextCrossType**](https://reference.aspose.com/cells/nodejs-cpp/textcrosstype) numaralandırmasını kullanarak çapraz türünü belirterek kontrol edebilirsiniz. Aşağıdaki değerlere sahiptir:

- **TextCrossType.Default**: MS Excel gibi gösterecek, bu bağlı olarak sonraki hücreye. Eğer sonraki hücre null ise, dize taşar ya da kısaltılır.

- **TextCrossType.CrossKeep**: MS Excel'den PDF/Görüntü aktarırken dizeyi gösterir.

- **TextCrossType.CrossOverride**: Diğer hücreleri çaprazlayarak tüm metni gösterir ve çaprazlanan hücrelerin metnini üzerine yazar.

- **TextCrossType.StrictInCell**: Sadece hücre genişliği içinde metni görüntüler.

## **PDF/Görüntüde dizeyi nasıl geçeceğinizi belirtin, TextCrossType kullanarak.**

Aşağıdaki örnek kod, örnek Excel dosyasını yükler ve farklı [**TextCrossType**](https://reference.aspose.com/cells/nodejs-cpp/textcrosstype) belirterek PDF/Görüntü formatına kaydeder. Örnek Excel dosyası ve çıktı dosyaları aşağıdaki linklerden indirilebilir:

[sampleCrossType.xlsx](81920905.xlsx)  

[outputCrossType.pdf](81920903.pdf)  

[outputCrossType.png](81920904.png)  

### Örnek Kod

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load template Excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleCrosssType.xlsx"));

// Initialize PDF save options
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();

// Set text cross type
pdfSaveOptions.setTextCrossType(AsposeCells.TextCrossType.StrictInCell);

// Save PDF file
workbook.save(outputDir + "outputCrosssType.pdf", pdfSaveOptions);

// Initialize image or print options
const imageSaveOptions = new AsposeCells.ImageOrPrintOptions();

// Set text cross type
imageSaveOptions.setTextCrossType(AsposeCells.TextCrossType.StrictInCell);

// Initialize sheet renderer object
const sheetRenderer = new AsposeCells.SheetRender(workbook.getWorksheets().get(0), imageSaveOptions);

sheetRenderer.toImage(0, outputDir + "outputCrosssType.png");
```  

