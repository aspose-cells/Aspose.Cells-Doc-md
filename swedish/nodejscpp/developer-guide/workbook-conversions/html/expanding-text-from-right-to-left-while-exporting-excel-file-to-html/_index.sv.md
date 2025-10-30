---  
title: Utöka texten från höger till vänster när du exporterar Excel filen till HTML med Node.js via C++  
linktitle: Expandera text från höger till vänster vid export av Excel fil till HTML  
type: docs  
weight: 60  
url: /sv/nodejs-cpp/expanding-text-from-right-to-left-while-exporting-excel-file-to/  
---  

{{% alert color="primary" %}}  

Aspose.Cells stödjer nu att expandera text från höger till vänster vid export av Excel-fil till HTML. Denna funktion har implementerats sedan v8.9.0.0. Nu om din käll-Excel-fil innehåller någon text som expanderar från höger till vänster, kommer Aspose.Cells att exportera den till HTML korrekt.  

{{% /alert %}}  
## **Expandera text från höger till vänster vid export av Excel-fil till HTML**  
Det följande kodexemplet konverterar [provexelfilen](5115502.xlsx) till HTML. Denna skärmbild visar hur provexelfilen ser ut i Microsoft Excel 2013.  

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_1.png)  

Denna skärmbild visar [utdata-HTML genererad med äldre version](5115509).  

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_2.png)  

Denna skärmbild visar [utdata-HTML genererad med nyare version](5115508).  

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_3.png)  

Som du kan se i skärmbilderna, expanderar den nyare versionen den högerjusterade texten till vänster korrekt precis som Microsoft Excel.  


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

{{< app/cells/assistant language="nodejs-cpp" >}}
