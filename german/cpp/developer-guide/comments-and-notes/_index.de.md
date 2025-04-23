---
title: Kommentare und Notizen mit C++ verwalten
linktitle: Kommentare und Notizen
type: docs
weight: 128
url: /de/cpp/comments-and-notes/
description: Kommentare oder Notizen mit Aspose.Cells for C++ einfügen und verwalten.
keywords: Kommentare einfügen, Notizen einfügen
---

## **Einführung**

Kommentare werden verwendet, um zusätzliche Informationen zu Zellen hinzuzufügen. Aspose.Cells bietet zwei Methoden zum Hinzufügen von Kommentaren zu Zellen. Die erste Methode besteht darin, Kommentare manuell in einer Designerdatei zu erstellen. Diese Kommentare werden dann mithilfe von Aspose.Cells importiert. Die zweite Methode besteht darin, Kommentare mithilfe der Aspose.Cells-API zur Laufzeit hinzuzufügen. In diesem Thema wird das Hinzufügen von Kommentaren zu Zellen mithilfe der Aspose.Cells-API erläutert. Auch die Formatierung von Kommentaren wird erklärt.

## **Einen Kommentar hinzufügen**

Fügen Sie mithilfe der [**Comments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/)-Sammlung und der [**Add**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/add/)-Methode der [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)-Objektsammlung einen Kommentar zu einer Zelle hinzu. Das neue [**Comment**](https://reference.aspose.com/cells/cpp/aspose.cells/comment/)-Objekt kann aus der [**Comments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/)-Sammlung durch Weitergabe des Kommentarindex abgerufen werden. Nach dem Abrufen des [**Comment**](https://reference.aspose.com/cells/cpp/aspose.cells/comment/)-Objekts passen Sie die Kommentarnotiz mithilfe der [**Comment**](https://reference.aspose.com/cells/cpp/aspose.cells/comment/)-Eigenschaft des [**GetNote()**](https://reference.aspose.com/cells/cpp/aspose.cells/comment/getnote/)-Objekts an.

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

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int32_t sheetIndex = workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Add a comment to cell "F5"
    int32_t commentIndex = worksheet.GetComments().Add(u"F5");

    // Access the newly added comment
    Comment comment = worksheet.GetComments().Get(commentIndex);

    // Set the comment note
    comment.SetNote(u"Hello Aspose!");

    // Save the Excel file
    U16String outputPath = outDir + u"book1.out.xls";
    workbook.Save(outputPath);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Kommentarformatierung**

Es ist auch möglich, das Erscheinungsbild von Kommentaren zu formatieren, indem ihre Höhe, Breite und Schriftarteneinstellungen konfiguriert werden.

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

    // Create workbook
    Workbook workbook;

    // Adding a new worksheet to the Workbook object
    int32_t sheetIndex = workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Adding a comment to "F5" cell
    int32_t commentIndex = worksheet.GetComments().Add(u"F5");

    // Accessing the newly added comment
    Comment comment = worksheet.GetComments().Get(commentIndex);

    // Setting the comment note
    comment.SetNote(u"Hello Aspose!");

    // Setting the font size of a comment to 14
    comment.GetFont().SetSize(14);

    // Setting the font of a comment to bold
    comment.GetFont().SetIsBold(true);

    // Setting the height of the font to 10
    comment.SetHeightCM(10);

    // Setting the width of the font to 2
    comment.SetWidthCM(2);

    // Saving the Excel file
    workbook.Save(outDir + u"book1.out.xls");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Ein Bild zum Kommentar hinzufügen**

Mit Microsoft Excel 2007 ist es auch möglich, ein Bild als Hintergrund für einen Zellenkommentar zu haben. In Excel 2007 wird dies durch die folgenden Schritte erreicht. (Es wird davon ausgegangen, dass bereits ein Zellenkommentar hinzugefügt wurde.)

1. Klicken Sie mit der rechten Maustaste auf die Zelle, die den Kommentar enthält.
1. Wählen Sie **Kommentare einblenden/ausblenden** und löschen Sie jeglichen Text aus dem Kommentar.
1. Klicken Sie auf den Rand des Kommentars, um ihn auszuwählen.
1. Wählen Sie **Format** und dann **Kommentar** aus.
1. Auf der Registerkarte **Farben und Linien** die **Farbe**-Liste erweitern.
1. Klicken Sie auf **Fülleffekte**.
1. Klicken Sie auf der Registerkarte **Bild** auf **Bild auswählen**.
1. Suchen Sie das Bild und wählen Sie es aus.
1. Klicken Sie auf **OK**, bis alle Dialogfelder geschlossen sind.

Auch Aspose.Cells bietet diese Funktion. Im Folgenden finden Sie einen Beispielcode, der eine XLSX-Datei von Grund auf erstellt und einem Zelle "A1" einen Kommentar mit einem Bild als Hintergrund hinzufügt.

```c++
#include <Aspose.Cells.h>
#include <fstream>
#include <vector>
#include <iostream>

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"../Data/01_SourceDirectory/");
    U16String outDir(u"../Data/02_OutputDirectory/");

    Workbook workbook;
    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet sheet = worksheets.Get(0);
    CommentCollection comments = sheet.GetComments();

    int32_t commentIndex = comments.Add(0, 0);
    Comment comment = comments.Get(commentIndex);
    comment.SetNote(u"First note.");

    Font commentFont = comment.GetFont();
    commentFont.SetName(u"Times New Roman");

    U16String imagePath = srcDir + u"logo.jpg";
    std::vector<uint8_t> imageData;
    std::ifstream file(imagePath.ToUtf8(), std::ios::binary | std::ios::ate);
    if (file)
    {
        std::streamsize size = file.tellg();
        file.seekg(0, std::ios::beg);
        imageData.resize(size);
        file.read(reinterpret_cast<char*>(imageData.data()), size);
    }
    Vector<uint8_t> data(imageData.data(), static_cast<int32_t>(imageData.size()));

    CommentShape shape = comment.GetCommentShape();
    shape.GetFill().SetImageData(data);

    U16String outputPath = outDir + u"book1.out.xlsx";
    workbook.Save(outputPath, SaveFormat::Xlsx);

    std::cout << "Workbook with image comment created successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Erweiterte Themen**
- [Ändern der Textrichtung des Kommentars](/cells/de/cpp/change-text-direction-of-the-comment/)
- [Ändern der Kommentarschriftfarbe](/cells/de/cpp/how-to-change-the-comment-font-color/)
- [Wie man den Kommentarhintergrund einstellt](/cells/de/cpp/how-to-set-comment-background/)
- [Antwortkommentare](/cells/de/cpp/threaded-comments/)
