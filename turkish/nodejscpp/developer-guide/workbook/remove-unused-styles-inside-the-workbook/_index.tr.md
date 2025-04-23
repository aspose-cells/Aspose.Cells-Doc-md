---  
title: Kullanılmayan Stillleri Çalışma Kitabından Node.js ve C++ kullanarak kaldırma  
linktitle: Çalışma Kitabı İçinde Kullanılmayan Stilleri Kaldırma  
type: docs  
weight: 340  
url: /tr/nodejs-cpp/remove-unused-styles-inside-the-workbook/  
description: Aspose.Cells for Node.js via C++ kullanarak çalışma kitabından kullanılmayan stilleri kaldırmayı öğrenin.  
---  

{{% alert color="primary" %}}  
Excel dosyalarındaki kullanılmayan stiller sadece yer kaplamaz, aynı zamanda PDF, HTML vb. farklı formatlara dönüştürürken performans sorunlarına da neden olur. Aspose.Cells, çalışma kitabındaki tüm kullanılmayan stilleri kaldırmanızı sağlayan [**Workbook.removeUnusedStyles()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#removeUnusedStyles--) sağlar.  
{{% /alert %}}  

Aşağıdaki kod, [**Workbook.removeUnusedStyles()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#removeUnusedStyles--) kullanımını açıklar. Kod, sağlanan bağlantıdan indirilebilecek şablon Excel dosyasını yükler. Bu dosyada **AsposeStyle** adlı kullanılmayan bir stil bulunmaktadır; bu stil ve diğer tüm kullanılmayan stiller, kod yürütüldükten sonra kaldırılacaktır.  

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Template-With-Unused-Custom-Style.xlsx");

// Load template excel file containing unused styles
const workbook = new AsposeCells.Workbook(filePath);

// Remove all unused styles inside the template this will also remove AsposeStyle which is an unused style inside the template
workbook.removeUnusedStyles();

// Save the file
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

