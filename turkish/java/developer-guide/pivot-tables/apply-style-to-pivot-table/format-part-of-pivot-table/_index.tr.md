---
title: Pivot Tablosunun Bir Bölümünü Biçimlendirme
description: Aspose.Cells for Java'da bir pivot tablosunun bir bölümünü, stilleri anlamsal PivotArea bölgelerine veya CellArea dikdörtgenlerine PivotTable.format aracılığıyla uygulayarak biçimlendirin; biçimler PivotTable.getPivotFormats içinde depolanır ve pivot tablosu yenilendiğinde korunur.
linktitle: Format Part of a Pivot Table
keywords: Aspose.Cells for Java, Pivot Tablosu, biçim, PivotArea, CellArea, PivotTable.format, PivotFormats, PivotTableSelectionType, LABEL_ONLY, DATA_ONLY, selectField, formatAll, Java
type: docs
weight: 20
url: /tr/java/format-part-of-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
`PivotTable.formatAll` tek bir stili tüm pivot tablosuna uygular ve üst sayfada ele alınmıştır. Etiketler, değerler, toplamlar veya raporun belirli bölgeleri arasında ayrım yapmaz.
Uygulamada, genellikle bir pivot tablosunun yalnızca bir kısmının öne çıkması gerekir. Yaygın hedefler, bir satır alanına ait etiketler, bir alan tarafından üretilen değer hücreleri, büyük toplam satırı veya ilk iki öğe satırı gibi keyfi bir dikdörtgen olabilir.
Bir pivot tablosunun çalışma sayfası hücrelerine doğrudan stil uygulamak aynı şey değildir. Excel, pivot tablo biçimlendirmesini sıradan hücre‑stil kayıtları yerine anlamsal `PivotArea` bölgeleri olarak depolar. Bir pivot‑alan biçimi, bir alanın etiketleri veya veri değerleri gibi bir bölgeye bağlı kalır ve pivot tablo yeniden hesaplandığında, yenilendiğinde veya genişletildiğinde yeniden çözümlenir. Öte yandan, bir hücreye doğrudan yazılan stil, o hücre konumuna aittir ve pivot modeli tarafından izlenmez.
Aspose.Cells, her iki biçimlendirme türünün de mevcut olması için tam `PivotTable.format` aşırı yüklü ailesini sunar:
- `format(PivotArea, Style)` bir stili, `PivotArea.select` veya `PivotArea.selectField` ile oluşturulan anlamsal bir bölgeye sabitler.
- `format(CellArea, Style)` bir stili, pivot tablosu içindeki bir çalışma sayfası dikdörtgenine sabitler.
- `format(int row, int column, Style)` tek bir hücreyi hedef alır.
- `formatAll(Style)` tüm pivot tabloyu biçimlendirir.

## **Bir Pivot Alanını Biçimlendirme**
Anlamsal alan iş akışı, bir vurgunun bir alana veya rapor bölgesine bağlı kalması gerektiğinde önerilen yaklaşımdır.
1. `new PivotArea(pivotTable)` ile bir `PivotArea` oluşturun. Bu nesne, belirli pivot tabloya ait anlamsal bir bölgeyi tanımlar.
2. Belirli bir eksende sıfır tabanlı konumuyla bir alanı `PivotArea.select(PivotFieldType axisType, int fieldPosition, PivotTableSelectionType selectionType)` yöntemiyle seçin.
   - `PivotTableSelectionType.DATA_AND_LABEL` alanın etiketlerini ve verilerini her ikisini de seçer.
   - `PivotTableSelectionType.LABEL_ONLY` yalnızca alanın etiketlerini seçer.
   - `PivotTableSelectionType.DATA_ONLY` yalnızca alanın veri hücrelerini seçer.
