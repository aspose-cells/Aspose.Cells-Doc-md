---
title: C++ kullanarak Yerleşik Stilde WordArt Metni ekleyin
linktitle: Dahili Stillerle Kelime Sanatı Metni Ekleyin
type: docs
weight: 270
url: /tr/cpp/add-word-art-text-with-built-in-styles/
description: Aspose.Cells for C++ kullanarak Yerleşik Stilde WordArt Metni eklemeyi öğrenin.
---

## **Olası Kullanım Senaryoları**
Aspose.Cells kullanarak Yerleşik Stilde WordArt Metni ekleyebilirsiniz. Bu amaçla [ShapeCollection.AddWordArt()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addwordart/) yöntemini kullanın.

## **Dahili Stillerle Word Art Metni Ekleme**
Aşağıdaki örnek kod farklı Dahili Stillerle Kelime Sanatı metinleri ekler. Lütfen bu kodla oluşturulan [çıktı excel dosyasını](5115470.xlsx) kontrol edin. Bu, Microsoft Excel'de [çıktı excel dosyası](5115470.xlsx)'nın nasıl göründüğüdür.

![todo:image_alt_text](add-word-art-text-with-built-in-styles_1.png)

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

    // Create workbook object
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Add Word Art Text with Built-in Styles
    ws.GetShapes().AddWordArt(PresetWordArtStyle::WordArtStyle1, u"Aspose File Format APIs", 0, 0, 0, 0, 100, 800);
    ws.GetShapes().AddWordArt(PresetWordArtStyle::WordArtStyle2, u"Aspose File Format APIs", 10, 0, 0, 0, 100, 800);
    ws.GetShapes().AddWordArt(PresetWordArtStyle::WordArtStyle3, u"Aspose File Format APIs", 20, 0, 0, 0, 100, 800);
    ws.GetShapes().AddWordArt(PresetWordArtStyle::WordArtStyle4, u"Aspose File Format APIs", 30, 0, 0, 0, 100, 800);
    ws.GetShapes().AddWordArt(PresetWordArtStyle::WordArtStyle5, u"Aspose File Format APIs", 40, 0, 0, 0, 100, 800);

    // Save the workbook in xlsx format
    wb.Save(outDir + u"output_out.xlsx");

    std::cout << "WordArt added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
