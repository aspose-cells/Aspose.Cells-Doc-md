---
title: OLE Objekt automatisch mit Microsoft Excel und C++ aktualisieren
linktitle: OLE Objekt automatisch aktualisieren
type: docs
weight: 270
url: /de/cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/
description: Lernen Sie, wie Sie OLE Objekte in Microsoft Excel mit Aspose.Cells und C++ automatisch aktualisieren.
---

{{% alert color="primary" %}}

Aspose.Cells stellt die Eigenschaft [**OleObject.GetAutoLoad()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getautoload/) bereit, um das OLE-Objekt beim Öffnen der Excel-Datei in Microsoft Excel zu aktualisieren. Aufgrund dieser Eigenschaft zeigt das OLE-Objekt das korrekte durch Microsoft Excel generierte OLE-Bild an.

{{% /alert %}}

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](5115231.xlsx), die ein nicht echtes OLE-Bild enthält. Das OLE-Objekt ist tatsächlich ein Microsoft Word-Dokument, aber die Beispiel-Excel-Datei zeigt das Tierbild anstelle des Microsoft Word-Bildes. Wenn Sie jedoch die [Ausgabedatei](5115225.xlsx) öffnen, sehen Sie, dass Microsoft Excel das richtige OLE-Bild anzeigt.

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
