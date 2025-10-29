---  
title: Ajouter une carte XML dans le classeur en utilisant la méthode XmlMapCollection.Add avec Node.js via C++  
linktitle: Ajouter une carte XML à l intérieur du classeur à l aide de la méthode Add d XmlMapCollection  
type: docs  
weight: 10  
url: /fr/nodejs-cpp/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/  
description: Apprenez comment ajouter une carte XML dans le classeur en utilisant la méthode XmlMapCollection.Add avec Aspose.Cells for Node.js via C++.  
---  

## **Scénarios d'utilisation possibles**  

Aspose.Cells fournit une méthode [**XmlMapCollection.add(string)**](https://reference.aspose.com/cells/nodejs-cpp/xmlmapcollection/#add-string-) que vous pouvez utiliser pour importer votre carte XML à l'intérieur du classeur.  

## **Ajouter une carte XML à l'intérieur du classeur en utilisant la méthode Add de XmlMapCollection**  

Le code d'exemple suivant ajoute une carte XML à l'intérieur du classeur à l'aide de la méthode [**XmlMapCollection.add(string)**](https://reference.aspose.com/cells/nodejs-cpp/xmlmapcollection/#add-string-) et l'enregistre en tant que [fichier Excel de sortie](5115434.xlsx). La capture d'écran montre la carte XML qui a été importée depuis le [sample.xml](5115433.xml) à l'intérieur du fichier Excel de sortie.  

![add-xml-map](add-xml-map.png)  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const wb = new AsposeCells.Workbook();

// Add xml map found inside the sample.xml inside the workbook
wb.getWorksheets().getXmlMaps().add(path.join(dataDir, "sample.xml"));

// Save the workbook in xlsx format
wb.save(path.join(dataDir, "output_out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
