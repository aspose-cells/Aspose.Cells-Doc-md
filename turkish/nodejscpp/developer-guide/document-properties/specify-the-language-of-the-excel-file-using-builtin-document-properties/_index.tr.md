---
title: Node.js ve C++ kullanarak Excel Dosyasının Dilini Belge Özellikleri ile belirtin
linktitle: Dahili Belge Özelliklerini Kullanarak Excel Dosyasının Dilini Belirtme
type: docs
weight: 30
url: /tr/nodejs-cpp/specify-the-language-of-the-excel-file-using-builtin-document-properties/
---

## **Olası Kullanım Senaryoları**

Bir Excel dosyasının dilini değiştirmek için dosyaya sağ tıklayın, Özellikler > Ayrıntılar bölümüne gidin ve Dil alanını düzenleyin. Programatik olarak değiştirmek için [**BuiltInDocumentPropertyCollection.getLanguage()**](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getLanguage--) özelliğini kullanın, Aspose.Cells for Node.js via C++ API'leriyle.

## **Dahili Belge Özelliklerini Kullanarak Excel Dosyasının Dilini Belirtme**

Aşağıdaki örnek kod, bir çalışma kitabı oluşturur ve bu kitabın dil adlı dahili belge özelliğini değiştirir. Bu kod tarafından oluşturulan [çıktı Excel dosyasını](64716891.xlsx) ve modifiye edilen Dil alanını gösteren ekran görüntüsünü inceleyin.

![todo:image_alt_text](specify-the-language-of-the-excel-file-using-builtin-document-properties_1.png)

## **Örnek Kod**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Create workbook object.
const wb = new AsposeCells.Workbook();

// Access built-in document property collection.
const bdpc = wb.getBuiltInDocumentProperties();

// Set the language of the Excel file.
bdpc.setLanguage("German, French");

// Save the workbook in xlsx format.
wb.save(path.join(outputDir, "outputSpecifyLanguageOfExcelFileUsingBuiltInDocumentProperties.xlsx"), AsposeCells.SaveFormat.Xlsx);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
