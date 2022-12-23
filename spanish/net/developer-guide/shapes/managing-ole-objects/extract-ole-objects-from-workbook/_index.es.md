---
title: Extraer objetos OLE del libro de trabajo
type: docs
weight: 110
url: /es/net/extract-ole-objects-from-workbook/
---
{{% alert color="primary" %}}

A veces, necesita extraer objetos OLE de un libro de trabajo. Aspose.Cells admite extraer y guardar esos objetos Ole.

Este artículo muestra cómo crear una aplicación de consola en Visual Studio.Net y extraer diferentes objetos OLE de un libro de trabajo con unas pocas líneas de código simples.

{{% /alert %}}

## **Extraer objetos OLE de un libro de trabajo**

### **Creación de un libro de plantilla**

1. Creó un libro de trabajo en Microsoft Excel.
1. Agregue un documento de Word Microsoft, un libro de Excel y un documento PDF como objetos OLE en la primera hoja de trabajo.

|**Documento de plantilla con objetos OLE (OleFile.xls)**|
|:- |
|![todo:imagen_alternativa_texto](extract-ole-objects-from-workbook_1.png)|

A continuación, extraiga los objetos OLE y guárdelos en el disco duro con sus respectivos tipos de archivo.

### **Descargar e Instalar Aspose.Cells**

1. [Descargar Aspose.Cells for .NET](https://downloads.aspose.com/cells/net).
1. Instálalo en tu computadora de desarrollo.

Todos los componentes Aspose, cuando están instalados, funcionan en modo de evaluación. El modo de evaluación no tiene límite de tiempo y solo inyecta marcas de agua en los documentos producidos.

### **Crear un proyecto**

Comenzar**Visual Studio.Net** y cree una nueva aplicación de consola. Este ejemplo mostrará una aplicación de consola C#, pero también puede usar VB.NET.

1. Añadir referencias
 1. Agregue una referencia al componente Aspose.Cells a su proyecto, por ejemplo, agregue una referencia a ...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll

### **Extraer objetos OLE**

El siguiente código hace el trabajo real de encontrar y extraer objetos OLE. Los objetos OLE (archivos DOC, XLS y PDF) se guardan en el disco.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ExtractOLEObjects-1.cs" >}}
