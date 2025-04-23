---  
title: XLSB revizyonlarını Node.js ve C++ kullanarak XLSM formatına dönüştürme  
linktitle: XLSB Revizyonunu XLSM ye Dönüştür  
type: docs  
weight: 290  
url: /tr/nodejs-cpp/convert-revision-of-xlsb-to-xlsm/  
description: Aspose.Cells for Node.js via C++ kullanarak XLSB dosyalarının revizyonlarını tamamen XLSM formatına nasıl dönüştürebileceğinizi öğrenin.  
---  

{{% alert color="primary" %}}  

Aspose.Cells artık XLSB dosyalarının revizyonlarını tamamen XLSM dosyalarına dönüştürmeyi destekler. Revizyonlar \xl\revisions yolu içinde bulunur. Bunları görmek için XLSB dosya uzantınızı ZIP'e değiştirin. \xl\revisions yolu, .bin uzantılı dosyaları içerir.  

Aspose.Cells kullanarak XLSB dosyanızı XLSM formatına dönüştürdüğünüzde, bu .bin dosyaları başarıyla .xml dosyalarına dönüşür; bu iki ekran görüntüsünde gösterilmektedir.  

{{% /alert %}}  

Aşağıdaki kod örneği, XLSB dosyasını Aspose.Cells for Node.js via C++ kullanarak XLSM formatına nasıl dönüştüreceğinizi gösterir.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsb");

// Open workbook
const workbook = new AsposeCells.Workbook(filePath);

// Save Workbook to XLSM format
workbook.save(path.join(dataDir, "output_out.xlsm"), AsposeCells.SaveFormat.Xlsm);
```  

