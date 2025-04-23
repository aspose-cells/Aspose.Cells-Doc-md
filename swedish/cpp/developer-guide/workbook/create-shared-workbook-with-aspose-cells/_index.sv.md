---  
title: Skapa delad arbetsbok med Aspose.Cells och C++  
linktitle: Skapa Delad arbetsbok med Aspose.Cells  
type: docs  
weight: 40  
url: /sv/cpp/create-shared-workbook-with-aspose-cells/  
description: Lär dig hur du skapar en delad arbetsbok med Aspose.Cells och C++.  
---  

## **Möjliga användningsscenario**  

Microsoft Excel tillåter dig att dela arbetsboken som visas i följande skärmdump. När du delar arbetsboken kan fler än en användare redigera arbetsboken i nätverket. Aspose.Cells gör det möjligt att skapa en delad arbetsbok med [**Workbook.GetShared()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshared/)-egenskapen.  

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_1.png)  

## **Skapa Delad arbetsbok med Aspose.Cells**  

Följande exempel skapar en delad arbetsbok genom att ställa in [**Workbook.GetShared()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshared/)-egenskapen till **true**. När du öppnar [utdata Excel-filen](55541786.xlsx) i Microsoft Excel, kommer du att se **Shared** med arbetsbokens namn som visas i denna skärmdump.  

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_2.png)  

## **Exempelkod**  

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
