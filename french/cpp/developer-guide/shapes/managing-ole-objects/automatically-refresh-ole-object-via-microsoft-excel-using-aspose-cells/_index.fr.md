---
title: Actualiser automatiquement l objet OLE via Microsoft Excel avec C++
linktitle: Actualiser automatiquement l objet OLE
type: docs
weight: 270
url: /fr/cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/
description: Apprenez comment actualiser automatiquement les objets OLE dans Microsoft Excel en utilisant Aspose.Cells avec C++.
---

{{% alert color="primary" %}}

Aspose.Cells fournit la propriété [**OleObject.GetAutoLoad()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getautoload/) pour actualiser l'objet OLE lorsque le fichier Excel est ouvert dans Microsoft Excel. Grâce à cette propriété, l'objet OLE affichera l'image OLE correcte générée par Microsoft Excel.

{{% /alert %}}

Le code d'exemple suivant charge le [fichier Excel d'exemple](5115231.xlsx) qui possède une image OLE non réelle. L'objet OLE est en fait un document Microsoft Word, mais le fichier Excel d'exemple affiche l'image de l'animal au lieu de l'image de Microsoft Word. Cependant, si vous ouvrez le [fichier Excel de sortie](5115225.xlsx), vous verrez que Microsoft Excel affiche la bonne image OLE.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create workbook object from your sample excel file
    Workbook wb(srcDir + u"sample.xlsx");

    // Access first worksheet
    Worksheet sheet = wb.GetWorksheets().Get(0);

    // Set auto load property of first ole object to true
    sheet.GetOleObjects().Get(0).SetAutoLoad(true);

    // Save the workbook in xlsx format
    wb.Save(srcDir + u"RefreshOLEObjects_out.xlsx", SaveFormat::Xlsx);

    std::cout << "OLE object refreshed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
