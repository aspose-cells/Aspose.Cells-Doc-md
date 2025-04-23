---
title: C++ ile Alt Toplamı Uygulama ve Detay Altındaki Kontur Özeti Satırlarının Yönünü Değiştirme
linktitle: Alt Detay Altında Toplam Uygulama ve Özet Satırların Yönünü Değiştirme
type: docs
weight: 100
url: /tr/cpp/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
description: Aspose.Cells for C++ API kullanarak, detayın altında kontur özet satırlarının yönünü değiştirme ve toplam uygulama yollarını öğrenin.
keywords: Alt detay altında toplam uygulama, toplam ekleme, özet detay altında özet satırların yönünü değiştirme, özet detay altında özet sütunlarını sağa değiştirme, toplam oluşturma ve özet detay altında özet satırlarının yönünü değiştirme
---

{{% alert color="primary" %}}

 Bu makale, veriye toplam uygulama ve detayın altındaki Kontur Özet Satırlarının yönünü değiştirmeyi açıklayacaktır.

 Verilere toplam uygulamak için [**Worksheet.Cells.Subtotal()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/subtotal/) yöntemini kullanabilirsiniz. Aşağıdaki parametreleri alır:

- **CellArea** - Toplam uygulanacak aralık
- **GroupBy** - Sıfıra dayalı bir tamsayı kaydırmak için alan
- **Function** - Toplam işlevi
- **TotalList** - Toplam eklenen sıfıra dayalı alan kaydırmaları dizisi
- **Replace** - Mevcut toplamların değiştirilip değiştirilmayacağını belirtir
- **PageBreaks** - Gruplar arasında sayfa sonu eklenip eklenmeyeceğini belirtir
- **SummaryBelowData** - Özette özetin veri altında eklenip eklenmeyeceğini belirtir.

Ayrıca, aşağıdaki ekran görüntüsünde gösterildiği gibi `Worksheet.Outline.SummaryRowBelow` özelliği kullanılarak Detayların altında özet satırlarının yönü kontrol edilebilir. Bu ayarı Microsoft Excel'de **Veri > Kontur > Ayarlar** kullanarak açabilirsiniz.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_1.png)

{{% /alert %}}

## Kaynak ve çıktı dosyalarının görüntüleri

Aşağıdaki ekran görüntüsü, aşağıda yer alan örnek kodda kullanılan kaynak Excel dosyasını göstermektedir ve içinde A ve B sütunlarında bazı veriler içermektedir.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_2.png)

Aşağıdaki ekran görüntüsü, örnek kod tarafından oluşturulan çıktı Excel dosyasını göstermektedir. Görebileceğiniz gibi, toplam A2:B11 aralığına uygulanmış ve özetin yönü detayın altında bulunmaktadır.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_3.png)

## Toplam uygulama ve kontur özet satırlarının yönünü değiştirmek için C++ kodu

Yukarıda gösterildiği gibi çıktıyı elde etmek için örnek kod burada bulunmaktadır.

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

    // Create workbook from source Excel file
    Workbook workbook(srcDir + u"Book1.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the Cells collection in the first worksheet
    Cells cells = worksheet.GetCells();

    // Create a cellarea i.e.., A2:B11
    CellArea ca = CellArea::CreateCellArea(u"A2", u"B11");

    // Apply subtotal, the consolidation function is Sum and it will applied to Second column (B) in the list
    cells.Subtotal(ca, 0, ConsolidationFunction::Sum, { 1 }, true, false, true);

    // Set the direction of outline summary
    worksheet.GetOutline().SetSummaryRowBelow(true);

    // Save the excel file
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "Subtotal applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
