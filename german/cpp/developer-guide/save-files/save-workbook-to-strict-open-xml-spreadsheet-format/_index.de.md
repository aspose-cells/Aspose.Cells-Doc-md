---
title: Arbeitsmappe im Strict Open XML Spreadsheet Format mit C++ speichern
linktitle: Arbeitsmappe im strengen Open XML Tabellenformat speichern
type: docs
weight: 150
url: /de/cpp/save-workbook-to-strict-open-xml-spreadsheet-format/
description: Lernen Sie, wie Sie eine Arbeitsmappe im Strict Open XML Spreadsheet Format mit Aspose.Cells for C++ speichern.
---

## **Mögliche Verwendungsszenarien**

Aspose.Cells ermöglicht es Ihnen, die Arbeitsmappe im *Strict Open XML Spreadsheet*-Format zu speichern. Dafür bietet es die [**GetCompliance()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getcompliance/)-Eigenschaft. Wenn Sie ihren Wert auf [**OoxmlCompliance::Iso29500_2008_Strict**](https://reference.aspose.com/cells/cpp/aspose.cells/ooxmlcompliance/) setzen, wird die Ausgabedatei im Strict Open XML Spreadsheet-Format gespeichert.

## **Arbeitsmappe im Strict Open XML-Tabellenkalkulationsformat speichern**

Das folgende Beispiel erstellt eine Arbeitsmappe, setzt die [**GetCompliance()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getcompliance/)-Eigenschaft auf [**OoxmlCompliance::Iso29500_2008_Strict**](https://reference.aspose.com/cells/cpp/aspose.cells/ooxmlcompliance/) und speichert sie als [Ausgabedatei](67338272.xlsx). Wenn Sie die Ausgabedatei in Microsoft Excel öffnen und den „Speichern unter“-Dialog öffnen, sehen Sie das Format als *Strict Open XML Spreadsheet*, wie in diesem Screenshot gezeigt.

![todo:image_alt_text](save-workbook-to-strict-open-xml-spreadsheet-format_1.png)

## **Beispielcode**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook
    Workbook wb;

    // Specify - Strict Open XML Spreadsheet - Format
    wb.GetSettings().SetCompliance(OoxmlCompliance::Iso29500_2008_Strict);

    // Add message in cell B4 of first worksheet
    Cell b4 = wb.GetWorksheets().Get(0).GetCells().Get(u"B4");
    b4.PutValue(u"This Excel file has Strict Open XML Spreadsheet format.");

    // Save to output Excel file
    wb.Save(u"outputSaveWorkbookToStrictOpenXMLSpreadsheetFormat.xlsx", SaveFormat::Xlsx);

    std::cout << "Workbook saved successfully with Strict Open XML Spreadsheet format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
