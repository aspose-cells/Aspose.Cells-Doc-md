---
title: Autor beim Schutz des Arbeitsbuchs mit Schreibschutz in C++ angeben
linktitle: Autor beim Schreibschutz des Arbeitsmappenschreibens spezifizieren
type: docs
weight: 40
url: /de/cpp/specify-author-while-write-protecting-workbook/
description: Erfahren Sie, wie Sie einen Autorennamen beim Schreibschutz einer Arbeitsmappe mit Aspose.Cells for C++ angeben.
---

## **Mögliche Verwendungsszenarien**

Sie können den Autor beim Schutz Ihres Arbeitsbuchs mit der Aspose.Cells-API angeben. Verwenden Sie hierzu die [**Workbook.GetAuthor()**](https://reference.aspose.com/cells/cpp/aspose.cells/writeprotection/getauthor/)-Eigenschaft.

## **Autor beim Schreibschutz des Arbeitsmappenschreibens spezifizieren**

Das folgende Beispiel erklärt die Nutzung der [**Workbook.GetAuthor()**](https://reference.aspose.com/cells/cpp/aspose.cells/writeprotection/getauthor/)-Eigenschaft. Der Code erstellt eine leere Arbeitsmappe, schützt sie mit einem Passwort, gibt den Autorennamen an und speichert sie als [Excel-Ausgabedatei](67338582.xlsx). Das folgende Screenshot zeigt die Wirkung des Beispiels auf die Ausgabedatei zur besseren Referenz.

![todo:image_alt_text](specify-author-while-write-protecting-workbook_1.png)

## **Beispielcode**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create empty workbook
    Workbook wb;

    // Write protect workbook with password
    wb.GetSettings().GetWriteProtection().SetPassword(u"1234");

    // Specify author while write protecting workbook
    wb.GetSettings().GetWriteProtection().SetAuthor(u"SimonAspose");

    // Save the workbook in XLSX format
    wb.Save(outDir + u"outputSpecifyAuthorWhileWriteProtectingWorkbook.xlsx");

    std::cout << "Workbook write protected with author specified successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
