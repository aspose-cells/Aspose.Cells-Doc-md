---
title: Speicherverbrauch bei der Arbeit mit großen Dateien und umfangreichen Datensätzen mit C++ optimieren
linktitle: Speicher optimieren
type: docs
weight: 180
url: /de/cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
description: Erfahren Sie, wie Sie den Speicherverbrauch bei der Arbeit mit großen Excel Dateien mit Aspose.Cells und C++ optimieren.
---

{{% alert color="primary" %}}

Beim Erstellen eines Arbeitsblatts mit großen Datensätzen oder beim Lesen einer großen Microsoft Excel-Datei ist die Gesamtmenge des RAMs, die der Prozess benötigt, immer ein Anliegen. Es gibt Maßnahmen, die ergriffen werden können, um mit der Herausforderung umzugehen. Aspose.Cells bietet einige relevante Optionen und API-Aufrufe, um den Speicherverbrauch zu verringern, zu reduzieren und zu optimieren. Außerdem kann dies helfen, den Prozess effizienter und schneller zu machen.

Verwenden Sie die [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/cpp/aspose.cells/memorysetting/)-Option, um den Speicherverbrauch für Zelleninhalte zu optimieren und die Gesamtspeicherkosten zu senken. Beim Erstellen eines großen Datensatzes für Zellen können Sie im Vergleich zur Verwendung der Standardeinstellung ([**MemorySetting.Normal**](https://reference.aspose.com/cells/cpp/aspose.cells/memorysetting/)) eine bestimmte Menge Speicher einsparen.

{{% /alert %}}

## **Speicheroptimierung**

### **Lesen großer Excel-Dateien**

Das folgende Beispiel zeigt, wie eine große Microsoft Excel-Datei im optimierten Modus gelesen wird.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Specify the LoadOptions
    LoadOptions opt;

    // Set the memory preferences
    opt.SetMemorySetting(MemorySetting::MemoryPreference);

    // Instantiate the Workbook
    // Load the Big Excel file having large Data set in it
    Workbook wb(srcDir + u"Book1.xlsx", opt);

    std::cout << "Workbook loaded successfully with memory preference setting!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Schreiben großer Excel-Dateien**

Das folgende Beispiel zeigt, wie Sie ein großes Datenset im optimierten Modus in ein Arbeitsblatt schreiben.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook
    Workbook wb;

    // Set the memory preferences
    // Note: This setting cannot take effect for the existing worksheets that are created before using the below line of code
    wb.GetSettings().SetMemorySetting(MemorySetting::MemoryPreference);

    // Note: The memory settings also would not work for the default sheet i.e., "Sheet1" etc. automatically created by the Workbook

    // To change the memory setting of existing sheets, please change memory setting for them manually:
    Cells cells = wb.GetWorksheets().Get(0).GetCells();
    cells.SetMemorySetting(MemorySetting::MemoryPreference);

    // Input large dataset into the cells of the worksheet.
    // Your code goes here.
    // .........

    // Get cells of the newly created Worksheet "Sheet2" whose memory setting is same with the one defined in WorkbookSettings:
    cells = wb.GetWorksheets().Add(u"Sheet2").GetCells();

    // Input large dataset into the cells of the worksheet.
    // Your code goes here.
    // .........

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Vorsicht**

Die Standardoption, [**MemorySetting.Normal**](https://reference.aspose.com/cells/cpp/aspose.cells/memorysetting/) wird für alle Versionen angewendet. In einigen Situationen, wie dem Erstellen einer Arbeitsmappe mit einem großen Datensatz für Zellen, kann die Option [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/cpp/aspose.cells/memorysetting/) den Speicherverbrauch optimieren und die Speicherkosten für die Anwendung verringern. Diese Option kann jedoch in einigen speziellen Fällen die Leistung beeinträchtigen.

1. **Zufälliger und wiederholter Zugriff auf Zellen**: Die effizienteste Sequenz für den Zugriff auf die Zellensammlung ist Zelle für Zelle in einer Zeile und dann Zeile für Zeile. Insbesondere wenn Sie Zeilen/Zellen über den Enumerator, der von [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/), [**RowCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/rowcollection/) und [**Row**](https://reference.aspose.com/cells/cpp/aspose.cells/row/) erworben wurde, abrufen, wird die Leistung mit [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/cpp/aspose.cells/memorysetting/) maximiert.
1. **Einfügen & Löschen von Zellen & Zeilen**: Bitte beachten Sie, dass bei vielen Einfüge/Löschvorgängen für Zellen/Zeilen die Leistungseinbuße im *MemoryPreference*-Modus im Vergleich zum *Normal*-Modus spürbar sein wird.
1. **Arbeiten mit verschiedenen Zelltypen**: Wenn die meisten Zellen Zeichenfolgen oder Formeln enthalten, wird der Speicherverbrauch wie im *Normal*-Modus sein, aber wenn es viele leere Zellen gibt oder Zellwerte numerisch, boolesch usw. sind, wird die Option [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/cpp/aspose.cells/memorysetting/) eine bessere Leistung bieten.
{{< app/cells/assistant language="cpp" >}}
