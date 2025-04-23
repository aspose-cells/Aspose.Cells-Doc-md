---  
title: Her Excel Çalışma Sayfası İçin Bir PDF Sayfası Çizin  Excel’den PDF’ye Dönüşüm ile Node.js ve C++  
linktitle: Excel Çalışsayfası Başına Bir PDF Sayfası Oluşturma  Excel den PDF ye Dönüştürme  
type: docs  
weight: 100  
url: /tr/nodejs-cpp/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/  
---  

{{% alert color="primary" %}}  

Büyük Microsoft Excel dosyaları (örneğin, çok sayfalı çalışma kitabı ve her sayfada 50 sütun ve 300 veya daha fazla satır veri) ile çalışırken, her çalışma sayfası için bir sayfa gösterilmesini isteyebilirsiniz, sayfa boyutuna bakmadan. Bu durumda, her sayfa çok farklı boyutlarda olabilir. Bu, Aspose.Cells for Node.js via C++ kullanılarak sağlanabilir.  

{{% /alert %}}  

Lütfen birden çok çalışsayfasına sahip bir Excel dosyasını PDF'ye dönüştüren aşağıdaki örnek kodu inceleyin.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Initialize a new Workbook
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "input.xlsx"));

// Implement one page per worksheet option
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();
pdfSaveOptions.setOnePagePerSheet(true);

// Save the PDF file
workbook.save(path.join(dataDir, "OutputFile.out.pdf"), pdfSaveOptions);
```  

{{% alert color="primary" %}}  

Eğer [PdfSaveOptions.getOnePagePerSheet()](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getOnePagePerSheet--) seçeneği **true** olarak ayarlanmışsa, tüm çalışma sayfası içeriği tek bir PDF sayfasına dönüştürülür.  

{{% /alert %}} {{% alert color="primary" %}}  

Eğer Excel tablonuz formüller içeriyorsa, PDF'ye dönüştürmeden hemen önce [Workbook.calculateFormula()](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) fonksiyonunu çağırmak en iyisidir. Bu, formüle bağlı değerlerin yeniden hesaplanmasını sağlar ve PDF'ye doğru değerler yansıtılır.  

{{% /alert %}}  

