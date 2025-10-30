---
title: Tab Farbe der Tabelle mit C++ festlegen
linktitle: Registerkartenfarbe des Arbeitsblatts festlegen
type: docs
weight: 120
url: /de/cpp/set-worksheet-tab-color/
description: Dieses Beispiel zeigt Code, der erklärt, wie man die Tab Farbe in Excel mit der C++ API oder Bibliothek programmatisch setzt.
keywords: Tab Farbe in Excel mit C++ setzen, Code zum Festlegen der Tab Farbe in Excel mit C++
---

{{% alert color="primary" %}}

Aspose.Cells ermöglicht es Ihnen, die Farbe einzelner Arbeitsblattregisterkarten zu ändern, um sie von anderen hervorzuheben. Zum Beispiel können Sie Ausgaben rot, Verkäufe grün, Vermögenswerte blau usw. machen.

{{% /alert %}}

## **Verwenden von Microsoft Excel zur Festlegung der Registerkartenfarbe des Arbeitsblatts**
1. Klicken Sie mit der rechten Maustaste auf eine Registerkarte im Registerblatt am unteren Rand des aktuellen Arbeitsblatts.
1. Wählen Sie **Registerkartenfarbe**.
1. Wählen Sie eine Farbe aus der Palette.
1. Klicken Sie auf **OK**.

## **Festlegen der Registerkartenfarbe mit Aspose.Cells**
Der folgende Beispielscode zeigt, wie Sie die Registerkartenfarbe mit Aspose.Cells festlegen können.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"worksheettabcolor.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the first worksheet in the book
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set the tab color to red
    worksheet.SetTabColor(Color::Red());

    // Save the Excel file
    workbook.Save(outputFilePath);

    std::cout << "Worksheet tab color set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
