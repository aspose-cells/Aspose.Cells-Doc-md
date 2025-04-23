---  
title: Ta bort oanvända stilar inne i arbetsboken med Node.js via C++  
linktitle: Ta bort oanvända stilar inne i arbetsboken  
type: docs  
weight: 340  
url: /sv/nodejs-cpp/remove-unused-styles-inside-the-workbook/  
description: Lär dig hur du tar bort oanvända stilar från en arbetsbok med Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Oanvända stilar i Excel-filer tar inte bara upp utrymme utan kan också orsaka prestandaproblem vid konvertering till olika format som PDF, HTML etc. Aspose.Cells tillhandahåller [**Workbook.removeUnusedStyles()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#removeUnusedStyles--) för att ta bort alla oanvända stilar i arbetsboken.  
{{% /alert %}}  

Följande kod förklarar användningen av [**Workbook.removeUnusedStyles()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#removeUnusedStyles--). Koden laddar [mallexcelfilen](5115520.xlsx) som du kan ladda ner från länken. Den innehåller en oanvänd stil som heter **AsposeStyle**; denna stil och alla andra oanvända stilar tas bort efter körning.  

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

