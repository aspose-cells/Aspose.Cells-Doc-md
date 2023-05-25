---
title: Guardar archivo en objeto de respuesta
type: docs
weight: 50
url: /es/net/saving-file-to-response-object/
---
{{% alert color="primary" %}}

Aspose.Cells permite manipular archivos. Este artículo explica las diversas formas en que los archivos se pueden guardar en un objeto de respuesta.

{{% /alert %}}

##  **Guardar archivo en objeto de respuesta**

También es posible generar un archivo dinámicamente y enviarlo directamente a un navegador cliente. Para ello, utilice una versión especial sobrecargada del**[Guardar](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/5)**método que acepta los siguientes parámetros:

- ASP.NET **[HttpResponse](https://docs.microsoft.com/en-gb/dotnet/api/system.web.httpresponse?view=netframework-4.8)**objeto.
- Nombre del archivo.
- *[ContenidoDisposición](https://reference.aspose.com/cells/net/aspose.cells/contentdisposition)**, el tipo de disposición de contenido del archivo de salida.
- *[GuardarOpciones](https://reference.aspose.com/cells/net/aspose.cells/saveoptions)**, el tipo de formato de archivo

 El**[Disposición de contenido](https://reference.aspose.com/cells/net/aspose.cells/contentdisposition)**La enumeración determina si el archivo que se envía al navegador ofrece la opción de abrirse solo directamente en el navegador o en una aplicación asociada con .xls/.xlsx u otra extensión.

La enumeración contiene los siguientes tipos de guardado predefinidos:

|**Tipo**|**Descripción**|
| :- | :- |
|Attachment|Envía la hoja de cálculo al navegador y se abre en una aplicación como archivo adjunto asociado con .xls/.xlsx u otras extensiones|
|Inline|Envía el documento al navegador y presenta una opción para guardar la hoja de cálculo en el disco o abrirla dentro del navegador|

###  **XLS archivos**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveXLSFile-1.cs" >}}

###  **XLSX archivos**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveXLSXFile-1.cs" >}}

###  **PDF archivos**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveInPdfFormat-1.cs" >}}

###  **Nota**

Debido al objeto "System.Web.HttpResponse" que no está incluido en .NET5 y .Netstandard,
Por lo tanto, esta función no existe en la versión Aspose.Cells .NET5 y .Netstandard, puede consultar el siguiente código para guardar el archivo en la transmisión y luego realizar la operación en la transmisión.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoStream-1.cs" >}}

