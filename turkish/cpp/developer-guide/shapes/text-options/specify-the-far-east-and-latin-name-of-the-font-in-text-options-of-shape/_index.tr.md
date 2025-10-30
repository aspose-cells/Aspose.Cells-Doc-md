---
title: C++ kullanarak Şekil in veya Metin Kutusu nun Yazı Tipi Adını Doğu ve Latin Dili belirsin
linktitle: Şekil Metin Seçenekleri nde Uzak Doğu ve Latin Yazı Tipi Adını Belirtin
type: docs
weight: 1600
url: /tr/cpp/specify-the-far-east-and-latin-name-of-the-font-in-text-options-of-shape/
description: Aspose.Cells for C++ kullanarak bir şeklin yazı tipi adlarını Doğu ve Latin dilinde nasıl belirteceğinizi öğrenin.
---

## **Olası Kullanım Senaryoları**

Bazen, Far East dilinde yazılmış metni göstermek istersiniz örneğin Japonca, Çince, Tayca vb. Aspose.Cells, Far East dilinin yazı tipi adını belirlemek için [**TextOptions.GetFarEastName()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/textoptions/getfareastname/) özelliğini sağlar. Ayrıca, Latin yazı tipi adını [**TextOptions.GetLatinName()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/textoptions/getlatinname/) özelliği kullanarak belirtebilirsiniz.

## **Şekil Metin Seçenekleri'nde Uzak Doğu ve Latin Yazı Tipi Adını Belirtin**

Aşağıdaki örnek kod, bir metin kutusu oluşturur ve içine bazı Japonca metinler ekler. Daha sonra, metnin Latin ve Doğu (Far East) yazı tipi adlarını belirler ve çalışma kitabını [çıktı Excel dosyası](67338274.xlsx) olarak kaydeder. Aşağıdaki ekran görüntüsü, Microsoft Excel'de çıktı metin kutusunun Latin ve Doğu yazı tipi adlarını gösterir.

![todo:image_alt_text](specify-the-far-east-and-latin-name-of-the-font-in-text-options-of-shape_1.png)

## **Örnek Kod**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    Workbook wb;

    Worksheet ws = wb.GetWorksheets().Get(0);

    int idx = ws.GetTextBoxes().Add(5, 5, 50, 200);
    TextBox tb = ws.GetTextBoxes().Get(idx);

    tb.SetText(u"\u3053\u3093\u306B\u3061\u306F\u4E16\u754C");

    tb.GetTextOptions().SetLatinName(u"Comic Sans MS");
    tb.GetTextOptions().SetFarEastName(u"KaiTi");

    wb.Save(u"outputSpecifyFarEastAndLatinNameOfFontInTextOptionsOfShape.xlsx", SaveFormat::Xlsx);

    std::cout << "Textbox created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
