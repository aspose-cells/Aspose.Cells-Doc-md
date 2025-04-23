---  
title: Her Çalışma Sayfasını Ayrı PDF Dosyasına Kaydetmek Node.js ve C++ kullanarak  
linktitle: Her bir Çalışsayfayı Farklı Bir PDF Dosyasına Kaydet  
type: docs  
weight: 130  
url: /tr/nodejs-cpp/save-each-worksheet-to-a-different-pdf-file/  
---  

{{% alert color="primary" %}}  
Aspose.Cells, XLS dosyalarını (resimler, grafikler vb. içeren) PDF'ye dönüştürmeyi destekler. Aspose.Cells for Node.js via C++ bağımsız olarak çalışabilir ve herhangi bir ek yazılım kullanmadan tüm süreci bellek içinde gerçekleştirerek tabloyu PDF'ye dönüştürür. 转换 için Aspose.PDF for Node.js ve C++ kullanmanız gerekmez.  
{{% /alert %}}  

## **Her Çalışsayarı Farklı Bir PDF Dosyasına Kaydet**  
Şablon Excel dosyanızdaki her çalışma sayfasını farklı PDF dosyaları oluşturmak için kaydetmeniz gerekiyorsa, bunu kolayca başarabilirsiniz. Bir seferde bir sheet indeksini [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/nodejs-cpp/pdfs saveoptions/#sheetSet) seçeneğiyle ayarlayarak PDF'ye dönüştürmeyi deneyebilirsiniz.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Get the Excel file path
const filePath = path.join(dataDir, "input.xlsx");

// Instantiate a new workbook and open the Excel file from its location
const workbook = new AsposeCells.Workbook(filePath);

// Get the count of the worksheets in the workbook
const sheetCount = workbook.getWorksheets().getCount();

// Define PdfSaveOptions
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();

// Take PDFs of each sheet
for (let j = 0; j < sheetCount; j++) {
const ws = workbook.getWorksheets().get(j);

// set worksheet to output
const sheetSet = new AsposeCells.SheetSet([ws.getIndex()]);
pdfSaveOptions.setSheetSet(sheetSet);

workbook.save(path.join(dataDir, `worksheet-${ws.getName()}.out.pdf`), pdfSaveOptions);
}
```  

{{% alert color="primary" %}}  
Eğer elektronik tablonuz formüller içeriyorsa, PDF formatına dönüştürmeden hemen önce [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) çağrısını yapmanız en iyisidir. Böyle yaparak formüle bağımlı değerler yeniden hesaplanacak ve doğru değerler PDF'de gösterilecektir.  
{{% /alert %}}  

