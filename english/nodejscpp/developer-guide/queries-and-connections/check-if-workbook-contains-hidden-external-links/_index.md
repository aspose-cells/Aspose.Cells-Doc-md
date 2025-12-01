---  
title: Check if Workbook contains hidden External Links with Node.js via C++  
linktitle: Check if Workbook contains hidden External Links  
type: docs  
weight: 230  
url: /nodejs-cpp/check-if-workbook-contains-hidden-external-links/  
description: Learn how to check if a workbook contains hidden external links using Aspose.Cells for Node.js via C++.  
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

## **Possible Usage Scenarios**  
Sometimes, the workbook contains external links which are hidden and cannot be viewed in Microsoft Excel. Aspose.Cells retrieves all the external links whether they are visible or hidden. However, you can check the [ExternalLink.isVisible()](https://reference.aspose.com/cells/nodejs-cpp/externallink/#isVisible--) property to check if the external link is visible or not.

## **Check if Workbook contains hidden External Links**  
The following sample code loads the [source excel file](5115413.xlsx) which contains hidden external links. These links cannot be viewed in Microsoft Excel but they are present inside the workbook. After printing [ExternalLink.getDataSource()](https://reference.aspose.com/cells/nodejs-cpp/externallink/#getDataSource--) and [ExternalLink.isReferred()](https://reference.aspose.com/cells/nodejs-cpp/externallink/#isReferred--) property, it prints the [ExternalLink.isVisible()](https://reference.aspose.com/cells/nodejs-cpp/externallink/#isVisible--) property. In the console output below, you see all of its external links are not visible.

### **Sample Code**  
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

### **Console Output**  
Here is the console output of the above sample code when executed with the given [sample excel file](5115413.xlsx).

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
