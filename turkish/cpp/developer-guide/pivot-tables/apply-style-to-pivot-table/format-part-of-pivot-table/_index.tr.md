---
title: Pivot Tablosunun Bir Bölümünü Biçimlendirme
linktitle: Pivot Tablosunun Bir Bölümünü Biçimlendirme
description: Pivot tablosunun bir bölümünü Aspose.Cells for C++ içinde, PivotTable.Format aracılığıyla anlamsal PivotArea bölgelerine veya CellArea dikdörtgenlerine stiller uygulayarak biçimlendirin; biçimler PivotTable.GetPivotFormats içinde depolanır ve pivot tablo yenilendiğinde korunur.
keywords: Aspose.Cells, pivot tablo, biçimlendirme, PivotArea, CellArea, PivotTable.Format, PivotFormats, PivotTableSelectionType, LabelOnly, DataOnly, SelectField, FormatAll, C++
type: docs
weight: 20
url: /tr/cpp/format-part-of-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
`PivotTable.FormatAll` tüm pivot tabloya tek bir stil uygular ve üst sayfada açıklanmıştır. Etiketler, değerler, toplamlar veya raporun belirli bölgeleri arasında ayrım yapmaz.  
Pratikte, bir pivot tablosunun yalnızca bir bölümü genellikle öne çıkarılmalıdır. Yaygın hedefler, bir satır alanına ait etiketler, bir alan tarafından üretilen değer hücreleri, toplam satırı veya ilk iki öğe satırı gibi rastgele bir dikdörtgen olabilir.  
Bir pivot tablosunun çalışma sayfası hücrelerine doğrudan stil uygulamak aynı şey değildir. Excel, pivot tablo biçimlendirmesini sıradan hücre‑stil kayıtları yerine anlamsal `PivotArea` bölgeleri olarak depolar. Bir pivot‑area formatı, bir alanın etiketleri veya veri değerleri gibi bir bölgeye bağlı kalır ve pivot tablo yeniden hesaplandığında, yenilendiğinde veya genişletildiğinde yeniden çözülür. Öte yandan, doğrudan bir hücreye yazılan stil, o hücre konumuna aittir ve pivot modeli tarafından izlenmez.  
Aspose.Cells, her iki biçimlendirme tipinin de kullanılabilmesi için tam `PivotTable.Format` aşırı yükleme ailesini sunar:
- `Format(const PivotArea&, const Style&)` stilini, `PivotArea.Select` veya `PivotArea.SelectField` ile oluşturulan anlamsal bir bölgeye bağlar.
- `Format(const CellArea&, const Style&)` stilini, pivot tablo içindeki bir çalışma sayfası dikdörtgenine bağlar.
- `Format(int32_t row, int32_t column, const Style&)` tek bir hücreyi hedefler.
- `FormatAll(const Style&)` tüm pivot tabloyu biçimlendirir.

## **Pivot Alanını Biçimlendirme**
Bir vurgunun bir alana veya rapor bölgesine eşlenmesi gerektiğinde önerilen yöntem anlamsal‑alan iş akışıdır.
1. `PivotArea pivotArea(pivotTable);` ifadesiyle bir `PivotArea` oluşturun. Bu nesne, o belirli pivot tabloya ait anlamsal bir bölgeyi tanımlar.
2. `PivotArea.Select(PivotFieldType axisType, int32_t fieldPosition, PivotTableSelectionType selectionType)` ile belirli bir eksende sıfır‑tabanlı konuma göre bir alanı seçin.  
   - `PivotTableSelectionType::DataAndLabel` alanın etiketlerini ve verilerini ikisini de seçer.  
   - `PivotTableSelectionType::LabelOnly` sadece alanın etiketlerini seçer.  
   - `PivotTableSelectionType::DataOnly` sadece alanın veri hücrelerini seçer.  
