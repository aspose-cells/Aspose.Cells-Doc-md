---  
title: Excel dosyasını PDF formatına dönüştür ve PDF/A 1a ile uyumlu hale getir  
linktitle: Excel dosyasını PDF formatına dönüştür ve PDF/A 1a ile uyumlu hale getir  
type: docs  
weight: 130  
url: /tr/nodejs-cpp/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/  
description: Aspose.Cells for Node.js via C++ kullanarak Excel dosyalarını PDF/A uyumlu PDF dosyalarına dönüştürmeyi öğrenin.  
---  

## **Olası Kullanım Senaryoları**  

PDF/A, belgelerin uzun vadeli korunması için tasarlanmış benzersiz bir PDF çeşididir. PDF/A, PDF'nin uluslararası standarda (ISO) göre standartlaştırılmış bir sürümüdür ve belgedeki kullanılan tüm yazı tiplerini gömme özelliği ile arşiv formatıdır. PDF/A, font bağlantısı (font gömme yerine) ve şifreleme gibi özellikleri yasaklamasıyla PDF'den ayrılır. Aspose.Cells for Node.js via C++, Excel dosyalarını PDF/A uyumlu PDF dosyalarına kaydetmenize olanak tanır (PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-2ab ve PDF/A-3u desteklenmektedir). Bu konu, Excel çalışma kitabını PDF/A uyumlu (PDF/A-1a) PDF dosyasına nasıl kaydedeceğinizi anlatır.  

## **Excel dosyasını PDF/A-1a uyumlu PDF formatına dönüştürme**  

Geliştiriciler, dönüştürme için farklı özellikleri ayarlamak üzere [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) sınıfını kullanabilir. [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) sınıfının farklı özelliklerini ayarlamak, çıktı PDF'sinin yazdırma, font, güvenlik ve sıkıştırma ayarları üzerinde kontrol sağlar. En önemli özellik, Excel dosyalarını PDF/A uyumlu PDF dosyalarına kaydetmenizi sağlayan [**PdfSaveOptions.getCompliance()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getCompliance--)'dir.  

Aşağıdaki örnek kod, bir Excel dosyasını PDF/A-1a ile uyumlu PDF biçimine nasıl dönüştüreceğinizi açıklar. Lütfen referans olması için [çıktı PDF'sine](outputCompliancePdfA1a.pdf) ve ekran görüntüsüne bakın.  

## **Ekran Görüntüsü**  

![todo:image_alt_text](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)  

## **Örnek Kod**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Create workbook object
const wb = new AsposeCells.Workbook();

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Access cell B5 and add some message inside it
const cell = ws.getCells().get("B5");
cell.putValue("This PDF format is compatible with PDFA-1a.");

// Create pdf save options and set its compliance to PDFA-1a
const opts = new AsposeCells.PdfSaveOptions();
opts.setCompliance(AsposeCells.PdfCompliance.PdfA1a);

// Save the output pdf
wb.save(path.join(outputDir, "outputCompliancePdfA1a.pdf"), opts);
```  

