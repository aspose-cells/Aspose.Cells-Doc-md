---
title: Gestire commenti e note con C++
linktitle: Commenti e note
type: docs
weight: 128
url: /it/cpp/comments-and-notes/
description: Inserire e gestire commenti o note con Aspose.Cells for C++.
keywords: Inserire commenti, inserire note
---

## **Introduzione**

I commenti vengono utilizzati per aggiungere informazioni aggiuntive alle celle. Aspose.Cells fornisce due metodi per aggiungere commenti alle celle. Il primo è creare commenti manualmente in un file di progettazione. Successivamente, questi commenti vengono importati utilizzando Aspose.Cells. Il secondo è aggiungere commenti utilizzando l'API di Aspose.Cells in fase di esecuzione. Questo argomento tratta l'aggiunta di commenti alle celle utilizzando l'API di Aspose.Cells. Verrà inoltre spiegato come formattare i commenti.

## **Aggiungere un commento**

Aggiungi un commento a una cella chiamando il metodo [**Add**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/add/) della raccolta [**Comments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/) (incapsulato nell'oggetto [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)). Il nuovo oggetto [**Comment**](https://reference.aspose.com/cells/cpp/aspose.cells/comment/) può essere accessibile dalla raccolta [**Comments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/) passando l'indice del commento. Dopo aver accesso all'oggetto [**Comment**](https://reference.aspose.com/cells/cpp/aspose.cells/comment/), personalizza la nota del commento utilizzando la proprietà [**GetNote()**](https://reference.aspose.com/cells/cpp/aspose.cells/comment/getnote/) dell'oggetto [**Comment**](https://reference.aspose.com/cells/cpp/aspose.cells/comment/).

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

## **Formattazione del commento**

È anche possibile formattare l'aspetto dei commenti configurando la loro altezza, larghezza e impostazioni del carattere.

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

## **Aggiungi un'immagine al commento**

Con Microsoft Excel 2007, è anche possibile avere un'immagine come sfondo di un commento di cella. In Excel 2007 questo si realizza seguendo i seguenti passaggi. (Si suppone che tu abbia già aggiunto un commento alla cella.)

1. Fare clic con il pulsante destro del mouse sulla cella che contiene il commento.
1. Selezionare **Mostra/Nascondi commenti**, e cancellare eventuali testi dal commento.
1. Fare clic sul bordo del commento per selezionarlo.
1. Selezionare **Formato**, quindi **Commento**.
1. Nella scheda **Colori e linee**, espandere l'elenco **Colore**.
1. Fare clic su **Effetti di riempimento**.
1. Nella scheda **Immagine**, fare clic su **Seleziona immagine**.
1. Trovare e selezionare l'immagine.
1. Fare clic su **OK** finché tutte le finestre di dialogo non si sono chiuse.

Aspose.Cells fornisce anche questa funzionalità. Di seguito è riportato un esempio di codice che crea un file XLSX da zero, aggiungendo un commento alla cella "A1" con un'immagine impostata come sfondo.

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

## **Argomenti avanzati**
- [Cambia la Direzione del Testo del Commento](/cells/it/cpp/change-text-direction-of-the-comment/)
- [Come cambiare il Colore del Testo del Commento](/cells/it/cpp/how-to-change-the-comment-font-color/)
- [Come impostare lo sfondo del commento](/cells/it/cpp/how-to-set-comment-background/)
- [Commenti in discussione](/cells/it/cpp/threaded-comments/)
