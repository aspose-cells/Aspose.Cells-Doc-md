---
title: Obtener o establecer el identificador de clase del objeto OLE incrustado
type: docs
weight: 920
url: /es/java/get-or-set-the-class-identifier-of-the-embedded-ole-object/
---

## **Escenarios de uso posibles**
Aspose.Cells proporciona la propiedad [OleObject.ClassIdentifier](https://reference.aspose.com/cells/java/com.aspose.cells/oleobject#ClassIdentifier) que puede utilizar para obtener o establecer el identificador de clase de un objeto ole incrustado. Los identificadores de clase de objetos Ole son GUID, es decir, Identificadores Únicos Globales. GUID siempre tiene 16 bytes de longitud, por lo tanto, los identificadores de clase también tienen 16 bytes de longitud. A menudo se encuentran dentro del Registro de Windows y proporcionan información a la aplicación host sobre cómo abrir el objeto ole incrustado que contiene varios recursos incrustados dentro de la aplicación cliente.
## **Obtener o establecer el identificador de clase del objeto OLE incrustado**
La siguiente captura de pantalla muestra el identificador de clase del objeto Ole, es decir, el GUID que se ha leído del [archivo de Excel de muestra](5473378.xls) que contiene el objeto ole de PowerPoint incrustado.

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)
## **Código de muestra**
Consulte el siguiente código de muestra ejecutado con [archivo de Excel de ejemplo](5473378.xls) y su salida en consola que imprime el *Identificador de clase* del Objeto Ole, es decir, el GUID. El GUID impreso es exactamente el mismo que se muestra dentro de la captura de pantalla.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetSettheClassIdentifier-GetSettheClassIdentifier.java" >}}
## **Salida de la consola**
Esta es la salida en consola del código de muestra anterior cuando se ejecuta con el [archivo de Excel de ejemplo](5473378.xls).

{{< highlight java >}}

 DC020317-E6E2-4A62-B9FA-B3EFE16626F4

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
