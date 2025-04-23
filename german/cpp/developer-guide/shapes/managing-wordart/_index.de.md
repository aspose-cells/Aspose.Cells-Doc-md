---
title: Fügen Sie WordArt Wasserzeichen zum Arbeitsblatt mit C++ hinzu
linktitle: Verwalten von WordArt
type: docs
weight: 180
url: /de/cpp/add-wordart-watermark-to-worksheet/
description: Lernen Sie, wie Sie WordArt Wasserzeichen mit Aspose.Cells for C++ zu Excel Arbeitsblättern hinzufügen.
---

{{% alert color="primary" %}} 

Verwenden Sie WordArt, um spezielle Texteffekte zu Tabellenkalkulationen hinzuzufügen. Zum Beispiel können Sie einen Titel über die Oberseite der Datei strecken, Text dekorieren und Text an eine Excel-Tabelle als Hintergrund-Wasserzeichen anwenden. Das WordArt wird zu einem Objekt, das Sie in Tabellenkalkulationen verschieben oder platzieren können, um Dekoration hinzuzufügen.

{{% /alert %}} 

Das folgende Beispiel zeigt, wie ein WordArt-Objekt hinzugefügt wird, um ein Hintergrundwasserzeichen für ein Arbeitsblatt festzulegen.

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

    // Instantiate a new Workbook
    Workbook workbook;

    // Get the first default sheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Add Watermark
    Shape wordart = sheet.GetShapes().AddTextEffect(MsoPresetTextEffect::TextEffect1,
        u"CONFIDENTIAL", u"Arial Black", 50, false, true,
        18, 8, 1, 1, 130, 800);

    // Get the fill format of the word art
    FillFormat wordArtFormat = wordart.GetFill();

    // Set the transparency
    wordArtFormat.SetTransparency(0.9);

    // Make the line invisible
    LineFormat lineFormat = wordart.GetLine();

    // Save the file
    U16String outputPath = outDir + u"Watermark_Test.out.xls";
    workbook.Save(outputPath);

    std::cout << "Watermark added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Erweiterte Themen**
- [Fügen Sie Word-Art-Text mit integrierten Stilen hinzu](/cells/de/cpp/add-word-art-text-with-built-in-styles/)
- [Sperren des WordArt-Wasserzeichens](/cells/de/cpp/locking-wordart-watermark/)
- [Voreingestellten WordArt-Stil auf den Text der Form setzen](/cells/de/cpp/set-preset-wordart-style-to-the-text-of-the-shape/)
