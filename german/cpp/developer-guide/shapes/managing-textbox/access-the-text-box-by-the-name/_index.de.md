---
title: Zugriff auf das Textfeld nach Namen mit C++
linktitle: Greifen Sie auf die Textbox über den Namen zu
type: docs
weight: 230
url: /de/cpp/access-the-text-box-by-the-name/
description: Erfahren Sie, wie Sie ein Textfeld anhand seines Namens mit Aspose.Cells for C++ zugreifen.
---

##Greifen Sie über den Namen auf die Textbox zu

 Früher wurden Textfelder anhand ihres Index aus der [**Worksheet.GetTextBoxes()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gettextboxes/)-Sammlung zugegriffen, jetzt können Sie auch auf das Textfeld nach Name aus dieser Sammlung zugreifen. Dies ist eine bequeme und schnelle Methode, um auf Ihr Textfeld zuzugreifen, wenn Sie bereits seinen Namen kennen.

Das folgende Beispiel erstellt zunächst ein Textfeld, weist ihm Text und einen Namen zu. Im Anschluss greifen wir über den Namen auf dasselbe Textfeld zu und geben dessen Text aus.

### C++-Code zum Zugreifen auf das Textfeld nach Namen

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Create an object of the Workbook class
    Workbook workbook;

    // Access first worksheet from the collection
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Add the TextBox to the worksheet
    int idx = sheet.GetTextBoxes().Add(10, 10, 10, 10);

    // Access newly created TextBox using its index & name it
    TextBox tb1 = sheet.GetTextBoxes().Get(idx);
    tb1.SetName(u"MyTextBox");

    // Set text for the TextBox
    tb1.SetText(u"This is MyTextBox");

    // Access the same TextBox via its name
    TextBox tb2 = sheet.GetTextBoxes().Get(u"MyTextBox");

    // Display the text of the TextBox accessed via name
    std::cout << tb2.GetText().ToUtf8() << std::endl;

    std::cout << "Press any key to continue..." << std::endl;
    std::cin.get();

    Aspose::Cells::Cleanup();
}
```

### Von der Beispiellösung generierte Konsolenausgabe

Hier ist die Konsolenausgabe des obigen Beispielcodes.

{{< highlight java >}}

This is MyTextBox

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
