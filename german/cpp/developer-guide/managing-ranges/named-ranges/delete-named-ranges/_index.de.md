---
title: Benannte Bereiche mit C++ löschen
linktitle: Benannte Bereiche löschen
type: docs
weight: 90
url: /de/cpp/delete-named-ranges/
description: Erfahren Sie, wie Sie definierte Namen oder benannte Bereiche aus Excel oder OpenOffice Dateien mit Aspose.Cells for C++ entfernen.
---

## **Einführung**
Wenn es zu viele definierte Namen oder benannte Bereiche in den Excel-Dateien gibt, müssen wir einige davon löschen, da sie nicht mehr referenziert werden.

## **Benannten Bereich in MS Excel entfernen**

Um einen benannten Bereich aus Excel zu entfernen, können Sie folgende Schritte befolgen:
1. Öffnen Sie Microsoft Excel und die Arbeitsmappe, die den benannten Bereich enthält.
2. Gehen Sie zum Register "Formeln" in der Excel-Menüleiste.
3. Klicken Sie auf die Schaltfläche "Namensmanager" in der Gruppe "Definierte Namen". Dadurch wird das Dialogfeld Namensmanager geöffnet.
4. Wählen Sie im Dialogfeld Namensmanager den benannten Bereich aus, den Sie entfernen möchten.
5. Klicken Sie auf die Schaltfläche "Löschen". Bestätigen Sie die Löschung beim Auffordern.
6. Klicken Sie auf die Schaltfläche "Schließen", um das Dialogfeld Namensmanager zu schließen.
7. Speichern Sie die Arbeitsmappe, um die Änderungen beizubehalten.

## **Benannten Bereich mit Aspose.Cells for C++ löschen**
Mit Aspose.Cells for C++ können Sie benannte Bereiche oder definierte Namen über [Text](https://reference.aspose.com/cells/cpp/aspose.cells/namecollection/remove/) oder [Index](https://reference.aspose.com/cells/cpp/aspose.cells/namecollection/removeat/) in der Liste entfernen.

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
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"Book2.xlsx";

    // Instantiate a new Workbook
    Workbook workbook(inputFilePath);

    // Get all the worksheets in the book
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Delete a named range by text
    worksheets.GetNames().Remove(u"NamedRange");

    // Delete a defined name by index
    worksheets.GetNames().RemoveAt(0);

    // Save the workbook to retain the changes
    workbook.Save(outputFilePath);

    std::cout << "Named ranges removed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Hinweis: Wenn der definierte Name sich auf Formeln bezieht, kann er nicht entfernt werden. Wir können nur die Formel des definierten Namens entfernen.

## **Einige benannte Bereiche entfernen**
Beim Entfernen eines definierten Namens müssen wir überprüfen, ob er von allen Formeln in der Datei referenziert wird.
Um die Leistung beim Entfernen benannter Bereiche zu verbessern, können wir einige gleichzeitig entfernen.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"Book2.xlsx";

    // Instantiate a new Workbook
    Workbook workbook(inputFilePath);

    // Get all the worksheets in the book
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Delete some defined names
    Vector<U16String> namesToRemove = { u"NamedRange1", u"NamedRange2" };
    worksheets.GetNames().Remove(namesToRemove);

    // Save the workbook to retain the changes
    workbook.Save(outputFilePath);

    std::cout << "Named ranges removed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Doppelte definierte Namen entfernen**
Einige Excel-Dateien sind beschädigt, weil einige definierte Namen doppelt vorhanden sind. Daher können wir diese doppelten Namen entfernen, um die Datei zu reparieren.

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
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"Book2.xlsx";

    // Instantiate a new Workbook
    Workbook workbook(inputFilePath);

    // Get all the worksheets in the book
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Delete some defined names
    worksheets.GetNames().RemoveDuplicateNames();

    // Save the workbook to retain the changes
    workbook.Save(outputFilePath);

    std::cout << "Workbook saved successfully after removing duplicate names!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
