---  
title: Spreadsheets dönüştürürken WordArt için Gradient Doldurma Render Etmek (Node.js ve C++ ile)  
linktitle: Hücre Dizelerini HTML ye Dönüştürürken WordArt için Gradient Doldurmayı Oluşturma  
type: docs  
weight: 90  
url: /tr/nodejs-cpp/render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to/  
description: Aspose.Cells for Node.js via C++ kullanarak WordArt için Gradient Doldurma Render etmeyi öğrenin.  
---  

## **Olası Kullanım Senaryoları**  
Aspose.Cells 17.1 öncesinde, Excel dosyası HTML formatına dönüştürülürken, WordArt'ın gradient dolumu render edilmezdi. Aspose.Cells 17.1 sürümünden itibaren WordArt gradient dolumu desteklenmektedir. Aşağıdaki ekran görüntüsü, Aspose.Cells 17.1 ve eski sürüm kullanılarak Excel dosyasının dönüştürülmesiyle gradient dolumu üzerindeki etkiyi karşılaştırır.  

![todo:image_alt_text](render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to-html_1.png)  

## **Hücre Dizelerini HTML'ye dönüştürürken word art için gradient doldurmayı oluştur.**  
Aşağıdaki örnek kod, [kaynak excel dosyasını](22774111.xlsx) [çıktı HTML formatına](22774109.zip) dönüştürür. Kaynak excel dosyası, yukarıdaki ekran görüntüsünde gösterilen gradient dolumu olan WordArt nesnesini içerir.  

## **Örnek Kod**  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sourceGradientFill.xlsx");

// Read the source excel file having text with gradient fill
const workbook = new AsposeCells.Workbook(filePath);

// Save workbook to html format
workbook.save(path.join(dataDir, "out_sourceGradientFill.html"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
