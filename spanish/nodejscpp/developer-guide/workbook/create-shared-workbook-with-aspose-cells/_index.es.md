---  
title: Crear libro compartido con Aspose.Cells for Node.js via C++  
linktitle: Crear libro compartido con Aspose.Cells  
type: docs  
weight: 40  
url: /es/nodejs-cpp/create-shared-workbook-with-aspose-cells/  
description: Aprende cómo crear un libro compartido usando Aspose.Cells for Node.js via C++.  
---  

## **Escenarios de uso posibles**  

Microsoft Excel permite compartir el libro como se muestra en la siguiente captura de pantalla. Cuando compartes el libro, más de un usuario puede editarlo en la red. Aspose.Cells for Node.js via C++ te permite crear un libro compartido con la propiedad [**WorkbookSettings.getShared()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShared--).  

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_1.png)  

## **Crear libro compartido con Aspose.Cells**  

El siguiente código de ejemplo crea un libro compartido estableciendo la propiedad [**WorkbookSettings.getShared()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShared--) como **true**. Cuando abras el [archivo de Excel de salida](55541786.xlsx) en Microsoft Excel, verás **Compartido** junto al nombre del libro de salida como se muestra en esta captura de pantalla.  

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_2.png)  

## **Código de muestra**  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create Workbook object
const wb = new AsposeCells.Workbook();

// Share the Workbook
wb.getSettings().setShared(true);

// Save the Shared Workbook
wb.save("outputSharedWorkbook.xlsx");
```  

