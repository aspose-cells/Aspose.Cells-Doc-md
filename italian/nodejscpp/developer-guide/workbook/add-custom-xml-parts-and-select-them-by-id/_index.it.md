---  
title: Aggiungi parti XML personalizzate e selezionale per ID con Node.js tramite C++  
linktitle: Aggiungi Parti XML personalizzate e selezionale per ID  
type: docs  
weight: 70  
url: /it/nodejs-cpp/add-custom-xml-parts-and-select-them-by-id/  
description: Impara come aggiungere parti XML personalizzate ai documenti Excel e selezionarle per ID usando Aspose.Cells for Node.js via C++.  
---  

## **Possibili Scenari di Utilizzo**  

Le parti XML personalizzate sono i dati XML memorizzati all’interno dei documenti Microsoft Excel e sono utilizzate dalle applicazioni che le gestiscono. Al momento, non esiste un modo diretto per aggiungerle tramite l’interfaccia di Microsoft Excel. Tuttavia, puoi aggiungerle programmaticamente in vari modi, ad esempio usando VSTO, Aspose.Cells, ecc. Usa il metodo [**Workbook.getCustomXmlParts()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getCustomXmlParts--) se vuoi aggiungere una Partitura XML Personalizzata usando l’API di Aspose.Cells. Puoi anche impostarne l’ID usando la proprietà [**CustomXmlPart.getID()**](https://reference.aspose.com/cells/nodejs-cpp/customxmlpart/#getID--). Se invece vuoi selezionare una Partita XML Personalizzata per ID, puoi usare il metodo [**Workbook.getCustomXmlParts()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getCustomXmlParts--).  

## **Aggiungi parti XML personalizzate e selezionale per ID**  

Il seguente esempio di codice aggiunge prima quattro Parti XML Personalizzate usando il metodo [**Workbook.getCustomXmlParts()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getCustomXmlParts--). Poi ne imposta gli ID tramite la proprietà [**CustomXmlPart.getID()**](https://reference.aspose.com/cells/nodejs-cpp/customxmlpart/#getID--). Infine, trova o seleziona una delle Parti XML Personalizzate aggiunte utilizzando il metodo [**Workbook.getCustomXmlParts()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getCustomXmlParts--). Vedi anche l’output console del codice di seguito come riferimento.  

## **Codice di Esempio**  

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

## **Output della console**  

{{< highlight java >}}  
 Found: CustomXmlPart ID Sport  
{{< /highlight >}}  

