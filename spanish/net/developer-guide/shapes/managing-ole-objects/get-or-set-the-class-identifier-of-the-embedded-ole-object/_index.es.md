---
title: Obtener o establecer el identificador de clase del objeto OLE incrustado
type: docs
weight: 200
url: /es/net/get-or-set-the-class-identifier-of-the-embedded-ole-object/
---
## **Posibles escenarios de uso**
 Aspose.Cells proporciona el[OleObject.ClassIdentifier](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/classidentifier)propiedad que puede usar para obtener o establecer el identificador de clase del objeto ole incrustado. Los identificadores de clase de objetos antiguos son en realidad GUID, es decir, identificadores únicos globales. GUID siempre tiene una longitud de 16 bytes, por lo que los identificadores de clase también tienen una longitud de 16 bytes. A menudo se encuentran dentro del Registro Windows y brindan información a la aplicación host sobre cómo abrir un objeto ole incrustado que contiene varios recursos incrustados dentro de la aplicación cliente.
## **Obtener o establecer el identificador de clase del objeto OLE incrustado**
 La siguiente captura de pantalla muestra el identificador de clase de objeto Ole, es decir, GUID, que se ha leído desde el[ejemplo de archivo de Excel](5115190.xls) que contiene el objeto ole incrustado PowerPoint.

![todo:imagen_alternativa_texto](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)
### **Código de muestra**
 Consulte el siguiente código de ejemplo ejecutado con[ejemplo de archivo de Excel](5115190.xls) su salida de consola que imprime el Identificador de clase de Ole Object, es decir, GUID. El GUID impreso es exactamente el mismo que se muestra en la captura de pantalla.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetSetClassIdentifierEmbedOleObject-GetSetClassIdentifierEmbedOleObject.cs" >}}
### **Salida de consola**
 Esta es la salida de la consola del código de muestra anterior cuando se ejecuta con el[ejemplo de archivo de Excel](5115190.xls).

{{< highlight "java" >}}

 DC020317-E6E2-4A62-B9FA-B3EFE16626F4

{{< /highlight >}}
