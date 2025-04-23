---  
title: Verifica se il Workbook contiene collegamenti esterni nascosti con Node.js tramite C++  
linktitle: Controllare se il foglio di lavoro contiene collegamenti esterni nascosti  
type: docs  
weight: 230  
url: /it/nodejs-cpp/check-if-workbook-contains-hidden-external-links/  
description: Impara come verificare se un workbook contiene collegamenti esterni nascosti usando Aspose.Cells for Node.js via C++.  
---  

## **Possibili Scenari di Utilizzo**  
A volte, il workbook contiene collegamenti esterni nascosti che non possono essere visualizzati in Microsoft Excel. Aspose.Cells recupera tutti i collegamenti esterni, siano essi visibili o nascosti. Tuttavia, puoi controllare la proprietà [ExternalLink.isVisible()](https://reference.aspose.com/cells/nodejs-cpp/externallink/#isVisible--) per verificare se il collegamento esterno è visibile o meno.

## **Controllare se il foglio di lavoro contiene collegamenti esterni nascosti**  
Il seguente esempio di codice carica il [file Excel di origine](5115413.xlsx) che contiene collegamenti esterni nascosti. Questi collegamenti non sono visibili in Microsoft Excel, ma sono presenti nel workbook. Dopo aver stampato le proprietà [ExternalLink.getDataSource()](https://reference.aspose.com/cells/nodejs-cpp/externallink/#getDataSource--) e [ExternalLink.isReferred()](https://reference.aspose.com/cells/nodejs-cpp/externallink/#isReferred--), vengono stampate anche le proprietà [ExternalLink.isVisible()](https://reference.aspose.com/cells/nodejs-cpp/externallink/#isVisible--). Nell'output della console sottostante, puoi notare che tutti i collegamenti esterni non sono visibili.

### **Codice di Esempio**  
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

### **Output della console**  
Ecco l'output della console del codice di esempio sopra quando eseguito con il [file di Excel di esempio](5115413.xlsx).

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
