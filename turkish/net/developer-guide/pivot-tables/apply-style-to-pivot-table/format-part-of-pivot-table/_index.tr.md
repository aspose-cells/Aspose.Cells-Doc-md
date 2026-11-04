---
title: Pivot Tablosunun Biçim Bölümü
linktitle: Pivot Tablosunun Biçim Bölümü
description: Aspose.Cells for .NET ile pivot tablosunun bir bölümünü, PivotTable.Format aracılığıyla anlamsal PivotArea bölgelerine veya CellArea dikdörtgenlerine stil uygulayarak biçimlendirin; biçimler PivotTable.PivotFormats içinde depolanır ve pivot tablo yenilendiğinde korunur.
keywords: Aspose.Cells, özet tablo, biçim, PivotArea, CellArea, PivotTable.Format, PivotFormats, PivotTableSelectionType, LabelOnly, DataOnly, SelectField, FormatAll, C#
type: docs
weight: 20
url: /tr/net/format-part-of-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
`PivotTable.FormatAll` tek bir stili tüm pivot tabloya uygular ve ana sayfada ele alınmıştır. Etiketler, değerler, toplamlar veya raporun belirli bölgeleri arasında ayrım yapmaz.  
Pratikte, genellikle pivot tablosunun sadece bir bölümü vurgulanması gerekir. Yaygın hedefler, bir satır alanına ait etiketler, bir alan tarafından üretilen değer hücreleri, toplam satırı veya ilk iki öğe satırı gibi rastgele bir dikdörtgen olabilir.  
Bir pivot tablosunun çalışma sayfası hücrelerine doğrudan stil uygulamak aynı şey değildir. Excel, pivot‑tablosu biçimlendirmesini sıradan hücre‑stil kayıtları yerine anlamsal `PivotArea` bölgeleri olarak depolar. Bir pivot‑alan biçimi, bir alanın etiketleri veya veri değerleri gibi bir bölgeye bağlı kalır ve pivot tablo yeniden hesaplandığında, yenilendiğinde veya genişletildiğinde tekrar çözülür. Öte yandan, doğrudan bir hücreye yazılan stil, o hücre konumuna aittir ve pivot modeli tarafından izlenmez.  
Aspose.Cells, her iki biçimlendirme türünün de kullanılabilmesi için tam `PivotTable.Format` aşırı yükleme ailesini sunar:
- `Format(PivotArea, Style)` stili, `PivotArea.Select` veya `PivotArea.SelectField` ile oluşturulan anlamsal bir bölgeye sabitler.
- `Format(CellArea, Style)` stili, pivot tablosu içindeki bir çalışma sayfası dikdörtgenine sabitler.
- `Format(int row, int column, Style)` tek bir hücreyi hedef alır.
- `FormatAll(Style)` tüm pivot tabloyu biçimlendirir.

## **Pivot Alanını Biçimlendirme**
Anlamsal alan iş akışı, bir vurgunun bir alana veya raporun bir bölgesine bağlı kalması gerektiğinde önerilen yaklaşımdır.
1. `new PivotArea(pivotTable)` ile bir `PivotArea` oluşturun. **Nesne**, o belirli pivot tabloya ait anlamsal bir bölgeyi tanımlar.  
2. `PivotArea.Select(PivotFieldType axisType, int fieldPosition, PivotTableSelectionType selectionType)` ile belirli bir eksende sıfır‑tabanlı konumuna göre bir alan seçin.  
   - `PivotTableSelectionType.DataAndLabel` alanın etiketlerini ve verilerini birlikte seçer.  
   - `PivotTableSelectionType.LabelOnly` yalnızca alanın etiketlerini seçer.  
   - `PivotTableSelectionType.DataOnly` yalnızca alanın veri hücrelerini seçer.  
3. `PivotArea.SelectField(PivotFieldType axisType, string fieldName)` ile bir alanı ada göre seçin. Bir satır alanı ada göre seçildiğinde, bölge o alanın öğeleri tarafından üretilen değer hücrelerine çözülür.  
4. `Workbook.CreateStyle()` ile bir `Style` oluşturun, yazı tipini, ön plan rengini ve katı arka plan desenini yapılandırın ve stili `PivotTable.Format(area, style)` yöntemine iletin.  
5. `PivotArea` aşırı yüklemesinin her çağrısı, `PivotTable.PivotFormats` içine bir `PivotTableFormat` girdisi ekler.  
6. Alan‑sabitlemeli biçimler, pivot verileri hesaplandığında işlenir. Bu nedenle, biçimleri uyguladıktan sonra stillerin görünür olmasını sağlamak için `PivotTable.CalculateData()` çağırın.  
Aşağıdaki örnek, küçük bir meyve‑satış pivot tablosu oluşturur, `Fruit` satır etiketlerini `PivotArea.Select` ve `PivotTableSelectionType.LabelOnly` ile biçimler, aynı satır alanı tarafından üretilen değer hücrelerini `PivotArea.SelectField` ile biçimler ve ardından pivot tabloyu yeniden hesaplayarak iki stili de uygular.

