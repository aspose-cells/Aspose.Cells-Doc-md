---  
title: Node.js aracılığıyla C++ kullanarak JSON dan CSV ye dönüştürme  
linktitle: JSON u CSV ye dönüştür  
type: docs  
weight: 210  
url: /tr/nodejs-cpp/convert-json-to-csv/  
description: Aspose.Cells for Node.js via C++ kullanarak JSON verisini CSV ye dönüştürmeyi öğrenin.  
---  

## **JSON'ı CSV'ye dönüştür**  

Aspose.Cells, basit ve iç içe JSON'un CSV'ye dönüştürülmesini destekler. Bu işlem için API [**JsonLayoutOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonlayoutoptions) ve [**JsonUtility**](https://reference.aspose.com/cells/nodejs-cpp/jsonutility) sınıflarını sağlar. [**JsonLayoutOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonlayoutoptions) sınıfı, [**JsonLayoutOptions.getArrayAsTable()**](https://reference.aspose.com/cells/nodejs-cpp/jsonlayoutoptions/#getArrayAsTable--) (diziyi tablo olarak işler) gibi JSON düzeni seçeneklerini sunar. [**JsonUtility**](https://reference.aspose.com/cells/nodejs-cpp/jsonutility) sınıfı ise JSON'u [**JsonLayoutOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonlayoutoptions) sınıfıyla ayarlı düzen seçenekleri ile işler.  

Aşağıdaki kod örneği, [kaynak JSON dosyasını](104398869.json) yüklemek ve [çıktı CSV dosyasını](104398870.csv) oluşturmak için [**JsonLayoutOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonlayoutoptions) ve [**JsonUtility**](https://reference.aspose.com/cells/nodejs-cpp/jsonutility) sınıflarını kullanmayı gösterir.  

### **Örnek Kod**  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");


// Create sample JSON if missing
const jsonPath = path.join(sourceDir, "SampleJson.json");

// Read JSON file
const str = fs.readFileSync(jsonPath, "utf-8");

// Create empty workbook
const workbook = new AsposeCells.Workbook();

// Get Cells
const cells = workbook.getWorksheets().get(0).getCells();

// Set JsonLayoutOptions
const importOptions = new AsposeCells.JsonLayoutOptions();
importOptions.setConvertNumericOrDate(true);
importOptions.setArrayAsTable(true);
importOptions.setIgnoreTitle(true);
AsposeCells.JsonUtility.importData(str, cells, 0, 0, importOptions);

// Save Workbook
workbook.save(outputDir + "SampleJson_out.csv");
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
