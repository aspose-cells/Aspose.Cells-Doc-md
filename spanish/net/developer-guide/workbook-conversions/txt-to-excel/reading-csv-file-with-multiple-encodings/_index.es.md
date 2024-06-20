---
title: Lectura de archivo CSV con múltiples codificaciones
type: docs
weight: 200
url: /es/net/reading-csv-file-with-multiple-encodings/
---

{{% alert color="primary" %}}

A veces, tu archivo CSV contiene múltiples codificaciones (Unicode, ANSI, UTF8, UTF7, etc). Aspose.Cells te permite cargar estos archivos CSV y convertirlos a otros formatos, por ejemplo, PDF o XLSX.

{{% /alert %}}

Aspose.Cells proporciona la propiedad [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/ismultiencoded), la cual necesitas configurar como **true** para cargar adecuadamente tu archivo CSV con múltiples codificaciones.

La siguiente captura de pantalla muestra un archivo CSV de muestra que contiene dos líneas. La primera línea está en codificación **ANSI** y la segunda línea está en codificación **Unicode**.

|**Archivo de entrada**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)|

La siguiente captura de pantalla muestra el archivo XLSX convertido del archivo CSV anterior sin configurar la propiedad [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/ismultiencoded) como **true**. Como puedes ver, el texto Unicode no se convirtió correctamente.

|**Archivo de salida 1: no se hizo ningún ajuste para la codificación múltiple**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)|

La siguiente captura de pantalla muestra el archivo XSLX convertido del archivo CSV después de configurar la propiedad [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/ismultiencoded) como **true**. Como puedes ver, el texto Unicode ahora se convierte correctamente.

|**Archivo de salida 2: IsMultiEncoded se establece en true**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)|

A continuación se muestra el código de ejemplo que convierte el archivo CSV anterior en formato XLSX adecuadamente.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ReadingCSVMultipleEncodings-1.cs" >}}

## Artículos relacionados

- [Abriendo Archivos CSV](/cells/es/net/opening-files-with-different-formats/#opening-csv-files)
