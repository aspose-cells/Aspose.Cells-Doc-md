---
title: Aggiorna automaticamente l oggetto OLE tramite Microsoft Excel con C++
linktitle: Aggiorna automaticamente l oggetto OLE
type: docs
weight: 270
url: /it/cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/
description: Impara come aggiornare automaticamente gli oggetti OLE in Microsoft Excel usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

Aspose.Cells fornisce la proprietà [**OleObject.GetAutoLoad()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getautoload/) per aggiornare l'oggetto OLE quando il file Excel viene aperto in Microsoft Excel. Grazie a questa proprietà, l'oggetto OLE mostrerà l'immagine OLE corretta generata da Microsoft Excel.

{{% /alert %}}

Il codice di esempio seguente carica il [file Excel di esempio](5115231.xlsx) che contiene un'immagine OLE non reale. L'oggetto OLE è in realtà un documento Microsoft Word, ma il file Excel di esempio mostra invece l'immagine dell'animale. Tuttavia, se apri il [file Excel di output](5115225.xlsx), vedrai che Microsoft Excel visualizza l'immagine OLE corretta.

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
{{< app/cells/assistant language="cpp" >}}
