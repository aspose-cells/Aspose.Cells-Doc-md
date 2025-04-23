---  
title: Erstellen Sie ein gemeinsames Arbeitsbuch mit Aspose.Cells in C++  
linktitle: Freigegebene Arbeitsmappe mit Aspose.Cells erstellen  
type: docs  
weight: 40  
url: /de/cpp/create-shared-workbook-with-aspose-cells/  
description: Lernen Sie, wie Sie mit Aspose.Cells in C++ ein gemeinsames Arbeitsbuch erstellen.  
---  

## **Mögliche Verwendungsszenarien**  

Microsoft Excel ermöglicht das Teilen des Arbeitsbuchs, wie im folgenden Screenshot gezeigt. Wenn Sie das Arbeitsbuch teilen, können mehrere Benutzer auf das Netzwerk zugreifen und es bearbeiten. Aspose.Cells ermöglicht es Ihnen, mit der [**Workbook.GetShared()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshared/)-Eigenschaft ein geteiltes Arbeitsbuch zu erstellen.  

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_1.png)  

## **Gemeinsame Arbeitsmappe mit Aspose.Cells erstellen**  

Der folgende Beispielcode erstellt ein geteiltes Arbeitsbuch, indem er die [**Workbook.GetShared()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshared/)-Eigenschaft auf **true** setzt. Wenn Sie die [Ausgabedatei](55541786.xlsx) in Microsoft Excel öffnen, sehen Sie **Shared** mit dem Namen der Arbeitsmappe, wie in diesem Screenshot gezeigt.  

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_2.png)  

## **Beispielcode**  

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create Workbook object
    std::unique_ptr<Workbook> wb = std::make_unique<Workbook>();

    // Share the Workbook
    wb->GetSettings().SetShared(true);

    // Save the Shared Workbook
    wb->Save(u"outputSharedWorkbook.xlsx");

    std::cout << "Shared workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```  
