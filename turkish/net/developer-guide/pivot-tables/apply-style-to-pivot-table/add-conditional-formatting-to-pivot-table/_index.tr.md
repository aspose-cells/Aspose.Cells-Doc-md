---
title: Pivot Tablosuna Koşullu Biçimlendirme Ekle
linktitle: Pivot Tablosuna Koşullu Biçimlendirme Ekle
description: Aspose.Cells for .NET içinde bir özet tabloya koşullu biçimlendirme ekleyin - kuralı ApplyTo ve PivotConditionFormatScopeType kapsamıyla veri bölgesine bağlayın veya hedefi AddCellArea ve PivotAreas ile tanımlayın, ardından FormatConditions.AddCondition ile kuralları ve stilleri ekleyin
keywords: Aspose.Cells, özet tablo, koşullu biçimlendirme, PivotConditionalFormat, ConditionalFormats, ApplyTo, PivotConditionFormatScopeType, Data, Field, Selection, AddCellArea, PivotAreas, AddPivotArea, FormatConditions, AddCondition, FormatConditionType, C#
type: docs
weight: 30
url: /tr/net/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
Üst sayfada ve yan sayfada açıklanan stiller statiktir - bir `PivotArea` veya `CellArea` bölgesi bir kez boyanır ve değerler ne olursa olsun stilini korur. Koşullu biçimlendirme ise kural‑tabanlı bir biçimlendirmedir - 200'ün üzerindeki her tutarı vurgulamak, ortadaki yüzde elliyi gölgelendirmek veya en alt sıralardaki öğeleri işaretlemek - ve vurgulama, özet tablo yeniden hesaplandığında veya yenilendiğinde değerleri takip eder.  
Aspose.Cells içinde, özet tablo koşullu biçimlendirme `PivotTable.ConditionalFormats` koleksiyonunda bulunur. Her giriş, iki soruyu bağımsız olarak yanıtlayan bir `PivotConditionalFormat` nesnesidir:
- **Kural nerede uygulanır?** Hedef bölge ya `ApplyTo(int row, int column, PivotConditionFormatScopeType scope)` yöntemiyle tanımlanır; bu, Excel kullanıcı arayüzündeki kapsam seçiciyi yansıtır, ya da `AddCellArea(CellArea)` ve `PivotAreas` koleksiyonu aracılığıyla açıkça adlandırılır.
- **Kural neyi test eder?** `FormatConditions` koleksiyonuna bir veya daha fazla koşul, `FormatConditionCollection.AddCondition(FormatConditionType type, OperatorType operatorType, string formula1, string formula2)` yöntemiyle eklenir ve her koşul kendi `Style` nesnesini taşır.

{{% alert color="primary" %}}
`PivotConditionalFormat` nesnesinin `FormatConditions` objesinde `FormatConditionCollection.Add(CellArea cellArea, FormatConditionType type, OperatorType operatorType, string formula1, string formula2)` veya `FormatConditionCollection.AddArea(CellArea)` metodunu çağırmayın. Bu iki aşırı yükleme, normal çalışma sayfası koşullu biçimlendirme API'sinden miras alınmıştır ve özet tablolar için çalışmaz — hücre alanı hiçbir zaman bir pivot alana dönüştürülmez, bu nedenle istek sessizce yok sayılır. Bölgeyi her zaman `PivotConditionalFormat` üzerinde (`ApplyTo`, `AddCellArea` veya `PivotAreas`) tanımlayın ve kuralı `AddCondition` aşırı yüklemelerinden biriyle ekleyin.
{{% /alert %}}

