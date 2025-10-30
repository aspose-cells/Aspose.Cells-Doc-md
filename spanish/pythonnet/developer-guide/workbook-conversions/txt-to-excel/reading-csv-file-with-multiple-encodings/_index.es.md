---
title: Lectura de archivo CSV con múltiples codificaciones
type: docs
weight: 200
url: /es/python-net/reading-csv-file-with-multiple-encodings/
description: Lectura de archivos CSV con múltiples codificaciones utilizando Aspose.Cells for Python via .NET API.
keywords: Lectura de archivos CSV con múltiples codificaciones en Python, convertir archivo CSV con múltiples codificaciones a Excel en Python via NET, convertir archivo CSV con múltiples codificaciones a xlsx en Python, Cargar archivo CSV con múltiples codificaciones a archivo de Excel en Python.
---

{{% alert color="primary" %}}

A veces, tu archivo CSV contiene múltiples codificaciones (Unicode, ANSI, UTF8, UTF7, etc). Aspose.Cells te permite cargar estos archivos CSV y convertirlos a otros formatos, por ejemplo, PDF o XLSX.

{{% /alert %}}

Aspose.Cells proporciona la propiedad [**TxtLoadOptions.is_multi_encoded**](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/is_multi_encoded/), la cual necesitas configurar como **true** para cargar adecuadamente tu archivo CSV con múltiples codificaciones.

La siguiente captura de pantalla muestra un archivo CSV de muestra que contiene dos líneas. La primera línea está en codificación **ANSI** y la segunda línea está en codificación **Unicode**.

|**Archivo de entrada**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)|

La siguiente captura de pantalla muestra el archivo XLSX convertido del archivo CSV anterior sin configurar la propiedad [**TxtLoadOptions.is_multi_encoded**](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/is_multi_encoded/) como **true**. Como puedes ver, el texto Unicode no se convirtió correctamente.

|**Archivo de salida 1: no se hizo ningún ajuste para la codificación múltiple**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)|

La siguiente captura de pantalla muestra el archivo XSLX convertido del archivo CSV después de configurar la propiedad [**TxtLoadOptions.is_multi_encoded**](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/is_multi_encoded/) como **true**. Como puedes ver, el texto Unicode ahora se convierte correctamente.

|**Archivo de salida 2: IsMultiEncoded se establece en true**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)|

A continuación se muestra el código de ejemplo que convierte el archivo CSV anterior en formato XLSX adecuadamente.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Txt-ReadingCSVMultipleEncodings-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
