---
title: Formas Diferentes de Guardar Archivos con Golang vía C++
linktitle: Guardar archivos
type: docs
weight: 40
url: /es/go-cpp/different-ways-to-save-files/
description: Aspose.Cells for C++ puede guardar archivos en diferentes formatos. Guardar archivos como PDF. Guardar archivos como HTML. Guardar archivos como DOCX. Guardar archivos como PPTX. Guardar archivos como JSON. Guardar archivos como MHTML.
keywords: Aspose.Cells guarda Excel en PDF, HTML, JSON, CSV, TXT, XML, DOCX, PPTX, MHT, MHTML y otros usando C++, Guardar o Convertir Libro de Trabajo a PDF, HTML, JSON, TXT, SQL en C++.
---

{{% alert color="primary" %}}

Aspose.Cells hace posible crear y guardar archivos. Este artículo explica las varias maneras en las que los archivos pueden ser guardados.

{{% /alert %}}

## **Diferentes formas de guardar archivos**

Aspose.Cells proporciona el [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) que representa un archivo de Microsoft Excel y proporciona las propiedades y métodos necesarios para trabajar con archivos de Excel. La clase [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) proporciona el método [**Save**](https://reference.aspose.com/cells/go-cpp/workbook/save/) utilizado para guardar archivos de Excel. El método [**Save**](https://reference.aspose.com/cells/go-cpp/workbook/save/) tiene muchas sobrecargas que se utilizan para guardar archivos de diferentes formas.

El formato de archivo en el que se guarda el archivo está decidido por la enumeración [**SaveFormat**](https://reference.aspose.com/cells/go-cpp/saveformat/)

|**Tipos de formato de archivo**|**Descripción**|
| :- | :- |
|CSV|Representa un archivo CSV|
|Excel97To2003|Representa un archivo de Excel 97 - 2003|
|Xlsx|Representa un archivo de Excel 2007 XLSX|
|Xlsm|Representa un archivo de Excel 2007 XLSM|
|Xltx|Representa una plantilla de Excel 2007 XLTX|
|Xltm|Representa un archivo habilitado para macros de Excel 2007 XLTM|
|Xlsb|Representa un archivo binario XLSB de Excel 2007|
|SpreadsheetML|Representa un archivo XML de hoja de cálculo|
|TSV|Representa un archivo de valores separados por tabulaciones|
|TabDelimited|Representa un archivo de texto delimitado por tabulaciones|
|ODS|Representa un archivo ODS|
|Html|Representa archivo(s) HTML|
|MHtml|Representa archivo(s) MHTML|
|Pdf|Representa un archivo PDF|
|XPS|Representa un documento XPS|
|TIFF|Representa el Formato de Archivo de Imágenes Etiquetado (TIFF)|

## **Cómo Guardar un Archivo en Diferentes Formatos**

Para guardar archivos en una ubicación de almacenamiento, especifique el nombre del archivo (junto con la ruta de almacenamiento) y el formato de archivo deseado (de la enumeración [**SaveFormat**](https://reference.aspose.com/cells/go-cpp/saveformat/)) al llamar al método [**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) del objeto [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveFiles.go" >}}
## **Cómo guardar un libro en formato PDF**
El formato de documento portátil (PDF) es un tipo de documento creado por Adobe a principios de los años 90. El propósito de este formato de archivo fue introducir un estándar para la representación de documentos y otros materiales de referencia en un formato independiente del software de aplicación, hardware y sistema operativo. El formato de archivo PDF tiene la capacidad completa de contener información como texto, imágenes, hipervínculos, campos de formulario, medios enriquecidos, firmas digitales, archivos adjuntos, metadatos, características geoespaciales y objetos 3D que pueden formar parte del documento fuente.

Los siguientes códigos muestran cómo guardar un libro como archivo PDF con Aspose.Cells:
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveFiles-1.go" >}}
## **Cómo guardar un libro en formato de texto o CSV**

A veces, deseas convertir o guardar un libro con múltiples hojas de cálculo en formato de texto. Para formatos de texto (por ejemplo, TXT, TabDelim, CSV, etc.), tanto Microsoft Excel como Aspose.Cells guardan por defecto el contenido de la hoja de cálculo activa únicamente.

El siguiente ejemplo de código explica cómo guardar un libro de trabajo completo en formato de texto. Cargue el libro de trabajo fuente que podría ser cualquier archivo de hoja de cálculo de Microsoft Excel u OpenOffice (por ejemplo, XLS, XLSX, XLSM, XLSB, ODS, etc.) con cualquier número de hojas de trabajo.

Cuando se ejecuta el código, convierte los datos de todas las hojas del libro de trabajo al formato TXT.

Puede modificar el mismo ejemplo para guardar su archivo en CSV. Por defecto, [**TxtSaveOptions.GetSeparator()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/getseparator/) es la coma, así que no especifique un separador al guardar en formato CSV. Tenga en cuenta: si usa la versión de evaluación y aunque la propiedad [**TxtSaveOptions.GetExportAllSheets()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getexportallsheets/) esté configurada en true, el programa solo exportará una hoja de cálculo.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveFiles-2.go" >}}
## **Cómo guardar archivo en archivos de texto con un separador personalizado**

Los archivos de texto contienen datos de la hoja de cálculo sin formato. El archivo es un tipo de archivo de texto sin formato que puede tener algunos delimitadores personalizados entre sus datos.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveFiles-3.go" >}}
## **Cómo guardar archivo en un flujo de datos**

Para guardar archivos en un flujo de datos, crea un objeto *MemoryStream* o *FileStream* y guarda el archivo en ese objeto de flujo llamando al método [**Save**](https://reference.aspose.com/cells/go-cpp/workbook/save/) del objeto [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/). Especifica el formato de archivo deseado al llamar al método [**Save**](https://reference.aspose.com/cells/go-cpp/workbook/save/) usando la enumeración [**SaveFormat**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveFiles-4.go" >}}
## **Cómo guardar archivo de Excel en archivos HTML y MHT**
Aspose.Cells puede simplemente guardar un archivo de Excel, JSON, CSV u otros archivos que podrían ser cargados por Aspose.Cells como archivos .html y .mht.
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveFiles-5.go" >}} 

## **Cómo guardar archivo de Excel en OpenOffice (ODS, SXC, FODS, OTS)**
Podemos guardar los archivos en formatos de OpenOffice: ODS, SXC, FODS, OTS, etc.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveFiles-6.go" >}}
## **Cómo guardar archivo de Excel en JSON o XML**

JSON (Notación de Objetos de JavaScript) es un formato de archivo estándar abierto para compartir datos que utiliza texto legible para almacenar y transmitir datos. Los archivos JSON se almacenan con la extensión .json. JSON requiere menos formato y es una buena alternativa para XML. JSON se deriva de JavaScript, pero es un formato de datos independiente del lenguaje. La generación y análisis de JSON son compatibles con muchos lenguajes de programación modernos. application/json es el tipo de medio utilizado para JSON.

Aspose.Cells es compatible con la posibilidad de guardar archivos en JSON o XML.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveFiles-7.go" >}}

## **Temas avanzados**
- [Ajustar el nivel de compresión del libro de trabajo](/cells/es/cpp/adjust-workbook-compression-level/)
- [Guardar libro de trabajo en formato de hoja de cálculo de Open XML estricto](/cells/es/cpp/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [Guardando archivo en objeto de respuesta](/cells/es/cpp/saving-file-to-response-object/)
