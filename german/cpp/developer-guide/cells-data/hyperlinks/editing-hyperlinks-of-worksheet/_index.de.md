---
title: Hyperlinks im Arbeitsblatt mit C++ bearbeiten
linktitle: Bearbeiten von Hyperlinks des Arbeitsblatts
type: docs
weight: 330
url: /de/cpp/editing-hyperlinks-of-worksheet/
description: Lernen Sie, wie man Hyperlinks im Arbeitsblatt durch die API Aspose.Cells for C++ bearbeitet.
keywords: Hyperlinks bearbeiten, Hyperlinks des Arbeitsblatts editieren, Hyperlink einer Zelle bearbeiten, Zugriff auf alle Hyperlinks des Arbeitsblatts
---

{{% alert color="primary" %}}

Aspose.Cells ermöglicht es Ihnen, über die [**GetHyperlinks()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gethyperlinks/)-Sammlung auf alle Hyperlinks des Arbeitsblatts zuzugreifen. Sie können von dieser Sammlung aus jeden Hyperlink einzeln aufrufen und seine Eigenschaften bearbeiten.

{{% /alert %}}

Der folgende Beispielcode greift auf alle Hyperlinks des Arbeitsblatts zu und ändert deren [**GetAddress()**](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink/getaddress/)-Eigenschaft auf die Aspose-Website.

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
