---
title: Hyperlinks im Bereich mit C++ abrufen
linktitle: Hyperlinks im Bereich abrufen
type: docs
weight: 100
url: /de/cpp/get-hyperlinks-in-range/
description: Lernen Sie, wie man Hyperlinks im Bereich durch die API Aspose.Cells for C++ erhält.
keywords: Hyperlinks in Bereich erhalten, Alle Hyperlinks im ausgewählten Bereich erhalten, Hyperlink im Bereich löschen, Die Hyperlinks im ausgewählten Bereich löschen
---

## **Hyperlinks im Bereich abrufen**

Die Klasse [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) bietet eine [**GetHyperlinks()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/gethyperlinks/)-Eigenschaft, die alle Hyperlinks im ausgewählten Bereich zurückgibt. Sie können auch den Hyperlink durch Aufruf der Methode [**Hyperlink.Delete**](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink/delete/) löschen.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"HyperlinksSample.xlsx");
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Range range = worksheet.GetCells().CreateRange(u"A2", u"B3");
    Vector<Hyperlink> hyperlinks = range.GetHyperlinks();

    for (int i = 0; i < hyperlinks.GetLength(); ++i)
    {
        Hyperlink& link = hyperlinks[i];
        std::cout << link.GetArea().ToString().ToUtf8() << " : " << link.GetAddress().ToUtf8() << std::endl;
        link.Delete();
    }

    workbook.Save(outDir + u"HyperlinksSample_out.xlsx");
    std::cout << "Hyperlinks processed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
