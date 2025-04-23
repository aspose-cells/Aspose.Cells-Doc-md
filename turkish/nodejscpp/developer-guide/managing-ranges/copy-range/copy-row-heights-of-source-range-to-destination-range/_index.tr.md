---  
title: Node.js ve C++ kullanarak Kaynak Aralığının Satır Yüksekliklerini Kopyala  
linktitle: Kaynak Aralığın Satır Yüksekliklerini Hedef Aralığa Kopyala  
type: docs  
weight: 590  
url: /tr/nodejs-cpp/copy-row-heights-of-source-range-to-destination-range/  
---  

{{% alert color="primary" %}}  

 Bazen kullanıcılar kaynak aralığının satır yüksekliğini hedef aralığa kopyalamak ister. Aspose.Cells for Node.js via C++ bu amaçla [**PasteType.RowHeights**](https://reference.aspose.com/cells/nodejs-cpp/pastetype/) enum sağlar. [**PasteOptions.getPasteType()**](https://reference.aspose.com/cells/nodejs-cpp/pasteoptions/#getPasteType--) özelliğini [**PasteType.RowHeights**](https://reference.aspose.com/cells/nodejs-cpp/pastetype/) ile ayarladığınızda, kaynak aralıktaki tüm satırların yüksekliği hedef aralığa kopyalanacaktır.  

{{% /alert %}}  

 Aşağıdaki örnek kod, [**PasteType.RowHeights**](https://reference.aspose.com/cells/nodejs-cpp/pastetype/) enumunu kullanarak kaynak aralığının satır yüksekliğini hedef aralığa nasıl kopyalayacağınızı gösterir. Bu kod tarafından oluşturulan çıktı Excel dosyasını Microsoft Excel’de açtığınızda, hedef aralık satır yüksekliği ile kaynak aralık satır yüksekliğinin birebir aynı olduğunu göreceksiniz.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const workbook = new AsposeCells.Workbook();

// Source worksheet
const srcSheet = workbook.getWorksheets().get(0);

// Add destination worksheet
const dstSheet = workbook.getWorksheets().add("Destination Sheet");

// Set the row height of the 4th row. This row height will be copied to destination range
srcSheet.getCells().setRowHeight(3, 50);

// Create source range to be copied
const srcRange = srcSheet.getCells().createRange("A1:D10");

// Create destination range in destination worksheet
const dstRange = dstSheet.getCells().createRange("A1:D10");

// PasteOptions, we want to copy row heights of source range to destination range
const opts = new AsposeCells.PasteOptions();
opts.setPasteType(AsposeCells.PasteType.RowHeights);

// Copy source range to destination range with paste options
dstRange.copy(srcRange, opts);

// Write informative message in cell D4 of destination worksheet
dstSheet.getCells().get("D4").putValue("Row heights of source range copied to destination range");

// Save the workbook in xlsx format
workbook.save(path.join(dataDir, "output_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```  

