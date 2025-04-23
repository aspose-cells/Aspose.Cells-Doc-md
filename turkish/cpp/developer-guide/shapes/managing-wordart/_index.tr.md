---
title: Çalışma Sayfasına WordArt Watermark Ekleme C++ ile
linktitle: WordArt ı Yönetme
type: docs
weight: 180
url: /tr/cpp/add-wordart-watermark-to-worksheet/
description: Aspose.Cells for C++ kullanarak Excel çalışma sayfalarına WordArt watermark eklemeyi öğrenin.
---

{{% alert color="primary" %}} 

WordArt'ı kullanarak elektronik tablolara özel metin efektleri ekleyin. Örneğin, başlığı dosyanın üst kısmına uzatın, metni süsleyin ve metni önceden ayarlanmış bir şekle uygun hale getirin veya metni bir Excel çalışma sayfasına arka plan filigranı olarak uygulayın. WordArt, elektronik tablolara dekorasyon eklemek için taşıyabileceğiniz bir nesne haline gelir.

{{% /alert %}} 

Aşağıdaki örnek, bir çalışma sayfası için arka plan filigranı olarak bir WordArt şekli eklemenin nasıl yapıldığını göstermektedir.

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

## **Gelişmiş Konular**
- [Dahili Stillerle Word Art Metni Ekleme](/cells/tr/cpp/add-word-art-text-with-built-in-styles/)
- [WordArt Filigranı Kilitleme](/cells/tr/cpp/locking-wordart-watermark/)
- [Metin şeklinin metnine önceden ayarlanmış WordArt stili ayarlayın](/cells/tr/cpp/set-preset-wordart-style-to-the-text-of-the-shape/)
