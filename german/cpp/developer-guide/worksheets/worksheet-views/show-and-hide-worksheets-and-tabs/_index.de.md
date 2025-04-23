---
title: Arbeitsblätter und Registerkarten mit C++ anzeigen und ausblenden
linktitle: Arbeitsblätter und Registerkarten anzeigen und ausblenden
type: docs
weight: 10
url: /de/cpp/show-and-hide-worksheets-and-tabs/
description: Dieser Artikel bietet Beispielcode für die Verwendung der C++ API oder Bibliothek, um ein Excel Arbeitsblatt programmatisch anzuzeigen und auszublenden. Außerdem wird gezeigt, wie man Excel Workbook Registerkarten ein und ausblendet.
---

{{% alert color="primary" %}}

Aspose.Cells ermöglicht es dem Benutzer, Elemente einer Arbeitsmappe einschließlich Arbeitsblätter und Registerkarten anzuzeigen und auszublenden.

{{% /alert %}}

## **Arbeitsblatt anzeigen und ausblenden**

Eine Excel-Datei kann ein oder mehrere Arbeitsblätter enthalten. Immer wenn wir eine Excel-Datei erstellen, fügen wir Arbeitsblätter hinzu, in denen wir arbeiten. Jedes Arbeitsblatt in einer Excel-Datei ist unabhängig von anderen Arbeitsblättern und verfügt über eigene Daten- und Formatierungseinstellungen usw. Manchmal benötigen Entwickler möglicherweise, dass einige Arbeitsblätter in der Excel-Datei ausgeblendet und andere sichtbar sind, um ihre eigenen Interessen zu wahren. **Aspose.Cells** ermöglicht Entwicklern daher, die Sichtbarkeit der Arbeitsblätter in ihren Excel-Dateien zu steuern.

Aspose.Cells stellt eine Klasse, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), bereit, die eine Excel-Datei repräsentiert. Die [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) Klasse enthält eine [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) Sammlung, die Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch die [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) Klasse repräsentiert. Die [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) Klasse bietet eine Vielzahl von Eigenschaften und Methoden zur Verwaltung von Arbeitsblättern. Um die Sichtbarkeit eines Arbeitsblatts zu steuern, verwenden Sie die Eigenschaft [**IsVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isvisible/) der [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) Klasse. [**IsVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isvisible/) ist eine boolesche Eigenschaft, die nur einen **true** oder **false** Wert speichern kann.

### **Ein Arbeitsblatt sichtbar machen**

Machen Sie ein Arbeitsblatt sichtbar, indem Sie die Eigenschaft [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) der [**IsVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isvisible/) Klasse auf **true** setzen.

### **Arbeitsblatt ausblenden**

Verstecken Sie ein Arbeitsblatt, indem Sie die Eigenschaft [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) der [**IsVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isvisible/) Klasse auf **false** setzen.

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
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook from file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Hide the first worksheet of the Excel file
    worksheet.SetIsVisible(false);

    // Save the modified Excel file in default (Excel 2003) format
    U16String outputFilePath = outDir + u"output.out.xls";
    workbook.Save(outputFilePath);

    std::cout << "Worksheet hidden and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Registerkarten anzeigen und ausblenden**

Wenn Sie am unteren Rand einer Microsoft Excel-Datei genau hinsehen, sehen Sie eine Reihe von Steuerelementen. Dazu gehören:

- Registerkarten.
- Registerkarten-Scrolltasten.

Registerkarten stellen die Arbeitsblätter in der Excel-Datei dar. Klicken Sie auf eine beliebige Registerkarte, um zu diesem Arbeitsblatt zu wechseln. Je mehr Arbeitsblätter in der Arbeitsmappe sind, desto mehr Registerkarten gibt es. Wenn die Excel-Datei eine gute Anzahl von Arbeitsblättern hat, benötigen Sie Tasten, um zwischen ihnen zu navigieren. Daher bietet Microsoft Excel Registerkarten-Scrolltasten zum Scrollen durch die Registerkarten an.

Mit Aspose.Cells können Entwickler die Sichtbarkeit von Registerkarten und Bildlaufschaltflächen für Registerkarten in Excel-Dateien steuern.

Aspose.Cells stellt eine Klasse, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), bereit, die eine Excel-Datei repräsentiert. Die [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) Klasse bietet eine Vielzahl von Eigenschaften und Methoden zur Verwaltung einer Excel-Datei. Um die Sichtbarkeit von Registerkarten in einer Excel-Datei zu steuern, können Entwickler die Eigenschaft [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) der [**WorkbookSettings.GetShowTabs()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshowtabs/) Klasse verwenden. [**WorkbookSettings.GetShowTabs()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshowtabs/) ist eine boolesche Eigenschaft, die nur einen **true** oder **false** Wert speichern kann.

### **Sichtbarkeit von Registerkarten**

Machen Sie Registerkarten sichtbar, indem Sie die Eigenschaft [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) der [**WorkbookSettings.GetShowTabs()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshowtabs/) Klasse auf **true** setzen.

### **Registerkarten ausblenden**

Verstecken Sie Registerkarten in einer Excel-Datei, indem Sie die Eigenschaft [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) der [**WorkbookSettings.GetShowTabs()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshowtabs/) Klasse auf **false** setzen.

Nachfolgend finden Sie ein vollständiges Beispiel, das eine Excel-Datei (book1.xls) öffnet, ihre Registerkarten ausblendet und die modifizierte Datei als Output.xls speichert. Nach der Codeausführung werden Sie feststellen, dass die Registerkarten der Arbeitsmappe ausgeblendet sind.

```c++
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
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get workbook settings
    WorkbookSettings settings = workbook.GetSettings();

    // Hiding the tabs of the Excel file
    settings.SetShowTabs(false);

    // Shows the tabs of the Excel file
    // settings.SetShowTabs(true);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Excel file modified successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Steuerung der Registerkartenleistenbreite**

```c++
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
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get workbook settings
    WorkbookSettings settings = workbook.GetSettings();

    // Show tabs in the Excel file
    settings.SetShowTabs(true);

    // Adjust the sheet tab bar width
    settings.SetSheetTabBarWidth(800);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Excel file modified successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
