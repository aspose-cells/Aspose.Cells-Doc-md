---
title: Wie man den Hintergrund im Kommentar in Excel mit C++ ändert
linktitle: Kommentarhintergrund
type: docs
weight: 190
url: /de/cpp/how-to-set-comment-background/
description: Wie man die Farbe im Kommentar in Excel ändert. Wie man in Excel mit C++ ein Bild oder Foto in den Kommentar einfügt.
keywords: Hinzufügen eines eingefügten Bildes, Farbkommenthintergrund in Excel
---

{{% alert color="primary" %}}

Kommentare werden Zellen hinzugefügt, um Kommentare zu erfassen, von den Details einer Formel, deren Herkunft bis hin zu Fragen von Prüfern. Kommentare spielen eine äußerst wichtige Rolle, wenn mehrere Personen dasselbe Dokument zu unterschiedlichen Zeiten besprechen oder überprüfen. Wie erkennt man die Kommentare verschiedener Personen? Ja, wir können für jeden Kommentar eine andere Hintergrundfarbe festlegen. Aber wenn wir viele Dokumente und Kommentare verarbeiten müssen, ist das manuell eine Katastrophe. Glücklicherweise bietet [**Aspose.Cells**](https://products.aspose.com/cells/cpp/) eine API, die es Ihnen ermöglicht, dies im Code zu tun.

{{% /alert %}}

## **Wie ändere ich die Farbe in einem Kommentar in Excel**

Wenn Sie die Standard-Hintergrundfarbe für Kommentare nicht benötigen, möchten Sie diese durch eine Farbe ersetzen, die Sie interessiert. Wie ändere ich die Hintergrundfarbe des Kommentarfelds in Excel?

Der folgende Code zeigt, wie Sie [**Aspose.Cells**](https://products.aspose.com/cells/cpp/) verwenden können, um Ihre bevorzugte Hintergrundfarbe für Ihre Kommentare hinzuzufügen.

Hier haben wir eine [Beispieldatei](exmaple.xlsx) für Sie vorbereitet. Diese Datei dient dazu, das Objekt Workbook im unten stehenden Code zu initialisieren.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    U16String inputPath = srcDir + u"exmaple.xlsx";
    Workbook book(inputPath);

    Worksheet worksheet = book.GetWorksheets().Get(0);
    Comment comment = worksheet.GetComments().Get(0);

    CommentShape shape = comment.GetCommentShape();
    shape.GetFill().GetSolidFill().SetColor(Color::Red());

    U16String outputPath = outDir + u"result.xlsx";
    book.Save(outputPath);

    std::cout << "Comment color changed successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

Führen Sie den obigen Code aus, und Sie erhalten eine [Ausgabedatei](result.xlsx).

## **Wie füge ich ein Bild oder eine Grafik in einen Kommentar in Excel ein**

Microsoft Excel ermöglicht es Benutzern, Spreadsheets nach ihren Wünschen anzupassen. Es ist sogar möglich, Hintergrundbilder zu Kommentaren hinzuzufügen. Das Hinzufügen eines Hintergrundbildes kann eine ästhetische Wahl sein oder dazu dienen, das Branding zu stärken.

Der folgende Beispielcode erstellt eine XLSX-Datei von Grund auf mit der [**Aspose.Cells**](https://products.aspose.com/cells/cpp/)-API und fügt einem Zellkommentar mit Hintergrundbild ein Bild hinzu.

```c++
#include <iostream>
#include "Aspose.Cells.h"
#include <vector>
#include <cstdint>

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a Workbook
    Workbook workbook;

    // Get a reference of comments collection with the first sheet
    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet worksheet = worksheets.Get(0);
    CommentCollection comments = worksheet.GetComments();

    // Add a comment to cell A1
    int32_t commentIndex = comments.Add(0, 0);
    Comment comment = comments.Get(commentIndex);
    comment.SetNote(u"First note.");
    Font font = comment.GetFont();
    font.SetName(u"Times New Roman");

    // Load an image into stream
    U16String imagePath = srcDir + u"image2.jpg";
    std::vector<uint8_t> imageData;
    // Assume image loading logic here
    // For simplicity, we assume imageData is populated with the image bytes

    // Set image data to the shape associated with the comment
    CommentShape commentShape = comment.GetCommentShape();
    commentShape.GetFill().SetImageData(Aspose::Cells::Vector<uint8_t>(imageData.data(), imageData.size()));

    // Save the workbook
    U16String outputPath = outDir + u"commentwithpicture1.out.xlsx";
    workbook.Save(outputPath, SaveFormat::Xlsx);

    std::cout << "Workbook saved successfully with comment and image!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
