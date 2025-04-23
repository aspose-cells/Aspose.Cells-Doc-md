---  
title: Node.js kullanarak C++ ile Çıkış HTML sinde Sayfa Sekmesi CSS sini Ayrı Export Et  
linktitle: Çıktı HTML sindeki Sayfa CSS sini Ayrı Ayrı Dışa Aktarma  
type: docs  
weight: 80  
url: /tr/nodejs-cpp/export-worksheet-css-separately-in-output/  
description: Excel dosyasını HTML ye dönüştürürken sayfa CSS sini ayrı olarak dışa aktarmayı nasıl yapacağınızı Aspose.Cells for Node.js via C++ kullanarak öğrenin.  
---  

## **Olası Kullanım Senaryoları**

Aspose.Cells for Node.js via C++, Excel dosyanızı HTML'ye dönüştürürken sayfa CSS'sini ayrı olarak dışa aktarma özelliği sunar. Bu amaçla [**HtmlSaveOptions.getExportWorksheetCSSSeparately()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportWorksheetCSSSeparately--) özelliğini kullanın ve Excel dosyasını HTML formatında kaydederken **true** olarak ayarlayın.

## **Çıktı HTML'sindeki Sayfa CSS'sini Ayrı Ayrı Dışa Aktarma**

Aşağıdaki örnek kod, bir Excel dosyası oluşturur, **B5** hücresine Kırmızı renkli metin ekler ve ardından [**HtmlSaveOptions.getExportWorksheetCSSSeparately()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportWorksheetCSSSeparately--) özelliği kullanarak HTML formatında kaydeder. Referans için kod tarafından oluşturulan [çıktı HTML](60489766.zip) dosyasına bakın. Örnekte **stylesheet.css** dosyasını bulacaksınız.

## **Örnek Kod**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create workbook object
const wb = new AsposeCells.Workbook();

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Access cell B5 and put value inside it
const cell = ws.getCells().get("B5");
cell.putValue("This is some text.");

// Set the style of the cell - font color is Red
const st = cell.getStyle();
st.getFont().setColor(AsposeCells.Color.Red);
cell.setStyle(st);

// Specify html save options - export worksheet css separately
const opts = new AsposeCells.HtmlSaveOptions();
opts.setExportWorksheetCSSSeparately(true);

// Save the workbook in html 
wb.save("outputExportWorksheetCSSSeparately.html", opts);
```

## **Tek Çalışsayı İş Kitabını HTML'ye Dışa Aktarma**

Birden çok sayfaya sahip bir çalışma kitabını Aspose.Cells for Node.js via C++ kullanarak HTML'ye dönüştürdüğünüzde, bir HTML dosyası ve CSS içeren klasör oluşturulur ve birden fazla HTML dosyası ile birlikte gelir. Tarayıcıda açıldığında sekmeler görünür olur. Aynı davranış, tek sayfa içeren çalışma kitapları için de gereklidir. Daha önce, tek sayfa çalışma kitapları için ayrı klasör oluşturulmazdı ve yalnızca bir HTML dosyası oluşturulurdu. Böyle bir HTML dosyası, tarayıcıda açıldığında sekmeleri göstermez. MS Excel, tek sayfalar için de uygun klasör ve HTML oluşturur, bu nedenle aynı davranış Aspose.Cells API'leri ile uygulanmıştır. Aşağıdaki bağlantıdan örnek dosyayı indirerek, örnek kodda kullanabilirsiniz:

[sampleSingleSheet.xlsx](79527937.xlsx)

## **Örnek Kod**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleSingleSheet.xlsx");
// Load the sample Excel file containing single sheet only
const wb = new AsposeCells.Workbook(sourceFilePath);

// Specify HTML save options
const options = new AsposeCells.HtmlSaveOptions();

// Set optional settings if required
options.setEncoding(AsposeCells.EncodingType.UTF8);
options.setExportImagesAsBase64(true);
options.setExportGridLines(true);
options.setExportSimilarBorderStyle(true);
options.setExportBogusRowData(true);
options.setExcludeUnusedStyles(true);
options.setExportHiddenWorksheet(true);

// Save the workbook in Html format with specified Html Save Options
wb.save(path.join(dataDir, "outputSampleSingleSheet.htm"), options);
```  

