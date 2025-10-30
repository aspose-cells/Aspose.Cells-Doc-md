---
title: Configuraciones avanzadas de protección desde Excel XP con Node.js vía C++
linktitle: Configuraciones de protección avanzada desde Excel XP
type: docs
weight: 30
url: /es/nodejs-cpp/advanced-protection-settings-since-excel-xp/
---


{{% alert color="primary" %}}

Desde el lanzamiento de Excel 2002 o XP, Microsoft ha añadido muchas configuraciones avanzadas de protección.

{{% /alert %}}


## **Introducción**

Estas configuraciones de protección restringen o permiten a los usuarios:

- Eliminar filas o columnas.
- Editar contenidos, objetos o escenarios.
- Formatear celdas, filas o columnas.
- Insertar filas, columnas o hipervínculos.
- Seleccionar celdas bloqueadas o desbloqueadas.
- Utilizar tablas dinámicas y mucho más.

Aspose.Cells for Node.js via C++ soporta todas las configuraciones avanzadas de protección ofrecidas por Excel XP o versiones posteriores.

### **Configuraciones de protección avanzada utilizando Excel XP y versiones posteriores**

Para ver las configuraciones de protección disponibles en Excel XP:

1. Desde el menú **Herramientas**, selecciona **Protección** seguido de **Proteger hoja**. Se mostrará un cuadro de diálogo.

Para ver la configuración de protección disponible en Excel 2016:

1. Desde el menú **Archivo**, selecciona **Proteger libro** seguido de **Proteger hoja actual**.
1. Selecciona **Proteger hoja** en el menú **Revisar**.

Los pasos mencionados anteriormente mostrarán un cuadro de diálogo donde puede permitir o restringir funciones de la hoja de trabajo o aplicar una contraseña a la hoja.

### **Configuraciones avanzadas de protección usando Aspose.Cells for Node.js via C++**

Aspose.Cells for Node.js via C++ soporta todas las configuraciones avanzadas de protección.

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contiene una colección [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) que permite acceder a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet).

La clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) proporciona la propiedad [**getProtection()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getProtection--) que se utiliza para aplicar estas configuraciones de protección avanzada. La propiedad [**getProtection()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getProtection--) es de hecho un objeto de la clase [**Protection**](https://reference.aspose.com/cells/nodejs-cpp/protection) que encapsula varias propiedades booleanas para deshabilitar o habilitar restricciones.

A continuación se muestra un pequeño ejemplo de aplicación. Abre un archivo de Excel y utiliza la mayoría de los ajustes de protección avanzados admitidos por Excel XP y versiones posteriores.

```javascript
try {
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fstream = fs.createReadStream(filePath);

// Reading the file stream into a buffer
const fileBuffer = [];
fstream.on('data', chunk => fileBuffer.push(chunk));
fstream.on('end', () => {
const workbook = new AsposeCells.Workbook(Buffer.concat(fileBuffer));

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Restricting users to delete columns of the worksheet
worksheet.getProtection().setAllowDeletingColumn(false);

// Restricting users to delete row of the worksheet
worksheet.getProtection().setAllowDeletingRow(false);

// Restricting users to edit contents of the worksheet
worksheet.getProtection().setAllowEditingContent(false);

// Restricting users to edit objects of the worksheet
worksheet.getProtection().setAllowEditingObject(false);

// Restricting users to edit scenarios of the worksheet
worksheet.getProtection().setAllowEditingScenario(false);

// Restricting users to filter
worksheet.getProtection().setAllowFiltering(false);

// Allowing users to format cells of the worksheet
worksheet.getProtection().setAllowFormattingCell(true);

// Allowing users to format rows of the worksheet
worksheet.getProtection().setAllowFormattingRow(true);

// Allowing users to insert columns in the worksheet
worksheet.getProtection().setAllowFormattingColumn(true);

// Allowing users to insert hyperlinks in the worksheet
worksheet.getProtection().setAllowInsertingHyperlink(true);

// Allowing users to insert rows in the worksheet
worksheet.getProtection().setAllowInsertingRow(true);

// Allowing users to select locked cells of the worksheet
worksheet.getProtection().setAllowSelectingLockedCell(true);

// Allowing users to select unlocked cells of the worksheet
worksheet.getProtection().setAllowSelectingUnlockedCell(true);

// Allowing users to sort
worksheet.getProtection().setAllowSorting(true);

// Allowing users to use pivot tables in the worksheet
worksheet.getProtection().setAllowUsingPivotTable(true);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"), AsposeCells.SaveFormat.Excel97To2003);

// Closing the file stream to free all resources
fstream.close();
```

{{% alert color="primary" %}}

Por favor, no llame al método [**protect(ProtectionType)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#protect-protectiontype-) de la clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) al usar la propiedad [**getProtection()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getProtection--). Además, guarda el archivo en formato Excel97To2003 o Xlsx porque las configuraciones avanzadas de protección solo son compatibles con Excel XP y versiones posteriores.

{{% /alert %}}

### **Problema de bloqueo de celdas**

Si desea restringir a los usuarios de editar celdas, las celdas deben estar bloqueadas antes de aplicar cualquier configuración de protección. De lo contrario, las celdas pueden editarse incluso si la hoja de cálculo está protegida. En Microsoft Excel XP, las celdas se pueden bloquear a través del siguiente cuadro de diálogo:

|**Cuadro de diálogo para bloquear celdas en Excel XP**|
| :- |
|![todo:image_alt_text](advanced-protection-settings-since-excel-xp_1.png)|

También es posible bloquear celdas usando la API Aspose.Cells. Cada celda puede obtener un formato [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) que contiene una propiedad Booleana, [**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--). Establezca la propiedad [**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--) en **true** o **false** para bloquear o desbloquear la celda.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().get("A1").getStyle().setIsLocked(true);
// Finally, Protect the sheet now.
worksheet.protect(AsposeCells.ProtectionType.All);
workbook.save(path.join(dataDir, "output.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
