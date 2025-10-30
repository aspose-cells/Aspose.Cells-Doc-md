---
title: Leer archivo CSV con múltiples codificaciones usando Node.js a través de C++
linktitle: Lectura de archivo CSV con múltiples codificaciones
type: docs
weight: 200
url: /es/nodejs-cpp/reading-csv-file-with-multiple-encodings/
description: Aprende cómo leer archivos CSV con múltiples codificaciones usando Aspose.Cells for Node.js via C++.
---


{{% alert color="primary" %}}

A veces, tu archivo CSV contiene múltiples codificaciones (Unicode, ANSI, UTF8, UTF7, etc). Aspose.Cells te permite cargar dichos archivos CSV y convertirlos a otros formatos, por ejemplo, PDF o XLSX.

{{% /alert %}}

Aspose.Cells proporciona la propiedad [**TxtLoadOptions.isMultiEncoded()**](https://reference.aspose.com/cells/nodejs-cpp/txtloadoptions/#isMultiEncoded--), que debe configurarse en **true** para cargar correctamente su archivo CSV con múltiples codificaciones.

La siguiente captura de pantalla muestra un archivo CSV de muestra que contiene dos líneas. La primera línea está en codificación **ANSI** y la segunda línea está en codificación **Unicode**.

|**Archivo de entrada**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)|

 La siguiente captura de pantalla muestra el archivo XLSX convertido desde el CSV anterior sin configurar la propiedad [**TxtLoadOptions.isMultiEncoded()**](https://reference.aspose.com/cells/nodejs-cpp/txtloadoptions/#isMultiEncoded--) en **true**. Como puede ver, el texto Unicode no se convirtió correctamente.

|**Archivo de salida 1: no se hizo ningún ajuste para la codificación múltiple**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)|

La siguiente captura de pantalla muestra el archivo XSLX convertido del CSV anterior después de configurar la propiedad [**TxtLoadOptions.isMultiEncoded()**](https://reference.aspose.com/cells/nodejs-cpp/txtloadoptions/#isMultiEncoded--) en **true**. Como puedes ver, el texto Unicode ahora se convierte correctamente.

|**Archivo de salida 2: IsMultiEncoded se establece en true**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)|

A continuación se muestra el código de ejemplo que convierte el archivo CSV anterior en formato XLSX adecuadamente.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "MultiEncoded.csv");

// Set Multi Encoded Property to True
const options = new AsposeCells.TxtLoadOptions();
options.setIsMultiEncoded(true);

// Load the CSV file into Workbook
const workbook = new AsposeCells.Workbook(filePath, options);

// Save it in XLSX format
workbook.save(path.join(dataDir, "MultiEncoded.csv.out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```

## Artículos relacionados

- [Abriendo Archivos CSV](/cells/es/nodejs-cpp/opening-files-with-different-formats/#opening-csv-files)
{{< app/cells/assistant language="nodejs-cpp" >}}
