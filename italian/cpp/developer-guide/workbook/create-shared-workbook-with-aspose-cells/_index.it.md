---  
title: Crea un workbook condiviso con Aspose.Cells con C++  
linktitle: Creare un libro di lavoro condiviso con Aspose.Cells  
type: docs  
weight: 40  
url: /it/cpp/create-shared-workbook-with-aspose-cells/  
description: Scopri come creare un workbook condiviso utilizzando Aspose.Cells con C++.  
---  

## **Possibili Scenari di Utilizzo**  

Microsoft Excel consente di condividere il workbook come mostrato nella schermata seguente. Quando condividi il workbook, più utenti possono modificarlo in rete. Aspose.Cells ti consente di creare un workbook condiviso con la proprietà [**Workbook.GetShared()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshared/).  

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_1.png)  

## **Creare un libro di lavoro condiviso con Aspose.Cells**  

Il seguente esempio di codice crea un workbook condiviso impostando la proprietà [**Workbook.GetShared()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshared/) come **true**. Quando apri il [file Excel di output](55541786.xlsx) in Microsoft Excel, vedrai la dicitura **Shared** insieme al nome del workbook come mostrato in questa schermata.  

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_2.png)  

## **Codice di Esempio**  

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
{{< app/cells/assistant language="cpp" >}}
