---
title: Guardando archivo en objeto de respuesta
type: docs
weight: 50
url: /es/net/saving-file-to-response-object/
---

{{% alert color="primary" %}}

Aspose.Cells hace posible manipular archivos. Este artículo explica las diferentes formas en las que los archivos se pueden guardar en un objeto de respuesta.

{{% /alert %}}

## **Guardando archivo en objeto de respuesta**

También es posible generar un archivo dinámicamente y enviarlo directamente al navegador del cliente. Para hacerlo, use una versión sobrecargada especial del método [**Save**](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/5) que acepta los siguientes parámetros:

- Objeto ASP.NET [**HttpResponse**](https://docs.microsoft.com/en-gb/dotnet/api/system.web.httpresponse?view=netframework-4.8).
- Nombre de archivo.
- [**ContentDisposition**](https://reference.aspose.com/cells/net/aspose.cells/contentdisposition), el tipo de disposición de contenido del archivo de salida.
- [**SaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/saveoptions), el tipo de formato de archivo

La enumeración [**ContentDisposition**](https://reference.aspose.com/cells/net/aspose.cells/contentdisposition) determina si el archivo que se envía al navegador proporciona la opción de abrirse directamente en el navegador o en una aplicación asociada con .xls/.xlsx u otra extensión.

La enumeración contiene los siguientes tipos de guardado predefinidos:

|**Tipo**|**Descripción**|
| :- | :- |
|Archivo adjunto|Envía la hoja de cálculo al navegador y se abre en una aplicación como un archivo adjunto asociado con .xls/.xlsx u otras extensiones|
|En línea|Envía el documento al navegador y presenta una opción para guardar la hoja de cálculo en el disco o abrir dentro del navegador|

### **Archivos XLS**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveXLSFile-1.cs" >}}

### **Archivos XLSX**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveXLSXFile-1.cs" >}}

### **Archivos PDF**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveInPdfFormat-1.cs" >}}

### **Nota**

Debido al objeto "System.Web.HttpResponse" que no está incluido en .NET5 y .Netstandard,
Por lo tanto, esta función no existe en la versión Aspose.Cells .NET5 y .Netstandard, puede consultar el siguiente código para guardar el archivo en el flujo, y luego realizar operaciones en el flujo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoStream-1.cs" >}}

