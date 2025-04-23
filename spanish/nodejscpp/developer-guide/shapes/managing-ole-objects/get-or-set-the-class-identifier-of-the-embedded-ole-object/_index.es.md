---  
title: Obtener o establecer el Identificador de Clase del Objeto OLE incrustado con Node.js mediante C++  
linktitle: Obtener o establecer el identificador de clase del objeto OLE incrustado  
type: docs  
weight: 200  
url: /es/nodejs-cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/  
description: Aprenda cómo obtener o establecer el identificador de clase de objetos OLE incrustados en Node.js usando Aspose.Cells mediante C++.  
---  

## **Escenarios de uso posibles**  
Aspose.Cells proporciona la propiedad [OleObject.getClassIdentifier()](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getClassIdentifier--) que puede usar para obtener o establecer el identificador de clase de un objeto OLE incrustado. Los identificadores de clase de objetos OLE son en realidad GUID, es decir, Identificadores Únicos Globales. El GUID siempre tiene 16 bytes de longitud; por lo tanto, los identificadores de clase también son de 16 bytes. A menudo se encuentran dentro del Registro de Windows y proporcionan información a la aplicación host sobre cómo abrir objetos OLE incrustados que contienen varios recursos incrustados dentro de la aplicación cliente.

## **Obtener o establecer el identificador de clase del objeto OLE incrustado**  
 La siguiente captura de pantalla muestra el identificador de clase del objeto OLE, es decir, GUID, que ha sido leído del [archivo de Excel de muestra](5115190.xls) que contiene el objeto PowerPoint OLE incrustado.

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)  
### **Código de muestra**  
Por favor, vea el siguiente código de muestra ejecutado con [archivo de Excel de muestra](5115190.xls) y su salida en consola, que imprime el identificador de clase del objeto OLE, es decir, GUID. El GUID impreso es exactamente el mismo que se muestra en la captura de pantalla.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load your sample workbook which contains embedded PowerPoint ole object
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xls"));

// Access its first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first ole object inside the worksheet
const oleObject = worksheet.getOleObjects().get(0);

// Convert 16-bytes array into GUID
const guid = new Uint8Array(oleObject.getClassIdentifier()).reduce((acc, byte) => acc + String.fromCharCode(byte), '');

// Print the GUID
console.log(guid.toUpperCase());
```  
### **Salida de la consola**  
Esta es la salida de consola del código de muestra anterior cuando se ejecuta con el [archivo de Excel de muestra](5115190.xls).

{{< highlight java >}}  
 DC020317-E6E2-4A62-B9FA-B3EFE16626F4  
{{< /highlight >}}  