```csharp
using System;
using System.Drawing;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
Cells cells = sheet.Cells;
// Fruit sales data
string[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells["A1"].PutValue("Fruit");
cells["B1"].PutValue("Year");
cells["C1"].PutValue("Amount");
for (int i = 0; i < fruits.Length; i++)
{
    cells[i + 1, 0].PutValue(fruits[i]);
    cells[i + 1, 1].PutValue(years[i]);
    cells[i + 1, 2].PutValue(amounts[i]);
}
// Pivot table with its top-left corner at E3
PivotTable pivotTable = sheet.PivotTables.Add("=A1:C7", 2, 4);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.CalculateData();
// Bold yellow fill on the row field's label cells
Style labelStyle = workbook.CreateStyle();
labelStyle.Font.IsBold = true;
labelStyle.ForegroundColor = Color.Yellow;
labelStyle.Pattern = BackgroundType.Solid;
PivotArea labelArea = new PivotArea(pivotTable);
labelArea.Select(PivotFieldType.Row, 0, PivotTableSelectionType.LabelOnly);
pivotTable.Format(labelArea, labelStyle);
// Light green fill on the value cells the row field produces
Style valueStyle = workbook.CreateStyle();
valueStyle.ForegroundColor = Color.LightGreen;
valueStyle.Pattern = BackgroundType.Solid;
PivotArea valueArea = new PivotArea(pivotTable);
valueArea.SelectField(PivotFieldType.Row, "Fruit");
pivotTable.Format(valueArea, valueStyle);
// Field-anchored formats are painted when the data is calculated
pivotTable.CalculateData();
// Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
workbook.Save("FormatPivotArea.xlsx");
```

## **Pivot Tablosunun Hücre Alanını Biçimlendirme**
İlgili bölge, anlamsal bir pivot bölgesi yerine düz bir çalışma sayfası dikdörtgeni olduğunda `PivotTable.Format(CellArea, Style)` kullanın.  
Bir `CellArea`, `StartRow`, `StartColumn`, `EndRow` ve `EndColumn` özellikleriyle tanımlanır. Değerler sıfır‑tabanlı çalışma sayfası koordinatlarıdır ve son koordinatlar, dikdörtgen içinde dahil edilen son satır ve sütunu gösterir; böylece alan, başlangıç konumundan son konuma kadar olan hücreleri kapsar.  
Alan‑sabitlemeli bir biçimden farklı olarak, bir `CellArea` biçimi hücrelere anında uygulanır. Stilin görünmesi için ek bir `CalculateData()` çağrısına gerek yoktur.  
Bir `CellArea` dikdörtgeni etiket ve değer hücrelerini birlikte içerebilir. Bir sonraki bölüm, Aspose‑Cells ve Excel’in bu dikdörtgeni dahili olarak nasıl temsil ettiğini açıklar.  
Aşağıdaki örnek, pivot tablosunun `E4:F5` dikdörtgenini eğik, açık‑mavi bir stil ile biçimler ve çalışma kitabını herhangi bir ek yeniden hesaplama olmaksızın kaydeder.

```csharp
using System;
using System.Drawing;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
Cells cells = sheet.Cells;
string[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells["A1"].PutValue("Fruit");
cells["B1"].PutValue("Year");
cells["C1"].PutValue("Amount");
for (int i = 0; i < fruits.Length; i++)
{
    cells[i + 1, 0].PutValue(fruits[i]);
    cells[i + 1, 1].PutValue(years[i]);
    cells[i + 1, 2].PutValue(amounts[i]);
}
PivotTable pivotTable = sheet.PivotTables.Add("=A1:C7", 2, 4);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.CalculateData();
// Highlight the first two fruit rows (the rectangle E4:F5)
Style highlightStyle = workbook.CreateStyle();
highlightStyle.Font.IsItalic = true;
highlightStyle.ForegroundColor = Color.FromArgb(0xFF, 0x99, 0xCC, 0xFF);
highlightStyle.Pattern = BackgroundType.Solid;
CellArea rectangle = new CellArea { StartRow = 3, StartColumn = 4, EndRow = 4, EndColumn = 5 };
pivotTable.Format(rectangle, highlightStyle);
// E4:F5 is italic on light blue immediately, no recalculation needed
workbook.Save("FormatPivotCellArea.xlsx");
```

