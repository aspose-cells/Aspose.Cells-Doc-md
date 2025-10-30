---
title: Modifica gli hyperlink del foglio di lavoro con C++
linktitle: Modifica collegamenti ipertestuali del foglio di calcolo
type: docs
weight: 330
url: /it/cpp/editing-hyperlinks-of-worksheet/
description: Impara come modificare gli hyperlink del foglio di lavoro tramite l API Aspose.Cells for C++.
keywords: Modifica collegamenti ipertestuali, Modifica collegamenti ipertestuali del foglio di lavoro, Modifica collegamento ipertestuale nella cella, Accedi a tutti i collegamenti ipertestuali del foglio di lavoro
---

{{% alert color="primary" %}}

Aspose.Cells ti consente di accedere a tutti i collegamenti ipertestuali del foglio di lavoro utilizzando la collezione [**GetHyperlinks()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gethyperlinks/). Puoi accedere a ciascun collegamento ipertestuale da questa collezione uno per uno e modificarne le proprietà.

{{% /alert %}}

Il seguente esempio di codice accede a tutti gli hyperlink del foglio di lavoro e ne modifica la proprietà [**GetAddress()**](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink/getaddress/) al sito web di Aspose.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook from input file
    Workbook workbook(srcDir + u"Sample.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Iterate through all hyperlinks in the worksheet
    for (int32_t i = 0; i < worksheet.GetHyperlinks().GetCount(); i++)
    {
        Hyperlink hl = worksheet.GetHyperlinks().Get(i);
        hl.SetAddress(u"http://www.aspose.com");
    }

    // Save the modified workbook to the output file
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "Hyperlinks updated successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