## **Kuralı Kapsamla Uygula (Excel UI Yöntemi)**
İlk yöntem, kuralı Excel kullanıcı arayüzünün yaptığı gibi konumlandırır. Özet tablo içindeki bir hücre, sıfır‑tabanlı çalışma sayfası koordinatlarıyla adlandırılır ve bir `PivotConditionFormatScopeType` kapsamı, Aspose.Cells'e kuralın o hücreden ne kadar uzağa uzanacağını bildirir:
- `PivotConditionFormatScopeType.Data` – özet tablonun ürettiği tüm değer hücreleri, büyük toplamlar dahil.
- `PivotConditionFormatScopeType.Field` – hücrenin tanımladığı alana ait değer hücreleri, büyük toplamlar hariç. Hücre, satır‑alanı etiketi gibi bir alan hücresi olmalıdır; bir değer hücresi gönderilirse istisna fırlatılır.
- `PivotConditionFormatScopeType.Selection` – hücrenin seçtiği kesişimdeki yalnızca değer hücreleri, genellikle tek bir değer hücresi.
Aşağıdaki örnek, sol üst köşesi E3'te bulunan bir meyve‑satışları özet tablosu oluşturur, `Data` kapsamı ile hücre F4'te (satır 3, sütun 5) bir koşullu biçimlendirme sabitler ve 200'ün üzerindeki her tutarı kırmızıda kalın beyaz olarak vurgular. Apple 220, Banana 330, Cherry 200 ve büyük toplam 750 değerleriyle, kural F4, F5 ve F7'yı boyar — çözülmüş bölge tüm veri sütunu F4:F7'dir ve yalnızca kuralı geçen hücreler aydınlanır.

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
// Üst sol köşesi E3'te bulunan pivot tablo
PivotTable pivotTable = sheet.PivotTables.Add("=A1:C7", 2, 4);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.CalculateData();
// Koşullu biçimi F4'te (satır 3, sütun 5) Veri kapsamıyla bağla
int index = pivotTable.ConditionalFormats.Add();
PivotConditionalFormat format = pivotTable.ConditionalFormats[index];
format.ApplyTo(3, 5, PivotConditionFormatScopeType.Data);
// Kural - 200'den büyük miktarları vurgula
int conditionIndex = format.FormatConditions.AddCondition(
    FormatConditionType.CellValue, OperatorType.GreaterThan, "200", null);
Style style = workbook.CreateStyle();
style.Font.IsBold = true;
style.Font.Color = Color.White;
style.ForegroundColor = Color.Red;
style.Pattern = BackgroundType.Solid;
format.FormatConditions[conditionIndex].Style = style;
workbook.Save("PivotConditionalFormatData.xlsx");
```

`Field` kapsamı ile aynı kuralı satır‑alanı etiketi E4'te (satır 3, sütun 4) sabitlediğinizde, bölge F4:F6 olarak çözülür — aynı veri sütunu, ancak büyük‑toplam satırı olmadan — çünkü kapsam artık tüm değer alanı yerine `Fruit` alanını tanımlar. `Selection` kapsamı F4'te sabitlendiğinde sadece F4 çözülür.

## **Bölgeyi Manuel Olarak Tanımla**

### **AddCellArea ile Çalışma Sayfası Dikdörtgeni**
`AddCellArea(CellArea)` verilen dikdörtgeni kuralın hedefi olarak kaydeder. Koordinatlar sıfır‑tabanlı çalışma sayfası koordinatlarıdır ve bölge tam olarak sağlanan dikdörtgendir — veri sütununa genişleme ya da büyük‑toplam mantığı yoktur. İlgili hücreler mevcut özet düzeninin bilinen sabit bir dikdörtgeni olduğunda bunu kullanın.

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
// F4:F6 dikdörtgenini hedefle (büyük toplam olmadan değer hücreleri)
int index = pivotTable.ConditionalFormats.Add();
PivotConditionalFormat format = pivotTable.ConditionalFormats[index];
format.AddCellArea(new CellArea { StartRow = 3, StartColumn = 5, EndRow = 5, EndColumn = 5 });
// Kural - 150 ile 300 arasındaki tutarlar için açık sarı renkte italik
int conditionIndex = format.FormatConditions.AddCondition(
    FormatConditionType.CellValue, OperatorType.Between, "150", "300");
Style style = workbook.CreateStyle();
style.Font.IsItalic = true;
style.ForegroundColor = Color.LightYellow;
style.Pattern = BackgroundType.Solid;
format.FormatConditions[conditionIndex].Style = style;
workbook.Save("PivotConditionalFormatCellArea.xlsx");
```

