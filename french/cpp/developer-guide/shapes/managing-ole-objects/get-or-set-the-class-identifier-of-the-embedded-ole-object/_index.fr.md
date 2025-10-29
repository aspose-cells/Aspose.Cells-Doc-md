---
title: Obtenir ou définir l identifiant de classe de l objet OLE intégré avec C++
linktitle: Obtenir ou définir l identifiant de classe de l objet OLE incorporé
type: docs
weight: 200
url: /fr/cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/
description: Apprenez comment obtenir ou définir l identifiant de classe des objets OLE intégrés en utilisant Aspose.Cells avec C++.
---

## **Scénarios d'utilisation possibles**
Aspose.Cells fournit la propriété [OleObject.GetClassIdentifier()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getclassidentifier/) que vous pouvez utiliser pour obtenir ou définir l'identifiant de classe de l'objet OLE intégré. Les identifiants de classe d'objet OLE sont en réalité des GUID, c'est-à-dire des identifiants uniques globaux. Le GUID fait toujours 16 octets, donc les identifiants de classe ont également une longueur de 16 octets. Ils se trouvent souvent dans le Registre Windows et fournissent des informations à l'application hôte sur la façon d'ouvrir les objets OLE intégrés contenant diverses ressources intégrées dans l'application cliente.

## **Obtenir ou définir l'identifiant de classe de l'objet OLE incorporé**
La capture d'écran suivante montre l'identifiant de classe d'objet OLE, c'est-à-dire le GUID, qui a été lu à partir du [fichier Excel d'exemple](5115190.xls) contenant l'objet PowerPoint OLE intégré.

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)

### **Code d'exemple**
Veuillez voir le code d'exemple ci-dessous exécuté avec le [fichier Excel d'exemple](5115190.xls) et sa sortie console qui affiche l'identifiant de classe de l'objet OLE, c'est-à-dire le GUID. Le GUID imprimé est exactement le même que celui montré dans la capture d'écran.

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

### **Sortie console**
Ceci est la sortie de la console du code d'exemple ci-dessus lorsqu'il est exécuté avec le [fichier excel d'exemple](5115190.xls).

{{< highlight java >}}
DC020317-E6E2-4A62-B9FA-B3EFE16626F4
{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
