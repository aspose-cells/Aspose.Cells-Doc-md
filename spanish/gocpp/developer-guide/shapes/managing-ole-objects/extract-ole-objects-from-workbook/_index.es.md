---
title: Extraer objetos OLE del libro con Golang vía C++
linktitle: Extraer objetos OLE del libro de trabajo
type: docs
weight: 110
url: /es/go-cpp/extract-ole-objects-from-workbook/
description: Aprender cómo extraer objetos OLE de un libro usando Aspose.Cells con Golang vía C++.
---

{{% alert color="primary" %}}

A veces, necesitas extraer objetos OLE de un libro de trabajo. Aspose.Cells soporta extraer y guardar esos objetos OLE.

Este artículo muestra cómo crear una aplicación de consola en Visual Studio y extraer diferentes objetos OLE de un libro de trabajo con unas pocas líneas de código.

{{% /alert %}}

## **Extraer objetos OLE de un libro de trabajo**

### **Crear un libro de trabajo de plantilla**

1. Crea un libro de trabajo en Microsoft Excel.
1. Agrega un documento de Microsoft Word, un libro de Excel y un documento PDF como objetos OLE en la primera hoja de trabajo.

| **Documento de plantilla con objetos OLE (OleFile.xls)** |
| :- |
|![todo:image_alt_text](extract-ole-objects-from-workbook_1.png)|

Luego, extrae los objetos OLE y guárdalos en el disco duro con sus respectivos tipos de archivo.

### **Descargar e instalar Aspose.Cells**

1. [Descargar Aspose.Cells for C++](https://downloads.aspose.com/cells/go-cpp/).
1. Instálelo en su equipo de desarrollo.

Todos los componentes de Aspose, al instalarse, funcionan en modo de evaluación. El modo de evaluación no tiene límite de tiempo y solo inserta marcas de agua en los documentos producidos.

### **Crear un proyecto**

Inicia **Visual Studio** y crea una nueva aplicación de consola. Este ejemplo mostrará una aplicación de consola en C++.

1. Agregar referencias
   1. Agrega una referencia al componente Aspose.Cells en tu proyecto, por ejemplo, agregando una referencia a ...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll.

### **Extraer objetos OLE**

El código a continuación realiza la tarea de encontrar y extraer objetos OLE. Los objetos OLE (archivos DOC, XLS y PDF) se guardan en el disco.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExtractOleObjectsFromWorkbook.go" >}}
