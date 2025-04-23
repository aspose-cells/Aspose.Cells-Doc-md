---
title: Excel zu HTML  Verwendung der PresentationPreference Option für ein besseres Layout mit C++
linktitle: Excel zu HTML  Verwenden Sie die PresentationPreference Option für ein besseres Layout
type: docs
weight: 220
url: /de/cpp/excel-to-html-use-presentationpreference-option-for-better-layout/
description: Lernen, wie man beim Speichern von Excel Dateien als HTML mit C++ ein besseres Layout rendert.
---

{{% alert color="primary" %}} 

Aspose.Cells bietet eine nützliche Eigenschaft HtmlSaveOptions.PresentationPreference für Entwickler, die beim Speichern einer Microsoft Excel-Datei im HTML- oder MHT-Format eine bessere Layout darstellung benötigen. Der Standardwert der Eigenschaft ist false. Wir empfehlen, diese Eigenschaft auf true zu setzen, um eine attraktivere Präsentation von Excel-Berichten zu erhalten.

{{% /alert %}} 

Bitte beachten Sie den unten stehenden Beispielscode, der zeigt, wie man eine HTML-Datei aus einem Excel-Bericht mit Präsentationspräferenz erstellt.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/HtmlSaveOptions.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Instantiate the Workbook and load an Excel file
    Workbook workbook(inputFilePath);

    // Create HtmlSaveOptions object
    HtmlSaveOptions options;

    // Set the Presentation preference option
    options.SetPresentationPreference(true);

    // Save the Excel file to HTML with specified option
    U16String outputFilePath = srcDir + u"outPresentationlayout1.out.html";
    workbook.Save(outputFilePath, options);

    std::cout << "Excel file saved as HTML successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
