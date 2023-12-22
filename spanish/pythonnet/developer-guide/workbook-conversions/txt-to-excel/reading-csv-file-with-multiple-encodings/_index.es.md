---
title: Lectura de archivo CSV con múltiples codificaciones
type: docs
weight: 200
url: /es/python-net/reading-csv-file-with-multiple-encodings/
description: Lectura del archivo CSV con múltiples codificaciones utilizando Aspose.Cells for Python via .NET API.
keywords: Python Reading CSV File with Multiple Encodings, Convert CSV File with Multiple Encodings to Excel in Python via NET, Python convert CSV File with Multiple Encodings to xlsx, Load CSV File with Multiple Encodings to Excel file.
---
{{% alert color="primary" %}}

A veces, su archivo CSV contiene múltiples codificaciones (Unicode, ANSI, UTF8, UTF7, etc.). Aspose.Cells le permite cargar dichos archivos CSV y convertirlos a otros formatos, por ejemplo, PDF o XLSX.

{{% /alert %}}

 Aspose.Cells proporciona la[**TxtLoadOptions.is_multi_encoded**](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/is_multi_encoded/) propiedad, que debe establecer en**verdadero** para cargar correctamente su archivo CSV con múltiples codificaciones.

 La siguiente captura de pantalla muestra un archivo CSV de muestra que contiene dos líneas. La primera línea está en**ANSI** codificación y la segunda línea está en**Unicódigo** codificación

|**Fichero de entrada**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)|

La siguiente captura de pantalla muestra el archivo XLSX convertido del archivo CSV anterior sin configurar el[**TxtLoadOptions.is_multi_encoded**](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/is_multi_encoded/)propiedad a *verdadero**. Como puede ver, el texto Unicode no se convirtió correctamente.

|**Archivo de salida 1: no se han realizado adaptaciones para codificación múltiple**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)|

 La siguiente captura de pantalla muestra el archivo XSLX convertido del archivo CSV anterior después de configurar el[**TxtLoadOptions.is_multi_encoded**](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/is_multi_encoded/)propiedad a *verdadero**. Como puede ver, el texto Unicode ahora se convierte correctamente.

|**Archivo de salida 2: IsMultiEncoded está establecido en verdadero**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)|

A continuación se muestra el código de muestra que convierte correctamente el archivo CSV anterior al formato XLSX.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Txt-ReadingCSVMultipleEncodings-1.py" >}}
