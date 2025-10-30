---
title: Extraer objetos OLE del libro de trabajo
type: docs
weight: 110
url: /es/python-net/extract-ole-objects-from-workbook/
---

{{% alert color="primary" %}}

A veces, necesitas extraer objetos OLE de un libro de trabajo. Aspose.Cells para Python via .NET soporta la extracción y guardado de estos objetos Ole.

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

### **Extraer objetos OLE usando la biblioteca de Excel Aspose.Cells para Python**

El código a continuación realiza el trabajo real de encontrar y extraer objetos OLE. Los objetos OLE (archivos DOC, XLS y PDF) se guardan en disco.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-ExtractOLEObjects-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
