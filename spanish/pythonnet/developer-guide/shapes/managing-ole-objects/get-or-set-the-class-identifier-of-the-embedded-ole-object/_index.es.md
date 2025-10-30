---
title: Obtener o establecer el identificador de clase del objeto OLE incrustado
type: docs
weight: 200
url: /es/python-net/get-or-set-the-class-identifier-of-the-embedded-ole-object/
---

## **Escenarios de uso posibles**
Aspose.Cells para Python via .NET proporciona la propiedad [OleObject.class_identifier](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobject/class_identifier) que puedes usar para obtener o establecer el identificador de clase del objeto Ole incrustado. Los identificadores de clase de Ole Object son en realidad GUIDs, es decir, Identificadores Únicos Globales. Un GUID siempre tiene una longitud de 16 bytes, por lo que los identificadores de clase también son de 16 bytes. A menudo se encuentran en el Registro de Windows y proporcionan información a la aplicación host sobre cómo abrir el objeto Ole incrustado que contiene varios recursos incrustados dentro de la aplicación cliente.

## **Obtener o establecer el identificador de clase del objeto OLE incrustado**
La siguiente captura de pantalla muestra el identificador de clase de objeto Ole, es decir, GUID que se ha leído del [archivo de Excel de ejemplo](5115190.xls) que contiene el objeto OLE de PowerPoint incrustado.

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)

### **Código de muestra**
Consulte el siguiente código de ejemplo ejecutado con el [archivo de Excel de ejemplo](5115190.xls) y su salida por consola que imprime el identificador de clase del objeto Ole, es decir, GUID. El GUID impreso es exactamente el mismo que se muestra dentro de la captura de pantalla.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-GetSetClassIdentifierEmbedOleObject.py" >}}

### **Salida de la consola**
Esta es la salida por consola del código de ejemplo anterior cuando se ejecuta con el [archivo de Excel de ejemplo](5115190.xls).

{{< highlight java >}}

 DC020317-E6E2-4A62-B9FA-B3EFE16626F4

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
