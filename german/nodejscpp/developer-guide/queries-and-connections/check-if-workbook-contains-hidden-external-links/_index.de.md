---  
title: Überprüfen, ob die Arbeitsmappe versteckte externe Links enthält mit Node.js über C++  
linktitle: Überprüfen, ob die Arbeitsmappe versteckte externe Verknüpfungen enthält  
type: docs  
weight: 230  
url: /de/nodejs-cpp/check-if-workbook-contains-hidden-external-links/  
description: Erfahren Sie, wie Sie überprüfen, ob eine Arbeitsmappe versteckte externe Links enthält, mit Aspose.Cells for Node.js via C++.  
---  

## **Mögliche Verwendungsszenarien**  
Manchmal enthält die Arbeitsmappe externe Links, die versteckt sind und in Microsoft Excel nicht sichtbar sind. Aspose.Cells liest alle externen Links aus, egal ob sie sichtbar sind oder nicht. Sie können jedoch die Eigenschaft [ExternalLink.isVisible()](https://reference.aspose.com/cells/nodejs-cpp/externallink/#isVisible--) verwenden, um zu prüfen, ob der externe Link sichtbar ist oder nicht.

## **Überprüfen, ob die Arbeitsmappe versteckte externe Verknüpfungen enthält**  
Das folgende Beispiel lädt die [Quelldatei](5115413.xlsx), die versteckte externe Links enthält. Diese Links sind in Microsoft Excel nicht sichtbar, sind aber im Arbeitsbuch vorhanden. Nach dem Drucken von [ExternalLink.getDataSource()](https://reference.aspose.com/cells/nodejs-cpp/externallink/#getDataSource--) und [ExternalLink.isReferred()](https://reference.aspose.com/cells/nodejs-cpp/externallink/#isReferred--) sowie der Eigenschaft [ExternalLink.isVisible()](https://reference.aspose.com/cells/nodejs-cpp/externallink/#isVisible--) wird diese ausgegeben. In der untenstehenden Konsolenausgabe sind alle externen Links sichtbar.

### **Beispielcode**  
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

### **Konsolenausgabe**  
Hier ist die Konsolenausgabe des obigen Beispielcodes bei Ausführung mit der angegebenen [Beispiel-Excel-Datei](5115413.xlsx).

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
