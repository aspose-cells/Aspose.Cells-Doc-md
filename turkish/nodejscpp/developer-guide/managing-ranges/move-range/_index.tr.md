---  
title: Node.js ve C++ kullanarak Çalışma Sayfasında Hücre Aralığını Taşıma  
linktitle: Çalışma Sayfasında Hücre Aralığını Taşıma  
type: docs  
weight: 370  
url: /tr/nodejs-cpp/move-range-of-cells-in-a-worksheet/  
description: Aspose.Cells for Node.js via C++ kullanarak bir çalışma sayfasında hücre aralığını nasıl hareket ettireceğinizi öğrenin.  
---  

{{% alert color="primary" %}}  
Bu makale, bir çalışma sayfasında hücrelerin bir aralığını nasıl taşıyacağını gösterir.  
{{% /alert %}}  

## **Çalışma Sayfasında Hücre Aralığını Taşıma**  
Örnek kod, görevi göstermek için bir şablon dosyası kullanır.  

**Giriş dosyası**  

![todo:image_alt_text](move-range-of-cells-in-a-worksheet_1.png)  

Lütfen A1:B5 aralığındaki hücreleri C1:D5'e taşıyan oluşturulan dosyayı inceleyin.  

**Çıkış dosyası**  

![todo:image_alt_text](move-range-of-cells-in-a-worksheet_2.png)  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xlsx");
// Instantiate the workbook object. Open the Excel file
const workbook = new AsposeCells.Workbook(filePath);

const cells = workbook.getWorksheets().get(0).getCells();

const range = cells.createRange("A1", "B5");
//move the range to right.
range.moveTo(0, 2);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
