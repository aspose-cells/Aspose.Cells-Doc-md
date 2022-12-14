---
title: Diferentes formas de guardar archivos
linktitle: Guardar archivos
type: docs
weight: 40
url: /es/net/different-ways-to-save-files/
---
{{% alert color="primary" %}}

Aspose.Cells permite crear y guardar archivos. Este artículo explica las diversas formas en que se pueden guardar los archivos.

{{% /alert %}}

## **Diferentes formas de guardar archivos**

 Aspose.Cells proporciona el**[Libro de trabajo](https://reference.aspose.com/cells/net/aspose.cells/workbook)** que representa un archivo de Excel Microsoft y proporciona las propiedades y los métodos necesarios para trabajar con archivos de Excel. los**[Libro de trabajo](https://reference.aspose.com/cells/net/aspose.cells/workbook)**la clase proporciona la**[Guardar](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)** método utilizado para guardar archivos de Excel. los**[Guardar](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**El método tiene muchas sobrecargas que se utilizan para guardar archivos de diferentes maneras.

 El formato de archivo en el que se guarda el archivo lo decide el**[Guardar formato] (https://reference.aspose.com/cells/net/aspose.cells/saveformat)**enumeración

|**Tipos de formato de archivo**|**Descripción**|
|:- |:- |
|CSV|Representa un archivo CSV|
|Excel97To2003|Representa un archivo Excel 97 - 2003|
|xlsx|Representa un archivo XLSX de Excel 2007|
|xlsm|Representa un archivo XLSM de Excel 2007|
|xltx|Representa un archivo XLTX de plantilla de Excel 2007|
|xltm|Representa un archivo XLTM habilitado para macros de Excel 2007|
|xlsb|Representa un archivo XLSB binario de Excel 2007|
|Hoja de cálculoML|Representa un archivo XML de hoja de cálculo|
|TSV|Representa un archivo de valores separados por tabulaciones|
|Delimitado por tabulaciones|Representa un archivo de texto delimitado por tabulaciones|
|SAO|Representa un archivo ODS|
|html|Representa archivo(s) HTML|
|MHtml|Representa un(os) archivo(s) MHTML|
|pdf|Representa un archivo PDF|
|XPS|Representa un documento XPS|
|PELEA|Representa el formato de archivo de imagen etiquetado (TIFF)|

## **Guardar archivo en diferentes formatos**

 Para guardar archivos en una ubicación de almacenamiento, especifique el nombre del archivo (completo con la ruta de almacenamiento) y el formato de archivo deseado (del**[Guardar formato] (https://reference.aspose.com/cells/net/aspose.cells/saveformat)** enumeración) al llamar al**[Libro de trabajo](https://reference.aspose.com/cells/net/aspose.cells/workbook)** objetos**[Guardar](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**método.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoSomeLocation-1.cs" >}}

## **Guardar libro de trabajo como PDF**
El formato de documento portátil (PDF) es un tipo de documento creado por Adobe en la década de 1990. El propósito de este formato de archivo era introducir un estándar para la representación de documentos y otro material de referencia en un formato que es independiente del software de la aplicación, el hardware y el sistema operativo. El formato de archivo PDF tiene la capacidad completa de contener información como texto, imágenes, hipervínculos, campos de formulario, medios enriquecidos, firmas digitales, archivos adjuntos, metadatos, características geoespaciales y objetos 3D que pueden convertirse en parte del documento de origen.

Los siguientes códigos muestran cómo guardar el libro de trabajo como archivo pdf con Aspose.Cells:
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Save-As-Pdf.cs" >}}

## **Guardar libro de trabajo en formato de texto o CSV**

A veces, desea convertir o guardar un libro de trabajo con varias hojas de trabajo en formato de texto. Para formatos de texto (por ejemplo, TXT, TabDelim, CSV, etc.), por defecto, tanto Microsoft Excel como Aspose.Cells guardan solo el contenido de la hoja de trabajo activa.

El siguiente ejemplo de código explica cómo guardar un libro completo en formato de texto. Cargue el libro de origen, que podría ser cualquier archivo de hoja de cálculo de Excel u OpenOffice Microsoft (es decir, XLS, XLSX, XLSM, XLSB, ODS, etc.) con cualquier número de hojas de trabajo.

Cuando se ejecuta el código, convierte los datos de todas las hojas del libro de trabajo al formato TXT.

 Puede modificar el mismo ejemplo para guardar su archivo en CSV. Por defecto,**[TxtSaveOptions.Separator](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/separator)**es una coma, así que no especifique un separador si guarda en formato CSV.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveWorkbookToTextCSVFormat-1.cs" >}}

## **Guardar archivos de texto con separador personalizado**

Los archivos de texto contienen datos de hojas de cálculo sin formato. El archivo es una especie de archivo de texto sin formato que puede tener algunos delimitadores personalizados entre sus datos.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingTextFilewithCustomSeparator-1.cs" >}}

## **Guardar archivo en una secuencia**

 Para guardar archivos en un flujo, cree un*Flujo de memoria* o*FileStream* objeto y guarde el archivo en ese objeto de flujo llamando al**[Libro de trabajo](https://reference.aspose.com/cells/net/aspose.cells/workbook)** objetos**[Guardar](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)** método. Especifique el formato de archivo deseado usando el**[Guardar formato] (https://reference.aspose.com/cells/net/aspose.cells/saveformat)** enumeración al llamar al**[Guardar](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**método.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoStream-1.cs" >}}

## **Guardar archivos como archivos Html y Mht**
Aspose.Cells puede simplemente guardar un archivo de Excel, JSON, CSV u otros archivos que Aspose.Cells podría cargar como archivos .html y .mht.
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-MHTML.cs" >}}
 

## **Guardar como OpenOffice (ODS, SXC, FODS, OTS)**
Podemos guardar los archivos en formato de oficina abierta: ODS, SXC, FODS, OTS, etc.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-ODS.cs" >}}

## **Guardar archivo de Excel como JSON o XML**

JSON (Notación de objetos de JavaScript) es un formato de archivo estándar abierto para compartir datos que utiliza texto legible por humanos para almacenar y transmitir datos. Los archivos JSON se almacenan con la extensión .json. JSON requiere menos formato y es una buena alternativa para XML. JSON se deriva de JavaScript, pero es un formato de datos independiente del idioma. Muchos lenguajes de programación modernos admiten la generación y el análisis de JSON. application/json es el tipo de medio utilizado para JSON.

Aspose.Cells admite guardar archivos en JSON o XML.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JSON.cs" >}}


## **Temas avanzados**
- [Ajustar el nivel de compresión del libro](/cells/es/net/adjust-workbook-compression-level/)
- [Guardar libro de trabajo en formato de hoja de cálculo XML abierto estricto](/cells/es/net/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [Guardar archivo en objeto de respuesta](/cells/es/net/saving-file-to-response-object/)
