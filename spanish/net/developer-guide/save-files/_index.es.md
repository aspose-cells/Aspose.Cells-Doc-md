---
title: Diferentes formas de guardar archivos
linktitle: Guardar archivos
type: docs
weight: 40
url: /es/net/different-ways-to-save-files/
description: Aspose.Cells for .NET puede guardar archivos en diferentes formatos. Guarde archivos en PDF. Guarde archivos en HTML. Guarde archivos en DOCX. Guarde archivos en PPTX. Guarde archivos en JSON. Guarde archivos en MHTML.
keywords: Aspose.Cells Save Excel to PDF, HTML, JSON, CSV, TXT, XML, DOCX, PPTX, MHT, MHTML and so on using C#, Save or Convert Workbook to PDF HTML JSON TXT SQL in C#.
---
{{% alert color="primary" %}}

Aspose.Cells permite crear y guardar archivos. Este artículo explica las diversas formas en que se pueden guardar archivos.

{{% /alert %}}

##  **Diferentes formas de guardar archivos**

 Aspose.Cells proporciona la**[Libro de trabajo](https://reference.aspose.com/cells/net/aspose.cells/workbook)** que representa un archivo de Excel Microsoft y proporciona las propiedades y métodos necesarios para trabajar con archivos de Excel. El**[Libro de trabajo](https://reference.aspose.com/cells/net/aspose.cells/workbook)** clase proporciona la**[Guardar](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)** Método utilizado para guardar archivos de Excel. El**[Guardar](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**El método tiene muchas sobrecargas que se utilizan para guardar archivos de diferentes maneras.

 El formato de archivo en el que se guarda el archivo lo decide el**[Guardar formato](https://reference.aspose.com/cells/net/aspose.cells/saveformat)**enumeración

|**Tipos de formato de archivo**|**Descripción**|
| :- | :- |
|CSV|Representa un archivo CSV|
|Excel97To2003|Representa un archivo Excel 97 - 2003.|
|xlsx|Representa un archivo Excel 2007 XLSX|
|xlsm|Representa un archivo Excel 2007 XLSM|
|xltx|Representa un archivo de plantilla XLTX de Excel 2007.|
|xltm|Representa un archivo XLTM habilitado para macros de Excel 2007|
|xlsb|Representa un archivo binario XLSB de Excel 2007.|
|SpreadsheetML|Representa un archivo XML de hoja de cálculo|
|TSV|Representa un archivo de valores separados por tabulaciones.|
|TabDelimited|Representa un archivo de texto delimitado por tabulaciones.|
|ODS|Representa un archivo ODS|
|HTML|Representa HTML archivo(s)|
|MHtml|Representa un archivo(s) MHTML|
|Pdf|Representa un archivo PDF|
|XPS|Representa un documento XPS|
|TIFF|Representa el formato de archivo de imagen etiquetado (TIFF)|

##  **Cómo guardar archivos en diferentes formatos**

Para guardar archivos en una ubicación de almacenamiento, especifique el nombre del archivo (completo con la ruta de almacenamiento) y el formato de archivo deseado (de la**[Guardar formato](https://reference.aspose.com/cells/net/aspose.cells/saveformat)** enumeración) al llamar al**[Libro de trabajo](https://reference.aspose.com/cells/net/aspose.cells/workbook)** objetos**[Guardar](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**método.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoSomeLocation-1.cs" >}}

##  **Cómo guardar un libro de trabajo en PDF**
El formato de documento portátil (PDF) es un tipo de documento creado por Adobe en la década de 1990. El propósito de este formato de archivo era introducir un estándar para la representación de documentos y otro material de referencia en un formato que sea independiente del software, hardware y sistema operativo de la aplicación. El formato de archivo PDF tiene capacidad total para contener información como texto, imágenes, hipervínculos, campos de formulario, medios enriquecidos, firmas digitales, archivos adjuntos, metadatos, características geoespaciales y objetos 3D que pueden formar parte del documento fuente.

Los siguientes códigos muestran cómo guardar el libro de trabajo como archivo pdf con Aspose.Cells:
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Save-As-Pdf.cs" >}}

##  **Cómo guardar un libro de trabajo en formato texto o CSV**

A veces, desea convertir o guardar un libro con varias hojas de trabajo en formato de texto. Para formatos de texto (por ejemplo, TXT, TabDelim, CSV, etc.), de forma predeterminada, tanto Microsoft Excel como Aspose.Cells guardan el contenido de la hoja de trabajo activa únicamente.

El siguiente ejemplo de código explica cómo guardar un libro completo en formato de texto. Cargue el libro de origen, que podría ser cualquier archivo de hoja de cálculo de Excel u OpenOffice Microsoft (es decir, XLS, XLSX, XLSM, XLSB, ODS, etc.) con cualquier cantidad de hojas de trabajo.

Cuando se ejecuta el código, convierte los datos de todas las hojas del libro al formato TXT.

 Puede modificar el mismo ejemplo para guardar su archivo en CSV. De forma predeterminada,**[TxtSaveOptions.Separator](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/separator)**es una coma, así que no especifique un separador si guarda en formato CSV.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveWorkbookToTextCSVFormat-1.cs" >}}

##  **Cómo guardar archivos en archivos de texto con un separador personalizado**

Los archivos de texto contienen datos de hojas de cálculo sin formato. El archivo es una especie de archivo de texto sin formato que puede tener algunos delimitadores personalizados entre sus datos.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingTextFilewithCustomSeparator-1.cs" >}}

##  **Cómo guardar un archivo en una secuencia**

 Para guardar archivos en una secuencia, cree una*Flujo de memoria* o*flujo de archivos*objeto y guarde el archivo en ese objeto de flujo llamando al**[Libro de trabajo](https://reference.aspose.com/cells/net/aspose.cells/workbook)** objetos**[Guardar](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)** método. Especifique el formato de archivo deseado usando el**[Guardar formato](https://reference.aspose.com/cells/net/aspose.cells/saveformat)** enumeración al llamar al**[Guardar](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**método.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoStream-1.cs" >}}

##  **Cómo guardar un archivo de Excel en archivos Html y Mht**
Aspose.Cells puede simplemente guardar un archivo de Excel, JSON, CSV u otros archivos que Aspose.Cells podría cargar como archivos .html y .mht.
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-MHTML.cs" >}}
 

##  **Cómo guardar un archivo de Excel en OpenOffice (ODS, SXC, FODS, OTS)**
Podemos guardar los archivos en formato de oficina abierta: ODS, SXC, FODS, OTS, etc.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-ODS.cs" >}}

##  **Cómo guardar un archivo de Excel en JSON o XML**

JSON (Notación de objetos JavaScript) es un formato de archivo estándar abierto para compartir datos que utiliza texto legible por humanos para almacenar y transmitir datos. Los archivos JSON se almacenan con la extensión .json. JSON requiere menos formato y es una buena alternativa para XML. JSON se deriva de JavaScript pero es un formato de datos independiente del idioma. La generación y el análisis de JSON son compatibles con muchos lenguajes de programación modernos. application/json es el tipo de medio utilizado para JSON.

Aspose.Cells admite guardar archivos en JSON o XML.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JSON.cs" >}}


##  **Temas avanzados**
- [Ajustar el nivel de compresión del libro de trabajo](/cells/es/net/adjust-workbook-compression-level/)
- [Guarde el libro de trabajo en un estricto formato de hoja de cálculo XML abierto](/cells/es/net/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [Guardar archivo en objeto de respuesta](/cells/es/net/saving-file-to-response-object/)
