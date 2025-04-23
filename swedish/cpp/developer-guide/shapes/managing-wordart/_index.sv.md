---
title: Lägg till WordArt vattenmärke till arbetsblad med C++
linktitle: Hantera WordArt
type: docs
weight: 180
url: /sv/cpp/add-wordart-watermark-to-worksheet/
description: Lär dig hur du lägger till WordArt vattenmärken i Excel arbetsblad med Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

 Använd WordArt för att lägga till speciella texteffekter till kalkylblad. Till exempel, sträck en rubrik överst på filen, dekorera text och få texten att passa en förinställd form eller applicera text på ett Excel-ark som en bakgrundsvattenstämpel. WordArt blir ett objekt som du kan flytta eller placera i kalkylblad för att lägga till dekoration.

{{% /alert %}} 

Följande exempel visar hur man lägger till en WordArt-form för att ställa in en bakgrundsvattenstämpel för ett arbetsblad.

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

## **Fortsatta ämnen**
- [Lägg till Word Art Text med Inbyggda Stilar](/cells/sv/cpp/add-word-art-text-with-built-in-styles/)
- [Låsa WordArt vattenstämpel](/cells/sv/cpp/locking-wordart-watermark/)
- [Ange förvald WordArt-stil för texten på formen](/cells/sv/cpp/set-preset-wordart-style-to-the-text-of-the-shape/)
