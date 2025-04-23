---
title: Encontrar si la hoja de cálculo es una hoja de diálogo con Node.js a través de C++
linktitle: Encontrar si la hoja de cálculo es una hoja de diálogo
type: docs
weight: 90
url: /es/nodejs-cpp/find-if-the-worksheet-is-dialog-sheet/
description: Este artículo proporciona instrucciones y código de ejemplo para determinar programáticamente si una hoja de cálculo de Excel es una hoja de diálogo usando Aspose.Cells for Node.js via C++.
keywords: Encontrar tipo de diálogo de hoja de cálculo de Excel en Node.js a través de C++, hoja de diálogo en Node.js a través de C++
---

## **Escenarios de uso posibles**

La hoja de diálogo es un formato antiguo de hoja que contiene un cuadro de diálogo. Esa hoja podría haber sido insertada por una versión antigua de Microsoft Excel, por ejemplo, 2003, como se muestra en esta captura de pantalla. También puede ser insertada con VBA en versiones más recientes, por ejemplo, Microsoft Excel 2016.

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

Puedes determinar si la hoja es una hoja de diálogo u otro tipo de hoja con la propiedad [**Worksheet.getType()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getType--) proporcionada por Aspose.Cells for Node.js via C++. Si devuelve el valor de enumeración [**SheetType.Dialog**](https://reference.aspose.com/cells/nodejs-cpp/sheettype), entonces significa que estás tratando con una hoja de diálogo.

## **Buscar si la hoja de trabajo es una hoja de diálogo**

El siguiente código de ejemplo carga el [archivo de Excel de muestra](64716820.xlsx) que contiene una hoja de diálogo. Verifica la propiedad [**Worksheet.getType()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getType--), la compara con [**SheetType.Dialog**](https://reference.aspose.com/cells/nodejs-cpp/sheettype), y luego imprime el mensaje. Consulta la salida en consola del código de ejemplo a continuación para más ayuda.

## **Código de muestra**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleFindIfWorksheetIsDialogSheet.xlsx");

// Load Excel file containing Dialog Sheet
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const ws = workbook.getWorksheets().get(0);

// Find if the sheet type is dialog and print the message
if (ws.getType() === AsposeCells.SheetType.Dialog) {
console.log("Worksheet is a Dialog Sheet.");
}
```

## **Salida de la consola**

{{< highlight js >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