3. `PivotArea.SelectField(PivotFieldType axisType, const char16_t* fieldName)` ile bir alanı isimle seçin. Bir satır alanı isimle seçildiğinde, bölge o alanın öğeleriyle oluşturulan değer hücrelerine çözülür.  
4. `Workbook.CreateStyle()` ile bir `Style` oluşturun, yazı tipini, ön plan rengini ve katı arka plan desenini yapılandırın ve stili `PivotTable.Format(pivotArea, style)` yöntemine geçirin.  
5. `PivotArea` aşırı yüklemesine yapılan her çağrı, `PivotTable.GetPivotFormats()`'e bir `PivotTableFormat` girdisi ekler.  
6. Alan‑bağlantılı formatlar pivot verileri hesaplandığında uygulanır. Bu nedenle, formatları uyguladıktan sonra stillerin görünür olması için `PivotTable.CalculateData()` çağırın.  
Aşağıdaki örnek küçük bir meyve‑satış pivot tablosu oluşturur, `Fruit` satır etiketlerini `PivotArea.Select` ve `PivotTableSelectionType::LabelOnly` ile biçimlendirir, aynı satır alanı tarafından üretilen değer hücrelerini `PivotArea.SelectField` ile biçimlendirir ve ardından pivot tabloyu yeniden hesaplayarak her iki stilin de uygulanmasını sağlar.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    // Fruit sales data
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    U16String fruits[] = { u"Apple", u"Banana", u"Apple", u"Banana", u"Cherry", u"Cherry" };
    int years[] = { 2024, 2024, 2025, 2025, 2024, 2025 };
    int amounts[] = { 100, 150, 120, 180, 90, 110 };
    for (int i = 0; i < 6; i++)
    {
        cells.Get(i + 1, 0).PutValue(fruits[i]);
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }
    // Pivot table with its top-left corner at E3
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=A1:C7", 2, 4);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.CalculateData();
    // Bold yellow fill on the row field's label cells
    Style labelStyle = workbook.CreateStyle();
    labelStyle.GetFont().SetIsBold(true);
    labelStyle.SetForegroundColor(Color::Yellow());
    labelStyle.SetPattern(BackgroundType::Solid);
    PivotArea labelArea(pivotTable);
    labelArea.Select(PivotFieldType::Row, 0, PivotTableSelectionType::LabelOnly);
    pivotTable.Format(labelArea, labelStyle);
    // Light green fill on the value cells the row field produces
    Style valueStyle = workbook.CreateStyle();
    valueStyle.SetForegroundColor(Color::LightGreen());
    valueStyle.SetPattern(BackgroundType::Solid);
    PivotArea valueArea(pivotTable);
    valueArea.SelectField(PivotFieldType::Row, u"Fruit");
    pivotTable.Format(valueArea, valueStyle);
    // Field-anchored formats are painted when the data is calculated
    pivotTable.CalculateData();
    // Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
    workbook.Save(u"FormatPivotArea.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Pivot Tablosunun Hücre Alanını Biçimlendirme**
İlgilenilen bölge anlamsal bir pivot bölgesi yerine düz bir çalışma sayfası dikdörtgeni olduğunda `PivotTable.Format(const CellArea&, const Style&)` kullanın.  
`CellArea`, `StartRow`, `StartColumn`, `EndRow` ve `EndColumn` açık alanlarıyla tanımlanır. Değerler sıfır‑tabanlı çalışma sayfası koordinatlarıdır ve son koordinatlar, dikdörtgene dahil edilen son satır ve sütunu belirler; böylece alan, başlangıç konumundan son konuma kadar (dahil) hücreleri kapsar.  
Alan‑bağlantılı bir formatın aksine, `CellArea` formatı hücrelere hemen uygulanır. Stil görünmesi için başka bir `CalculateData()` çağrısına gerek yoktur.  
`CellArea` dikdörtgeni etiket hücreleri ve değer hücrelerini birlikte içerebilir. Sonraki bölüm, Aspose.Cells ve Excel'in bu dikdörtgeni dahili olarak nasıl temsil ettiğini açıklar.  
Aşağıdaki örnek, pivot tablosunun `E4:F5` dikdörtgenini italik, açık‑mavi bir stil ile biçimlendirir ve çalışma kitabını başka bir yeniden hesaplama yapmadan kaydeder.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    U16String fruits[] = { u"Apple", u"Banana", u"Apple", u"Banana", u"Cherry", u"Cherry" };
    int years[] = { 2024, 2024, 2025, 2025, 2024, 2025 };
    int amounts[] = { 100, 150, 120, 180, 90, 110 };
    for (int i = 0; i < 6; i++)
    {
        cells.Get(i + 1, 0).PutValue(fruits[i]);
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=A1:C7", 2, 4);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.CalculateData();
    // Highlight the first two fruit rows (the rectangle E4:F5)
    Style highlightStyle = workbook.CreateStyle();
    highlightStyle.GetFont().SetIsItalic(true);
    highlightStyle.SetForegroundColor(Color{ 0xFF, 0x99, 0xCC, 0xFF });
    highlightStyle.SetPattern(BackgroundType::Solid);
    CellArea rectangle;
    rectangle.StartRow = 3;
    rectangle.StartColumn = 4;
    rectangle.EndRow = 4;
    rectangle.EndColumn = 5;
    pivotTable.Format(rectangle, highlightStyle);
    // E4:F5 is italic on light blue immediately, no recalculation needed
    workbook.Save(u"FormatPivotCellArea.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Pivot Alanları ve Hücre Alanları Nasıl Eşlenir**
Excel, pivot tablo biçimlendirmesini sıradan çalışma sayfası hücre‑stil kayıtları yerine `pivotArea` kayıtları olarak depolar. Aynı model Aspose.Cells tarafından da kullanılır; bu yüzden bir biçimlendirme isteği kaydedildiğinde pivot alanlarına dönüştürülür.  
Kullanıcı tarafından sağlanan `CellArea` ile dahili olarak depolanan pivot alanları arasındaki ilişki her iki yönde de çok‑tan‑çok şeklindedir.  
- Bir `CellArea` birkaç pivot alanı üretebilir. Dikdörtgen hem etiket hem de değer hücrelerini kapsıyorsa, etiket ve veri kurallarına ayrı ayrı bölünür; çünkü pivot modeli etiket biçimlendirmesini ve veri biçimlendirmesini bağımsız olarak ele alır.  
- Bir pivot alanı, birkaç ayrı `CellArea` örneğine çözülebilir. Toplam satırı gibi anlamsal bir bölge ya da öğeleri bitişik olmayan bir alan, birden çok dikdörtgeni kapsayabilir. Bu yüzden `PivotArea.GetCellAreas()` tek bir dikdörtgen yerine bir `Vector<CellArea>` döndürür.  
`PivotTable.Format` ile gerçekleştirilen her biçimlendirme işlemi `PivotTable.GetPivotFormats()` içinde kaydedilir. Her `PivotTableFormat` girişi, ilişkili `PivotArea` ve ona uygulanan `Style`ı gösterir. `PivotArea` aşırı yüklemesi çağrı başına tek bir girdi eklerken, farklı anlamsal bölgeler içeren bir `CellArea` birden çok girdi ekleyebilir.  
Depolanan bölgeleri ayırt etmek için her `PivotArea`, `GetOnlyLabel()` ve `GetOnlyData()` bayraklarını ortaya çıkarır. Aşağıdaki örnek, hem etiketleri hem de değerleri kapsayan tek bir dikdörtgeni biçimlendirir, `PivotTable.GetPivotFormats()`'ı inceler ve her depolanmış pivot alanının çözüldüğü `CellArea` koordinatlarını yazdırır.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    U16String fruits[] = { u"Apple", u"Banana", u"Apple", u"Banana", u"Cherry", u"Cherry" };
    int years[] = { 2024, 2024, 2025, 2025, 2024, 2025 };
    int amounts[] = { 100, 150, 120, 180, 90, 110 };
    for (int i = 0; i < 6; i++)
    {
        cells.Get(i + 1, 0).PutValue(fruits[i]);
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=A1:C7", 2, 4);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.CalculateData();
    Style highlightStyle = workbook.CreateStyle();
    highlightStyle.GetFont().SetIsItalic(true);
    highlightStyle.SetForegroundColor(Color{ 0xFF, 0x99, 0xCC, 0xFF });
    highlightStyle.SetPattern(BackgroundType::Solid);
    // ONE rectangle in...
    CellArea rectangle;
    rectangle.StartRow = 3;
    rectangle.StartColumn = 4;
    rectangle.EndRow = 4;
    rectangle.EndColumn = 5;
    pivotTable.Format(rectangle, highlightStyle);
    // ...TWO semantic pivot areas out: the label part and the data part are stored separately
    std::cout << "Stored formats: " << pivotTable.GetPivotFormats().GetCount() << std::endl;
    for (int i = 0; i < pivotTable.GetPivotFormats().GetCount(); i++)
    {
        PivotArea storedArea = pivotTable.GetPivotFormats().Get(i).GetPivotArea();
        std::cout << "Format " << i << ": OnlyLabel=" << (storedArea.GetOnlyLabel() ? "true" : "false")
                  << ", OnlyData=" << (storedArea.GetOnlyData() ? "true" : "false") << std::endl;
        Vector<CellArea> resolved = storedArea.GetCellAreas();
        for (int j = 0; j < resolved.GetLength(); j++)
        {
            std::cout << "    rows " << (resolved[j].StartRow + 1) << "-" << (resolved[j].EndRow + 1)
                      << ", columns " << (resolved[j].StartColumn + 1) << "-" << (resolved[j].EndColumn + 1) << std::endl;
        }
    }
    // This prints:
    // Stored formats: 2
    // Format 0: OnlyLabel=true, OnlyData=false
    //     rows 4-5, columns 5-5        (E4:E5, the label part)
    // Format 1: OnlyLabel=false, OnlyData=true
    //     rows 4-5, columns 6-6        (F4:F5, the data part)
    workbook.Save(u"FormatPivotAreasMap.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}
Biçimler sıradan hücre stilleri yerine pivot alanları olarak depolandığı için yeniden hesaplamalar ve yenilemeler sırasında korunur. Pivot tablo `PivotTable.RefreshData` ile yenilendiğinde, `CalculateData` ile yeniden hesaplandığında veya kaydedilip yeniden yüklendiğinde, her depolanmış pivot alanı bölgesinin mevcut konumuna yeniden çözülür ve stili yeniden uygulanır.
{{% /alert %}}

Yenilemeler sırasında bir vurgunun bir alana veya anlamsal bölgeye bağlı kalması gerektiğinde `Select` veya `SelectField` ile oluşturulmuş bir `PivotArea` kullanın; geçerli pivot tablo düzeninde sabit bir dikdörtgeni biçimlendirmek yeterli olduğunda bir `CellArea` kullanın. Tek hücre için `Format(int32_t row, int32_t column, const Style&)` aşırı yüklemesi bireysel bir hücreyi hedefler. Tüm pivot tabloyu bir kerede yeniden biçimlendirmek istediğinizde, üst sayfada açıklanan `FormatAll` yöntemini kullanın.

## **İlgili Makaleler**
- [Pivot Tablosuna Stil Uygulama](/cells/tr/cpp/apply-style-to-pivot-table/)
- [Pivot Tablosuna Satır ve Sütun Alanları Ekleme](/cells/tr/cpp/pivot-table-add-row-and-column-fields/)
- [Pivot Tablosunda Değer Alanlarını Yönetme](/cells/tr/cpp/manage-value-fields/)
- [Pivot Tablosunu Yenileme](/cells/tr/cpp/refresh-pivot-table/)

{{< app/cells/assistant language="cpp" >}}