### **PivotAreas ile Anlamsal Özet Bölgesi**
`PivotAreas`, yan sayfanın statik stiller için kullandığı aynı anlamsal‑bölge modelidir. Bir `PivotArea` oluşturun, `Select` ya da `SelectField` ile bir alan veya bölge seçin ve `PivotAreas.AddPivotArea(PivotArea)` ile ekleyin. Anlamsal bir bölge alanına bağlı kalır, bu yüzden koşullu biçimlendirme özet tablo yenilendiğinde ve yerleşim değiştiğinde alanı takip eder. `PivotAreas.Add(PivotArea)` aşırı yüklemesi hâlâ derlenir ancak kullanım dışı olarak işaretlenmiştir — `AddPivotArea` tercih edin.

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
// Kuralı, Amount veri alanına anlamsal bir bölge olarak ekle
int index = pivotTable.ConditionalFormats.Add();
PivotConditionalFormat format = pivotTable.ConditionalFormats[index];
PivotArea area = new PivotArea(pivotTable);
area.SelectField(PivotFieldType.Data, "Amount");
format.PivotAreas.AddPivotArea(area);
// Kural - 150'nin altındaki tutarlar için gri metin
int conditionIndex = format.FormatConditions.AddCondition(
    FormatConditionType.CellValue, OperatorType.LessThan, "150", null);
Style style = workbook.CreateStyle();
style.Font.Color = Color.Gray;
format.FormatConditions[conditionIndex].Style = style;
workbook.Save("PivotConditionalFormatPivotArea.xlsx");
```

## **Kuralların Nerede Saklandığı ve Yeniden Yüklemede Nasıl Korunduğu**
Her `ConditionalFormats.Add()` çağrısı, özet tabloya bir `PivotConditionalFormat` ekler. Koşullar, formülleri ve stilleri çalışma kitabıyla birlikte kaydedilir — aşağıdaki örnekte dosya yeniden açıldığında aynı kural, tipi, operatörü ve formülü bozulmadan gösterilir ve `GetCellAreas()` aynı bölgeleri rapor eder. Hiç koşul almamış girişler, çalışma kitabı kaydedildiğinde silinir; bu, Excel'in kuralı olmayan bir koşullu biçimlendirmeyi atmasıyla aynı şekildedir.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook("PivotConditionalFormatData.xlsx");
PivotTable pivotTable = workbook.Worksheets[0].PivotTables[0];
Console.WriteLine("Conditional formats: " + pivotTable.ConditionalFormats.Count);
for (int i = 0; i < pivotTable.ConditionalFormats.Count; i++)
{
    PivotConditionalFormat format = pivotTable.ConditionalFormats[i];
    for (int j = 0; j < format.FormatConditions.Count; j++)
    {
        FormatCondition condition = format.FormatConditions[j];
        Console.WriteLine($"Format {i}: {condition.Type} {condition.Operator} formula1={condition.Formula1}");
    }
    foreach (CellArea area in format.GetCellAreas())
        Console.WriteLine($"    rows {area.StartRow + 1}-{area.EndRow + 1}, columns {area.StartColumn + 1}-{area.EndColumn + 1}");
}
// Bu çıktıyı verir:
// Conditional formats: 1
// Format 0: CellValue GreaterThan formula1==200
//     rows 4-7, columns 6-6        (F4:F7, çözülmüş veri bölgesi)
```

## **İlgili Makaleler**
- [Pivot Tablosuna Stil Uygulama](/cells/tr/net/apply-style-to-pivot-table/)
- [Özet Tablosunun Bir Bölümünü Biçimlendirme](/cells/tr/net/format-part-of-pivot-table/)
- [Pivot Tablosunda İlk 10 Göster veya Filtrele](/cells/tr/net/top-10-show-or-filter-in-pivot-table/)
- [Etiket veya Değer ile Özet Tabloları Filtreleme](/cells/tr/net/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="csharp" >}}