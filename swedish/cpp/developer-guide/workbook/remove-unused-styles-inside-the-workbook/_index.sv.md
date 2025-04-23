---  
title: Ta bort oanvända stilar i arbetsboken med C++  
linktitle: Ta bort oanvända stilar inne i arbetsboken  
type: docs  
weight: 340  
url: /sv/cpp/remove-unused-styles-inside-the-workbook/  
description: Ta bort oanvända stilar i Excel arbetsbok med Aspose.Cells och C++.  
---  

{{% alert color="primary" %}}  

Oanvända stilar i Excel-filer tar inte bara upp utrymme utan kan också orsaka prestandaproblem vid konvertering till olika format som PDF, HTML etc. Aspose.Cells tillhandahåller [**Workbook.RemoveUnusedStyles()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/removeunusedstyles/) för att ta bort alla oanvända stilar i arbetsboken.  

{{% /alert %}}  

Följande kod förklarar användningen av [**Workbook.RemoveUnusedStyles()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/removeunusedstyles/). Koden laddar [mallexcelfilen](5115520.xlsx) som du kan ladda ner från länken. Den innehåller en oanvänd stil som heter **AsposeStyle**; denna stil och alla andra oanvända stilar tas bort efter körning.  

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)  

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
    // Path to the documents directory.
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load template Excel file containing unused styles
    U16String templateFilePath = srcDir + u"Template-With-Unused-Custom-Style.xlsx";
    Workbook workbook(templateFilePath);

    // Remove all unused styles inside the template
    // This will also remove AsposeStyle which is an unused style inside the template
    workbook.RemoveUnusedStyles();

    // Save the file
    U16String outputFilePath = srcDir + u"output_out.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Unused styles removed and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
