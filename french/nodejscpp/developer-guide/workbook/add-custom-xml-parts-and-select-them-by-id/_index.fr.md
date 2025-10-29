---  
title: Ajouter des parties XML personnalisées et les sélectionner par ID avec Node.js via C++  
linktitle: Ajouter des parties XML personnalisées et les sélectionner par ID  
type: docs  
weight: 70  
url: /fr/nodejs-cpp/add-custom-xml-parts-and-select-them-by-id/  
description: Découvrez comment ajouter des parties XML personnalisées aux documents Excel et les sélectionner par ID en utilisant Aspose.Cells for Node.js via C++.  
---  

## **Scénarios d'utilisation possibles**  

Les parties XML personnalisées sont les données XML stockées à l'intérieur des documents Microsoft Excel et sont utilisées par les applications qui en ont besoin. Il n'existe pas de moyen direct de les ajouter via l'interface utilisateur de Microsoft Excel pour le moment. Cependant, vous pouvez les ajouter de manière programmatique de diverses façons, par exemple avec VSTO, Aspose.Cells, etc. Utilisez [**Workbook.getCustomXmlParts()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getCustomXmlParts--) si vous souhaitez ajouter une partie XML personnalisée en utilisant l'API Aspose.Cells. Vous pouvez également définir son ID avec la propriété [**CustomXmlPart.getID()**](https://reference.aspose.com/cells/nodejs-cpp/customxmlpart/#getID--). De même, si vous souhaitez sélectionner une partie XML personnalisée par ID, vous pouvez utiliser la méthode [**Workbook.getCustomXmlParts()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getCustomXmlParts--).  

## **Ajouter des parties XML personnalisées et les sélectionner par ID**  

Le code d'exemple suivant ajoute d'abord quatre parties XML personnalisées en utilisant la méthode [**Workbook.getCustomXmlParts()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getCustomXmlParts--). Il définit ensuite leurs IDs avec la propriété [**CustomXmlPart.getID()**](https://reference.aspose.com/cells/nodejs-cpp/customxmlpart/#getID--). Enfin, il trouve ou sélectionne une des parties XML personnalisées ajoutées en utilisant la méthode [**Workbook.getCustomXmlParts()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getCustomXmlParts--). Consultez également la sortie console du code ci-dessous pour référence.  

## **Code d'exemple**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const wb = new AsposeCells.Workbook(filePath);

// Some data in the form of byte array.
// Please use correct XML and Schema instead.
const btsData = new Uint8Array([1, 2, 3]);
const btsSchema = new Uint8Array([1, 2, 3]);

// Create four custom xml parts.
wb.getCustomXmlParts().add(btsData, btsSchema);
wb.getCustomXmlParts().add(btsData, btsSchema);
wb.getCustomXmlParts().add(btsData, btsSchema);
wb.getCustomXmlParts().add(btsData, btsSchema);

// Assign ids to custom xml parts.
wb.getCustomXmlParts().get(0).setID("Fruit");
wb.getCustomXmlParts().get(1).setID("Color");
wb.getCustomXmlParts().get(2).setID("Sport");
wb.getCustomXmlParts().get(3).setID("Shape");

// Specify search custom xml part id.
let srchID = "Fruit";
srchID = "Color";
srchID = "Sport";

// Search custom xml part by the search id.
const cxp = wb.getCustomXmlParts().selectByID(srchID);

// Print the found or not found message on console.
if (cxp.isNull()) {
console.log(`Not Found: CustomXmlPart ID ${srchID}`);
} else {
console.log(`Found: CustomXmlPart ID ${srchID}`);
}

console.log("AddCustomXMLPartsAndSelectThemByID executed successfully.");
```  

## **Sortie console**  

{{< highlight java >}}  
 Found: CustomXmlPart ID Sport  
{{< /highlight >}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
