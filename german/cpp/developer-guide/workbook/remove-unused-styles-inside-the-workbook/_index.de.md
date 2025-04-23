---  
title: Unbenutzte Stile in der Arbeitsmappe mit C++ entfernen  
linktitle: Entfernen Sie unbenutzte Stile innerhalb der Arbeitsmappe  
type: docs  
weight: 340  
url: /de/cpp/remove-unused-styles-inside-the-workbook/  
description: Unbenutzte Stile in Excel Arbeitsmappe mit Aspose.Cells und C++ entfernen.  
---  

{{% alert color="primary" %}}  

Unbenutzte Stile in Excel-Dateien beanspruchen nicht nur Speicherplatz, sondern verursachen auch Leistungsprobleme beim Umwandeln in verschiedene Formate wie PDF, HTML usw. Aspose.Cells bietet [**Workbook.RemoveUnusedStyles()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/removeunusedstyles/) zum Entfernen aller unbenutzten Stile innerhalb der Arbeitsmappe.  

{{% /alert %}}  

Der folgende Code erklärt die Verwendung von [**Workbook.RemoveUnusedStyles()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/removeunusedstyles/). Der Code lädt die [Vorlagendatei](5115520.xlsx), die Sie über den bereitgestellten Link herunterladen können. Sie enthält einen unbenutzten Stil namens **AsposeStyle**; dieser Stil und alle anderen unbenutzten Stile werden nach der Ausführung des Codes entfernt.  

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
