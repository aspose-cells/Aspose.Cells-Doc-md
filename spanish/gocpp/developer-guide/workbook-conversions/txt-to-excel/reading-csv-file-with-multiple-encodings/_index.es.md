---
title: Leer archivo CSV con múltiples codificaciones con Golang a través de C++
linktitle: Lectura de archivo CSV con múltiples codificaciones
type: docs
weight: 200
url: /es/go-cpp/reading-csv-file-with-multiple-encodings/
description: Aprenda cómo leer archivos CSV con múltiples codificaciones usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

 A veces, su archivo CSV contiene múltiples codificaciones (Unicode, ANSI, UTF8, UTF7, etc). Aspose.Cells le permite cargar tales archivos CSV y convertirlos a otros formatos, por ejemplo, PDF o XLSX.

{{% /alert %}}

Aspose.Cells proporciona la propiedad [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/go-cpp/txtloadoptions/ismultiencoded/), que debe configurarse en **true** para cargar correctamente su archivo CSV con múltiples codificaciones.

 La siguiente captura de pantalla muestra un archivo CSV de ejemplo que contiene dos líneas. La primera línea está en codificación **ANSI** y la segunda en codificación **Unicode**.

|**Archivo de entrada**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)|

 La siguiente captura de pantalla muestra el archivo XLSX convertido desde el CSV anterior sin configurar la propiedad [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/go-cpp/txtloadoptions/ismultiencoded/) en **true**. Como puede ver, el texto Unicode no se convirtió correctamente.

|**Archivo de salida 1: no se hizo ningún ajuste para la codificación múltiple**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)|

La siguiente captura de pantalla muestra el archivo XLSX convertido desde el archivo CSV anterior después de configurar la propiedad [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/go-cpp/txtloadoptions/ismultiencoded/) en **true**. Como puedes ver, el texto Unicode ahora se convierte correctamente.

|**Archivo de salida 2: IsMultiEncoded se establece en true**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)|

A continuación se muestra el código de ejemplo que convierte el archivo CSV anterior en formato XLSX adecuadamente.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ReadingCsvFileWithMultipleEncodings.go" >}}
## Artículos relacionados

- [Abriendo Archivos CSV](/cells/es/cpp/opening-files-with-different-formats/#opening-csv-files)
