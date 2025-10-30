---
title: Modifikation eines bestehenden Stils mit C++
description: Aspose.Cells ist eine C++ Bibliothek zum Arbeiten mit Tabellenkalkulationsdateien, die Benutzern ermöglicht, bestehende Zellstile zu modifizieren. Dieser Artikel beschreibt, wie man einen bestehenden Zellstil mit der Aspose.Cells Bibliothek ändert, sodass Benutzer das Aussehen der Zellen nach Bedarf anpassen können.
keywords: Existierende Stile ändern, das Erscheinungsbild Ihrer Anwendung anpassen, Anleitungen, Tutorials, Hilfedokumentationen, Entwicklerdokumentationen, API Referenzen, Beispielcode, Downloads, Support.
type: docs
weight: 90
url: /de/cpp/modify-an-existing-style/
---

{{% alert color="primary" %}}

Um dieselben Formatierungsoptionen auf Zellen anzuwenden, erstellen Sie ein neues Formatierungsstil-Objekt. Ein Formatierungsstil-Objekt ist eine Kombination von Formatierungseigenschaften, wie Schriftart, Schriftgröße, Einzug, Nummer, Rand, Muster usw., benannt und als Satz gespeichert. Wenn angewendet, werden alle Formatierungen in diesem Stil angewendet.

Sie können auch einen vorhandenen Stil verwenden, ihn mit der Arbeitsmappe speichern und zum Formatieren von Informationen mit denselben Attributen verwenden.

Wenn Zellen nicht explizit formatiert sind, wird der **Normal**-Stil (der Standardstil der Arbeitsmappe) angewendet. Microsoft Excel definiert neben dem Normalstil mehrere Stile, darunter Komma, Währung und Prozent.

Aspose.Cells ermöglicht die Änderung aller dieser Stile oder eines anderen Stils, den Sie mit Ihren gewünschten Attributen definieren.

{{% /alert %}}

## **Verwendung von Microsoft Excel**

So aktualisieren Sie einen Stil in Microsoft Excel 97-2003:

1. Klicken Sie im Menü **Format** auf **Stil**.
1. Wählen Sie den Stil aus, den Sie aus der Liste **Stilname** ändern möchten.
1. Klicken Sie auf **Ändern**.
1. Wählen Sie die Stiloptionen aus, die Sie mithilfe der Registerkarten im Dialogfeld Zellen formatieren möchten.
1. Klicken Sie auf **OK**.
1. Legen Sie unter **Stil enthält** die gewünschten Stileigenschaften fest.
1. Klicken Sie auf **OK**, um den Stil zu speichern und auf den ausgewählten Bereich anzuwenden.

## **Verwendung von Aspose.Cells**

Die folgenden Beispiele zeigen, wie man die [**Style.Update**](https://reference.aspose.com/cells/cpp/aspose.cells/style/update/)-Methode verwendet.

### **Erstellen und Ändern eines Stils**

Dieses Beispiel erstellt ein [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/)-Objekt, wendet es auf einen Zellbereich an und modifiziert das [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/)-Objekt. Die Änderungen werden automatisch auf die Zellen und den Bereich angewendet, auf den der Stil angewendet wurde.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create a workbook.
    Workbook workbook;

    // Create a new style object.
    Style style = workbook.CreateStyle();

    // Set the number format.
    style.SetNumber(14);

    // Set the font color to red color.
    style.GetFont().SetColor(Color::Red());

    // Name the style.
    style.SetName(u"Date1");

    // Get the first worksheet cells.
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    // Specify the style (described above) to A1 cell.
    cells.Get(u"A1").SetStyle(style);

    // Create a range (B1:D1).
    Range range = cells.CreateRange(u"B1", u"D1");

    // Initialize styleflag object.
    StyleFlag flag;

    // Set all formatting attributes on.
    flag.SetAll(true);

    // Apply the style (described above) to the range.
    range.ApplyStyle(style, flag);

    // Modify the style (described above) and change the font color from red to black.
    style.GetFont().SetColor(Color::Black());

    // Done! Since the named style (described above) has been set to a cell and range,
    // The change would be reflected (new modification is implemented) to cell (A1) and range (B1:D1).
    style.Update();

    // Save the excel file.
    U16String dataDir(u"..\\Data\\02_OutputDirectory\\");
    workbook.Save(dataDir + u"book_styles.out.xls");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Ändern eines vorhandenen Stils**

Dieses Beispiel verwendet eine einfache Vorlagendatei in Excel, auf die bereits ein Stil namens Prozent auf einen Bereich angewendet wurde. Das Beispiel:

1. holt den Stil,
1. erstellt ein Stil-Objekt und
1. ändert die Formatierung des Stils.

Die Änderungen werden automatisch auf den Bereich angewendet, auf den der Stil angewendet wurde.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputPath = srcDir + u"book1.xlsx";

    /*
     * Create a workbook.
     * Open a template file. 
     * In the book1.xlsx file, we have applied Ms Excel's 
     * Named style i.e., "Percent" to the range "A1:C8".
    */
    Workbook workbook(inputPath);

    // We get the Percent style and create a style object.
    Style style = workbook.GetNamedStyle(u"Percent");

    // Change the number format to "0.00%".
    style.SetNumber(11);

    // Set the font color.
    Color redColor = Color::Red();
    style.GetFont().SetColor(redColor);

    // Update the style. so, the style of range "A1:C8" will be changed too.
    style.Update();

    // Save the excel file.	
    U16String outputPath = srcDir + u"book2.out.xlsx";
    workbook.Save(outputPath);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
