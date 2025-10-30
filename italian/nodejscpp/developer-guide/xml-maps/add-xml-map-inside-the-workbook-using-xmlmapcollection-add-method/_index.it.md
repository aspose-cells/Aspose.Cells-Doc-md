---  
title: Aggiungi mappa XML all’interno del workbook usando il metodo XmlMapCollection.Add con Node.js tramite C++  
linktitle: Aggiungi mappa XML all interno del foglio di lavoro utilizzando il metodo XmlMapCollection.Add  
type: docs  
weight: 10  
url: /it/nodejs-cpp/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/  
description: Impara come aggiungere una mappa XML all’interno del workbook usando il metodo XmlMapCollection.Add con Aspose.Cells for Node.js via C++.  
---  

## **Possibili Scenari di Utilizzo**  

Aspose.Cells fornisce il metodo [**XmlMapCollection.add(string)**](https://reference.aspose.com/cells/nodejs-cpp/xmlmapcollection/#add-string-) che puoi utilizzare per importare la tua mappa XML all'interno del workbook.  

## **Aggiungi mappa XML all'interno del foglio di lavoro utilizzando il metodo XmlMapCollection.Add**  

Il seguente codice di esempio aggiunge una mappa XML all'interno del workbook utilizzando il metodo [**XmlMapCollection.add(string)**](https://reference.aspose.com/cells/nodejs-cpp/xmlmapcollection/#add-string-) e lo salva come [file Excel di output](5115434.xlsx). La schermata mostra la mappa XML che è stata importata dal file [sample.xml](5115433.xml) all'interno del file Excel di output.  

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
