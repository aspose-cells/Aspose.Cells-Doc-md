---
title: Aspose.Cells for Java'da Pivot Tablolarına Stil Uygulama
linktitle: Aspose.Cells for Java'da Pivot Tablolarına Stil Uygulama
description: Aspose.Cells for Java'da pivot tablolarına yerleşik ve özel stiller uygulamayı öğrenin; eski XLS otomatik biçimleri, modern Excel 2007+ adlandırılmış stiller, özel pivot tablo stilleri ve FormatAll kısayolu dahil.
keywords: Aspose.Cells Java pivot tablo stili, PivotTableStyleType, AutoFormatType, FormatAll, özel stil, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /tr/java/apply-style-to-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells, hem eski pivot otomatik biçimlerini (`.xls` dosyaları için tasarlanmış) hem de modern adlandırılmış veya özel pivot tablo stillerini (`.xlsx`, `.xlsm` ve `.xlsb` dosyaları için tasarlanmış) uygulamayı destekler. Çağırmanız gereken API, çalışma kitabının yüklendiği formata değil, kaydedildiği dosya biçimine göre belirlenir.
{{% /alert %}}

## **Giriş**
Aspose.Cells, pivot tablolar için iki paralel stil API'si sunar. Aralarındaki seçim, çalışma kitabını okuduğunuz formata değil, kaydettiğiniz dosya biçimine göre belirlenir. Bir `.xls` dosyasından yüklenen çalışma kitabı `.xlsx` olarak yeniden kaydedilebilir ve bu durumda eski stil API'si yerine modern stil API'si geçerlidir.
- `PivotTable.PivotTableStyleType` yerleşik adlandırılmış stillerden birini seçer (açık ve koyu temalar, Excel 2017'de eklenen stiller dahil). Bu hazır ayarlar salt okunurdur.
- `PivotTable.PivotTableStyleName` `Workbook.getWorksheets().getTableStyles().addPivotTableStyle(...)` aracılığıyla kendinizin tanımladığı özel bir stili seçer. Hazır ayarların sunduğundan farklı renkleri, kenarlıkları veya yazı tiplerini değiştirmek istediğinizde özel stiller gereklidir.
Ayrıca `PivotTable.formatAll(Style)`, tek bir `Style` nesnesini pivotun her hücresine uygulayan ve yukarıdaki stil adı API'lerinden herhangi biriyle ayarlananları geçersiz kılan bir kısayoldur. Bu, temel tema ne olursa olsun tek tip bir görünüm gerektiğinde kullanışlıdır.

## **Eski XLS Hazır Otomatik Biçimi Uygulama**
`PivotTable.AutoFormatType`, `com.aspose.cells.PivotTableAutoFormatType` numaralandırmasından bir değer kabul eder. Kullanılabilir değerler `REPORT_1`'den `REPORT_10`'a, `CLASSIC` ve `TABLE_1`'den `TABLE_10`'a kadar olan değerlerdir.
Aşağıdaki örnek yeni bir çalışma kitabı yükler, Fruit/Year/Amount örnek verilerini ekler, bir pivot tablo oluşturur, `PivotTableAutoFormatType.REPORT_5` uygular ve sonucu `.xls` olarak kaydeder.

{{% alert color="primary" %}}
**Neden sütun alanı yok?** Rapor serisi otomatik biçimleri (`Report1`'den `Report10`'a, `Table1`'den `Table10`'a) klasik Excel'de yalnızca satır alanları ve değerleri olan **tek boyutlu pivot tablolar** için tasarlanmıştır — sütun alanı başlıkları için yerleşik stillemeleri yoktur. Pivotunuz sütun alanları gerektiriyorsa, modern Excel'in kullandığı iki boyutlu düzen için tasarlanmış olan [Senaryo 2](#apply-a-modern-named-preset-pivot-table-style) içindeki modern `PivotTableStyleType` hazır ayarlarını kullanın.
{{% /alert %}}

```java
import com.aspose.cells.*;
// Senaryo 1: Eski bir XLS önceden ayarlanmış otomatik biçimi uygula
// Kullanılan API: PivotTable.AutoFormatType
// Hedef dosya formatı: .xls (eski)
// Eksiksiz örnekler ve veri dosyaları için lütfen https://github.com/aspose-cells/Aspose.Cells-for-.NET adresine gidin
// Yeni bir çalışma kitabı oluştur
Workbook workbook = new Workbook();
// İlk çalışma sayfasını al
Worksheet sheet = workbook.getWorksheets().get(0);
// Kaynak verileri başlık satırıyla (Meyve, Yıl, Miktar) doldur
// ve 2020 ile 2021 yılları arasında üzüm, yaban mersini, kivi, kirazı kapsayan 9 veri satırı
sheet.getCells().get(0, 0).putValue("Fruit");
sheet.getCells().get(0, 1).putValue("Year");
sheet.getCells().get(0, 2).putValue("Amount");
sheet.getCells().get(1, 0).putValue("grape");
sheet.getCells().get(1, 1).putValue(2020);
sheet.getCells().get(1, 2).putValue(50);
sheet.getCells().get(2, 0).putValue("blueberry");
sheet.getCells().get(2, 1).putValue(2020);
sheet.getCells().get(2, 2).putValue(30);
sheet.getCells().get(3, 0).putValue("kiwi");
sheet.getCells().get(3, 1).putValue(2020);
sheet.getCells().get(3, 2).putValue(25);
sheet.getCells().get(4, 0).putValue("cherry");
sheet.getCells().get(4, 1).putValue(2020);
sheet.getCells().get(4, 2).putValue(40);
sheet.getCells().get(5, 0).putValue("grape");
sheet.getCells().get(5, 1).putValue(2021);
sheet.getCells().get(5, 2).putValue(60);
sheet.getCells().get(6, 0).putValue("blueberry");
sheet.getCells().get(6, 1).putValue(2021);
sheet.getCells().get(6, 2).putValue(35);
sheet.getCells().get(7, 0).putValue("kiwi");
sheet.getCells().get(7, 1).putValue(2021);
sheet.getCells().get(7, 2).putValue(28);
sheet.getCells().get(8, 0).putValue("cherry");
sheet.getCells().get(8, 1).putValue(2021);
sheet.getCells().get(8, 2).putValue(45);
sheet.getCells().get(9, 0).putValue("grape");
sheet.getCells().get(9, 1).putValue(2020);
sheet.getCells().get(9, 2).putValue(45);
// E3 hedef hücresine, A1:C10 kaynak aralığını kullanarak "Pivot1" adlı bir özet tablo ekle
int pivotIndex = sheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = sheet.getPivotTables().get(pivotIndex);
// Alanları ata: Meyve -> Satırlar, Miktar -> Veri
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
// Eski XLS önceden ayarlanmış "Report5" otomatik biçimini uygula
// Not: Bu özellik yalnızca .xls olarak kaydederken anlamlıdır.
// .xlsx/.xlsm/.xlsb olarak kaydedildiğinde, Excel AutoFormatType'ı yoksayar
// ve PivotTableStyleType / PivotTableStyleName'in belirttiğini kullanır.
pivotTable.setAutoFormatType(PivotTableAutoFormatType.REPORT_5);
// Çalışma kitabını eski .xls formatında kaydet
workbook.save("output.xls");
```

## **Modern Adlandırılmış Hazır Pivot Tablo Stilini Uygulama**

## **Özel Pivot Tablo Stili Tanımlama ve Uygulama**
Yerleşik hazır ayarlar değiştirilemez. Renkleri, kenarlıkları veya yazı tiplerini geçersiz kılmanız gerektiğinde özel bir pivot stili tanımlamalısınız. İş akışı üç adımdan oluşur:
1. `Workbook.getWorksheets().getTableStyles().addPivotTableStyle(String name)` aracılığıyla çalışma kitabının `TableStyles` koleksiyonuna özel bir stil ekleyin. Bu, yeni oluşturulan stilin dizinini döndürür.
2. `TableStyle.getTableStyleElements().add(TableStyleElementType)` aracılığıyla öğeler (örneğin `WholeTable` veya `GrandTotalRow`) ekleyerek stili yapılandırın, ardından `TableStyleElement.setElementStyle(Style)` ile her öğeye bir `Style` atayın.
3. Stili pivot tabloya, `PivotTable.PivotTableStyleName` özelliğini stilin adına ayarlayarak uygulayın. Burada `PivotTableStyleType` kullanmayın, çünkü bu özellik yerleşik hazır ayarları seçer.

{{% alert color="primary" %}}
`PivotTableStyleName` ve `PivotTableStyleType` birbirinin yerine kullanılamaz. Yerleşik hazır ayarlar için `PivotTableStyleType`, `addPivotTableStyle` ile tanımladığınız özel stiller için `PivotTableStyleName` kullanın. İkisini birden ayarlamak zararsızdır, ancak yalnızca amaçlanan kaynağa uygun olan işlenir.
{{% /alert %}}

Kullanılabilir `TableStyleElementType` değerleri arasında `WHOLE_TABLE`, `FIRST_ROW`, `LAST_ROW`, `FIRST_COLUMN`, `LAST_COLUMN`, `GRAND_TOTAL_ROW`, `GRAND_TOTAL_COLUMN`, `PAGE_FIELD_LABELS` ve `PAGE_FIELD_VALUES` bulunur.
Aşağıdaki örnek, `WholeTable` üzerinde ince siyah kenarlık ve `GrandTotalRow` üzerinde kalın kırmızı yazı tipi ile özel bir pivot stili tanımlar, ardından bunu `PivotTableStyleName` aracılığıyla uygular ve `.xlsx` olarak kaydeder.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
// Kaynak verileri doldur: başlık satırı + 9 veri satırı (A1:C10)
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(100);
worksheet.getCells().get("A3").putValue("Blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(200);
worksheet.getCells().get("A4").putValue("Kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(300);
worksheet.getCells().get("A5").putValue("Cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(400);
worksheet.getCells().get("A6").putValue("Grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(500);
worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(600);
worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(700);
worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(800);
worksheet.getCells().get("A10").putValue("Grape");
worksheet.getCells().get("B10").putValue(2021);
worksheet.getCells().get("C10").putValue(900);
// A1:C10'dan kaynaklanan ve E3'e sabitlenen "Pivot1" adlı pivot tablo ekle
int pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
// Adım 1: yeni bir özel pivot tablo stili kaydet ve dizinini yakala
int styleIndex = workbook.getWorksheets().getTableStyles().addPivotTableStyle("CustomPivotStyle");
TableStyle tableStyle = workbook.getWorksheets().getTableStyles().get(styleIndex);
// Adım 2: bir WholeTable öğesi ekle ve dört kenara ince siyah kenarlıklar uygula
int wholeTableElementIndex = tableStyle.getTableStyleElements().add(TableStyleElementType.WHOLE_TABLE);
TableStyleElement wholeTableElement = tableStyle.getTableStyleElements().get(wholeTableElementIndex);
Style wholeTableStyle = workbook.createStyle();
BorderCollection borders = wholeTableStyle.getBorders();
Border borderTop = borders.getByBorderType(BorderType.TOP_BORDER);
borderTop.setLineStyle(CellBorderType.THIN);
borderTop.setColor(Color.getBlack());
Border borderBottom = borders.getByBorderType(BorderType.BOTTOM_BORDER);
borderBottom.setLineStyle(CellBorderType.THIN);
borderBottom.setColor(Color.getBlack());
Border borderLeft = borders.getByBorderType(BorderType.LEFT_BORDER);
borderLeft.setLineStyle(CellBorderType.THIN);
borderLeft.setColor(Color.getBlack());
Border borderRight = borders.getByBorderType(BorderType.RIGHT_BORDER);
borderRight.setLineStyle(CellBorderType.THIN);
borderRight.setColor(Color.getBlack());
wholeTableElement.setElementStyle(wholeTableStyle);
// Adım 3: bir GrandTotalRow öğesi ekle ve kırmızı kalın yazı tipi uygula
int grandTotalElementIndex = tableStyle.getTableStyleElements().add(TableStyleElementType.GRAND_TOTAL_ROW);
TableStyleElement grandTotalElement = tableStyle.getTableStyleElements().get(grandTotalElementIndex);
Style grandTotalStyle = workbook.createStyle();
grandTotalStyle.getFont().setBold(true);
grandTotalStyle.getFont().setColor(Color.getRed());
grandTotalElement.setElementStyle(grandTotalStyle);
// Adım 4: özel stili ada göre uygula (PivotTableStyleType ile DEĞİL, bu yerleşik ön ayarlar içindir)
pivotTable.setPivotTableStyleName("CustomPivotStyle");
workbook.save("output.xlsx");
```

## **FormatAll ile Her Pivot Hücresine Tek Bir Stil Uygulama**
`PivotTable.formatAll(Style)`, tek bir `Style` nesnesini pivot tablonun veri alanı, satır ve sütun başlıkları ve toplamlar dahil her hücresine uygulayan bir kısayoldur. `PivotTableStyleType` veya `PivotTableStyleName` ile daha önce ayarlananlar geçersiz kılınır.

{{% alert color="primary" %}}
`FormatAll`, hem `PivotTableStyleType` hem de `PivotTableStyleName` öğelerini geçersiz kılar. Yalnızca pivot tablonun tamamında temadan bağımsız tek tip bir görünüm gerektiğinde kullanın.
{{% /alert %}}

Aşağıdaki örnek, sarı düz dolgulu, kalın koyu mavi yazı tipli ve tüm kenarlarında ince siyah kenarlıklı bir `Style` oluşturur, ardından bunu `formatAll` ile uygular ve `.xlsx` olarak kaydeder.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
// Kaynak verileri doldur: başlık satırı (satır 1) + 9 veri satırı (satır 2-10)
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(5000);
worksheet.getCells().get("A3").putValue("Blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(3000);
worksheet.getCells().get("A4").putValue("Kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(4000);
worksheet.getCells().get("A5").putValue("Cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(2000);
worksheet.getCells().get("A6").putValue("Grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(6000);
worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(3500);
worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(4500);
worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(2500);
worksheet.getCells().get("A10").putValue("Grape");
worksheet.getCells().get("B10").putValue(2021);
worksheet.getCells().get("C10").putValue(5500);
// Özet tablo ekle: kaynak aralık A1:C10, hedef hücre E3, ad "Pivot1"
int pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);
// Özet tablo alanlarını ata: Fruit -> Satır alanı, Year -> Sütun alanı, Amount -> Veri alanı
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
// Özet tablonun her hücresine uygulanacak bir Stil oluştur
Style style = workbook.createStyle();
style.setForegroundColor(Color.getYellow());
style.setPattern(BackgroundType.SOLID);
style.getFont().setBold(true);
style.getFont().setColor(Color.getDarkBlue());
style.getBorders().getByBorderType(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN);
style.getBorders().getByBorderType(BorderType.TOP_BORDER).setColor(Color.getBlack());
style.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN);
style.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setColor(Color.getBlack());
style.getBorders().getByBorderType(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN);
style.getBorders().getByBorderType(BorderType.LEFT_BORDER).setColor(Color.getBlack());
style.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN);
style.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setColor(Color.getBlack());
// FormatAll uygula: bu tek stili özet tablonun her hücresine zorla uygular,
// daha önce ayarlanmış PivotTableStyleType / PivotTableStyleName değerlerini geçersiz kılar
pivotTable.formatAll(style);
// Çalışma kitabını modern .xlsx formatında kaydet
workbook.save("output.xlsx");
```

## **Hangi Stil API'sini Kullanmalıyım?**
Stil API'si seçimi, kaydettiğiniz dosya biçimine bağlıdır. Hızlı bir başvuru olarak aşağıdaki tabloyu kullanın.
| Hedef dosya biçimi | Kullanılacak API | Notlar |
|---|---|---|
| `.xls` (eski) | `PivotTable.AutoFormatType` | `com.aspose.cells.PivotTableAutoFormatType` değerleri (ör. `REPORT_1`–`REPORT_10`, `CLASSIC`, `TABLE_1`–`TABLE_10`). Modern biçimlerde kaydederken yoksayılır. |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, yerleşik stil) | `PivotTable.PivotTableStyleType` | `com.aspose.cells.PivotTableStyleType` değerleri (açık/koyu temalar, Excel 2017 eklemeleri dahil). |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, özel stil) | `PivotTable.PivotTableStyleName` + `Worksheets.TableStyles.addPivotTableStyle(...)` | Yerleşik hazır ayarlar yeterli olmadığında kullanın. `TableStyleElement.setElementStyle(...)` aracılığıyla yapılandırın. |
| Herhangi bir biçim (tek tip geçersiz kılma) | `PivotTable.formatAll(Style)` | Pivotun tamamında diğer tüm stil ayarlarını geçersiz kılan kısayol. |
Kararsız kaldığınızda, `.xlsx` olarak kaydedin ve yerleşik temalar için `PivotTableStyleType`, özel temalar için `PivotTableStyleName` kullanın.

{{< app/cells/assistant language="java" >}}