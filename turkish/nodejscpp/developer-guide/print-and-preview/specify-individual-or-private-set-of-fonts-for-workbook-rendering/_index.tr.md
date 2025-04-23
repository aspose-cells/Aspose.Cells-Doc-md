---  
title: Node.js kullanarak Çalışma Kitabı Render ı için Bireysel veya Özel Yazı Tipleri Seti Belirleme  
linktitle: Çalışma Kitabı Rendeleme için Bireysel veya Özel Font Kümesini Belirtin  
type: docs  
weight: 40  
url: /tr/nodejs-cpp/specify-individual-or-private-set-of-fonts-for-workbook-rendering/  
description: Aspose.Cells for Node.js via C++ kullanarak çalışma kitabı render ında bireysel veya özel yazı tipi setleri nasıl belirlenir öğrenin.  
---  

## **Olası Kullanım Senaryoları**  

Genellikle, tüm çalışma kitapları için yazı tipi dizini veya listesi belirlenir; fakat bazen, çalışma kitaplarınız için bireysel veya özel yazı tipi setleri belirlemeniz gerekebilir. Aspose.Cells for Node.js via C++, çalışma kitabınız için bireysel veya özel yazı tipi setlerini belirlemek için kullanılabilecek [**IndividualFontConfigs**](https://reference.aspose.com/cells/nodejs-cpp/individualfontconfigs) sınıfını sağlar.  

## **Çalışma Kitabı Rendeleme İçin Bireysel veya Özel Font Kümesini Belirtin**  

Aşağıdaki örnek kod, belirtilen bireysel veya özel yazı tipi setleriyle [örnek Excel dosyasını](67338268.xlsx) yükler. Kod içindeki [örnek font](67338271.zip) ve üretilen [çıktı PDF'si](67338269.pdf) ile ilgili bilgileri görebilirsiniz. Bu ekran görüntüsü, yazı tipi başarıyla bulunduğunda çıktı PDF'sinin nasıl göründüğünü gösterir.  

![todo:image_alt_text](specify-individual-or-private-set-of-fonts-for-workbook-rendering_1.png)  

## **Örnek Kod**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Path of your custom font directory.
const customFontsDir = "C:\\TempDir\\CustomFonts";

// Specify individual font configs custom font directory.
const fontConfigs = new AsposeCells.IndividualFontConfigs();

// If you comment this line or if custom font directory is wrong or 
// if it does not contain required font then output pdf will not be rendered correctly.
fontConfigs.setFontFolder(customFontsDir, false);

// Specify load options with font configs.
const opts = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);
opts.setFontConfigs(fontConfigs);

const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleSpecifyIndividualOrPrivateSetOfFontsForWorkbookRendering.xlsx");
// Output directory
const outputDir = path.join(__dirname, "output");
// Load the sample Excel file with individual font configs. 
const wb = new AsposeCells.Workbook(filePath, opts);

// Save to PDF format.
wb.save(outputDir + "outputSpecifyIndividualOrPrivateSetOfFontsForWorkbookRendering.pdf", AsposeCells.SaveFormat.Pdf);
```  

