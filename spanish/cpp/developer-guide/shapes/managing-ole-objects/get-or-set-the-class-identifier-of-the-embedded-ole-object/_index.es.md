---
title: Obtener o establecer el identificador de clase del objeto OLE incrustado con C++
linktitle: Obtener o establecer el identificador de clase del objeto OLE incrustado
type: docs
weight: 200
url: /es/cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/
description: Aprende cómo obtener o establecer el identificador de clase de objetos OLE incrustados usando Aspose.Cells con C++.
---

## **Escenarios de uso posibles**
Aspose.Cells proporciona la propiedad [OleObject.GetClassIdentifier()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getclassidentifier/) que puedes usar para obtener o establecer el identificador de clase del objeto OLE incrustado. Los identificadores de clase de objetos OLE en realidad son GUIDs, es decir, Identificadores únicos globales. GUID siempre tiene 16 bytes de largo, por lo que los identificadores de clase también son de 16 bytes. Se encuentran a menudo en el Registro de Windows y proporcionan información a la aplicación anfitriona sobre cómo abrir objetos OLE incrustados que contienen diversos recursos incrustados dentro de la aplicación cliente.

## **Obtener o establecer el identificador de clase del objeto OLE incrustado**
La siguiente captura de pantalla muestra el Identificador de Clase del Objeto OLE, es decir, GUID, que ha sido leído desde el [archivo de Excel de ejemplo](5115190.xls) que contiene el objeto OLE incrustado de PowerPoint.

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)

### **Código de muestra**
Por favor, mira el siguiente código de ejemplo ejecutado con el [archivo de Excel de ejemplo](5115190.xls) y su salida en consola, que imprime el Identificador de Clase del Objeto OLE, es decir, GUID. El GUID impreso es exactamente el mismo que se muestra en la captura de pantalla.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
#include <guiddef.h>

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    Workbook wb(srcDir + u"sample.xls");
    Worksheet ws = wb.GetWorksheets().Get(0);
    OleObject oleObj = ws.GetOleObjects().Get(0);

    Vector<uint8_t> classIdentifier = oleObj.GetClassIdentifier();
    GUID guid;
    memcpy(&guid, classIdentifier.GetData(), sizeof(GUID));

    char guidStr[39];
    snprintf(guidStr, sizeof(guidStr), "{%08X-%04X-%04X-%02X%02X-%02X%02X%02X%02X}",
             guid.Data1, guid.Data2, guid.Data3,
             guid.Data4[0], guid.Data4[1], guid.Data4[2], guid.Data4[3],
             guid.Data4[4], guid.Data4[5], guid.Data4[6], guid.Data4[7]);

    std::cout << guidStr << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Salida de la consola**
Esta es la salida por consola del código de ejemplo anterior cuando se ejecuta con el [archivo de Excel de ejemplo](5115190.xls).

{{< highlight java >}}
DC020317-E6E2-4A62-B9FA-B3EFE16626F4
{{< /highlight >}}
