---
title: Ottieni o imposta l identificatore di classe dell OLE embedded con C++
linktitle: Ottieni o Imposta l Identificatore di Classe dell Oggetto OLE Incorporato
type: docs
weight: 200
url: /it/cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/
description: Impara come ottenere o impostare l identificatore di classe degli oggetti OLE incorporati usando Aspose.Cells con C++.
---

## **Possibili Scenari di Utilizzo**
Aspose.Cells fornisce la proprietà [OleObject.GetClassIdentifier()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.oleobject/getclassidentifier/) che puoi usare per ottenere o impostare l'identificatore di classe dell'OLE embedded. Gli identificatori di classe degli oggetti OLE sono in realtà GUID, ovvero identificativi univoci globali. Il GUID è lungo sempre 16 byte, quindi anche gli identificatori di classe sono lunghi 16 byte. Sono spesso trovati all’interno del Registro di Windows e forniscono informazioni all’applicazione host su come aprire gli oggetti OLE includenti varie risorse incorporate.

## **Ottieni o Imposta l'Identificatore di Classe dell'Oggetto OLE Incorporato**
Il seguente screenshot mostra l'identificatore di classe dell'oggetto OLE, cioè GUID, che è stato letto dal [file Excel di esempio](5115190.xls) contenente l'oggetto PowerPoint OLE incorporato.

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)

### **Codice di Esempio**
Vedi il seguente esempio di codice eseguito con il [file Excel di esempio](5115190.xls) e l’output della console che stampa l'ID di classe dell'OLE, ovvero GUID. Il GUID stampato è esattamente lo stesso mostrato nello screenshot.

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

### **Output della console**
Questo è l'output della console del codice di esempio precedente quando eseguito con il [file di Excel di esempio](5115190.xls).

{{< highlight java >}}
DC020317-E6E2-4A62-B9FA-B3EFE16626F4
{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
