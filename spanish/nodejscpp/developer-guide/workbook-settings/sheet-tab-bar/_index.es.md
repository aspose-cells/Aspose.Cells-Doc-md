---  
title: Cómo controlar la barra de pestañas de hojas con Node.js a través de C++  
linktitle: Cómo Controlar la Barra de Pestañas de la Hoja  
type: docs  
weight: 600  
url: /es/nodejs-cpp/how-to-control-sheet-tab-bar/  
description: Aprende cómo controlar la barra de pestañas de hojas usando Aspose.Cells for Node.js via C++.  
keywords: Cómo controlar la barra de pestañas de hojas en Node.js vía C++, Operar la barra de pestañas de hojas en Node.js vía C++, Establecer la barra de pestañas de hojas en Node.js vía C++, Controlar la barra de pestañas de hojas en Node.js vía C++.  
---  

## **Escenarios de uso posibles**  
Cuando necesitas ajustar la visualización de la barra de hojas de Excel, debes saber cómo controlar la pestaña de la hoja, como ocultar o mostrar la barra de pestañas, cambiar el ancho de la barra de pestañas, especificar la primera pestaña visible, etc. Aspose.Cells for Node.js via C++ soporta estas funciones. Aspose.Cells proporciona las siguientes propiedades y métodos para ayudarte a lograr tus objetivos.

- [**WorkbookSettings.getShowTabs()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShowTabs--)
- [**WorkbookSettings.getSheetTabBarWidth()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getSheetTabBarWidth--)
- [**WorkbookSettings.getFirstVisibleTab()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getFirstVisibleTab--)

## **Cómo controlar la barra de pestañas de hojas usando Aspose.Cells for Node.js via C++**  
Este ejemplo muestra cómo:

1. Crear un libro de trabajo.
1. Agregar datos a las celdas en la primera hoja de cálculo.
1. Mostrar la pestaña de la hoja y configurar el ancho de la barra de pestañas.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
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

// Display the sheet tab and set the width of the tab bar
workbook.getSettings().setShowTabs(true);
workbook.getSettings().setSheetTabBarWidth(150);

workbook.save("out.xlsx");
```

Vista previa del archivo resultante:  
<br>  
<image src="result.png" width="70%" />  


{{< app/cells/assistant language="nodejs-cpp" >}}
