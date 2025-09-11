---  
title: Create Shared Workbook with Aspose.Cells with C++  
linktitle: Create Shared Workbook with Aspose.Cells  
type: docs  
weight: 40  
url: /cpp/create-shared-workbook-with-aspose-cells/  
description: Learn how to create a shared workbook using Aspose.Cells with C++.  
---  

## **Possible Usage Scenarios**  

Microsoft Excel allows you to share the workbook as shown in the following screenshot. When you share the workbook, then more than one user can edit the workbook on the network. Aspose.Cells enables you to create a shared workbook with the [**Workbook.GetShared()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshared/) property.  

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_1.png)  

## **Create Shared Workbook with Aspose.Cells**  

The following sample code creates a shared workbook by setting the [**Workbook.GetShared()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshared/) property as **true**. When you open the [output Excel file](55541786.xlsx) in Microsoft Excel, you will see **Shared** with the output workbook name as shown in this screenshot.  

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_2.png)  

## **Sample Code**  

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