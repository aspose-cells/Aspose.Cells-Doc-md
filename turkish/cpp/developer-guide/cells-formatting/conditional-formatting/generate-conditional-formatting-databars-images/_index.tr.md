---
title: C++ ile Koşullu Biçimlendirme VeriBar’ları Görüntüleri Üret
linktitle: Koşullu Biçimlendirme DataBar Görüntüleri Oluşturma
description: Aspose.Cells, veri çubuğu ve resimlerin koşullu biçimlendirmeyle oluşturulmasına imkan sağlayan C++ kütüphanesidir. Bu, hücrelerin değerine göre hücrenin görünümünü özelleştirmeye olanak tanır. Bu makale, Aspose.Cells kütüphanesini kullanarak koşullu biçimlendirme veri çubukları ve resimleri nasıl oluşturulacağını tanıtacaktır.
keywords: Aspose.Cells, Koşullu Biçimlendirme, Veri Çubukları, Görüntüler, Elektronik Tablolar
type: docs
weight: 40
url: /tr/cpp/generate-conditional-formatting-databars-images/
---

{{% alert color="primary" %}}

Bazen Koşullu Biçimlendirme DataBar'ların görüntülerini oluşturmanız gerekebilir. Aspose.Cells [**DataBar.ToImage()**](https://reference.aspose.com/cells/cpp/aspose.cells/databar/toimage/) yöntemini kullanarak bu görüntüleri oluşturabilirsiniz. Bu makale, Aspose.Cells kullanarak DataBar görüntüsünün nasıl oluşturulacağını gösterir.

{{% /alert %}}

Aşağıdaki örnek kod, C1 hücresinin Veri Çubuğu görüntüsünü üretir. İlk olarak, hücrenin biçim koşulu nesnesine erişir ve ardından bu nesneden, [**DataBar**](https://reference.aspose.com/cells/cpp/aspose.cells/databar/) nesnesine erişerek ve onun [**ToImage()**](https://reference.aspose.com/cells/cpp/aspose.cells/databar/toimage/) metodunu kullanarak hücrenin resmini oluşturur. Son olarak, resmi diske kaydeder.

```cpp
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"sampleGenerateDatabarImage.xlsx");
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cell cell = worksheet.GetCells().Get(u"C1");

    int idx = worksheet.GetConditionalFormattings().Add();
    FormatConditionCollection fcc = worksheet.GetConditionalFormattings().Get(idx);
    fcc.AddCondition(FormatConditionType::DataBar);
    fcc.AddArea(CellArea::CreateCellArea(u"C1", u"C4"));

    DataBar dbar = fcc.Get(0).GetDataBar();

    ImageOrPrintOptions opts;
    opts.SetImageType(ImageType::Png);

    Vector<uint8_t> imgBytes = dbar.ToImage(cell, opts);

    std::ofstream outFile((outDir + u"outputGenerateDatabarImage.png").ToUtf8(), std::ios::binary);
    outFile.write(reinterpret_cast<const char*>(imgBytes.GetData()), imgBytes.GetLength());
    outFile.close();

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
