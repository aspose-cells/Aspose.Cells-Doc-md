---
title: Laden Sie ein Webbild von einer URL in ein Excel Arbeitsblatt mit C++
linktitle: Ein Webbild von einer URL in ein Excel Arbeitsblatt laden
type: docs
weight: 30
url: /de/cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/
description: Erfahren Sie, wie Sie ein Bild von URL in ein in Excel eingebettetes Bild mit C++ und der API Aspose.Cells for C++ umwandeln.
keywords: Excel zeigt Bild von URL, Excel URL zu Bild, Bild in Excel aus URL anzeigen, Excel Bild aus URL einfügen, URL in Bild umwandeln in Excel, Excel Bild von URL, Bild aus URL in Excel laden, C++, Excel
---

## Laden eines Bildes von einer URL in ein Excel-Arbeitsblatt

Die API Aspose.Cells for C++ bietet eine einfache Methode, um Bilder von URLs in Excel-Arbeitsblätter zu laden. In diesem Artikel wird erklärt, wie Bilddaten in einen Arbeitsspeicher-Stream heruntergeladen und mit Aspose.Cells in das Arbeitsblatt eingefügt werden. Das Bild wird im Excel-Dokument eingebettet und benötigt beim Öffnen keine externen Downloads.

## Beispielcode

```c++
#include <iostream>
#include <Aspose.Cells.h>
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"../Data/01_SourceDirectory/");
    U16String outDir(u"../Data/02_OutputDirectory/");

    try
    {
        // Create a new workbook
        Workbook wb;

        // Get the first worksheet
        WorksheetCollection worksheets = wb.GetWorksheets();
        Worksheet sheet = worksheets.Get(0);

        // Get the pictures collection
        PictureCollection pictures = sheet.GetPictures();

        // Insert the picture from local file to B2 cell (row 1, column 1)
        // Note: Image file should be pre-downloaded to source directory
        U16String imagePath = srcDir + u"aspose-logo.jpg";
        pictures.Add(1, 1, imagePath);

        // Save the Excel file
        wb.Save(outDir + u"webimagebook.out.xlsx");
        std::cout << "Image added successfully." << std::endl;
    }
    catch (const std::exception& ex)
    {
        std::cerr << "Error: " << ex.what() << std::endl;
        return 1;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

Für Szenarien, bei denen immer aktualisierte Bilder von einer URL erforderlich sind, verwenden Sie die in [Verknüpftes Bild von Webadresse einfügen] beschriebene Methode. Dieser Ansatz lädt das Bild jedes Mal, wenn das Arbeitsblatt geöffnet wird, von der URL.

{{% /alert %}}
