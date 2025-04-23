---  
title: Node.js kullanarak Excel dosyasını HTML ye dışa aktarırken sağa doğru genişleyen metin  
linktitle: Excel den HTML ye Dönüştürürken Metni Sağdan Sola Doğru Genişletme  
type: docs  
weight: 60  
url: /tr/nodejs-cpp/expanding-text-from-right-to-left-while-exporting-excel-file-to/  
---  

{{% alert color="primary" %}}  

Aspose.Cells, Excel dosyasını HTML'e dönüştürürken metni sağdan sola doğru genişletmeyi destekler. Bu özellik, v8.9.0.0'dan itibaren uygulanmıştır. Artık kaynak Excel dosyanız sağdan sola doğru genişleyen metin içeriyorsa, Aspose.Cells bunu HTML olarak doğru bir şekilde dışa aktaracaktır.  

{{% /alert %}}  
## **Excel dosyasını HTML'e dönüştüren aşağıdaki örnek kod. Bu ekran görüntüsü, örnek Excel dosyasının Microsoft Excel 2013'te nasıl göründüğünü göstermektedir.**  
Aşağıdaki örnek kod, [örnek excel dosyasını](5115502.xlsx) HTML'ye dönüştürür. Bu ekran görüntüsü, örnek excelin Microsoft Excel 2013'te nasıl göründüğünü göstermektedir.  

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_1.png)  

Bu ekran görüntüsü, eski sürümle oluşturulan [çıktı HTML'yi](5115509) göstermektedir.  

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_2.png)  

Bu ekran görüntüsü, daha yeni sürümle oluşturulan [çıktı HTML'yi](5115508) göstermektedir.  

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_3.png)  

Ekran görüntülerinde görebileceğiniz gibi, yeni sürüm sağa hizalanan metni Microsoft Excel gibi doğru bir şekilde sola genişletebilmektedir.  


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Load source excel file inside the workbook object
const wb = new AsposeCells.Workbook(filePath);

// Save workbook in html format
wb.save(path.join(dataDir, `ExpandTextFromRightToLeft_out_${AsposeCells.CellsHelper.getVersion()}.html`), AsposeCells.SaveFormat.Html);
```  

