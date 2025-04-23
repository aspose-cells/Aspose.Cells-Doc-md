---  
title: Exportera DataBar, ColorScale och IconSet villkorsstyrd formatering under konvertering av Excel till HTML med Node.js via C++  
linktitle: Exportera DataBar, ColorScale och IconSet Villkorlig formatering vid konvertering av Excel till HTML  
type: docs  
weight: 30  
url: /sv/nodejs-cpp/export-databar-colorscale-and-iconset-conditional-formatting-while-excel-to-html-conversion/  
---  

{{% alert color="primary" %}} 

Du kan exportera DataBar, ColorScale och IconSet villkorsstyrd formatering när du konverterar din Excel-fil till HTML. Denna funktion stöds delvis av Microsoft Excel, men Aspose.Cells for Node.js via C++ stöder den fullt ut.

{{% /alert %}}  

## **Exportera DataBar, ColorScale och IconSet villkorlig formatering vid Excel till HTML-omvandling**  
Den följande skärmbilden visar [provexelfilen](5115558.xlsx) med DataBar, ColorScale och IconSet Conditional Formatting. Du kan ladda ner [provexelfilen](5115558.xlsx) från den angivna länken.  

![todo:image_alt_text](conversion_1.png)  

Den följande skärmbilden visar Aspose.Cells utdata-HTML-fil som visar DataBar, ColorScale och IconSet Conditional Formatting. Som du kan se ser den ut precis som [provexelfilen](5115558.xlsx).  

![todo:image_alt_text](conversion_2.png)  

### **Exempelkod**  
Följande kodexempel konverterar exempel-Excelfilen till HTML, vilket är en vanlig [Excel till HTML-konvertering](/cells/sv/nodejs-cpp/convert-workbook-to-different-formats/#convertworkbooktodifferentformats-convertingexcelworkbooktohtml).  
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


