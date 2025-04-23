---
title: Kopieren Sie die Seitenansicht Einstellungen vom Quell Arbeitsblatt in das Ziel Arbeitsblatt mit C++
linktitle: Seitenansicht Einstellungen kopieren
type: docs
weight: 80
url: /de/cpp/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/
description: Dieser Artikel erklärt, wie man die C++ API oder Beispielcode verwendet, um die Seitenansicht Einstellungen programmgesteuert vom Quell Arbeitsblatt in das Ziel Arbeitsblatt zu kopieren.
keywords: Seitenansicht Einstellungen kopieren c++, Seitenansicht Einstellungen auf Ziel Arbeitsblatt kopieren c++
---

## **Mögliche Verwendungsszenarien**

Wenn Sie ein neues Blatt zu einer Arbeitsmappe hinzufügen, enthält es die Standard-*Seiteneinrichtungseinstellungen*. Es kann vorkommen, dass Sie die Einstellungen ([**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/)) von einem Arbeitsblatt auf ein anderes Arbeitsblatt übertragen müssen. In diesem Dokument wird erläutert, wie die Seiteneinrichtungseinstellungen von einem Arbeitsblatt auf ein anderes mithilfe der Aspose.Cells-APIs kopiert werden.

## **Seiteneinrichtungseinstellungen von der Quellarbeitsmappe in die Zieltabelle kopieren**

Der folgende Beispielcode veranschaulicht, wie die *Seiteneinrichtungseinstellungen* von einem Arbeitsblatt auf ein anderes mithilfe der Methode [**PageSetup.Copy()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/copy/) kopiert werden. Bitte beachten Sie den folgenden Beispielcode und dessen Konsolenausgabe als Referenz.

## **Beispielcode**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    Workbook wb;

    wb.GetWorksheets().Add(u"TestSheet1");
    wb.GetWorksheets().Add(u"TestSheet2");

    Worksheet TestSheet1 = wb.GetWorksheets().Get(u"TestSheet1");
    Worksheet TestSheet2 = wb.GetWorksheets().Get(u"TestSheet2");

    TestSheet1.GetPageSetup().SetPaperSize(PaperSizeType::PaperA3ExtraTransverse);

    std::cout << "Before Paper Size: " << static_cast<int>(TestSheet1.GetPageSetup().GetPaperSize()) << std::endl;
    std::cout << "Before Paper Size: " << static_cast<int>(TestSheet2.GetPageSetup().GetPaperSize()) << std::endl;
    std::cout << std::endl;

    CopyOptions copyOptions;
    TestSheet2.GetPageSetup().Copy(TestSheet1.GetPageSetup(), copyOptions);

    std::cout << "After Paper Size: " << static_cast<int>(TestSheet1.GetPageSetup().GetPaperSize()) << std::endl;
    std::cout << "After Paper Size: " << static_cast<int>(TestSheet2.GetPageSetup().GetPaperSize()) << std::endl;
    std::cout << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Konsolenausgabe**

{{< highlight java >}}

Before Paper Size: PaperA3ExtraTransverse

Before Paper Size: PaperLetter

After Paper Size: PaperA3ExtraTransverse

After Paper Size: PaperA3ExtraTransverse

{{< /highlight >}}
