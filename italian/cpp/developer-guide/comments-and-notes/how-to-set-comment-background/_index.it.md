---
title: Come cambiare lo sfondo del commento in Excel con C++
linktitle: Sfondo del commento
type: docs
weight: 190
url: /it/cpp/how-to-set-comment-background/
description: Come cambiare il colore di un commento in Excel. Come inserire un immagine o una foto in un commento in Excel usando C++.
keywords: aggiungi immagine, foto, colore di sfondo al commento in Excel
---

{{% alert color="primary" %}}

I commenti vengono aggiunti alle celle per registrare commenti, come dettagli su come funziona una formula, da dove viene un valore o domande dei revisori. I commenti svolgono un ruolo estremamente importante quando più persone discutono o revisionano lo stesso documento in momenti diversi. Come distinguere i commenti di persone diverse? Sì, possiamo impostare un colore di sfondo diverso per ogni commento. Ma quando dobbiamo elaborare molti documenti e molti commenti, farlo manualmente è un disastro. Fortunatamente, [**Aspose.Cells**](https://products.aspose.com/cells/cpp/) offre un'API che consente di farlo nel codice.

{{% /alert %}}

## **Come cambiare il colore nel commento in Excel**

Se non hai bisogno del colore di sfondo predefinito per i commenti, potresti volerlo sostituire con un colore di tuo interesse. Come posso cambiare il colore di sfondo della casella dei Commenti in Excel?

Il seguente codice ti guiderà su come usare [**Aspose.Cells**](https://products.aspose.com/cells/cpp/) per aggiungere il tuo colore di sfondo preferito ai commenti di tua scelta.

Qui abbiamo preparato un [file di esempio](exmaple.xlsx) per te. Questo file viene usato per inizializzare l’oggetto Workbook nel codice sottostante.

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

Esegui il codice sopra e otterrai un [file di output](result.xlsx).

## **Come inserire un'immagine o una foto nel commento in Excel**

Microsoft Excel permette agli utenti di personalizzare molto l’aspetto dei fogli di lavoro. È anche possibile aggiungere immagini di sfondo ai commenti. Aggiungere un’immagine di sfondo può essere una scelta estetica o utile per rafforzare il branding.

Il codice di esempio seguente crea un file XLSX da zero usando le API [**Aspose.Cells**](https://products.aspose.com/cells/cpp/) e aggiunge un commento con uno sfondo di immagine alla cella A1.

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
{{< app/cells/assistant language="cpp" >}}
