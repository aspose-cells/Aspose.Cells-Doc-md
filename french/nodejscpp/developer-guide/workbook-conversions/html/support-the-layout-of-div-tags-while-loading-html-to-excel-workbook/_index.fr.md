---  
title: Prise en charge de la mise en page des balises DIV lors du chargement de HTML dans un classeur Excel avec Node.js via C++  
linktitle: Prise en charge de la mise en page des balises DIV lors du chargement de HTML dans un classeur Excel  
type: docs  
weight: 50  
url: /fr/nodejs-cpp/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/  
---  

{{% alert color="primary" %}}  
Normalement, la mise en page des balises div est ignorée lors du chargement du HTML dans un objet classeur Excel. Cependant, si vous souhaitez que la mise en page des balises div ne soit pas ignorée, veuillez régler la propriété [HtmlLoadOptions.getSupportDivTag()](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getSupportDivTag--) sur **true**. La valeur par défaut de cette propriété est **false**.  
{{% /alert %}}  

Le code exemple suivant illustre l'utilisation de la propriété [HtmlLoadOptions.getSupportDivTag()](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getSupportDivTag--) . Veuillez télécharger le [logo Aspose](5115218.png) utilisé dans le HTML d'entrée et le [fichier Excel de sortie](5115220.xlsx) généré par le code.

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
