---  
title: Node.js ile Birlik Aralığı Oluşturma (C++ ile)  
linktitle: Birleşik Aralık Oluştur  
type: docs  
weight: 360  
url: /tr/nodejs-cpp/create-union-range/  
description: Aspose.Cells for Node.js via C++ kullanarak Birlik Aralığı oluşturmayı öğrenin.  
keywords: Node.js üzerinden Birlik Aralığı Oluşturma, Aspose.Cells Node.js Birlik Aralığı, Çalışma Sayfası Topluluğu ile Birlik Aralığı oluşturma Node.js  
---  

## **Birleşik Aralık Oluştur**  
Aspose.Cells, [WorksheetCollection.createUnionRange](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#createUnionRange-string-number-) metodunu kullanarak Birlik Aralığı oluşturma özelliği sağlar. [WorksheetCollection.createUnionRange](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#createUnionRange-string-number-) metodu iki parametre alır, birincisi, birleşim aralığını oluşturmak için adres, ikincisi ise çalışma sayfasının indeksidir. [WorksheetCollection.createUnionRange](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#createUnionRange-string-number-) metodu bir [UnionRange](https://reference.aspose.com/cells/nodejs-cpp/unionrange) nesnesi döner.  

Aşağıdaki kod örneği, [WorksheetCollection.createUnionRange](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#createUnionRange-string-number-) metodunu kullanarak Birlik Aralığı oluşturmayı gösterir. Kod tarafından oluşturulan çıktı dosyası referans için eklenmiştir.  

- [Çıktı Dosyası](106364952.xlsx)  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Create union range
const unionRange = workbook.getWorksheets().createUnionRange("sheet1!A1:A10,sheet1!C1:C10", 0);

// Put value "ABCD" in the range
unionRange.setValue("ABCD");

// Save the output workbook.
workbook.save("CreateUnionRange_out.xlsx");
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
