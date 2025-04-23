---
title: Excel zu JSON Konvertierung mit C++
linktitle: Excel in JSON konvertieren
type: docs
weight: 300
url: /de/cpp/convert-excel-to-json/
description: Erfahren Sie, wie Sie mit Aspose.Cells und C++ Excel Dateien in JSON konvertieren.
keywords: Exportieren von Arbeitsmappe nach JSON ohne Office 2013, Office 2016, Office 2019 und Office 365
---

{{% alert color="primary" %}}

Aspose.Cells unterstützt die Umwandlung einer Arbeitsmappe in eine JSON (JavaScript Object Notation)-Datei.

{{% /alert %}}

## **Excel-Arbeitsmappe in JSON konvertieren**

Sie müssen sich keine Sorgen machen, wie man eine Excel-Arbeitsmappe in JSON konvertiert, denn die Aspose.Cells for C++-Bibliothek hat die beste Lösung. Die Aspose.Cells API bietet Unterstützung für die Konvertierung von Tabellenkalkulationen in JSON-Format. Um die Arbeitsmappe in JSON zu exportieren, übergeben Sie [**SaveFormat.Json**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) als zweiten Parameter der [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)-Methode. Sie können auch die Klasse [**JsonSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/jsonsaveoptions/) verwenden, um zusätzliche Einstellungen für den Export des Arbeitsblatts nach JSON festzulegen.

Das folgende Codebeispiel zeigt den Export einer Excel-Arbeitsmappe nach JSON. Bitte sehen Sie sich den Code an, um die [Quelldatei](sample.xlsx) zu konvertieren, sowie die durch den Code generierte JSON-Datei zur Referenz.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load your source workbook
    U16String inputFilePath(u"sample.xlsx");
    Workbook workbook(inputFilePath);

    // Convert the workbook to JSON file.
    U16String outputFilePath(u"sample_out.json");
    workbook.Save(outputFilePath, SaveFormat::Json);

    std::cout << "Workbook converted to JSON successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Das folgende Codebeispiel verwendet die JsonSaveOptions-Klasse, um zusätzliche Einstellungen festzulegen, und demonstriert den Export einer Excel-Arbeitsmappe nach JSON. Bitte sehen Sie sich den Code an, um die [Quelle Datei](sample.xlsx) in die durch den Code generierte JSON-Datei zu konvertieren.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create an options of saving the file.
    JsonSaveOptions options;

    // Set the exporting range.
    options.SetExportArea(CellArea::CreateCellArea(u"B1", u"C4"));

    // Load your source workbook
    Workbook workbook(u"sample.xlsx");

    // Convert the workbook to json file.
    workbook.Save(u"sample_out.json", options);

    std::cout << "Workbook successfully converted to JSON!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

