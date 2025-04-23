---  
title: Node.js aracılığıyla C++ kullanarak Çalışma Kitabını Yazarken Yazar Belirtin  
linktitle: Çalışma Kitabını Korumaya Alırken Yazarı Belirtme  
type: docs  
weight: 40  
url: /tr/nodejs-cpp/specify-author-while-write-protecting-workbook/  
description: Aspose.Cells for Node.js via C++ kullanarak çalışma kitabını yazdırırken bir yazar adı belirtin.  
---  

## **Olası Kullanım Senaryoları**

Aspose.Cells API kullanarak çalışma kitabınızı yazarken yazar adını belirtebilirsiniz. Bu amaçla [**Workbook.getAuthor()**](https://reference.aspose.com/cells/nodejs-cpp/writeprotection/#getAuthor--) özelliğini kullanın.

## **Çalışma Kitabını Yazma Koruması Sırasında Yazar Belirtme**

Aşağıdaki örnek kod, [**Workbook.getAuthor()**](https://reference.aspose.com/cells/nodejs-cpp/writeprotection/#getAuthor--) özelliğinin kullanımını açıklar. Kod, boş bir çalışma kitabı oluşturur, şifre ile korur, yazar adını belirtir ve [çıktı Excel dosyası](67338582.xlsx) olarak kaydeder. Aşağıdaki ekran görüntüsü, örnek kodun çıktı Excel dosyasına etkisini gösterir.

![todo:image_alt_text](specify-author-while-write-protecting-workbook_1.png)

## **Örnek Kod**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Create empty workbook.
const workbook = new AsposeCells.Workbook();

// Write protect workbook with password.
workbook.getSettings().getWriteProtection().setPassword("1234");

// Specify author while write protecting workbook.
workbook.getSettings().getWriteProtection().setAuthor("SimonAspose");

// Save the workbook in XLSX format.
const outputDir = path.join(__dirname, "output");
workbook.save(path.join(outputDir, "outputSpecifyAuthorWhileWriteProtectingWorkbook.xlsx"));
```  

