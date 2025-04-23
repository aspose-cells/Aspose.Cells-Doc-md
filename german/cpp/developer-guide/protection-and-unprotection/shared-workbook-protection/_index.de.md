---
title: Arbeitsmappe mit C++ passwortschützen oder entsperren
linktitle: Arbeitsmappe mit Kennwort schützen oder entschützen
type: docs
weight: 10
url: /de/cpp/password-protect-or-unprotect-the-shared-workbook/
description: Lernen Sie, wie Sie eine freigegebene Arbeitsmappe mit {Aspose.Cells for C++} passwortschützen oder entsperren.
---

## **Mögliche Verwendungsszenarien**

Sie können die freigegebene Arbeitsmappe mit Microsoft Excel schützen oder den Schutz aufheben, wie im folgenden Screenshot gezeigt. Aspose.Cells unterstützt diese Funktion auch mit den Methoden [**Workbook::ProtectSharedWorkbook()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/protectsharedworkbook/) und [**Workbook::UnprotectSharedWorkbook()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/unprotectsharedworkbook/).

![todo:image_alt_text](password-protect-or-unprotect-the-shared-workbook_1.png)

## **Freigegebenes Arbeitsblatt passwortgeschützt oder nicht passwortgeschützt machen**

Der folgende Beispielcode erstellt eine Arbeitsmappe, schützt sie und ermöglicht die Freigabe und speichert sie als [Ausgabedatei Excel](55541777.xlsx). Im Screenshot ist zu sehen, dass beim Versuch, den Schutz aufzuheben, Microsoft Excel Sie auffordert, das Passwort zum Aufheben des Schutzes einzugeben.

![todo:image_alt_text](password-protect-or-unprotect-the-shared-workbook_2.png)

## **Beispielcode**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create empty Excel file
    Workbook wb;

    // Protect the Shared Workbook with Password
    wb.ProtectSharedWorkbook(u"1234");

    // Uncomment this line to Unprotect the Shared Workbook
    // wb.UnprotectSharedWorkbook(u"1234");

    // Save the output Excel file
    wb.Save(u"outputProtectSharedWorkbook.xlsx");

    std::cout << "Shared workbook protection applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
