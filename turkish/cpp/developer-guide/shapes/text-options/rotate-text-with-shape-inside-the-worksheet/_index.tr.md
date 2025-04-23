---
title: Çalışma Sayfası İçinde Şekil ile Metni Döndürme ile C++
linktitle: Metni Şekil ile Döndür
type: docs
weight: 1300
url: /tr/cpp/rotate-text-with-shape-inside-the-worksheet/
description: Excel sayfalarında şekillerle metin döndürmeyi Aspose.Cells for C++ kullanarak nasıl kontrol edileceğini öğrenin.
---

## **Olası Kullanım Senaryoları**

Microsoft Excel kullanarak herhangi bir şeklin içine metin ekleyebilirsiniz. Çok eski Microsoft Excel 2003 kullanıyorsanız, metin şekil ile birlikte dönmeyecektir. Ancak, daha yeni sürümleri olan Microsoft Excel, örneğin 2007, 2010, 2013 veya 2016 kullanıyorsanız, metin şekil ile beraber dönecektir. Metnin şekil ile dönüp dönmeyeceğini [**ShapeTextAlignment.GetRotateTextWithShape()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/getrotatetextwithshape/) özelliği ile kontrol edebilirsiniz. Bu özelliğin varsayılan değeri **true**'dur, yani metin şekil ile birlikte döner. Eğer **false** olarak ayarlarsanız, metin şekil ile dönmez.

## **Çalışma Sayfası İçindeki Şekil ile Metni Döndürme**

Aşağıdaki örnek kod, üçgen şekil içeren ve metni şekil ile birlikte dönen bir [örnek Excel dosyası](64716896.xlsx) yükler. Eğer Microsoft Excel'de bu örnek Excel dosyasını açarsanız ve üçgen şekli döndürürseniz, metin de onunla birlikte döner. Daha sonra kod, [**ShapeTextAlignment.GetRotateTextWithShape()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/getrotatetextwithshape/) özelliğini **false** olarak ayarlar ve [çıktı Excel dosyası](64716897.xlsx) olarak kaydeder. Şimdi çıktı Excel dosyasını Microsoft Excel'de açıp üçgen şekli döndürürseniz, metin onunla birlikte dönmez. Kodun örnek etkisini görmek için aşağıdaki ekran görüntüsüne bakabilirsiniz.

![todo:image_alt_text](rotate-text-with-shape-inside-the-worksheet_1.png)

## **Örnek Kod**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
using namespace Aspose::Cells::Drawing::Texts;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load sample Excel file
    Workbook wb(srcDir + u"sampleRotateTextWithShapeInsideWorksheet.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell B4 and add message inside it
    Cell b4 = ws.GetCells().Get(u"B4");
    b4.PutValue(u"Text is not rotating with shape because RotateTextWithShape is false.");

    // Access first shape
    Shape sh = ws.GetShapes().Get(0);

    // Access shape text alignment
    ShapeTextAlignment shapeTextAlignment = sh.GetTextBody().GetTextAlignment();

    // Do not rotate text with shape by setting RotateTextWithShape as false
    shapeTextAlignment.SetRotateTextWithShape(false);

    // Save the output Excel file
    wb.Save(outDir + u"outputRotateTextWithShapeInsideWorksheet.xlsx");

    Aspose::Cells::Cleanup();
}
```
