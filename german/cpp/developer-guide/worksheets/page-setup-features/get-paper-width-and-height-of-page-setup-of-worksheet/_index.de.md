---
title: Ermitteln der Breite und Höhe des Seiten Setups des Arbeitsblatts in C++
linktitle: Ermitteln der Papierbreite und höhe im Seiten Setup
type: docs
weight: 50
url: /de/cpp/get-paper-width-and-height-of-page-setup-of-worksheet/
description: Erfahren Sie, wie Sie die Papierbreite und höhe des Seiten Setups eines Excel Arbeitsblatts programmatisch mit C++ Code mithilfe der Aspose.Cells for C++ API erhalten.
keywords: Excel Seiten Setup Papierbreite c++, Excel Seiten Setup Papierhöhe c++
---

## **Mögliche Verwendungsszenarien**

Manchmal müssen Sie die Breite und Höhe der Papiergröße kennen, wie sie im Seiten-Setup des Arbeitsblatts eingestellt ist. Verwenden Sie dazu die [**GetPaperWidth()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getpaperwidth/)- und [**GetPaperHeight()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getpaperheight/)-Methoden.

## **Papierbreite und -höhe des Seitenlayouts des Arbeitsblatts abrufen**

Der folgende Beispielcode erklärt die Verwendung der [**GetPaperWidth()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getpaperwidth/)- und [**GetPaperHeight()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getpaperheight/)-Methoden. Es ändert zuerst die Papiergröße auf *A2* und ermittelt dann die Breite und Höhe des Papiers, anschließend ändert es die Papiergröße auf *A3*, *A4*, *Brief* und ermittelt jeweils die Breite und Höhe des Papiers.

### **Beispielcode**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook class
    Workbook book;

    // Access first worksheet
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Set paper size to A2 and print paper width and height in inches
    sheet.GetPageSetup().SetPaperSize(PaperSizeType::PaperA2);
    cout << "PaperA2: " << sheet.GetPageSetup().GetPaperWidth() << "x" << sheet.GetPageSetup().GetPaperHeight() << endl;

    // Set paper size to A3 and print paper width and height in inches
    sheet.GetPageSetup().SetPaperSize(PaperSizeType::PaperA3);
    cout << "PaperA3: " << sheet.GetPageSetup().GetPaperWidth() << "x" << sheet.GetPageSetup().GetPaperHeight() << endl;

    // Set paper size to A4 and print paper width and height in inches
    sheet.GetPageSetup().SetPaperSize(PaperSizeType::PaperA4);
    cout << "PaperA4: " << sheet.GetPageSetup().GetPaperWidth() << "x" << sheet.GetPageSetup().GetPaperHeight() << endl;

    // Set paper size to Letter and print paper width and height in inches
    sheet.GetPageSetup().SetPaperSize(PaperSizeType::PaperLetter);
    cout << "PaperLetter: " << sheet.GetPageSetup().GetPaperWidth() << "x" << sheet.GetPageSetup().GetPaperHeight() << endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Konsolenausgabe**

Hier ist die Konsolenausgabe des obigen Beispielcodes.

{{< highlight java >}}

PaperA2: 16.54x23.39

PaperA3: 11.69x16.54

PaperA4: 8.27x11.69

PaperLetter: 8.5x11

{{< /highlight >}}
