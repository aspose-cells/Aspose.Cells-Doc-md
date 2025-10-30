---
title: Erweiterte Schutzeinstellungen seit Excel XP mit C++
linktitle: Erweiterte Schutzeinstellungen seit Excel XP
type: docs
weight: 30
url: /de/cpp/advanced-protection-settings-since-excel-xp/
description: Erfahren Sie, wie man erweiterte Schutzeinstellungen in Excel Dateien mit Aspose.Cells und C++ anwendet.
---

{{% alert color="primary" %}}

Seit der Veröffentlichung von Excel 2002 oder XP hat Microsoft viele erweiterte Schutzeinstellungen hinzugefügt.

{{% /alert %}}

## **Einführung**

Diese Schutzeinstellungen beschränken oder erlauben Benutzern:

- Zeilen oder Spalten löschen.
- Inhalte, Objekte oder Szenarien bearbeiten.
- Zellen, Reihen oder Spalten formatieren.
- Zeilen, Spalten oder Hyperlinks einfügen.
- Gesperrte oder ungesperrte Zellen auswählen.
- Pivot-Tabellen verwenden und vieles mehr.

Aspose.Cells unterstützt alle erweiterten Schutzeinstellungen, die von Excel XP oder späteren Versionen angeboten werden.

### **Erweiterte Schutzeinstellungen mit Excel XP und späteren Versionen verwenden**

Um die Schutzeinstellungen in Excel XP anzuzeigen:

1. Wählen Sie im **Extras**-Menü **Schutz** und danach **Arbeitsblatt schützen** aus. Es wird ein Dialogfeld angezeigt.

Um die verfügbaren Schutzeinstellungen in Excel 2016 anzuzeigen:

1. Wählen Sie im **Datei**-Menü **Arbeitsmappe schützen** und danach **Aktuelles Blatt schützen** aus.
1. Wählen Sie **Arbeitsblatt schützen** im **Überprüfen**-Menü aus.

Die oben genannten Schritte zeigen ein Dialogfeld, in dem Sie Arbeitsblattfunktionen zulassen, einschränken oder ein Passwort für das Arbeitsblatt festlegen können.

### **Erweiterte Schutzeinstellungen mit Aspose.Cells verwenden**

Aspose.Cells unterstützt alle erweiterten Schutzeinstellungen.

Aspose.Cells stellt eine Klasse, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), bereit, die eine Microsoft Excel-Datei darstellt. Die Klasse [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) enthält eine [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)-Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) repräsentiert.

Die Klasse [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) stellt die Eigenschaft [**GetProtection()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getprotection/) bereit, die verwendet wird, um diese erweiterten Schutzeinstellungen anzuwenden. Die Eigenschaft [**GetProtection()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getprotection/) ist tatsächlich ein Objekt der Klasse [**Protection**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/), das mehrere boolesche Eigenschaften zum Deaktivieren oder Aktivieren von Beschränkungen umschließt.

Unten finden Sie eine kleine Beispielanwendung. Es öffnet eine Excel-Datei und verwendet die meisten von Excel XP und späteren Versionen unterstützten erweiterten Schutzeinstellungen.

```cpp
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook
    Workbook excel(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = excel.GetWorksheets().Get(0);

    // Restricting users to delete columns of the worksheet
    worksheet.GetProtection().SetAllowDeletingColumn(false);

    // Restricting users to delete row of the worksheet
    worksheet.GetProtection().SetAllowDeletingRow(false);

    // Restricting users to edit contents of the worksheet
    worksheet.GetProtection().SetAllowEditingContent(false);

    // Restricting users to edit objects of the worksheet
    worksheet.GetProtection().SetAllowEditingObject(false);

    // Restricting users to edit scenarios of the worksheet
    worksheet.GetProtection().SetAllowEditingScenario(false);

    // Restricting users to filter
    worksheet.GetProtection().SetAllowFiltering(false);

    // Allowing users to format cells of the worksheet
    worksheet.GetProtection().SetAllowFormattingCell(true);

    // Allowing users to format rows of the worksheet
    worksheet.GetProtection().SetAllowFormattingRow(true);

    // Allowing users to format columns of the worksheet
    worksheet.GetProtection().SetAllowFormattingColumn(true);

    // Allowing users to insert hyperlinks in the worksheet
    worksheet.GetProtection().SetAllowInsertingHyperlink(true);

    // Allowing users to insert rows in the worksheet
    worksheet.GetProtection().SetAllowInsertingRow(true);

    // Allowing users to select locked cells of the worksheet
    worksheet.GetProtection().SetAllowSelectingLockedCell(true);

    // Allowing users to select unlocked cells of the worksheet
    worksheet.GetProtection().SetAllowSelectingUnlockedCell(true);

    // Allowing users to sort
    worksheet.GetProtection().SetAllowSorting(true);

    // Allowing users to use pivot tables in the worksheet
    worksheet.GetProtection().SetAllowUsingPivotTable(true);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xls";
    excel.Save(outputFilePath, SaveFormat::Excel97To2003);

    Aspose::Cells::Cleanup();

    return 0;
}
```

{{% alert color="primary" %}}

Bitte rufen Sie beim Verwenden der [**GetProtection()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getprotection/)-Eigenschaft die [**Protect**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/protect/)-Methode der [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)-Klasse nicht auf. Speichern Sie die Datei außerdem im Excel97To2003- oder Xlsx-Format, da die erweiterten Schutzeinstellungen nur von Excel XP und späteren Versionen unterstützt werden.

{{% /alert %}}

### **Problem mit Zellsperre**

Wenn Sie Nutzer daran hindern möchten, Zellen zu bearbeiten, müssen die Zellen vor der Anwendung der Schutz-Einstellungen gesperrt werden. Andernfalls können die Zellen auch bei aktiviertem Schutz bearbeitet werden. In Microsoft Excel XP können Zellen über den folgenden Dialog gesperrt werden:

|**Dialog zum Sperren von Zellen in Excel XP**|
| :- |
|![todo:image_alt_text](advanced-protection-settings-since-excel-xp_1.png)|

Es ist auch möglich, Zellen mit der Aspose.Cells-API zu sperren. Jede Zelle kann eine [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/)-Formatierung erhalten, die eine boolesche Eigenschaft [**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/) enthält. Setzen Sie die [**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/)-Eigenschaft auf **true** oder **false**, um die Zelle zu sperren oder zu entsperren.

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
    U16String outputFilePath = outDir + u"output.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Lock the style of cell A1
    worksheet.GetCells().Get(u"A1").GetStyle().SetIsLocked(true);

    // Protect the sheet
    worksheet.Protect(ProtectionType::All);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Worksheet protected successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
