---  
title: Microsoft Excel kullanarak OLE nesnesini otomatik yenileme, Aspose.Cells for Node.js via C++ kullanımıyla  
linktitle: Aspose.Cells kullanarak Microsoft Excel üzerinden OLE nesnesini otomatik olarak yenileyin  
type: docs  
weight: 270  
url: /tr/nodejs-cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/  
description: Excel de OLE nesnelerini otomatik olarak yenilemek için Aspose.Cells for Node.js via C++ kullanma adımlarını öğrenin.  
---  

{{% alert color="primary" %}}  
Aspose.Cells, Microsoft Excel'de excel dosyası açıldığında OLE nesnesini yenilemek için [**OleObject.getAutoLoad()**](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getAutoLoad--) özelliğini sağlar. Bu özellik sayesinde OLE nesnesi, Microsoft Excel tarafından oluşturulan doğru OLE görüntüsünü gösterecektir.  
{{% /alert %}}  

Aşağıdaki örnek kod, gerçek dışı bir OLE görüntüsüne sahip olan [örnek excel dosyasını](5115231.xlsx) yükler. OLE nesnesi aslında bir Microsoft Word belgesidir ancak örnek excel dosyası, Microsoft Word görüntüsü yerine hayvan görüntüsünü göstermektedir. Ancak [çıktı excel dosyasını](5115225.xlsx) açarsanız, Microsoft Excel'in doğru OLE görüntüsünü gösterdiğini göreceksiniz.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object from your sample excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample_oleobject.xlsx"));

// Access first worksheet
const sheet = workbook.getWorksheets().get(0);

// Set auto load property of first ole object to true
sheet.getOleObjects().get(0).setAutoLoad(true);

// Save the workbook in xlsx format
workbook.save(path.join(dataDir, "RefreshOLEObjects_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```  
