---  
title: Node.js ve C++ kullanarak Excel i HTML ye dönüştürürken Belge Çalışma Kitabı ve Sayfa Özelliklerini dışa aktarmayı öğrenin.  
linktitle: Excel den HTML e belge çalışma kitabı ve çalışma sayfası özelliklerini dışa aktar  
type: docs  
weight: 50  
url: /tr/nodejs-cpp/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/  
description: Aspose.Cells for Node.js via C++ kullanarak Excel den HTML ye Belge, Çalışma Kitabı ve Çalışma Sayfası özelliklerini nasıl dışa aktaracağınızı öğrenin.  
---  

## **Olası Kullanım Senaryoları**  

Bir Microsoft Excel dosyası, Microsoft Excel veya Aspose.Cells for Node.js via C++ kullanılarak HTML'ye aktarıldığında, aşağıdaki ekran görüntüsünde gösterildiği gibi çeşitli Belge, Çalışma Kitabı ve Çalışma Sayfası özellikleri de dışa aktarılır. Bu özellikleri dışa aktarmaktan kaçınmak için, [**HtmlSaveOptions.getExportDocumentProperties()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportDocumentProperties--), [**HtmlSaveOptions.getExportWorkbookProperties()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportWorkbookProperties--) ve [**HtmlSaveOptions.getExportWorksheetProperties()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportWorksheetProperties--) parametrelerini **false** yapabilirsiniz. Bu özelliklerin varsayılan değeri **true**'dur. Aşağıdaki ekran görüntüsü, bu özelliklerin dışa aktarılan HTML içindeki görünümünü gösterir.  

![todo:image_alt_text](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)  

## **Belge, Çalışma Kitabı ve Çalışma Sayfası Özelliklerini Excel'den HTML'e Dışa Aktar**  

Aşağıdaki örnek kod, [örnek Excel dosyasını](61767776.xlsx) yükler ve Belge, Çalışma Kitabı ve Çalışma Sayfası özelliklerini dışa aktarmadan HTML'ye dönüştürür [çıktı HTML'si](61767779.zip).  

## **Örnek Kod**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleExportDocumentWorkbookAndWorksheetPropertiesInHTML.xlsx");

// Load the sample Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Specify Html Save Options
const options = new AsposeCells.HtmlSaveOptions();

// We do not want to export document, workbook and worksheet properties
options.setExportDocumentProperties(false);
options.setExportWorkbookProperties(false);
options.setExportWorksheetProperties(false);

// Export the Excel file to Html with Html Save Options
workbook.save("outputExportDocumentWorkbookAndWorksheetPropertiesInHTML.html", options);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
