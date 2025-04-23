---  
title: Especificar dígitos significativos que se almacenarán en archivo de Excel con Node.js vía C++  
linktitle: Especificación de Dígitos Significativos a ser Almacenados en un Archivo de Excel  
type: docs  
weight: 30  
url: /es/nodejs-cpp/specifying-significant-digits-to-be-stored-in-excel-file/  
description: Aprende cómo especificar dígitos significativos que se almacenarán en un archivo de Excel usando Aspose.Cells for Node.js via C++.  
---  

## **Escenarios de uso posibles**  

Por defecto, Aspose.Cells for Node.js via C++ almacena 17 dígitos significativos de valores doble dentro del archivo de Excel, a diferencia de MS-Excel que solo almacena 15 dígitos significativos. Puedes cambiar el comportamiento predeterminado de Aspose.Cells de 17 a 15 dígitos significativos usando la propiedad [**CellsHelper.getSignificantDigits()**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#getSignificantDigits--).  

## **Especificación de Dígitos Significativos a ser almacenados en un archivo de Excel**  

El siguiente código de ejemplo fuerza a Aspose.Cells a usar 15 dígitos significativos al almacenar valores doble dentro del archivo de Excel. Por favor, revisa el [archivo Excel de salida](22774105.xlsx). Cambia su extensión a .zip y descomprímelo, verás que solo se almacenan 15 dígitos significativos en el archivo de Excel. La siguiente captura de pantalla explica el efecto de la propiedad [**CellsHelper.getSignificantDigits()**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#getSignificantDigits--) en el archivo Excel de salida.  

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)  

## **Código de muestra**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// By default, Aspose.Cells stores 17 significant digits unlike
// MS-Excel which stores only 15 significant digits
AsposeCells.CellsHelper.setSignificantDigits(15);

// Create workbook
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access cell A1
const c = worksheet.getCells().get("A1");

// Put double value, only 15 significant digits as specified by
// CellsHelper.SignificantDigits above will be stored in excel file just like MS-Excel does
c.putValue(1234567890.123451711);

// Save the workbook
workbook.save(path.join(dataDir, "out_SignificantDigits.xlsx"));
```  

