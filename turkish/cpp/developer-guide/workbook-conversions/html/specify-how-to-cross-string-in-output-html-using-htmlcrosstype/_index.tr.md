---
title: Çıktı HTML’sinde satırları çapraz şekilde nasıl göstereceğinizi HtmlCrossType ile belirtin C++ kullanarak
linktitle: Çıktı HTML’sinde HtmlCrossType ayarlayın
type: docs
weight: 140
url: /tr/cpp/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
description: Aspose.Cells for C++ kullanarak HTML çıktısında metin taşmasını kontrol etmeyi öğrenin; HtmlCrossType ile.
---

## **Olası Kullanım Senaryoları**

 Bir hücre, hücre genişliğinden daha büyük metin veya dize içeriyorsa, dize taşar; eğer sonraki hücre boşsa veya yoksa. Excel dosyanızı HTML’ye kaydederken, [**HtmlCrossType**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype/) enumerasyonu kullanarak çapraz tipi belirterek bu taşmayı kontrol edebilirsiniz. Aşağıdaki değerleri içerir:

- **HtmlCrossType.Default**: MS Excel gibi görüntüle, bir sonraki hücreye bağlıdır. Eğer bir sonraki hücre boşsa, dize taşır veya kırpılır.

- **HtmlCrossType.MSExport**: Diziyi MS Excel'in HTML olarak dışa aktarması gibi görüntüle.

- **HtmlCrossType.Cross**: HTML çapraz dizisini görüntüle, büyük HTML dosyaları oluşturma performansı, Değerin Varsayılana veya Hücreye Sığdırmak olarak ayarlanmasından on kat daha hızlı olacaktır.

- **HtmlCrossType.FitToCell**: Dizeyi yalnızca hücre genişliği içinde gösterir.

## **Çıkış HTML'sinde dizeyi nasıl geçeceğini HtmlCrossType kullanarak belirtin**

 Aşağıdaki örnek kod, [örnek Excel dosyasını](51740732.xlsx) yükler ve farklı [**HtmlCrossType**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype/) değerleri belirterek HTML formatında kaydeder. Lütfen bu kod ile üretilen [çıktı HTML'leri](51740734.zip) indirin. Örnek Excel dosyası, bu ekran görüntüsünde gösterildiği gibi kırmızı renkli çerçeve ile sınırlanmış bir resmi içerir ve bu ekran görüntüsü, [**HtmlCrossType**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype/) değerlerinin çıktı HTML'sine etkisini gösterir.

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **Örnek Kod**

```c++
#include <iostream>
#include <string>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String inputFilePath(u"sampleHtmlCrossStringType.xlsx");
    Workbook wb(inputFilePath);

    HtmlSaveOptions opts;
    opts.SetHtmlCrossStringType(HtmlCrossType::Default);
    opts.SetHtmlCrossStringType(HtmlCrossType::MSExport);
    opts.SetHtmlCrossStringType(HtmlCrossType::Cross);
    opts.SetHtmlCrossStringType(HtmlCrossType::FitToCell);

    int htmlCrossType = static_cast<int>(opts.GetHtmlCrossStringType());
    std::string numStr = std::to_string(htmlCrossType);
    U16String outputFilePath = U16String(u"out") + U16String(numStr.c_str()) + U16String(u".htm");
    wb.Save(outputFilePath, opts);

    Aspose::Cells::Cleanup();
}
```
