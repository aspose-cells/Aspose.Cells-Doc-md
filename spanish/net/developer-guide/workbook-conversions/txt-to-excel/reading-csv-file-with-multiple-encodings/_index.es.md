---
title: Lectura de archivos CSV con múltiples codificaciones
type: docs
weight: 200
url: /es/net/reading-csv-file-with-multiple-encodings/
---
{{% alert color="primary" %}}

A veces, su archivo CSV contiene múltiples codificaciones (Unicode, ANSI, UTF8, UTF7, etc.). Aspose.Cells le permite cargar dichos archivos CSV y convertirlos a otros formatos, por ejemplo, PDF o XLSX.

{{% /alert %}}

 Aspose.Cells proporciona el[**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/ismultiencoded)propiedad, que debe establecer en**verdadero** para cargar correctamente su archivo CSV con múltiples codificaciones.

 La siguiente captura de pantalla muestra un archivo CSV de muestra que contiene dos líneas. La primera línea está en**ANSI** codificación y la segunda línea está en**Unicode** codificación

|**Fichero de entrada**|
|:- |
|![todo:imagen_alternativa_texto](reading-csv-file-with-multiple-encodings_1.png)|

 La siguiente captura de pantalla muestra el archivo XLSX convertido a partir del archivo CSV anterior sin configurar el[**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/ismultiencoded) propiedad a**verdadero**. Como puede ver, el texto Unicode no se convirtió correctamente.

|**Archivo de salida 1: no se realizaron adaptaciones para la codificación múltiple**|
|:- |
|![todo:imagen_alternativa_texto](reading-csv-file-with-multiple-encodings_2.png)|

 La siguiente captura de pantalla muestra el archivo XSLX convertido del archivo CSV anterior después de configurar el[**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/ismultiencoded) propiedad a**verdadero**. Como puede ver, el texto Unicode ahora se convierte correctamente.

|**Archivo de salida 2: IsMultiEncoded se establece en verdadero**|
|:- |
|![todo:imagen_alternativa_texto](reading-csv-file-with-multiple-encodings_3.png)|

A continuación se muestra el código de muestra que convierte correctamente el archivo CSV anterior al formato XLSX.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ReadingCSVMultipleEncodings-1.cs" >}}

## Artículos relacionados

- [Abrir archivos CSV](/cells/es/net/opening-files-with-different-formats/#opening-csv-files)
