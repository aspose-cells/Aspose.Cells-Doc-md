---  
title: Agregar mapa XML dentro del libro de trabajo usando XmlMapCollection.Add con Node.js a través de C++  
linktitle: Agregar mapa XML dentro del libro usando el método XmlMapCollection.Add  
type: docs  
weight: 10  
url: /es/nodejs-cpp/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/  
description: Aprende cómo agregar un mapa XML dentro del libro de trabajo usando el método XmlMapCollection.Add con Aspose.Cells for Node.js via C++.  
---  

## **Escenarios de uso posibles**  

Aspose.Cells proporciona el método [**XmlMapCollection.add(string)**](https://reference.aspose.com/cells/nodejs-cpp/xmlmapcollection/#add-string-) que puede usar para importar su mapa XML dentro del libro.  

## **Agregar mapa XML dentro del libro utilizando el método XmlMapCollection.Add**  

El siguiente código de ejemplo agrega un mapa XML dentro del libro utilizando el método [**XmlMapCollection.add(string)**](https://reference.aspose.com/cells/nodejs-cpp/xmlmapcollection/#add-string-) y lo guarda como [archivo de Excel de salida](5115434.xlsx). La captura de pantalla muestra el mapa XML que se ha importado de [sample.xml](5115433.xml) dentro del archivo de Excel de salida.  

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