3. `PivotArea.selectField(PivotFieldType axisType, String fieldName)` ile bir alanı isme göre seçin. Bir satır alanı isimle seçildiğinde, bölge o alanın öğeleri tarafından üretilen değer hücrelerine çözülür.
4. `Workbook.createStyle()` ile bir `Style` oluşturun, yazı tipini, ön plan rengini ve katı arka plan desenini yapılandırın ve stili `PivotTable.format(area, style)` metoduna iletin.
5. `PivotArea` aşırı yüklemesine yapılan her çağrı, `PivotTable.getPivotFormats()` içine bir `PivotTableFormat` kaydı ekler.
6. Alan‑bağlantılı biçimler, pivot verileri hesaplandığında uygulanır. Bu nedenle, biçimleri uyguladıktan sonra `PivotTable.calculateData()` çağırarak stillerin görünür olmasını sağlayın.
Aşağıdaki örnek, küçük bir meyve‑satış pivot tablosu oluşturur, `Fruit` satır etiketlerini `PivotArea.select` ve `PivotTableSelectionType.LABEL_ONLY` ile biçimler, aynı satır alanı tarafından üretilen değer hücrelerini `PivotArea.selectField` ile biçimler ve ardından pivot tabloyu yeniden hesaplayarak her iki stilin de uygulanmasını sağlar.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();
// Fruit sales data
String[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (int i = 0; i < fruits.length; i++)
{
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
// Pivot table with its top-left corner at E3
PivotTable pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Bold yellow fill on the row field's label cells
Style labelStyle = workbook.createStyle();
labelStyle.getFont().setBold(true);
labelStyle.setForegroundColor(Color.getYellow());
labelStyle.setPattern(BackgroundType.SOLID);
PivotArea labelArea = new PivotArea(pivotTable);
labelArea.select(PivotFieldType.ROW, 0, PivotTableSelectionType.LABEL_ONLY);
pivotTable.format(labelArea, labelStyle);
// Light green fill on the value cells the row field produces
Style valueStyle = workbook.createStyle();
valueStyle.setForegroundColor(Color.getLightGreen());
valueStyle.setPattern(BackgroundType.SOLID);
PivotArea valueArea = new PivotArea(pivotTable);
valueArea.selectField(PivotFieldType.ROW, "Fruit");
pivotTable.format(valueArea, valueStyle);
// Field-anchored formats are painted when the data is calculated
pivotTable.calculateData();
// Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
workbook.save("FormatPivotArea.xlsx");
```

## **Pivot Tablosunun Bir Hücre Alanını Biçimlendirme**
İlgili bölge bir anlamsal pivot bölgesi yerine basit bir çalışma sayfası dikdörtgeni olduğunda `PivotTable.format(CellArea, Style)` kullanın.
`CellArea`, `getStartRow()`, `getStartColumn()`, `getEndRow()` ve `getEndColumn()` özellikleriyle tanımlanır. Değerler sıfır tabanlı çalışma sayfası koordinatlarıdır ve bitiş koordinatları dikdörtgende dahil edilen son satır ve sütunu gösterir; böylece alan, başlangıç konumundan bitiş konumuna kadar olan hücreleri kapsar.
Alan‑bağlantılı bir biçimden farklı olarak, `CellArea` biçimi hücrelere anında uygulanır. Stil görünmesi için başka bir `calculateData()` çağrısına gerek yoktur.
`CellArea` dikdörtgeni etiket hücreleri ve değer hücrelerini birlikte içerebilir. Sonraki bölüm, Aspose.Cells ve Excel'in bu dikdörtgeni içsel olarak nasıl temsil ettiğini açıklar.
Aşağıdaki örnek, pivot tablosunun `E4:F5` dikdörtgenini italik, açık mavi bir stil ile biçimler ve çalışma kitabını başka bir yeniden hesaplama yapmadan kaydeder.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();
String[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (int i = 0; i < fruits.length; i++)
{
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
PivotTable pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Highlight the first two fruit rows (the rectangle E4:F5)
Style highlightStyle = workbook.createStyle();
highlightStyle.getFont().setItalic(true);
highlightStyle.setForegroundColor(Color.fromArgb(0xFF, 0x99, 0xCC, 0xFF));
highlightStyle.setPattern(BackgroundType.SOLID);
CellArea rectangle = new CellArea();
rectangle.StartRow = 3;
rectangle.StartColumn = 4;
rectangle.EndRow = 4;
rectangle.EndColumn = 5;
pivotTable.format(rectangle, highlightStyle);
// E4:F5 is italic on light blue immediately, no recalculation needed
workbook.save("FormatPivotCellArea.xlsx");
```

## **Pivot Alanları ve Hücre Alanları Nasıl Eşlenir**
Excel, pivot tablo biçimlendirmesini sıradan çalışma sayfası hücre‑stil kayıtları yerine `pivotArea` kayıtları olarak depolar. Aynı model Aspose.Cells tarafından da kullanılır; bu nedenle bir biçimlendirme isteği kaydedildiğinde pivot alanlarına dönüştürülür.
Kullanıcı tarafından sağlanan `CellArea` ile dahili olarak depolanan pivot alanları arasındaki ilişki her iki yönde de çok‑çok’tür.
- Bir `CellArea` birden fazla pivot alanı üretebilir. Dikdörtgen hem etiket hem de değer hücrelerini kapsıyorsa, pivot modeli etiket biçimlendirmesini ve veri biçimlendirmesini bağımsız olarak ele aldığı için, alan ayrı etiket ve veri kurallarına ayrılır.
- Bir pivot alanı, birbirinden ayrı birden fazla `CellArea` örneğine çözülebilir. Büyük toplam satırı gibi anlamsal bir bölge veya öğeleri kesintisiz olmayan bir alan, birden çok dikdörtgeni kapsayabilir. Bu nedenle `PivotArea.getCellAreas()` tek bir dikdörtgen yerine bir koleksiyon döndürür.
`PivotTable.format` aracılığıyla gerçekleştirilen her biçimlendirme işlemi `PivotTable.getPivotFormats()` içinde kaydedilir. Her `PivotTableFormat` kaydı, ilişkili `PivotArea` ve ona uygulanan `Style` öğesini gösterir. `PivotArea` aşırı yüklemesi çağrı başına tam bir kayıt eklerken, farklı anlamsal bölgeler içeren bir `CellArea` birden fazla kayıt ekleyebilir.
Depolanan bölgeleri ayırt etmek için, her `PivotArea` `getOnlyLabel()` ve `getOnlyData()` bayraklarını sunar. Aşağıdaki örnek, hem etiketleri hem de değerleri kapsayan tek bir dikdörtgeni biçimler, `PivotTable.getPivotFormats()`'ı inceler ve her depolanan pivot alanının çözüldüğü `CellArea` koordinatlarını yazdırır.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();
String[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (int i = 0; i < fruits.length; i++)
{
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
PivotTable pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
Style highlightStyle = workbook.createStyle();
highlightStyle.getFont().setItalic(true);
highlightStyle.setForegroundColor(Color.fromArgb(0xFF, 0x99, 0xCC, 0xFF));
highlightStyle.setPattern(BackgroundType.SOLID);
// ONE rectangle in...
CellArea rectangle = new CellArea();
rectangle.StartRow = 3;
rectangle.StartColumn = 4;
rectangle.EndRow = 4;
rectangle.EndColumn = 5;
pivotTable.format(rectangle, highlightStyle);
// ...TWO semantic pivot areas out: the label part and the data part are stored separately
System.out.println("Stored formats: " + pivotTable.getPivotFormats().getCount());
for (int i = 0; i < pivotTable.getPivotFormats().getCount(); i++)
{
    PivotArea storedArea = pivotTable.getPivotFormats().get(i).getPivotArea();
    System.out.println("Format " + i + ": OnlyLabel=" + storedArea.getOnlyLabel()
            + ", OnlyData=" + storedArea.getOnlyData());
    for (CellArea resolved : storedArea.getCellAreas())
    {
        System.out.println("    rows " + (resolved.StartRow + 1) + "-" + (resolved.EndRow + 1)
                + ", columns " + (resolved.StartColumn + 1) + "-" + (resolved.EndColumn + 1));
    }
}
// This prints:
// Stored formats: 2
// Format 0: OnlyLabel=true, OnlyData=false
//     rows 4-5, columns 5-5        (E4:E5, the label part)
// Format 1: OnlyLabel=false, OnlyData=true
//     rows 4-5, columns 6-6        (F4:F5, the data part)
workbook.save("FormatPivotAreasMap.xlsx");
```

{{% alert color="primary" %}}
Biçimler, sıradan hücre stilleri yerine pivot alanları olarak depolandığı için yeniden hesaplamalar ve yenilemeler sırasında korunur. Pivot tablo `PivotTable.refreshData` ile yenilendiğinde, `calculateData` ile yeniden hesaplandığında veya kaydedilip yeniden yüklendiğinde, her depolanan pivot alanı bölgesinin mevcut konumuna yeniden çözülür ve stili tekrar uygulanır.
{{% /alert %}}

`select` veya `selectField` ile oluşturulmuş bir `PivotArea` kullanın; vurgunun yenilemeler boyunca bir alana veya anlamsal bir bölgeye bağlı kalması gerektiğinde, ve mevcut pivot‑tablo düzeninde sabit bir dikdörtgeni biçimlendirmek yeterli olduğunda `CellArea` kullanın. Tek hücre `format(int row, int column, Style)` aşırı yüklemesi tek bir hücreyi hedef alır. Tüm pivot tabloyu bir kerede yeniden biçimlendirmek istediğinizde, üst sayfada ele alınan `formatAll` kullanın.

## **İlgili Makaleler**
- [Pivot Tablosuna Stil Uygulama](/cells/tr/java/apply-style-to-pivot-table/)
- [Pivot Tablosu Satır ve Sütun Alanları Ekleme](/cells/tr/java/pivot-table-add-row-and-column-fields/)
- [Pivot Tablosunda Değer Alanlarını Yönetme](/cells/tr/java/manage-value-fields/)
- [Pivot Tablosunu Yenileme](/cells/tr/java/refresh-pivot-table/)

{{< app/cells/assistant language="java" >}}