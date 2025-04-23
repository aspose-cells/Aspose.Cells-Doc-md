---
title: Hur man ändrar bakgrund i kommentar i Excel med C++
linktitle: Kommentarbakgrund
type: docs
weight: 190
url: /sv/cpp/how-to-set-comment-background/
description: Hur man ändrar färg på kommentar i Excel. Hur man infogar bild eller bild i kommentar i Excel med C++.
keywords: lägg till infälld bild färg kommentar bakgrund excel
---

{{% alert color="primary" %}}

Kommentarer läggs till celler för att registrera kommentarer, allt från detaljer om hur en formel fungerar, var en värde kommer ifrån, eller frågor från granskare. Kommentarer spelar en extremt viktig roll när flera personer diskuterar eller granskar samma dokument vid olika tillfällen. Hur kan man skilja olika personers kommentarer? Ja, vi kan ställa in en annan bakgrundsfärg för varje kommentar. Men när vi behöver behandla många dokument och många kommentarer är det en mardröm att göra det manuellt. Lyckligtvis erbjuder [**Aspose.Cells**](https://products.aspose.com/cells/cpp/) ett API som låter dig göra detta i kod.

{{% /alert %}}

## **Hur man ändrar färg i kommentar i Excel**

När du inte behöver standardbakgrundsfärgen för kommentarer kan du vilja ersätta den med en färg du är intresserad av. Hur ändrar jag bakgrundsfärgen på kommentarrutan i Excel?

Följande kod kommer att guida dig hur du använder [**Aspose.Cells**](https://products.aspose.com/cells/cpp/) för att lägga till din favoritbakgrundsfärg till valfria kommentarer.

Här har vi förberett en [exempel fil](exmaple.xlsx) för dig. Denna fil används för att initialisera Workbook-objektet i koden nedan.

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

Kör ovanstående kod, och du får en [utdata fil](result.xlsx).

## **Hur man infogar bild eller bild i kommentar i Excel**

Microsoft Excel låter användare anpassa utseendet och känslan av kalkylblad i stor utsträckning. Det är till och med möjligt att lägga till bakgrundsbilder i kommentarer. Att lägga till en bakgrundsbild kan vara ett estetiskt val eller användas för att stärka varumärket.

Exempelkoden nedan skapar en XLSX-fil från början med [**Aspose.Cells**](https://products.aspose.com/cells/cpp/) API, och lägger till en kommentar med bakgrundsbild i cell A1.

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
