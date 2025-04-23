---
title: Propagar fórmula en tabla u objeto de lista automáticamente al ingresar datos en nuevas filas con Node.js mediante C++
linktitle: Establecer fórmula de tabla
type: docs
weight: 260
url: /es/nodejs-cpp/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
description: Aprende a propagar automáticamente las fórmulas en tablas u objetos de lista mientras ingresas datos en nuevas filas usando Aspose.Cells for Node.js via C++.
---

## **Escenarios de uso posibles**
A veces deseas que una fórmula en tu tabla u objeto de lista se propague automáticamente a las nuevas filas mientras ingresas datos. Este es el comportamiento predeterminado de Microsoft Excel. Para lograr la misma funcionalidad con Aspose.Cells for Node.js via C++, usa la propiedad [ListColumn.getFormula()](https://reference.aspose.com/cells/nodejs-cpp/listcolumn/#getFormula--)

## **Propagar fórmula en tabla u objeto de lista automáticamente al ingresar datos en nuevas filas**
El siguiente código de ejemplo crea una Tabla u Objeto de Lista de tal manera que la fórmula en la columna B se propagará automáticamente a filas nuevas cuando ingreses nuevos datos. Por favor, revisa el [archivo Excel de salida](5115469.xlsx) generado con este código. Si ingresas cualquier número en la celda A3, verás que la fórmula en la celda B2 se propagará automáticamente a la celda B3.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const book = new AsposeCells.Workbook();

// Access first worksheet
const sheet = book.getWorksheets().get(0);

// Add column headings in cell A1 and B1
sheet.getCells().get(0, 0).putValue("Column A");
sheet.getCells().get(0, 1).putValue("Column B");

// Add list object, set its name and style
const listObject = sheet.getListObjects().get(sheet.getListObjects().add(0, 0, 1, sheet.getCells().getMaxColumn(), true));
listObject.setTableStyleType(AsposeCells.TableStyleType.TableStyleMedium2);
listObject.setDisplayName("Table");

// Set the formula of second column so that it propagates to new rows automatically while entering data
listObject.getListColumns().get(1).setFormula("=[Column A] + 1");

// Save the workbook in xlsx format
book.save(path.join(dataDir, "output_out.xlsx"));
```
