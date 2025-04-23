---
title: Beim Setzen der Style.Custom Eigenschaft den benutzerdefinierten Zahlenformat bei C++ überprüfen
description: Aspose.Cells ist eine C++ Bibliothek zur Arbeit mit Tabellenkalkulationsdateien, die das Überprüfen benutzerdefinierter Zahlenformate beim Styling unterstützt. Dieser Artikel zeigt, wie man die Aspose.Cells Bibliothek verwendet, um benutzerdefinierte Zahlenformate zu überprüfen und sicherzustellen, dass das Styling korrekt ist.
keywords: Aspose.Cells, C++ Bibliotheken, Tabellenkalkulationen, Styling, benutzerdefiniertes Zahlenformat, Überprüfung, Validierung
type: docs
weight: 170
url: /de/cpp/check-custom-number-format-when-setting-style-custom-property/
---

## **Mögliche Verwendungsszenarien**

Wenn Sie eine ungültige benutzerdefinierte Zahlenformatierung an die [**Style.GetCustom()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getcustom/)-Eigenschaft zuweisen, wirft Aspose.Cells keine Ausnahme. Wenn Sie jedoch möchten, dass Aspose.Cells überprüft, ob das zugewiesene benutzerdefinierte Zahlenformat gültig ist, setzen Sie bitte die [**Workbook.GetCheckCustomNumberFormat()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getcheckcustomnumberformat/)-Eigenschaft auf **true**.

## **Benutzerdefiniertes Zahlenformat überprüfen beim Festlegen der Style.Custom-Eigenschaft**

Das folgende Beispiel weist der [**Style.GetCustom()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getcustom/)-Eigenschaft ein ungültiges benutzerdefiniertes Zahlenformat zu. Da wir bereits die [**Workbook.GetCheckCustomNumberFormat()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getcheckcustomnumberformat/)-Eigenschaft auf **true** gesetzt haben, wird eine Ausnahme ausgelöst, z.B. Ungültiges Zahlenformat. Lesen Sie die Kommentare im Code für weitere Hinweise.

## **Beispielcode**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create an instance of Workbook class
    Workbook book;

    // Setting this property to true will make Aspose.Cells to throw exception
    // when invalid custom number format is assigned to Style.Custom property
    book.GetSettings().SetCheckCustomNumberFormat(true);

    // Access first worksheet
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Access cell A1 and put some number to it
    Cell cell = sheet.GetCells().Get(u"A1");
    cell.PutValue(2347);

    // Access cell's style and set its Style.Custom property
    Style style = cell.GetStyle();

    // This line will throw exception if Workbook.Settings.CheckCustomNumberFormat is set to true
    style.SetCustom(u"ggg @ fff"); // Invalid custom number format

    std::cout << "Custom number format set." << std::endl;

    Aspose::Cells::Cleanup();
}
```
