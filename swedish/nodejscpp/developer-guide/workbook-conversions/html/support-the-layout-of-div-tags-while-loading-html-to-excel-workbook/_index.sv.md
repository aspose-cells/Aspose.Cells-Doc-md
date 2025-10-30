---  
title: Stöd för layout av DIV taggar när du laddar HTML till Excel arbetsbok med Node.js via C++  
linktitle: Stöd för layout av DIV taggar när du laddar HTML till Excel arbetsbok  
type: docs  
weight: 50  
url: /sv/nodejs-cpp/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/  
---  

{{% alert color="primary" %}}  
Vanligtvis ignoreras layouten av div-taggar när HTML laddas in i ett Excel-arbetsboksobjekt. Men om du vill att layouten av div-taggar inte ska ignoreras, ska du ställa in egenskapen [HtmlLoadOptions.getSupportDivTag()](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getSupportDivTag--) till **true**. Standardvärdet för denna egenskap är **false**.  
{{% /alert %}}  

Följande kodexempel illustrerar användningen av egenskapen [HtmlLoadOptions.getSupportDivTag()](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getSupportDivTag--). Vänligen ladda ner [Aspose-logotypen](5115218.png) som används inuti input HTML och [output-Excel-filen](5115220.xlsx) som genereras av koden.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const exportHtml = `
<html>
<body>
<table>
<tr>
<td>
<div>This is some Text.</div>
<div>
<div>
<span>This is some more Text</span>
</div>
<div>
<span>abc@abc.com</span>
</div>
<div>
<span>1234567890</span>
</div>
<div>
<span>ABC DEF</span>
</div>
</div>
<div>Generated On May 30, 2016 02:33 PM <br />Time Call Received from Jan 01, 2016 to May 30, 2016</div>
</td>
<td>
<img src="${dataDir}/ASpose_logo_100x100.png" />
</td>
</tr>
</table>
</body>
</html>`;

const ms = Buffer.from(exportHtml, "utf-8");

// Specify HTML load options, support div tag layouts
const loadOptions = new AsposeCells.HtmlLoadOptions(AsposeCells.LoadFormat.Html);
loadOptions.setSupportDivTag(true);

// Create workbook object from the html using load options
const wb = new AsposeCells.Workbook(ms, loadOptions);

// Auto fit rows and columns of first worksheet
const ws = wb.getWorksheets().get(0);
ws.autoFitRows();
ws.autoFitColumns();

// Save the workbook in xlsx format
wb.save(path.join(dataDir, "DivTagsLayout_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
