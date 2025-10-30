---
title: Obtener o Establecer el Identificador de Clase del Objeto OLE Embebido con Golang a través de C++
linktitle: Obtener o establecer el identificador de clase del objeto OLE incrustado
type: docs
weight: 200
url: /es/go-cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/
description: Aprenda cómo obtener o establecer el identificador de clase de los objetos OLE incrustados usando Aspose.Cells con Golang a través de C++.
---

## **Escenarios de uso posibles**
Aspose.Cells proporciona la propiedad [OleObject.GetClassIdentifier()](https://reference.aspose.com/cells/go-cpp/oleobject/getclassidentifier/) que puede usar para obtener o establecer el identificador de clase del objeto OLE embebido. Los Identificadores de Clase de Objetos OLE son en realidad GUIDs, es decir, Identificadores Únicos Globales. El GUID tiene una longitud de 16 bytes, por lo tanto, los identificadores de clase también son de 16 bytes. A menudo se encuentran dentro del Registro de Windows y proporcionan información a la aplicación host sobre cómo abrir objetos OLE incrustados que contienen diversos recursos incrustados dentro de la aplicación cliente.

## **Obtener o establecer el identificador de clase del objeto OLE incrustado**
La siguiente captura de pantalla muestra el Identificador de Clase del Objeto OLE, es decir, GUID, que ha sido leído desde el [archivo de Excel de ejemplo](5115190.xls) que contiene el objeto OLE incrustado de PowerPoint.

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)

### **Código de muestra**
Por favor, mira el siguiente código de ejemplo ejecutado con el [archivo de Excel de ejemplo](5115190.xls) y su salida en consola, que imprime el Identificador de Clase del Objeto OLE, es decir, GUID. El GUID impreso es exactamente el mismo que se muestra en la captura de pantalla.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetOrSetTheClassIdentifierOfTheEmbeddedOleObject.go" >}}
### **Salida de la consola**
Esta es la salida por consola del código de ejemplo anterior cuando se ejecuta con el [archivo de Excel de ejemplo](5115190.xls).

{{< highlight java >}}
DC020317-E6E2-4A62-B9FA-B3EFE16626F4
{{< /highlight >}}
