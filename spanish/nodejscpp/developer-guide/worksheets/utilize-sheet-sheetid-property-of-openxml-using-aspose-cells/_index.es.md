---
title: Utiliza la propiedad Sheet.SheetId de OpenXml usando Aspose.Cells for Node.js via C++
linktitle: Utilice la propiedad Sheet.SheetId de OpenXml usando Aspose.Cells
type: docs
weight: 200
url: /es/nodejs-cpp/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/
description: Este artículo demuestra cómo utilizar la propiedad Sheet.SheetId de OpenXml usando manipulación de Excel con Aspose.Cells for Node.js via C++ de manera programática.
keywords: propiedad de la ID de hoja de OpenXml en node.js a través de C++, ID de hoja de cálculo de Excel en node.js mediante C++
---

## **Escenarios de uso posibles**

*Sheet.SheetId* está disponible dentro del módulo *DocumentFormat.OpenXml.Spreadsheet* y forma parte de OpenXml. Puedes ver esta propiedad y su valor dentro de *workbook.xml* como se muestra en la siguiente captura de pantalla. Aspose.Cells proporciona la propiedad equivalente como [**Worksheet.getTabId()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getTabId--).

![todo:image_alt_text](utilize-sheet-sheetid-property-of-openxml-using-aspose-cells_1.png)

## **Utilice la propiedad Sheet.SheetId de OpenXml usando Aspose.Cells for Node.js via C++**

El siguiente código de ejemplo carga el [archivo de Excel de ejemplo](51740716.xlsx), lee su Id de hoja o pestaña, luego le asigna un nuevo Id de pestaña y lo guarda como [archivo de Excel de salida](51740717.xlsx). También consulte la salida de consola del código que se muestra a continuación como referencia.

## **Código de muestra**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleSheetId.xlsx");

// Load source Excel file
const wb = new AsposeCells.Workbook(filePath);

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Print its Sheet or Tab Id on console
console.log("Sheet or Tab Id: " + ws.getTabId());

// Change Sheet or Tab Id
ws.setTabId(358);

// Save the workbook
wb.save("outputSheetId.xlsx");
```

## **Salida de la consola**

{{< highlight text >}}

Sheet or Tab Id: 1297

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
