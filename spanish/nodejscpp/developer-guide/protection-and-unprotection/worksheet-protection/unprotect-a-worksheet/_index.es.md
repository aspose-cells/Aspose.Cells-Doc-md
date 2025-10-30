---
title: Desproteger una hoja de cálculo con Node.js vía C++
linktitle: Desproteger una hoja de cálculo
type: docs
weight: 20
url: /es/nodejs-cpp/unprotect-a-worksheet/
---

{{% alert color="primary" %}}

Si un desarrollador necesita quitar la protección de una hoja de cálculo protegida en tiempo de ejecución para poder realizar algunos cambios en el archivo, esto se puede hacer fácilmente con Aspose.Cells.

{{% /alert %}}

## **Desproteger una Hoja de Cálculo**

### **Usar Microsoft Excel**

Para quitar la protección de una hoja de cálculo:

Desde el menú **Herramientas**, seleccione **Protección** y luego **Desproteger hoja**. La protección se eliminará a menos que la hoja esté protegida con contraseña. En ese caso, aparecerá un cuadro de diálogo solicitando la contraseña. Ingrese la contraseña y la hoja quedará desprotegida.

### **Desproteger una hoja de cálculo simplemente protegida utilizando Aspose.Cells**

Una hoja de cálculo puede desprotegerse llamando al método [**unprotect()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#unprotect--) de la clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). Una hoja protegida sin contraseña no tiene protección con contraseña. Estas pueden desprotegerse llamando al método [**unprotect()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#unprotect--) sin pasarle un parámetro.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Unprotecting the worksheet without a password
worksheet.unprotect();

// Saving the Workbook
workbook.save(path.join(dataDir, "output.xls"), AsposeCells.SaveFormat.Excel97To2003);
```

### **Desproteger una hoja de cálculo protegida con contraseña utilizando Aspose.Cells**

Una hoja protectada con contraseña es aquella protegida con una contraseña. Tales hojas se pueden desproteger llamando a una versión sobrecargada del método [**unprotect()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#unprotect--) que recibe la contraseña como parámetro.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Unprotecting the worksheet with a password
worksheet.unprotect("");

// Save Workbook
workbook.save(path.join(dataDir, "output.out.xls"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