## **Pivot Alanları ve Hücre Alanları Nasıl Haritalanır**
Excel, pivot‑tablosu biçimlendirmesini sıradan çalışma sayfası hücre‑stil kayıtları yerine `pivotArea` kayıtları olarak depolar. Aynı model Aspose.Cells tarafından da kullanılır; bu yüzden bir biçimlendirme isteği kaydedildiğinde pivot alanlarına dönüştürülür.  
Kullanıcı tarafından sağlanan `CellArea` ile dahili olarak saklanan pivot alanları arasındaki ilişki her iki yönde de çok‑tan‑çok’tur.  
- Tek bir `CellArea` birden çok pivot alanı üretebilir. Dikdörtgen hem etiket hem de değer hücrelerini kapsıyorsa, pivot modeli etiket biçimlendirmesi ile veri biçimlendirmesini bağımsız olarak ele aldığı için ayrı etiket ve veri kurallarına ayrılır.  
- Tek bir pivot alanı, birden çok ayrı `CellArea` örneğine çözülür. Toplam satırı gibi anlamsal bir bölge veya öğeleri ardışık olmayan bir alan, birden çok dikdörtgeni kapsayabilir. Bu yüzden `PivotArea.GetCellAreas()` tek bir dikdörtgen yerine bir koleksiyon döndürür.  
`PivotTable.Format` aracılığıyla gerçekleştirilen her biçimlendirme işlemi `PivotTable.PivotFormats` içinde kaydedilir. Her `PivotTableFormat` girdisi, ilişkili `PivotArea` ve ona uygulanan `Style` bilgilerini sunar. `PivotArea` aşırı yüklemesi her çağrı başına tam bir giriş eklerken, farklı anlamsal bölgeler içeren bir `CellArea` birden çok giriş ekleyebilir.  
Saklanan bölgeleri ayırt etmek için her `PivotArea`, `OnlyLabel` ve `OnlyData` bayraklarını ortaya çıkarır. Aşağıdaki örnek, hem etiketleri hem de değerleri kapsayan tek bir dikdörtgeni biçimler, `PivotTable.PivotFormats` koleksiyonunu inceler ve her saklanan pivot alanının çözüldüğü `CellArea` koordinatlarını yazdırır.

```csharp
using System;
using System.Drawing;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
Cells cells = sheet.Cells;
string[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells["A1"].PutValue("Fruit");
cells["B1"].PutValue("Year");
cells["C1"].PutValue("Amount");
for (int i = 0; i < fruits.Length; i++)
{
    cells[i + 1, 0].PutValue(fruits[i]);
    cells[i + 1, 1].PutValue(years[i]);
    cells[i + 1, 2].PutValue(amounts[i]);
}
PivotTable pivotTable = sheet.PivotTables.Add("=A1:C7", 2, 4);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.CalculateData();
Style highlightStyle = workbook.CreateStyle();
highlightStyle.Font.IsItalic = true;
highlightStyle.ForegroundColor = Color.FromArgb(0xFF, 0x99, 0xCC, 0xFF);
highlightStyle.Pattern = BackgroundType.Solid;
// ONE rectangle in...
CellArea rectangle = new CellArea { StartRow = 3, StartColumn = 4, EndRow = 4, EndColumn = 5 };
pivotTable.Format(rectangle, highlightStyle);
// ...TWO semantic pivot areas out: the label part and the data part are stored separately
Console.WriteLine("Stored formats: " + pivotTable.PivotFormats.Count);
for (int i = 0; i < pivotTable.PivotFormats.Count; i++)
{
    PivotArea storedArea = pivotTable.PivotFormats[i].PivotArea;
    Console.WriteLine($"Format {i}: OnlyLabel={storedArea.OnlyLabel}, OnlyData={storedArea.OnlyData}");
    foreach (CellArea resolved in storedArea.GetCellAreas())
        Console.WriteLine($"    rows {resolved.StartRow + 1}-{resolved.EndRow + 1}, columns {resolved.StartColumn + 1}-{resolved.EndColumn + 1}");
}
// This prints:
// Stored formats: 2
// Format 0: OnlyLabel=True, OnlyData=False
//     rows 4-5, columns 5-5        (E4:E5, the label part)
// Format 1: OnlyLabel=False, OnlyData=True
//     rows 4-5, columns 6-6        (F4:F5, the data part)
workbook.Save("FormatPivotAreasMap.xlsx");
```

{{% alert color="primary" %}}
Biçimler, sıradan hücre stilleri yerine pivot alanları olarak saklandığı için yeniden hesaplamalar ve yenilemeler sırasında korunur. Pivot tablo `PivotTable.RefreshData` ile yenilendiğinde, `CalculateData` ile yeniden hesaplandığında veya kaydedilip tekrar yüklendiğinde, her saklanan pivot alanı bölgesinin mevcut konumuna yeniden çözülür ve stili yeniden uygulanır.
{{% /alert %}}

Bir vurgunun yenilemeler sırasında bir alana veya anlamsal bir bölgeye bağlı kalması gerektiğinde `Select` ya da `SelectField` ile oluşturulmuş bir `PivotArea` kullanın; sabit bir dikdörtgeni biçimlendirmek yeterli olduğunda `CellArea` kullanın. Tek hücreyi hedeflemek için `Format(int row, int column, Style)` aşırı yüklemesi kullanılabilir. Tüm pivot tabloyu bir seferde yeniden biçimlendirmek için, ana sayfada açıklanan `FormatAll` kullanın.

## **İlgili Makaleler**
- [Pivot Tablosuna Stil Uygulama](/cells/tr/net/apply-style-to-pivot-table/)
- [Pivot Tablosuna Satır ve Sütun Alanları Ekleme](/cells/tr/net/pivot-table-add-row-and-column-fields/)
- [Pivot Tablosunda Değer Alanlarını Yönetme](/cells/tr/net/manage-value-fields/)
- [Pivot Tablosunu Yenileme](/cells/tr/net/refresh-pivot-table/)

{{< app/cells/assistant language="csharp" >}}