---  
title: Node.js kullanarak C++ ile Çalışma Sayfası Sekmesi Rengini Ayarla  
linktitle: Çalışma Taşrafları Sekme Rengi Ayarla  
type: docs  
weight: 120  
url: /tr/nodejs-cpp/set-worksheet-tab-color/  
description: Bu makale, Node.js kullanarak C++ aracılığıyla Excel çalışma sayfası sekmesi rengini programatik olarak ayarlayan örnek kodu gösterir.  
keywords: excel sekme rengi ayarla Node.js üzerinden C++ ile, excel sekme rengi ayarlama kodu Node.js üzerinde C++ ile  
---  

{{% alert color="primary" %}}  

Aspose.Cells, bireysel çalışma sayfası sekmelerinin rengini değiştirmenize olanak tanır, böylece onları geri kalanından ayırt edebilirsiniz. Örneğin, Giderleri kırmızı, Satışları yeşil, Varlıkları mavi vb. yapabilirsiniz.

{{% /alert %}}  
## **Microsoft Excel ile Çalışma Sayfası Sekmesi Rengini Ayarlama**  
1. Mevcut çalışma sayfasının altındaki sekme sayfasında bir sekmeye sağ tıklayın.  
1. **Sekme rengi**'ni seçin.  
1. Paletten bir renk seçin.  
1. **Tamam**'a tıklayın.  
## **Aspose.Cells ile Çalışma Taşraflarında Sekme Rengi Ayarı**  
Aşağıdaki örnek kod, Aspose.Cells ile sekme rengini ayarlamanın nasıl yapıldığını göstermektedir.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a new Workbook
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Book1.xlsx"));

// Get the first worksheet in the book
const worksheet = workbook.getWorksheets().get(0);

// Set the tab color
worksheet.setTabColor(AsposeCells.Color.Red);

// Save the Excel file
workbook.save(path.join(dataDir, "worksheettabcolor.out.xls"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
