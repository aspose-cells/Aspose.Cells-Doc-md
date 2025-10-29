---  
title: Vérifier si le classeur contient des liens externes cachés avec Node.js via C++  
linktitle: Vérifiez si le classeur contient des liens externes cachés  
type: docs  
weight: 230  
url: /fr/nodejs-cpp/check-if-workbook-contains-hidden-external-links/  
description: Apprenez comment vérifier si un classeur contient des liens externes cachés en utilisant Aspose.Cells for Node.js via C++.  
---  

## **Scénarios d'utilisation possibles**  
Parfois, le classeur contient des liens externes qui sont cachés et ne peuvent pas être vus dans Microsoft Excel. Aspose.Cells récupère tous les liens externes qu'ils soient visibles ou cachés. Cependant, vous pouvez vérifier la propriété [ExternalLink.isVisible()](https://reference.aspose.com/cells/nodejs-cpp/externallink/#isVisible--) pour voir si le lien externe est visible ou non.

## **Vérifiez si le classeur contient des liens externes cachés**  
Le code d'exemple ci-dessous charge le [fichier Excel source](5115413.xlsx) qui contient des liens externes cachés. Ces liens ne peuvent pas être vus dans Microsoft Excel mais ils sont présents dans le classeur. Après avoir affiché [ExternalLink.getDataSource()](https://reference.aspose.com/cells/nodejs-cpp/externallink/#getDataSource--) et la propriété [ExternalLink.isReferred()](https://reference.aspose.com/cells/nodejs-cpp/externallink/#isReferred--), il affiche la propriété [ExternalLink.isVisible()](https://reference.aspose.com/cells/nodejs-cpp/externallink/#isVisible--) dans la console. Dans la sortie, vous voyez que tous ses liens externes ne sont pas visibles.

### **Code d'exemple**  
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

### **Sortie console**  
Voici la sortie console du code d'exemple ci-dessus lors de son exécution avec le [fichier Excel d'exemple](5115413.xlsx) donné.

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
