---
title: Encriptar y desencriptar archivos ODS con Node.js a través de C++
linktitle: Cifrar y Descifrar archivos ODS
type: docs
weight: 10
url: /es/nodejs-cpp/encrypt-and-decrypt-ods-files/
description: Proteger con contraseña y cifrar archivos ODS usando Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}
OpenOffice.org es un paquete de oficina completo que soporta proteger y cifrar archivos con contraseña. Sin embargo, un archivo ODS encriptado solo puede abrirse en OpenOffice tras proporcionar la contraseña. Excel no puede abrir el archivo ODS encriptado y puede mostrar mensajes de advertencia. Las opciones de cifrado no son aplicables a archivos ODS, a diferencia de otros tipos de archivos. 
Aspose.Cells permite encriptar y desencriptar archivos ODS. Los archivos ODS desencriptados pueden abrirse tanto en Excel como en OpenOffice.
{{% /alert %}}

## **Cifrar con OpenOffice Calc**
1. Selecciona **Guardar como** y haz clic en la casilla **Guardar con contraseña**.
1. Haz clic en el botón **Guardar**.
1. Escribe tu contraseña deseada en los campos **Introducir Contraseña para Abrir** y **Confirmar Contraseña** en la ventana Establecer Contraseña que se abre. 
1. Haz clic en el botón **Aceptar** para guardar el archivo.

## **Cifra archivo ODS con Aspose.Cells for Node.js via C++**
Para cifrar un archivo ODS, carga el archivo y establece el valor [**WorkbookSettings.getPassword()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getPassword--) con la contraseña actual antes de guardarlo. El archivo ODS cifrado resultante solo puede abrirse en OpenOffice.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "source");
const outputDir = path.join(__dirname, "output");

// Open an ODS file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleODSFile.ods"));

// Password protect the file
workbook.getSettings().setPassword("1234");

// Save the ODS file
workbook.save(path.join(outputDir, "outputEncryptedODSFile.ods"));
```

## **Descifrar archivo ODS con Aspose.Cells for Node.js via C++**
Para descifrar un archivo ODS, carga el archivo proporcionando una contraseña en [**LoadOptions.getPassword()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getPassword--). Una vez cargado, establece la cadena [**WorkbookSettings.getPassword()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getPassword--) en null.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Open an encrypted ODS file
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Ods);

// Set original password
loadOptions.setPassword("1234");

// Load the encrypted ODS file with the appropriate load options
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleEncryptedODSFile.ods"), loadOptions);

// Set the password to null
workbook.getSettings().setPassword(null);

// Save the decrypted ODS file
workbook.save(outputDir + "outputDecryptedODSFile.ods");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
