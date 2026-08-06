---
title: Pivot Tablosunda Sayfa Alanı Düzenini Değiştirme
linktitle: Pivot Tablosunda Sayfa Alanı Düzenini Değiştirme
description: Aspose.Cells for Java kullanarak bir pivot tabloda sayfa alanı bölgesinin düzenini nasıl kontrol edeceğinizi öğrenin; pivot tablonun üst kısmındaki sayfa alanlarının görüntülenme sırası, kaydırma sayısı ve alan sırasının ayarlanması dahil.
keywords: Aspose.Cells, Java kütüphanesi, elektronik tablo, pivot tablosu, sayfa alanı, sayfa alanı sırası, sayfa alanı kaydırma sayısı, sayfa alanını taşı
type: docs
weight: 191
url: /tr/java/change-page-field-layout/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
Bu makale, **Pivot Tablosuna Sayfa Alanı Ekleme** konusunun devamı niteliğindedir. Pivot tablonun üst kısmındaki filtre kontrolleri şeridinin — yani sayfa alanı bölgesinin — görüntülenme sırası, kaydırma sayısı ve alan yeniden sıralaması dahil düzeninin nasıl kontrol edileceğini gösterir.
{{% /alert %}}
## **Giriş**
Microsoft Excel'deki bir Pivot Tablosu, tablonun satır/sütun/veri gövdesinin üzerinde konumlanan özel bir **sayfa alanı bölgesi** sunar. Bu bölge, her sayfa alanı için bir tane olmak üzere bir açılır filtre kontrol şeridi olarak işlenir ve son kullanıcıların pivot tablosunu yıl veya bölge gibi ölçütlere göre dilimlemek için tıkladığı yerdir. Aspose.Cells bu bölgeyi `pivotTable.getPageFields()` koleksiyonu aracılığıyla modeller ve şeridin görsel olarak nasıl yerleştirileceğini kontrol eden üç özellik sunar:
- `pivotTable.getPageFieldOrder()` (bir `Aspose.Cells.PrintOrderType` değeri) ek sayfa alanlarının mevcut alanların *yanına* mı yoksa *altına* mı yerleştirileceğine karar verir.
- `pivotTable.getPageFieldWrapCount()` kaydırmadan önce satır veya sütun başına yerleştirilecek sayfa alanı sayısını ayarlar.
- `pivotTable.getPageFields().move(currIndex, destIndex)` sıralama modunu değiştirmeden sayfa alanlarını yeniden sıralar.
Bu makale, ortak bir veri kümesi üzerinde bu üç işlemin her birini gösteren ve elde edilen düzenleri yan yana karşılaştırabilmeniz için üç kod örneğini adım adım açıklar.
## **Kaynak Veri**
Aşağıdaki üç örnek de bu sekiz satırlık satış verisini `PivotData` adlı bir çalışma sayfasına yükler. Veriler iki sayfa alanı adayı (`Year`, `Region`), bir satır alanı adayı (`Fruit`) ve bir ölçü (`Amount`) içerir; bu da sayfa alanı şeridinin incelenmesini anlamlı kılar.
| Fruit  | Year | Region | Amount |
|--------|------|--------|--------|
| Apple  | 2022 | North  | 150    |
| Apple  | 2023 | North  | 180    |
| Banana | 2022 | South  | 120    |
| Banana | 2023 | South  | 140    |
| Cherry | 2022 | East   | 200    |
| Cherry | 2023 | East   | 220    |
| Grape  | 2022 | West   | 90     |
| Grape  | 2023 | West   | 110    |
Sekiz satırın tamamı her kod örneğinde aynı sırada doldurulur; dolayısıyla senaryolar arasında kaynak veriler hiçbir zaman farklılık göstermez — yalnızca sayfa alanı düzeni özellikleri değişir.
## **Örnek 1: Önce Yukarıdan Aşağıya (Over Then Down)**
İlk senaryoda iki sayfa alanını (`Year`, `Region`) pivot tablosunun üst kısmında **tek bir satırda yan yana** görünecek şekilde yapılandırıyoruz. `Fruit` öğesini satır eksenine atarız, `Year` öğesini sayfa ekseninde birinci, `Region` öğesini ise ikinci sıraya yerleştiririz (`addFieldToArea` çağrılarının sırası başlangıç indeksini belirler), `Amount` (Sum) öğesini veri alanı olarak ekleriz ve ardından `pivotTable.setPageFieldOrder(PrintOrderType.OVER_THEN_DOWN)` ile `pivotTable.setPageFieldWrapCount(2)` ayarlarını yaparız. `OVER_THEN_DOWN` ve kaydırma sayısı 2 ile iki sayfa alanı, pivot tablonun üst kısmında tek bir satırda yatay olarak yan yana yerleştirilir; dolayısıyla şerit genişliği iki olan tek bir satır kaplar.
```java
import com.aspose.cells.*;
import java.io.File;

String dataDir = "output";
if (!new File(dataDir).exists()) new File(dataDir).mkdirs();

Workbook workbook = new Workbook();
WorksheetCollection worksheets = workbook.getWorksheets();

Worksheet pivotDataSheet = worksheets.add("PivotData");
Cells pivotDataCells = pivotDataSheet.getCells();

// Başlıklar (satır 0)
pivotDataCells.get(0, 0).putValue("Fruit");
pivotDataCells.get(0, 1).putValue("Year");
pivotDataCells.get(0, 2).putValue("Region");
pivotDataCells.get(0, 3).putValue("Amount");

// Satır 1: Apple, 2022, North, 150
pivotDataCells.get(1, 0).putValue("Apple");
pivotDataCells.get(1, 1).putValue(2022);
pivotDataCells.get(1, 2).putValue("North");
pivotDataCells.get(1, 3).putValue(150);

// Satır 2: Apple, 2023, North, 180
pivotDataCells.get(2, 0).putValue("Apple");
pivotDataCells.get(2, 1).putValue(2023);
pivotDataCells.get(2, 2).putValue("North");
pivotDataCells.get(2, 3).putValue(180);

// Satır 3: Banana, 2022, South, 120
pivotDataCells.get(3, 0).putValue("Banana");
pivotDataCells.get(3, 1).putValue(2022);
pivotDataCells.get(3, 2).putValue("South");
pivotDataCells.get(3, 3).putValue(120);

// Satır 4: Banana, 2023, South, 140
pivotDataCells.get(4, 0).putValue("Banana");
pivotDataCells.get(4, 1).putValue(2023);
pivotDataCells.get(4, 2).putValue("South");
pivotDataCells.get(4, 3).putValue(140);

// Satır 5: Cherry, 2022, East, 200
pivotDataCells.get(5, 0).putValue("Cherry");
pivotDataCells.get(5, 1).putValue(2022);
pivotDataCells.get(5, 2).putValue("East");
pivotDataCells.get(5, 3).putValue(200);

// Satır 6: Cherry, 2023, East, 220
pivotDataCells.get(6, 0).putValue("Cherry");
pivotDataCells.get(6, 1).putValue(2023);
pivotDataCells.get(6, 2).putValue("East");
pivotDataCells.get(6, 3).putValue(220);

// Satır 7: Grape, 2022, West, 90
pivotDataCells.get(7, 0).putValue("Grape");
pivotDataCells.get(7, 1).putValue(2022);
pivotDataCells.get(7, 2).putValue("West");
pivotDataCells.get(7, 3).putValue(90);

// Satır 8: Grape, 2023, West, 110
pivotDataCells.get(8, 0).putValue("Grape");
pivotDataCells.get(8, 1).putValue(2023);
pivotDataCells.get(8, 2).putValue("West");
pivotDataCells.get(8, 3).putValue(110);

// PivotTableReport sayfasını ekle
Worksheet pivotTableSheet = worksheets.add("PivotTableReport");
PivotTableCollection pivotTables = pivotTableSheet.getPivotTables();

// PivotData!A1:D9'dan kaynaklanan ve PivotTableReport üzerinde A1'e yerleştirilen pivot tablo oluştur
int pivotIndex = pivotTables.add("PivotData!A1:D9", "A1", "PivotTable1");
PivotTable pivotTable = pivotTables.get(pivotIndex);

// Alanları ekle
pivotTable.addFieldToArea(PivotFieldType.ROW, 0);   // Fruit
pivotTable.addFieldToArea(PivotFieldType.PAGE, 1);  // Year
pivotTable.addFieldToArea(PivotFieldType.PAGE, 2);  // Region
pivotTable.addFieldToArea(PivotFieldType.DATA, 3);  // Amount
pivotTable.getDataFields().get(0).setFunction(ConsolidationFunction.SUM);

// Sayfa alanı düzenini yapılandır: sayfa alanlarını önce yatay olarak yerleştir, her 2 alandan sonra alt satıra geç
pivotTable.setPageFieldOrder(PrintOrderType.OVER_THEN_DOWN);
pivotTable.setPageFieldWrapCount(2);

// Yenile ve hesapla
pivotTable.calculateData();

// Kaydet
workbook.save(dataDir + "/pageFieldLayout_overThenDown.xlsx");
```
## **Örnek 2: Önce Aşağıdan Yukarıya (Down Then Over)**
Bu örnekte `Fruit` öğesini satır eksenine, `Year` ve `Region` öğelerini sayfa eksenine (`Year` birinci sırada olacak şekilde) ve `Amount` (Sum) öğesini veri alanı olarak Örnek 1'deki gibi yerleştiriyoruz. Ardından `pivotTable.setPageFieldOrder(PrintOrderType.DOWN_THEN_OVER)` ve `pivotTable.setPageFieldWrapCount(2)` ayarlarını yaparız. `DOWN_THEN_OVER` ve kaydırma sayısı 2 ile iki sayfa alanı dikey olarak istiflenir — `Year` üstte, `Region` doğrudan altında — ve pivot tablonun üst kısmında tek bir sütun oluşturur. Dolayısıyla şerit, Örnek 1'in aksine, genişliği bir olan iki satır kaplar.
```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet pivotData = workbook.getWorksheets().get(0);
pivotData.setName("PivotData");
int pivotReportIdx = workbook.getWorksheets().add();
Worksheet pivotReport = workbook.getWorksheets().get(pivotReportIdx);
pivotReport.setName("PivotTableReport");

String[] headers = new String[] { "Fruit", "Year", "Region", "Amount" };
for (int c = 0; c < headers.length; c++)
{
    pivotData.getCells().get(0, c).putValue(headers[c]);
}

Object[][] data = new Object[][]
{
    {"Apple", 2022, "North", 150},
    {"Apple", 2023, "North", 180},
    {"Banana", 2022, "South", 120},
    {"Banana", 2023, "South", 140},
    {"Cherry", 2022, "East", 200},
    {"Cherry", 2023, "East", 220},
    {"Grape", 2022, "West", 90},
    {"Grape", 2023, "West", 110}
};

for (int r = 0; r < data.length; r++)
{
    for (int c = 0; c < data[r].length; c++)
    {
        pivotData.getCells().get(r + 1, c).putValue(data[r][c]);
    }
}

int idx = pivotReport.getPivotTables().add("PivotData!A1:D9", "A1", "PivotTable");
PivotTable pivotTable = pivotReport.getPivotTables().get(idx);

pivotTable.addFieldToArea(PivotFieldType.ROW, 0);
pivotTable.addFieldToArea(PivotFieldType.PAGE, 1);
pivotTable.addFieldToArea(PivotFieldType.PAGE, 2);
pivotTable.addFieldToArea(PivotFieldType.DATA, 3);

pivotTable.setPageFieldOrder(PrintOrderType.DOWN_THEN_OVER);
pivotTable.setPageFieldWrapCount(2);

pivotTable.calculateData();

workbook.save("pageFieldLayout_downThenOver.xlsx");
```
## **Örnek 3: Sayfa Alanını Taşıma**
Üçüncü senaryoda bu veri kümesini ve alan atamasını koruyoruz, nötr bir düzen (`OVER_THEN_DOWN` ve kaydırma sayısı `2`) ayarlıyoruz ve ardından `pageFields.move` işlemini gösteriyoruz. `move(0, 1)` çağrısı, 0 indeksindeki sayfa alanını (`Year`) 1 konumuna taşır ve 1 konumundaki sayfa alanı (`Region`) 0 konumuna kayar. Bu çağrıdan sonra `Region` birinci sayfa alanı, `Year` ise ikinci sayfa alanı olur. Kaydırma ve sıralama modu değişmediğinden şerit yine yatay olarak yan yana işlenir — yalnızca iki açılır menünün sırası değiştirilmiş olur.
```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();

Worksheet dataSheet = workbook.getWorksheets().get(0);
dataSheet.setName("PivotData");

dataSheet.getCells().get("A1").putValue("Fruit");
dataSheet.getCells().get("B1").putValue("Year");
dataSheet.getCells().get("C1").putValue("Region");
dataSheet.getCells().get("D1").putValue("Amount");

dataSheet.getCells().get("A2").putValue("Apple");
dataSheet.getCells().get("B2").putValue(2022);
dataSheet.getCells().get("C2").putValue("North");
dataSheet.getCells().get("D2").putValue(150);

dataSheet.getCells().get("A3").putValue("Apple");
dataSheet.getCells().get("B3").putValue(2023);
dataSheet.getCells().get("C3").putValue("North");
dataSheet.getCells().get("D3").putValue(180);

dataSheet.getCells().get("A4").putValue("Banana");
dataSheet.getCells().get("B4").putValue(2022);
dataSheet.getCells().get("C4").putValue("South");
dataSheet.getCells().get("D4").putValue(120);

dataSheet.getCells().get("A5").putValue("Banana");
dataSheet.getCells().get("B5").putValue(2023);
dataSheet.getCells().get("C5").putValue("South");
dataSheet.getCells().get("D5").putValue(140);

dataSheet.getCells().get("A6").putValue("Cherry");
dataSheet.getCells().get("B6").putValue(2022);
dataSheet.getCells().get("C6").putValue("East");
dataSheet.getCells().get("D6").putValue(200);

dataSheet.getCells().get("A7").putValue("Cherry");
dataSheet.getCells().get("B7").putValue(2023);
dataSheet.getCells().get("C7").putValue("East");
dataSheet.getCells().get("D7").putValue(220);

dataSheet.getCells().get("A8").putValue("Grape");
dataSheet.getCells().get("B8").putValue(2022);
dataSheet.getCells().get("C8").putValue("West");
dataSheet.getCells().get("D8").putValue(90);

dataSheet.getCells().get("A9").putValue("Grape");
dataSheet.getCells().get("B9").putValue(2023);
dataSheet.getCells().get("C9").putValue("West");
dataSheet.getCells().get("D9").putValue(110);

Worksheet pivotSheet = workbook.getWorksheets().add("PivotTableReport");

int pivotIdx = pivotSheet.getPivotTables().add("PivotData!A1:D9", "A3", "PivotTable");
PivotTable pivotTable = pivotSheet.getPivotTables().get(pivotIdx);

pivotTable.addFieldToArea(PivotFieldType.ROW, 0);
pivotTable.addFieldToArea(PivotFieldType.PAGE, 1);
pivotTable.addFieldToArea(PivotFieldType.PAGE, 2);
pivotTable.addFieldToArea(PivotFieldType.DATA, 3);

pivotTable.setPageFieldOrder(PrintOrderType.OVER_THEN_DOWN);
pivotTable.setPageFieldWrapCount(2);

pivotTable.getPageFields().move(0, 1);

pivotTable.calculateData();

workbook.save("pageFieldLayout_move.xlsx");
```
## **İlgili Makaleler**
- [Pivot Tablosuna Sayfa Alanı Ekleme](/cells/tr/java/add-page-field-in-pivot-table/) — sayfa alanlarının bir pivot tabloya nasıl ekleneceğini tanıtan ana sayfa.
- [Pivot Tablosunda Satır ve Sütun Alanları](/cells/tr/java/row-and-column-fields/) — burada gösterilen sayfa ekseni çalışmasını tamamlayan şekilde alanların satır ve sütun eksenlerine atanmasını ele alır.
- [Pivot Tablosunda Değer Alanlarını Yönetme](/cells/tr/java/manage-value-fields/) — bu makalede kullanılan `Sum` toplama işlemi dahil veri (değer) alanının nasıl yapılandırılacağını açıklar.
- [Pivot Tablosunu Yenileme](/cells/tr/java/refresh-pivot-table/) — sayfa alanları yeniden sıralandıktan sonra gerekli olan `refreshData()` ve `calculateData()` çağrılarını açıklar.
- [Pivot Tablosuna Stil Uygulama](/cells/tr/java/apply-style-to-pivot-table/) — sayfa alanı şeridi yerleştirildikten sonra işlenmiş pivot tablonun nasıl biçimlendirileceğini gösterir.
{{< app/cells/assistant language="java" >}}