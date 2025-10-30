---
title: Festlegen von signifikanten Ziffern, die in Excel Dateien mit C++ gespeichert werden sollen
linktitle: Festlegung der signifikanten Ziffern
type: docs
weight: 30
url: /de/cpp/specifying-significant-digits-to-be-stored-in-excel-file/
description: Lernen Sie, wie Sie mit Aspose.Cells für C++ die signifikanten Ziffern festlegen, die in Excel Dateien gespeichert werden sollen.
---

## **Mögliche Verwendungsszenarien**

Standardmäßig speichert Aspose.Cells 17 signifikante Ziffern von Double-Werten in der Excel-Datei, im Gegensatz zu MS-Excel, das nur 15 signifikante Ziffern speichert. Sie können dieses Standardverhalten von 17 auf 15 signifikante Ziffern mit der [**GetSignificantDigits()**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/getsignificantdigits/) Eigenschaft ändern.

## **Angabe von signifikanten Ziffern, die in der Excel-Datei gespeichert werden sollen**

Der folgende Beispielcode erzwingt, dass Aspose.Cells beim Speichern von Double-Werten in der Excel-Datei 15 signifikante Ziffern verwendet. Überprüfen Sie die [Ausgabe-Excel-Datei](22774105.xlsx). Benennen Sie die Erweiterung in .zip um und entpacken Sie sie, dann sehen Sie, dass nur 15 signifikante Ziffern in der Excel-Datei gespeichert sind. Das folgende Screenshot zeigt die Wirkung der [**GetSignificantDigits()**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/getsignificantdigits/) Eigenschaft auf die Ausgabedatei.

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)

## **Beispielcode**

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

    // By default, Aspose.Cells stores 17 significant digits unlike
    // MS-Excel which stores only 15 significant digits
    CellsHelper::SetSignificantDigits(15);

    // Create workbook
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell A1
    Cell c = worksheet.GetCells().Get(u"A1");

    // Put double value, only 15 significant digits as specified by
    // CellsHelper.SignificantDigits above will be stored in excel file just like MS-Excel does
    c.PutValue(1234567890.123451711);

    // Save the workbook
    workbook.Save(outDir + u"out_SignificantDigits.xlsx");

    std::cout << "Workbook saved successfully with significant digits set to 15!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
