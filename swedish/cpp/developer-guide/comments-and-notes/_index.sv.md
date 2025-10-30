---
title: Hantera kommentarer och anteckningar med C++
linktitle: Kommentarer och noteringar
type: docs
weight: 128
url: /sv/cpp/comments-and-notes/
description: Infoga och hantera kommentarer eller anteckningar med Aspose.Cells for C++.
keywords: Infoga kommentarer, infoga noteringar
---

## **Introduktion**

Kommentarer används för att lägga till ytterligare information i celler. Aspose.Cells tillhandahåller två metoder för att lägga till kommentarer i celler. Den första är att skapa kommentarer i en designerfil manuellt. Dessa kommentarer importeras sedan med hjälp av Aspose.Cells. Den andra är att lägga till kommentarer med hjälp av Aspose.Cells API vid körning. Detta ämne diskuterar att lägga till kommentarer i celler med hjälp av Aspose.Cells API. Formatering av kommentarer kommer också att förklaras.

## **Lägga till en kommentar**

Lägg till en kommentar i en cell genom att anropa [**Comments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/) samlingen [**Add**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/add/) metod (inkapslad i [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) objektet). Det nya [**Comment**](https://reference.aspose.com/cells/cpp/aspose.cells/comment/) objektet kan nås från [**Comments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/) samlingen genom att skicka kommentarindexet. Efter att ha fått tillgång till [**Comment**](https://reference.aspose.com/cells/cpp/aspose.cells/comment/) objektet, anpassa kommentarnoteringen genom att använda [**Comment**](https://reference.aspose.com/cells/cpp/aspose.cells/comment/) objektets [**GetNote()**](https://reference.aspose.com/cells/cpp/aspose.cells/comment/getnote/) egenskap.

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

## **Kommentarformatering**

Det är också möjligt att formatera kommentarers utseende genom att konfigurera deras höjd, bredd och teckensnittsinställningar.

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

## **Lägg till en bild till en kommentar**

Med Microsoft Excel 2007 är det också möjligt att ha en bild som bakgrund till en cellkommentar. I Excel 2007 uppnås detta genom följande steg. (De förutsätter att du redan har lagt till en cellkommentar.)

1. Högerklicka på cellen som innehåller kommentaren.
1. Välj ** Visa/dölj kommentarer ** och ta bort all text från kommentaren.
1. Klicka på kommentarens kant för att markera den.
1. Välj ** Formatera **, sedan ** Kommentar **.
1. På fliken ** Färg och linjer **, expandera **Färg** listan.
1. Klicka på **Fyllnings effekter**.
1. På fliken **Bild**, klicka på **Välj bild**.
1. Hitta och välj bilden.
1. Klicka **OK** tills alla dialogrutor har stängts.

Aspose.Cells tillhandahåller också den här funktionen. Nedan finns ett kodexempel som skapar en XLSX-fil från grunden och lägger till en kommentar i cellen "A1" med en bild som bakgrund.

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

## **Fortsatta ämnen**
- [Ändra textriktning för kommentaren](/cells/sv/cpp/change-text-direction-of-the-comment/)
- [Hur man ändrar färgen på kommentarsfönstret](/cells/sv/cpp/how-to-change-the-comment-font-color/)
- [Hur man ställer in kommentarens bakgrund](/cells/sv/cpp/how-to-set-comment-background/)
- [Trådade Kommentarer](/cells/sv/cpp/threaded-comments/)
{{< app/cells/assistant language="cpp" >}}
