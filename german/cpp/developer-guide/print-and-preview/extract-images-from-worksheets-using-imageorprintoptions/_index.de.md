---
title: Bilder aus Arbeitsblättern mit ImageOrPrintOptions in C++ extrahieren
linktitle: Bilder aus Arbeitsblättern extrahieren
type: docs
weight: 140
url: /de/cpp/extract-images-from-worksheets-using-imageorprintoptions/
description: Erfahren Sie, wie Sie Bilder aus Excel Arbeitsblättern extrahieren und sie auf einem lokalen Laufwerk speichern können, unter Verwendung von Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

Microsoft Excel-Benutzer können Bilder zu Tabellenkalkulationen hinzufügen. Mit Aspose.Cells ist es möglich, Bilder aus Microsoft Excel-Dateien zu lesen und auf einem lokalen Laufwerk zu speichern. Dieser Artikel zeigt, wie das geht.

{{% /alert %}} 

Der nachstehende Beispielscode zeigt, wie Bilder aus einer Excel-Datei extrahiert und gespeichert werden können.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Open a template Excel file
    Workbook workbook(srcDir + u"sampleExtractImagesFromWorksheets.xlsx");

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the first Picture in the first worksheet
    Picture pic = worksheet.GetPictures().Get(0);

    // Define ImageOrPrintOptions
    ImageOrPrintOptions printoption;

    // Specify the image format
    printoption.SetImageType(ImageType::Jpeg);

    // Save the image
    pic.ToImage(outDir + u"outputExtractImagesFromWorksheets.jpg", printoption);

    std::cout << "Image extracted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
