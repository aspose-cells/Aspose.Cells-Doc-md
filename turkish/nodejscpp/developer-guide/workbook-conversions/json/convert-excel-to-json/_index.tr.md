---  
title: Node.js aracılığıyla C++ kullanarak Excel den JSON a Dönüştürme  
linktitle: Excel i JSON a Dönüştür  
type: docs  
weight: 300  
url: /tr/nodejs-cpp/convert-excel-to-json/  
description: Aspose.Cells for Node.js via C++ kullanarak Excel dosyasını JSON a dönüştürmeyi öğrenin.  
keywords: Node.js aracılığıyla C++ kullanarak Workbook u JSON a aktarma, Excel i JSON a dönüştürme  
---  

{{% alert color="primary" %}}  
Aspose.Cells, bir Workbook'un JSON (JavaScript Nesne Gösterimi) dosyasına dönüştürülmesini destekler.  
{{% /alert %}}  

## **Excel Çalışma Kitabını JSON'a Dönüştür**  

Excel Workbook'u JSON'a dönüştürmenin nasıl yapılacağını merak etmeyin, çünkü Aspose.Cells for Node.js via C++ kütüphanesi en iyi çözümü sunar. Aspose.Cells API, elektronik tabloları JSON formatına dönüştürmeyi destekler. Workbook'u JSON'a aktarmak için, [**SaveFormat.Json**](https://reference.aspose.com/cells/nodejs-cpp/saveformat/) parametresini [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-) metodunun ikinci parametresi olarak geçirin. Ayrıca, sayfayı JSON'a ihracatını yapılandırmak için [**JsonSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonsaveoptions/) sınıfını kullanabilirsiniz.  

Aşağıdaki kod örneği, Excel Workbook'u JSON'a dışa aktarmayı gösterir. Kaynak dosyayı ([sample.xlsx](sample.xlsx)) JSON dosyasına dönüştürmek için kodu kullanın ve referans için sunulmuştur.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Convert the workbook to json file.
workbook.save("sample_out.json");
```  

Aşağıdaki kod örneği, JsonSaveOptions sınıfını kullanarak ek ayarları belirler ve Excel Workbook'u JSON'a dışa aktarmayı gösterir. Kaynak dosya ([sample.xlsx](sample.xlsx))'yi JSON dosyasına dönüştürmek için kodu inceleyebilirsiniz.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create an options of saving the file.
const options = new AsposeCells.JsonSaveOptions();

// Set the exporting range.
options.setExportArea(AsposeCells.CellArea.createCellArea("B1", "C4"));

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Convert the workbook to json file.
workbook.save("sample_out.json", options);
```  


