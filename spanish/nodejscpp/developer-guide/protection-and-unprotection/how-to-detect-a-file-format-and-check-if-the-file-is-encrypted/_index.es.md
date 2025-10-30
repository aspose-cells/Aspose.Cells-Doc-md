---  
title: Cómo detectar un formato de archivo y verificar si el archivo está cifrado con Node.js a través de C++  
linktitle: Cómo Detectar el Formato de un Archivo y Verificar si el Archivo está Encriptado  
type: docs  
weight: 2700  
url: /es/nodejs-cpp/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/  
description: Aprende cómo detectar un formato de archivo y verificar si un archivo está cifrado usando Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
A veces necesitas detectar el formato de un archivo antes de abrirlo porque la extensión del archivo no garantiza que el contenido sea apropiado. El archivo podría estar cifrado (archivo protegido con contraseña), por lo que no se puede leer directamente, o no deberíamos leerlo. Aspose.Cells for Node.js via C++ proporciona el método estático [**FileFormatUtil.detectFileFormat(Uint8Array)**](https://reference.aspose.com/cells/nodejs-cpp/fileformatutil/#detectFileFormat-uint8array-) y algunas API relevantes que puedes usar para procesar documentos.  
{{% /alert %}}  

El siguiente código de ejemplo ilustra cómo detectar el formato de un archivo (usando la ruta del archivo) y verificar su extensión. También puedes determinar si el archivo está encriptado.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Detect file format
const info = AsposeCells.FileFormatUtil.detectFileFormat(new Uint8Array(require("fs").readFileSync(filePath)));

// Gets the detected load format
console.log("The spreadsheet format is: " + AsposeCells.FileFormatUtil.loadFormatToExtension(info.getLoadFormat()));

// Check if the file is encrypted.
console.log("The file is encrypted: " + info.isEncrypted());
```  
{{< app/cells/assistant language="nodejs-cpp" >}}
