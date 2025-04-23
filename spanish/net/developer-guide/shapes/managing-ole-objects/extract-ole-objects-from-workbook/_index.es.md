---
title: Extraer objetos OLE del libro de trabajo
type: docs
weight: 110
url: /es/net/extract-ole-objects-from-workbook/
---

{{% alert color="primary" %}}

A veces, es necesario extraer objetos OLE de un libro de trabajo. Aspose.Cells admite la extracción y el guardado de esos objetos OLE.

Este artículo muestra cómo crear una aplicación de consola en Visual Studio.Net y extraer diferentes objetos OLE de un libro de trabajo con unas pocas líneas de código sencillas.

{{% /alert %}}

## **Extraer objetos OLE de un libro de trabajo**

### **Crear un libro de trabajo de plantilla**

1. Crear un libro de trabajo en Microsoft Excel.
1. Agregar un documento de Word de Microsoft, un libro de trabajo de Excel y un documento PDF como objetos OLE en la primera hoja de cálculo.

| **Documento de plantilla con objetos OLE (OleFile.xls)** |
| :- |
|![todo:image_alt_text](extract-ole-objects-from-workbook_1.png)|

A continuación, extraiga los objetos OLE y guárdelos en el disco duro con sus respectivos tipos de archivo.

### **Descargar e instalar Aspose.Cells**

1. [Descargar Aspose.Cells for .NET](https://downloads.aspose.com/cells/net).
1. Instálelo en su equipo de desarrollo.

Todos los componentes de Aspose, al instalarse, funcionan en modo de evaluación. El modo de evaluación no tiene límite de tiempo y solo inserta marcas de agua en los documentos producidos.

### **Crear un proyecto**

Inicie **Visual Studio.Net** y cree una nueva aplicación de consola. Este ejemplo mostrará una aplicación de consola en C#, pero también puede usar VB.NET.

1. Agregar referencias
   1. Agregar una referencia al componente Aspose.Cells a su proyecto, por ejemplo agregar una referencia a ...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll

### **Extraer objetos OLE**

El código a continuación realiza el trabajo real de encontrar y extraer objetos OLE. Los objetos OLE (archivos DOC, XLS y PDF) se guardan en disco.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ExtractOLEObjects-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
