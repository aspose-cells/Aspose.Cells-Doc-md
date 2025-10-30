---
title: Ränder mit C++ festlegen
linktitle: Seitenränder einrichten
type: docs
weight: 20
url: /de/cpp/setting-margins/
description: Erfahren Sie, wie Sie die Seitenränder eines Excel Arbeitsblatts mit C++ festlegen. Dieser Leitfaden deckt das Einstellen der Seitenränder, das Zentrieren des Inhalts und die Konfiguration der Kopf und Fußzeilenränder programmgesteuert mit Aspose.Cells for C++ ab.
keywords: Stellen Sie den Rand eines Excel Arbeitsblatts auf zentriert C++, setzen Sie Kopf und Fußzeilenränder C++
---

{{% alert color="primary" %}}

Aspose.Cells unterstützt vollständig die Seiteneinrichtungsoptionen von Microsoft Excel. Entwickler müssen möglicherweise die Seiteneinrichtungseinstellungen für Arbeitsblätter konfigurieren, um den Druckprozess zu steuern. Dieses Thema erläutert, wie Sie Aspose.Cells verwenden, um die Seitennränder zu konfigurieren.

{{% /alert %}}

## **Ränder einstellen**

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), die eine Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) enthält die Sammlung [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/), die Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) dargestellt.

Die Klasse [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) bietet die Eigenschaft [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/), mit der die Seiteneinrichtung für ein Arbeitsblatt festgelegt wird. Das Attribut [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) ist ein Objekt der Klasse [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/), das Entwicklern ermöglicht, unterschiedliche Seitenanordnungen für ein gedrucktes Arbeitsblatt zu konfigurieren. Die Klasse [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) stellt verschiedene Eigenschaften und Methoden bereit, um die Seiteneinrichtung zu konfigurieren.

### **Seitenränder**

Setzen Sie Seitenränder (links, rechts, oben, unten) mit Mitgliedern der Klasse [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/). Einige der Methoden, die verwendet werden, um Seitenränder festzulegen, sind unten aufgeführt:

- [**GetLeftMargin()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getleftmargin/)
- [**GetRightMargin()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getrightmargin/)
- [**GetTopMargin()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/gettopmargin/)
- [**GetBottomMargin()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getbottommargin/)

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

    // Create a workbook object
    Workbook workbook;

    // Get the worksheets in the workbook
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Get the first (default) worksheet
    Worksheet worksheet = worksheets.Get(0);

    // Get the pagesetup object
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Set bottom, left, right, and top page margins
    pageSetup.SetBottomMargin(2);
    pageSetup.SetLeftMargin(1);
    pageSetup.SetRightMargin(1);
    pageSetup.SetTopMargin(3);

    // Save the Workbook
    workbook.Save(outDir + u"SetMargins_out.xls");

    std::cout << "Margins set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **In der Lage zu zentrieren etwas auf einer Seite horizontal und vertikal. Die Klasse {0} hat Mitglieder zu diesem Zweck: {1} und {2}.**

Es ist möglich, etwas horizontal und vertikal auf einer Seite zu zentrieren. Dafür gibt es nützliche Mitglieder der Klassen [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/), [**GetCenterHorizontally()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getcenterhorizontally/) und [**GetCenterVertically()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getcentervertically/).

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

    // Create a workbook object
    Workbook workbook;

    // Get the worksheets in the workbook
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Get the first (default) worksheet
    Worksheet worksheet = worksheets.Get(0);

    // Get the pagesetup object
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Specify Center on page Horizontally and Vertically
    pageSetup.SetCenterHorizontally(true);
    pageSetup.SetCenterVertically(true);

    // Save the Workbook
    workbook.Save(outDir + u"CenterOnPage_out.xls");

    std::cout << "Workbook saved successfully with centered page setup!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Kopf- und Fußzeilen Ränder**

Setzen Sie Kopf- und Fußzeilenränder mit den Mitgliedern der Klasse [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/), wie [**GetHeaderMargin()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getheadermargin/) und [**GetFooterMargin()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getfootermargin/).

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

    // Create a workbook object
    Workbook workbook;

    // Get the worksheets in the workbook
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Get the first (default) worksheet
    Worksheet worksheet = worksheets.Get(0);

    // Get the pagesetup object
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Specify Header / Footer margins
    pageSetup.SetHeaderMargin(2);
    pageSetup.SetFooterMargin(2);

    // Save the Workbook
    workbook.Save(outDir + u"CenterOnPage_out.xls");

    std::cout << "Workbook saved successfully with centered header and footer margins!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
