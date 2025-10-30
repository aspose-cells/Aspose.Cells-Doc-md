---  
title: Node.js via C++ kullanarak Excel den HTML ye Dışa Aktarırken DataBar, ColorScale ve IconSet Koşullu Biçimlendirmeleri dışa aktarın  
linktitle: DataBar, ColorScale ve IconSet Koşullu Biçimlendirmeyi Excel den HTML e Dönüşüm Sırasında Dışa Aktarın  
type: docs  
weight: 30  
url: /tr/nodejs-cpp/export-databar-colorscale-and-iconset-conditional-formatting-while-excel-to-html-conversion/  
---  

{{% alert color="primary" %}} 

Excel dosyanızı HTML'ye dönüştürürken DataBar, ColorScale ve IconSet Koşullu Biçimlendirmeleri dışa aktarabilirsiniz. Bu özellik kısmen Microsoft Excel tarafından desteklenmektedir, ancak Aspose.Cells for Node.js via C++ bunu tam olarak destekler.

{{% /alert %}}  

## **Excel'den HTML'ye Databar, ColorScale ve IconSet Koşullu Biçimlendirmeyi Dışa Aktar**  
Aşağıdaki ekran görüntüsü, VeriÇubuğu, RenkÖlçeği ve SimgeSeti Koşullu Biçimlendirme ile [örnek excel dosyasını](5115558.xlsx) göstermektedir. Verilen bağlantıdan [örnek excel dosyasını](5115558.xlsx) indirebilirsiniz.  

![todo:image_alt_text](conversion_1.png)  

Aşağıdaki ekran görüntüsü, Aspose.Cells çıktı HTML dosyasını VeriÇubuğu, RenkÖlçeği ve SimgeSeti Koşullu Biçimlendirme göstermektedir. Gördüğünüz gibi, [örnek excel dosyası](5115558.xlsx)'yle tamamen aynı görünüyor.  

![todo:image_alt_text](conversion_2.png)  

### **Örnek Kod**  
Aşağıdaki örnek kod, örnek excel dosyasını HTML'ye dönüştürür; bu, sadece normal bir [Excel'den HTML'ye dönüşüm](/cells/tr/nodejs-cpp/convert-workbook-to-different-formats/#convertworkbooktodifferentformats-convertingexcelworkbooktohtml) örneğidir.  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Specify the file path
const filePath = path.join(dataDir, "sample.xlsx");

// Load your sample excel file in a workbook object
const wb = new AsposeCells.Workbook(filePath);

// Save it in HTML format
wb.save(path.join(dataDir, "ConvertingToHTMLFiles_out.html"), AsposeCells.SaveFormat.Html);
```  


{{< app/cells/assistant language="nodejs-cpp" >}}
