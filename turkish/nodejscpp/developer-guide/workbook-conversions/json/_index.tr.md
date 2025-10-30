---  
title: JSON ile Node.js kullanımı  
linktitle: Json  
type: docs  
weight: 300  
url: /tr/nodejs-cpp/convert-workbook-to-json/  
description: Aspose.Cells for Node.js via C++ kullanarak Excel Çalışma Kitabını JSON a dönüştürmeyi öğrenin.  
---  

{{% alert color="primary" %}}  
Aspose.Cells, bir çalışma kitabını Json (JavaScript Nesne Notasyonu) dosyasına dönüştürmeyi destekler.  
{{% /alert %}}  

## **Excel Çalışma Kitabını JSON'a Dönüştür**  

Aspose.Cells API, elektronik tabloyu JSON formatına dönüştürmeyi destekler. Çalışma kitabını JSON'a aktarmak için, [**SaveFormat.Json**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) parametresini [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-) metodunun ikinci parametresi olarak geçirin. Ayrıca, JSON'a dışa aktarım ayarlarını belirlemek için [**JsonSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonsaveoptions) sınıfını kullanabilirsiniz.  

Aşağıdaki kod örneği, aktif çalışma sayfasını JSON'a dışa aktarmayı, [**SaveFormat.Json**](https://reference.aspose.com/cells/nodejs-cpp/saveformat/#json) enum üyesi kullanarak gösterir. Lütfen kaynak dosya (book1.xlsx) ve kod tarafından üretilen çıktı Json dosyası (book1.Json) arasındaki dönüşüm örneğine bakın.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Convert the workbook to json file.
workbook.save(path.join(dataDir, "book1.json"));
```  

## **Gelişmiş Konular**  
- [CSV'yi JSON'a dönüştür](/cells/tr/nodejs-cpp/convert-csv-to-json/)  
- [Excel'i JSON'a dönüştür](/cells/tr/nodejs-cpp/convert-excel-to-json/)  
- [JSON'ı CSV'ye dönüştür](/cells/tr/nodejs-cpp/convert-json-to-csv/)  
- [JSON'ı Excel'e dönüştür](/cells/tr/nodejs-cpp/convert-json-to-excel/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
