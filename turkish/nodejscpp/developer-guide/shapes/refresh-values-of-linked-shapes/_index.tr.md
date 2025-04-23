---  
title: Bağlantılı Şekillerin Değerlerini Güncelleyerek Node.js ile C++ üzerinden Güncelle  
linktitle: Bağlı Şekillerin Değerlerini Yenile  
type: docs  
weight: 3200  
url: /tr/nodejs-cpp/refresh-values-of-linked-shapes/  
description: Excel de bağlantılı şekillerin değerlerini nasıl yenileyeceğinizi öğrenin Aspose.Cells for Node.js via C++ ile.  
---  

{{% alert color="primary" %}}  

Bazen, Excel dosyanızda bir hücreye bağlı olan bir bağlantılı şekil vardır. Microsoft Excel'de, bağlantılı hücrenin değerini değiştirmeniz, bağlantılı şeklin değerini de değiştirir. Bu, Aspose.Cells for Node.js via C++ ile XLS veya XLSX formatında çalışma kitabınızı kaydetmek istiyorsanız çalışır. Ancak, çalışma kitabınızı PDF veya HTML formatında kaydetmek istiyorsanız, [**ShapeCollection.updateSelectedValue()**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#updateSelectedValue--) metodunu çağırarak bağlantılı şeklin değerini yenilemeniz gerekir.  

{{% /alert %}}  

## Örnek  

Aşağıdaki ekran görüntüsü, aşağıdaki örnek kodda kullanılan kaynak Excel dosyasını gösterir. Bu dosyada A1 ile E4 hücreleri arasında bağlantılı bir resim vardır. Aspose.Cells ile B4 hücresinin değerini değiştirecek ve ardından [**ShapeCollection.updateSelectedValue()**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#updateSelectedValue--) metodunu çağırarak resmin değerini yenileyecek ve PDF formatında kaydedeceğiz.  

![todo:image_alt_text](refresh-values-of-linked-shapes_1.jpg)  

Sağlanan bağlantılardan [ kaynak Excel dosyasını](95584291.xlsx) ve [çıktı PDF'sini](95584292.pdf) indirebilirsiniz.  

### Bağlantılı şekillerin değerlerini yenilemek için Node.js kodu  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Create workbook from source file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleRefreshValueOfLinkedShapes.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Change the value of cell B4
const cell = worksheet.getCells().get("B4");
cell.putValue(100);

// Update the value of the Linked Picture which is linked to cell B4
worksheet.getShapes().updateSelectedValue();

// Save the workbook in PDF format
workbook.save(path.join(outputDir, "outputRefreshValueOfLinkedShapes.pdf"), AsposeCells.SaveFormat.Pdf);
```  
