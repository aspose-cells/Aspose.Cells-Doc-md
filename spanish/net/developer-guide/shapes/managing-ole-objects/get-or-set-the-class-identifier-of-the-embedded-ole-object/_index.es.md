---
title: Obtener o establecer el identificador de clase del objeto OLE incrustado
type: docs
weight: 200
url: /es/net/get-or-set-the-class-identifier-of-the-embedded-ole-object/
---

## **Escenarios de uso posibles**
Aspose.Cells proporciona la propiedad [OleObject.ClassIdentifier](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/classidentifier) que puede utilizar para obtener o establecer el identificador de clase del objeto OLE incrustado. Los identificadores de clase de objeto Ole son en realidad GUID, es decir, Identificadores Únicos Globales. GUID siempre tiene 16 bytes de longitud, por lo tanto, los identificadores de clase también tienen 16 bytes de longitud. A menudo se encuentran dentro del Registro de Windows y proporcionan información a la aplicación host sobre cómo abrir el objeto OLE incrustado que contiene varios recursos incrustados dentro de la aplicación cliente.
## **Obtener o establecer el identificador de clase del objeto OLE incrustado**
La siguiente captura de pantalla muestra el identificador de clase de objeto Ole, es decir, GUID que se ha leído del [archivo de Excel de ejemplo](5115190.xls) que contiene el objeto OLE de PowerPoint incrustado.

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)
### **Código de muestra**
Consulte el siguiente código de ejemplo ejecutado con el [archivo de Excel de ejemplo](5115190.xls) y su salida por consola que imprime el identificador de clase del objeto Ole, es decir, GUID. El GUID impreso es exactamente el mismo que se muestra dentro de la captura de pantalla.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetSetClassIdentifierEmbedOleObject-GetSetClassIdentifierEmbedOleObject.cs" >}}
### **Salida de la consola**
Esta es la salida por consola del código de ejemplo anterior cuando se ejecuta con el [archivo de Excel de ejemplo](5115190.xls).

{{< highlight java >}}

 DC020317-E6E2-4A62-B9FA-B3EFE16626F4

{{< /highlight >}}
