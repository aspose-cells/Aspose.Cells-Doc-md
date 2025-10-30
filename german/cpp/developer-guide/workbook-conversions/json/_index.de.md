---
title: Arbeitsmappe mit C++ in JSON konvertieren
linktitle: Arbeitsmappe in JSON konvertieren
type: docs
weight: 300
url: /de/cpp/convert-workbook-to-json/
description: Erfahren Sie, wie Sie Excel Arbeitsmappen mit Aspose.Cells for C++ in JSON Format umwandeln.
---

{{% alert color="primary" %}}

Aspose.Cells unterstützt die Konvertierung einer Arbeitsmappe in eine JSON (JavaScript Object Notation)-Datei.

{{% /alert %}}

## **Excel-Arbeitsmappe in JSON konvertieren**

Das Aspose.Cells API unterstützt die Konvertierung von Tabellenblättern in JSON-Format. Um die Arbeitsmappe in JSON zu exportieren, übergeben Sie [**SaveFormat::Json**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) als zweiten Parameter der [**Workbook::Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)-Methode. Sie können auch die [**JsonSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/jsonsaveoptions/)-Klasse verwenden, um zusätzliche Einstellungen für den Export des Arbeitsblatts in JSON anzugeben.

Das folgende Codebeispiel zeigt, wie das aktive Arbeitsblatt mit der [**SaveFormat::Json**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/)-Aufzählungsmitglied in JSON exportiert wird. Bitte beachten Sie den Code zum Konvertieren der [Quelldatei](book1.xlsx) in die [Ausgabe-JSON-Datei](book1.json), die vom Code generiert wurde.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Save the workbook as JSON
    U16String outputFilePath = srcDir + u"book1.json";
    workbook.Save(outputFilePath);

    std::cout << "Workbook converted to JSON successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Erweiterte Themen**
- [Konvertieren von CSV in JSON](/cells/de/cpp/convert-csv-to-json/)
- [Excel nach JSON konvertieren](/cells/de/cpp/convert-excel-to-json/)
- [JSON in CSV konvertieren](/cells/de/cpp/convert-json-to-csv/)
- [JSON in Excel konvertieren](/cells/de/cpp/convert-json-to-excel/)
{{< app/cells/assistant language="cpp" >}}
