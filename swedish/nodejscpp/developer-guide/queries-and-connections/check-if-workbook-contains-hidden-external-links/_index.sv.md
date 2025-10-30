---  
title: Kontrollera om arbetsboken innehåller dolda externa länkar med Node.js via C++  
linktitle: Kontrollera om arbetsboken innehåller dolda externa länkar  
type: docs  
weight: 230  
url: /sv/nodejs-cpp/check-if-workbook-contains-hidden-external-links/  
description: Lär dig hur man kontrollerar om en arbetsbok innehåller dolda externa länkar med Aspose.Cells for Node.js via C++.  
---  

## **Möjliga användningsscenario**  
Ibland innehåller arbetsboken externa länkar som är dolda och inte kan ses i Microsoft Excel. Aspose.Cells hämtar alla externa länkar oavsett om de är synliga eller dolda. Du kan dock kontrollera [ExternalLink.isVisible()](https://reference.aspose.com/cells/nodejs-cpp/externallink/#isVisible--) egenskapen för att se om den externa länken är synlig eller inte.

## **Kontrollera om arbetsboken innehåller dolda externa länkar**  
Följande exempel laddar [källfilen](5115413.xlsx) som innehåller dolda externa länkar. Dessa länkar kan inte ses i Microsoft Excel men de finns i arbetsboken. Efter att ha skrivit ut [ExternalLink.getDataSource()](https://reference.aspose.com/cells/nodejs-cpp/externallink/#getDataSource--) och [ExternalLink.isReferred()](https://reference.aspose.com/cells/nodejs-cpp/externallink/#isReferred--) egenskaper, skrivs [ExternalLink.isVisible()](https://reference.aspose.com/cells/nodejs-cpp/externallink/#isVisible--) ut. I konsolutdata nedan kan du se att alla externa länkar inte är synliga.

### **Exempelkod**  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access the external link collection of the workbook
const links = workbook.getWorksheets().getExternalLinks();

// Print all the external links and check their IsVisible property
for (let i = 0; i < links.getCount(); i++) {
console.log("Data Source: " + links.get(i).getDataSource());
console.log("Is Referred: " + links.get(i).getIsReferred());
console.log("Is Visible: " + links.get(i).getIsVisible());
console.log();
}
```  

### **Konsoloutput**  
Här är konsoloutputen av ovanstående kodexempel när den körs med den angivna [prov-Excel-filen](5115413.xlsx).

{{< highlight java >}}  
 Data Source: C:\International\DDB\FAS 133\Swap Rates\GS_1M_3M_1_2_5_¥$_(B)IRSwaps_0400.xls  

Is Referred: True  

Is Visible: False  

Data Source: C:\DIST DAY\MAY TEMPLATES\030601t.xls  

Is Referred: True  

Is Visible: False  

Data Source: C:\AREVIEW\2002 Controllable\Autobrct.xls  

Is Referred: True  

Is Visible: False  

Data Source: C:\CARDSFO\Main Files\Rate Forecast\FY 11\IFR 11 01 (New Model REPORTS 11.08.07).xls  

Is Referred: True  

Is Visible: False  
{{< /highlight >}}  
{{< app/cells/assistant language="nodejs-cpp" >}}
