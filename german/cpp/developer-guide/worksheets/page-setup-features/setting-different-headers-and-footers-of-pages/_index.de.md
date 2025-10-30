---
title: Verschiedene Kopf und Fußzeilen für verschiedene Seiten mit C++ festlegen
linktitle: Verschiedene Kopf und Fußzeilen festlegen
type: docs
weight: 35
url: /de/cpp/setting-different-headers-and-footers-for-pages-to-excel/
description: Dieser Artikel liefert Beispielcode, der zeigt, wie Sie die verschiedenen Kopf und Fußzeilen der Excel Page Setup Einstellungen programmgesteuert mit der C++ Bibliothek und API festlegen können. Sie können die Kopf und Fußzeilen für die erste Seite, ungerade Seiten und gerade Seiten einstellen.
keywords: Excel Kopf und Fußzeile für die erste Seite festlegen, Excel Kopf und Fußzeile für ungerade Seiten festlegen, Excel Kopf und Fußzeile für gerade Seiten festlegen mit C++
---

{{% alert color="primary" %}}

MS Excel unterstützt das Festlegen unterschiedlicher Kopf- und Fußzeilen für die erste Seite, ungerade Seiten und gerade Seiten seit Excel 2007.
Aspose.Cells unterstützt dieselbe Funktion.

{{% /alert %}}

## **Setzen verschiedener Kopf- und Fußzeilen in MS Excel**

**![Setzen verschiedener Kopf- und Fußzeilen](difpage.png)**

1. Klicken Sie auf **Seitenlayout > Drucktitel > Kopf-/Fußzeile**.
1. Aktivieren Sie **Unterscheidung zwischen ungeraden und geraden Seiten** oder **Unterschiedliche erste Seite**.
1. Geben Sie verschiedene Kopf- und Fußzeilen ein.

## **Setzen von verschiedenen Kopf- und Fußzeilen mit Aspose.Cells**

Aspose.Cells verhält sich genauso wie Excel.
1. Setzt die Flags [PageSetup.IsHFDiffOddEven](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/ishfdiffoddeven/) und [PageSetup.IsHFDiffFirst](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/ishfdifffirst/) 
1. Geben Sie verschiedene Kopf- und Fußzeilen ein.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook wb;

    // Get the first worksheet's page setup
    PageSetup pageSetup = wb.GetWorksheets().Get(0).GetPageSetup();

    // Set different headers for odd and even pages
    pageSetup.SetIsHFDiffOddEven(true);
    pageSetup.SetHeader(1, u"I am the header of the Odd page.");
    pageSetup.SetEvenHeader(1, u"I am the header of the Even page.");

    // Set a different header for the first page
    pageSetup.SetIsHFDiffFirst(true);
    pageSetup.SetFirstPageHeader(1, u"I am the header of the First page.");

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
