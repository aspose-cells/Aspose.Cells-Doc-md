---  
title: Hur man ställer in AutoRecover egenskapen för arbetsboken med Node.js via C++  
linktitle: Hur man ställer in egenskapen AutoRecover för arbetsboken  
type: docs  
weight: 220  
url: /sv/nodejs-cpp/how-to-set-autorecover-property-of-workbook/  
description: Lär dig hur man ställer in AutoRecover egenskapen för en arbetsbok med Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Du kan använda Aspose.Cells för att ställa in AutoRecover-egenskapen för arbetsboken. Standardvärdet för denna egenskap är **true**. När du ställer in den till **false** inaktiveras autospar funktioner i Microsoft Excel för den aktuella Excel-filen.  

Aspose.Cells tillhandahåller egenskapen [**Workbook.getAutoRecover()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getAutoRecover--) för att aktivera eller inaktivera detta alternativ.  
{{% /alert %}}  

Följande kod förklarar hur man använder [**Workbook.getAutoRecover()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getAutoRecover--) egenskapen för arbetsboken. Koden läser först det förvalda värdet av egenskapen som är **true**, ställer sedan in det som **false** och sparar arbetsboken. Därefter läser den arbetsboken igen och hämtar värdet av egenskapen som är **false** vid denna tidpunkt.  

## Node.js-kod för att ställa in AutoRecover-egenskapen för arbetsboken  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const workbook = new AsposeCells.Workbook();

// Read AutoRecover property
console.log("AutoRecover: " + workbook.getSettings().getAutoRecover());

// Set AutoRecover property to false
workbook.getSettings().setAutoRecover(false);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));

// Read the saved workbook again
const workbook2 = new AsposeCells.Workbook(path.join(dataDir, "output_out.xlsx"));

// Read AutoRecover property
console.log("AutoRecover: " + workbook2.getSettings().getAutoRecover());
```  

## **Output**  

Här är konsoloutputen från ovanstående exempelkod.  

{{< highlight java >}}  
AutoRecover: True  
AutoRecover: False  
{{< /highlight >}}  

