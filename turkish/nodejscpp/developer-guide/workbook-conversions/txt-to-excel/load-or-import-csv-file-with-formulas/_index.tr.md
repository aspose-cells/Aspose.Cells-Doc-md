---  
title: Node.js kullanarak Formüllü CSV Dosyasını Yükle veya İçeri Aktar  
linktitle: Formülleri içeren CSV dosyasını yükle veya içe aktar  
type: docs  
weight: 350  
url: /tr/nodejs-cpp/load-or-import-csv-file-with-formulas/  
description: Formüllü CSV dosyalarını nasıl yükleyeceğinizi ve içeri aktaracağınızı Aspose.Cells for Node.js via C++ ile öğrenin.  
---  

{{% alert color="primary" %}}  

CSV dosyaları genellikle metin verisi içerir ve formüller içermez. Ancak bazen, CSV dosyaları da formüller içerebilir. Bu tür CSV dosyalarını, [TxtLoadOptions.getHasFormula()](https://reference.aspose.com/cells/nodejs-cpp/txtloadoptions/#getHasFormula--) ayarını **true** yaparak yüklemelisiniz. Bu özellik **true** olarak ayarlandığında, Aspose.Cells formülleri basit metin olarak işlemez; formüller olarak kabul edilir ve Aspose.Cells formül hesaplama motoru tarafından正常 işlenir.

{{% /alert %}}  

Aşağıdaki kod, formüllü CSV dosyasını nasıl yükleyeceğinizi ve içeri aktaracağınızı gösterir. Herhangi bir CSV dosyasını kullanabilirsiniz. Örnek olarak, bu veriyi içeren [basit CSV dosyası](5115034.csv) kullanıyoruz. Görüldüğü gibi, formüller içerir.

{{< highlight javascript >}}  
const fs = require('fs');  
const AsposeCells = require('aspose.cells');  

let loadOptions = new AsposeCells.TxtLoadOptions();  
loadOptions.setHasFormula(true);  

let workbook = new AsposeCells.Workbook();  
workbook.open("path/to/your/file.csv", loadOptions);  
workbook.save("path/to/output.xlsx");  
{{< /highlight >}}  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.csv");

// TxtLoadOptions configuration
const opts = new AsposeCells.TxtLoadOptions();
opts.setSeparator(',');
opts.setHasFormula(true);

// Load your CSV file with formulas in a Workbook object
const workbook = new AsposeCells.Workbook(filePath, opts);

// You can also import your CSV file like this
// The code below is importing CSV file starting from cell D4
const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().importCSV(filePath, opts, 3, 3);

// Save your workbook in Xlsx format
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

Kod ilk olarak CSV dosyasını yükler, ardından tekrar D4 hücresine içe aktarır. Son olarak, çalışma kitabı nesnesini XLSX biçiminde kaydeder. [Çıktı XLSX dosyası](5115052.xlsx) böyle görünür. Görüldüğü gibi, C3 ve F4 hücreleri formüller içerir ve sonucu 800'dür.

|![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)|  
| :- |  


