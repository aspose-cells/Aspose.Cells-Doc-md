---
title: Guardar archivo en el objeto de respuesta con Golang a través de C++
linktitle: Guardando archivo en objeto de respuesta
type: docs
weight: 50
url: /es/go-cpp/saving-file-to-response-object/
description: Aprenda cómo guardar archivos dinámicamente y enviarlos directamente a un navegador cliente usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells hace posible manipular archivos. Este artículo explica las diferentes formas en las que los archivos se pueden guardar en un objeto de respuesta.

{{% /alert %}}

## **Guardando archivo en objeto de respuesta**

También es posible generar un archivo dinámicamente y enviarlo directamente al navegador del cliente. Para hacerlo, use una versión sobrecargada especial del método [**Save**](https://reference.aspose.com/cells/go-cpp/workbook/save_string_saveformat/) que acepta los siguientes parámetros:

- Objeto **HttpResponse**.
- Nombre de archivo.
- [**ContentDisposition**](https://reference.aspose.com/cells/go-cpp/contentdisposition/), el tipo de disposición de contenido del archivo de salida.
- [**SaveOptions**](https://reference.aspose.com/cells/go-cpp/saveoptions/), el tipo de formato de archivo.

La enumeración [**ContentDisposition**](https://reference.aspose.com/cells/go-cpp/contentdisposition/) determina si el archivo que se envía al navegador proporciona la opción de abrirse directamente en el navegador o en una aplicación asociada con .xls/.xlsx u otra extensión.

La enumeración contiene los siguientes tipos de guardado predefinidos:

|**Tipo**|**Descripción**|
| :- | :- |
|Archivo adjunto|Envía la hoja de cálculo al navegador y se abre en una aplicación como un archivo adjunto asociado con .xls/.xlsx u otras extensiones|
|En línea|Envía el documento al navegador y presenta una opción para guardar la hoja de cálculo en el disco o abrir dentro del navegador|

### **Archivos XLS**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToResponseObject.go" >}}
### **Archivos XLSX**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToResponseObject-1.go" >}}
### **Archivos PDF**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToResponseObject-2.go" >}}
### **Nota**

Debido al objeto "System.Web.HttpResponse" que no está incluido en .NET5 y .Netstandard,
Por lo tanto, esta función no existe en la versión Aspose.Cells .NET5 y .Netstandard, puede consultar el siguiente código para guardar el archivo en el flujo, y luego realizar operaciones en el flujo.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToResponseObject-3.go" >}}
