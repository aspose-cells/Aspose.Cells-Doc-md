---
title: Cómo controlar la vista del libro de trabajo con Node.js a través de C++
linktitle: Cómo Controlar la Vista del Libro de Trabajo
type: docs
weight: 600
url: /es/nodejs-cpp/how-to-control-workbook-view/
description: Aprende cómo controlar la vista del libro de trabajo a través de la API Aspose.Cells for Node.js via C++.
keywords: Cómo controlar la vista del libro de trabajo en Node.js vía C++, establecer la vista de Excel en Node.js vía C++, operando la vista del libro de trabajo en Node.js vía C++, establecer la vista del libro de trabajo en Node.js vía C++, controlar la vista de Excel en Node.js vía C++.
---

## **Escenarios de uso posibles**
Cuando necesitas ajustar la visualización de las páginas de Excel, debes saber cómo controlar cada módulo, como barras de desplazamiento horizontales y verticales, si ocultar los archivos de Excel abiertos, etc. Aspose.Cells for Node.js via C++ ofrece esta función. Aspose.Cells for Node.js via C++ proporciona las siguientes propiedades y métodos para ayudarte a lograr tus metas.

- [**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isHScrollBarVisible--)
- [**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isVScrollBarVisible--)
- [**WorkbookSettings.isHidden()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isHidden--)
- [**WorkbookSettings.isMinimized()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isMinimized--)
- [**WorkbookSettings.getWindowHeight()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getWindowHeight--)
- [**WorkbookSettings.getWindowWidth()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getWindowWidth--)
- [**WorkbookSettings.getWindowLeft()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getWindowLeft--)
- [**WorkbookSettings.getWindowTop()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getWindowTop--)

## **Cómo controlar la vista del libro de trabajo usando Aspose.Cells for Node.js via C++**
Este ejemplo muestra cómo:

1. Crear un libro de trabajo.
1. Agregar datos a las celdas en la primera hoja de cálculo.
1. Ocultar las barras de desplazamiento horizontal y vertical de la Vista del Libro de Trabajo.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Instantiating an Workbook object
const workbook = new AsposeCells.Workbook();
// Obtaining the reference of the newly added worksheet
const ws = workbook.getWorksheets().get(0);
const cells = ws.getCells();

// Setting the value to the cells
let cell = cells.get("A1");
cell.putValue("Fruit");
cell = cells.get("B1");
cell.putValue("Count");
cell = cells.get("C1");
cell.putValue("Price");

cell = cells.get("A2");
cell.putValue("Apple");
cell = cells.get("A3");
cell.putValue("Mango");
cell = cells.get("A4");
cell.putValue("Blackberry");
cell = cells.get("A5");
cell.putValue("Cherry");

cell = cells.get("B2");
cell.putValue(5);
cell = cells.get("B3");
cell.putValue(3);
cell = cells.get("B4");
cell.putValue(6);
cell = cells.get("B5");
cell.putValue(4);

cell = cells.get("C2");
cell.putValue(5);
cell = cells.get("C3");
cell.putValue(20);
cell = cells.get("C4");
cell.putValue(30);
cell = cells.get("C5");
cell.putValue(60);

cell = cells.get("E10");
const temp = workbook.createStyle();
temp.getFont().setColor(AsposeCells.Color.Red);
cell.setStyle(temp);

// Hide horizontal and vertical scrollbars
workbook.getSettings().setIsHScrollBarVisible(false);
workbook.getSettings().setIsVScrollBarVisible(false);

workbook.save("out.xlsx");
```

Vista previa del archivo resultante:
<br>
<image src="result.png" width="70%" />

