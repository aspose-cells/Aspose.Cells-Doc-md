---
title: Aspose.Cells for Java'te PivotTable'lara stil uygulama
linktitle: PivotTable Stillerini Uygulama
description: Aspose.Cells for Java'da pivot tablolara yerleşik ve özel stillerin nasıl uygulanacağını öğrenin; eski XLS otomatik biçimleri, modern Excel 2007+ adlandırılmış stilleri, özel pivot tablo stilleri ve FormatAll kısayolu dahil.
keywords: Aspose.Cells Java pivot tablo stili, PivotTableStyleType, AutoFormatType, FormatAll, özel stil, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /tr/java/apply-style-to-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells hem eski pivot otomatik biçimlerini (`.xls` dosyaları için tasarlanmış) hem de modern adlandırılmış veya özel pivot tablo stillerini (`.xlsx`, `.xlsm` ve `.xlsb` dosyaları için tasarlanmış) uygulamayı destekler. Çağırmanız gereken API, çalışma kitabının yüklendiği formata değil, kaydedildiği dosya formatına bağlıdır.

{{% /alert %}}

## **Giriş**

Aspose.Cells, pivot tablolar için iki paralel stil API'si sunar. Aralarındaki seçim, çalışma kitabını okuduğunuz formata değil, kaydettiğiniz dosya formatına göre belirlenir. Bir `.xls` dosyasından yüklenen çalışma kitabı `.xlsx` olarak yeniden kaydedilebilir ve bu durumda eski stil API'si yerine modern stil API'si geçerli olur.

Eski `.xls` çıktısı için `PivotTable.AutoFormatType` özelliğini `com.aspose.cells.PivotTableAutoFormatType` numaralandırmasıyla birlikte kullanın. Bu API, klasik Excel'in pivot tablolar için sunduğu otomatik biçim seçicisine karşılık gelir.

Modern `.xlsx`, `.xlsm` ve `.xlsb` çıktısı için iki çeşit stil API'si mevcuttur:

- `PivotTable.PivotTableStyleType`, yerleşik adlandırılmış stillerden birini seçer (açık ve koyu temalar, Excel 2017'de eklenen stiller dahil). Bu hazır ayarlar salt okunurdur.
- `PivotTable.PivotTableStyleName`, `Workbook.getWorksheets().getTableStyles().addPivotTableStyle(...)` aracılığıyla kendinizin tanımladığı özel bir stili seçer. Hazır ayarların sunduğunun ötesinde renkleri, kenarlıkları veya yazı tiplerini değiştirmek istediğinizde özel stiller gereklidir.

Ek olarak, `PivotTable.formatAll(Style)`, tek bir `Style` nesnesini pivot tablonun her hücresine uygulayan ve yukarıdaki stil adı API'lerinden herhangi biriyle ayarlananı geçersiz kılan bir kısayoldur. Bu, hangi tema kullanılırsa kullanılsın tek tip bir görünüm gerektiğinde kullanışlıdır.

## **Eski Bir XLS Hazır Otomatik Biçimi Uygulama**

`PivotTable.AutoFormatType`, `com.aspose.cells.PivotTableAutoFormatType` numaralandırmasından bir değer kabul eder. Kullanılabilir değerler `REPORT_1`'den `REPORT_10`'a, `CLASSIC` ve `TABLE_1`'den `TABLE_10`'a kadardır.

{{% alert color="primary" %}}

`AutoFormatType` yalnızca çalışma kitabı `.xls` olarak kaydedildiğinde dikkate alınır. Aynı çalışma kitabı `.xlsx`, `.xlsm` veya `.xlsb` olarak kaydedildiğinde, Excel bu özelliği yok sayar ve `PivotTableStyleType` ile `PivotTableStyleName` ayarlarına geri döner.

{{% /alert %}}

Aşağıdaki örnek, yeni bir çalışma kitabı yükler, Fruit/Year/Amount örnek verilerini doldurur, bir pivot tablo ekler, `PivotTableAutoFormatType.REPORT_5` uygular ve sonucu `.xls` olarak kaydeder.

{{% alert color="primary" %}}

**Neden sütun alanı yok?** Report serisi otomatik biçimleri (`Report1`–`Report10`, `Table1`–`Table10`), klasik Excel'de yalnızca satır alanları ve değerler içeren **tek boyutlu özet tablolar** için tasarlanmıştı — sütun alanı başlıkları için yerleşik bir biçimlendirmeleri yoktur. Özet tablonuzun sütun alanlarına ihtiyacı varsa, bunun yerine aşağıdaki Senaryo 2'deki modern `PivotTableStyleType` ön ayarlarını kullanın; bunlar modern Excel'in kullandığı iki boyutlu düzen için tasarlanmıştır.

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

// Başlık satırıyla (Fruit, Year, Amount) kaynak verileri doldur
// ve 2020 ile 2021 yıllarını kapsayan grape, blueberry, kiwi, cherry için 9 veri satırı
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

// E3 hedef hücresinde, "Pivot1" adında, A1:C10 kaynak aralığını kullanarak bir pivot tablo ekle
int pivotIndex = sheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = sheet.getPivotTables().get(pivotIndex);

// Alanları ata: Fruit -> Satırlar, Year -> Sütunlar, Amount -> Veri
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

// Eski XLS önceden ayarlanmış otomatik biçimi "Report5" uygula
// Not: Bu özellik yalnızca .xls olarak kaydederken anlamlıdır.
// .xlsx/.xlsm/.xlsb olarak kaydedildiğinde, Excel AutoFormatType özelliğini yoksayar
// ve PivotTableStyleType / PivotTableStyleName'in belirttiği biçimi kullanır.
pivotTable.setAutoFormatType(PivotTableAutoFormatType.REPORT_5);

// Çalışma kitabını eski .xls formatında kaydet
workbook.save("output.xls");
```

## **Modern Adlandırılmış Hazır Bir Pivot Tablo Stili Uygulama**

`PivotTable.PivotTableStyleType`, `com.aspose.cells.PivotTableStyleType` numaralandırmasından bir değer kabul eder. Numaralandırma, açık temalar `PIVOT_TABLE_STYLE_LIGHT_1`'den `PIVOT_TABLE_STYLE_LIGHT_28`'e ve koyu temalar `PIVOT_TABLE_STYLE_DARK_1`'den `PIVOT_TABLE_STYLE_DARK_28`'e kadar olan stilleri kapsar. Excel 2017'de eklenen stiller (açık ve koyu temaların ikinci dalgası) aynı numaralandırma aracılığıyla erişilebilir.

Bu, herhangi bir modern dosya formatı için önerilen API'dir. Eski otomatik biçimin aksine, burada seçilen stil Excel tarafından aslına uygun şekilde işlenir ve diğer Office araçlarıyla yapılan gidiş-dönüş işlemlerinde korunur.

Aşağıdaki örnek aynı Fruit/Year/Amount verilerini kullanır, özdeş bir pivot tablo oluşturur, `PIVOT_TABLE_STYLE_DARK_1` uygular ve çalışma kitabını `.xlsx` olarak kaydeder.

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// Başlık satırı: Meyve / Yıl / Tutar
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// 9 satır Meyve / Yıl / Tutar verisi
worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(100);

worksheet.getCells().get("A3").putValue("Blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(150);

worksheet.getCells().get("A4").putValue("Kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(200);

worksheet.getCells().get("A5").putValue("Cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(180);

worksheet.getCells().get("A6").putValue("Grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(120);

worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(170);

worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(210);

worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(190);

worksheet.getCells().get("A10").putValue("Grape");
worksheet.getCells().get("B10").putValue(2021);
worksheet.getCells().get("C10").putValue(130);

// E3 hücresine "Pivot1" adında bir pivot tablo ekle, kaynak olarak A1:C10
int pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Pivot alanlarını ata: Meyve -> Satır alanı, Yıl -> Sütun alanı, Tutar -> Veri alanı
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

// Modern bir Excel 2007+ adlandırılmış ön ayar pivot stili uygula.
// PivotTableStyleType, .xlsx / .xlsm / .xlsb dosyaları için doğru API'dir; AutoFormatType
// bu formatlar için Excel tarafından yok sayılır. PivotTableStyleDark1, koyu tema
// ailesine aittir (PivotTableStyleDark1..PivotTableStyleDark28) ve aynı enum ayrıca
// daha yeni Excel 2017 açık/koyu temalarını da sunar (PivotTableStyleLight1..Light28 / Dark1..Dark28).
pivotTable.setPivotTableStyleType(PivotTableStyleType.PIVOT_TABLE_STYLE_DARK_1);

// Modern .xlsx olarak kaydet - bu, PivotTableStyleType'ın anlamlı olduğu formattır.
workbook.save("output.xlsx");
```

## **Özel Bir Pivot Tablo Stili Tanımlama ve Uygulama**

Yerleşik hazır ayarlar değiştirilemez. Renkleri, kenarlıkları veya yazı tiplerini geçersiz kılmanız gerektiğinde, özel bir pivot stili tanımlamalısınız. İş akışı üç adımdan oluşur:

1. `Workbook.getWorksheets().getTableStyles().addPivotTableStyle(String name)` aracılığıyla çalışma kitabının `TableStyles` koleksiyonuna özel bir stil ekleyin. Bu, yeni oluşturulan stilin dizinini döndürür.
2. `TableStyle.getTableStyleElements().add(TableStyleElementType)` aracılığıyla öğeler (`WholeTable` veya `GrandTotalRow` gibi) ekleyerek, ardından her öğeye `TableStyleElement.setElementStyle(Style)` ile bir `Style` atayarak stili yapılandırın.
3. `PivotTable.PivotTableStyleName` özelliğini stilin adına ayarlayarak özel stili pivota uygulayın. Burada `PivotTableStyleType` kullanmayın, çünkü bu özellik yerleşik hazır ayarları seçer.

{{% alert color="primary" %}}

`PivotTableStyleName` ve `PivotTableStyleType` birbirinin yerine kullanılamaz. Yerleşik hazır ayarlar için `PivotTableStyleType`, `addPivotTableStyle` aracılığıyla tanımladığınız özel stiller için `PivotTableStyleName` kullanın. İkisini birden ayarlamak zararsızdır, ancak yalnızca amaçlanan kaynağa uygun olan işlenir.

{{% /alert %}}

Kullanılabilir `TableStyleElementType` değerleri şunları içerir: `WHOLE_TABLE`, `FIRST_ROW`, `LAST_ROW`, `FIRST_COLUMN`, `LAST_COLUMN`, `GRAND_TOTAL_ROW`, `GRAND_TOTAL_COLUMN`, `PAGE_FIELD_LABELS` ve `PAGE_FIELD_VALUES`.

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

// A1:C10'dan kaynaklanan, E3'e sabitlenmiş, "Pivot1" adlı pivot tablo ekle
int pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

// Adım 1: yeni özel bir pivot tablo stili kaydet ve dizinini yakala
int styleIndex = workbook.getWorksheets().getTableStyles().addPivotTableStyle("CustomPivotStyle");
TableStyle tableStyle = workbook.getWorksheets().getTableStyles().get(styleIndex);

// Adım 2: bir WholeTable öğesi ekle ve dört kenara da ince siyah kenarlıklar uygula
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

// Adım 3: bir GrandTotalRow öğesi ekle ve kalın kırmızı yazı tipi uygula
int grandTotalElementIndex = tableStyle.getTableStyleElements().add(TableStyleElementType.GRAND_TOTAL_ROW);
TableStyleElement grandTotalElement = tableStyle.getTableStyleElements().get(grandTotalElementIndex);
Style grandTotalStyle = workbook.createStyle();
grandTotalStyle.getFont().setBold(true);
grandTotalStyle.getFont().setColor(Color.getRed());
grandTotalElement.setElementStyle(grandTotalStyle);

// Adım 4: özel stili ada göre uygula (yerleşik önayarlar için olan PivotTableStyleType ile DEĞİL)
pivotTable.setPivotTableStyleName("CustomPivotStyle");

workbook.save("output.xlsx");
```

## **FormatAll ile Her Pivot Hücresine Tek Bir Stil Uygulama**

`PivotTable.formatAll(Style)`, pivot tablonun her hücresine (veri alanı, satır ve sütun başlıkları ve toplamlar dahil) tek bir `Style` nesnesi uygulayan bir kısayoldur. `PivotTableStyleType` veya `PivotTableStyleName` aracılığıyla daha önce ayarlanan her şey geçersiz kılınır.

{{% alert color="primary" %}}

`FormatAll`, hem `PivotTableStyleType` hem de `PivotTableStyleName` değerlerini geçersiz kılar. Yalnızca tüm pivot genelinde temadan bağımsız tek tip bir görünüm gerektiğinde kullanın.

{{% /alert %}}

Aşağıdaki örnek, sarı düz dolgu, kalın koyu mavi yazı tipi ve tüm kenarlarda ince siyah kenarlıklar içeren bir `Style` oluşturur, ardından bunu `formatAll` ile uygular ve `.xlsx` olarak kaydeder.

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

// Pivot tablo ekle: kaynak aralığı A1:C10, hedef hücre E3, ad "Pivot1"
int pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Pivot alanlarını ata: Fruit -> Satır alanı, Year -> Sütun alanı, Amount -> Veri alanı
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

// Pivot tablosunun her hücresine uygulanacak bir Style oluştur
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

// FormatAll uygula: bu tek stili pivot tablosunun her hücresine zorla uygular,
// daha önce ayarlanmış olan PivotTableStyleType / PivotTableStyleName öğelerini geçersiz kılar
pivotTable.formatAll(style);

// Çalışma kitabını modern .xlsx formatında kaydet
workbook.save("output.xlsx");
```

## **Hangi Stil API'sini Kullanmalıyım?**

Stil API'si seçimi, kaydettiğiniz dosya formatına bağlıdır. Hızlı bir başvuru olarak aşağıdaki tabloyu kullanın.

| Hedef dosya formatı | Kullanılacak API | Notlar |
|---|---|---|
| `.xls` (eski) | `PivotTable.AutoFormatType` | `com.aspose.cells.PivotTableAutoFormatType` numaralandırmasından değerler (ör. `REPORT_1`–`REPORT_10`, `CLASSIC`, `TABLE_1`–`TABLE_10`). Modern formatlar olarak kaydederken yok sayılır. |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, yerleşik stil) | `PivotTable.PivotTableStyleType` | `com.aspose.cells.PivotTableStyleType` numaralandırmasından değerler (açık/koyu temalar, Excel 2017 eklemeleri dahil). |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, özel stil) | `PivotTable.PivotTableStyleName` + `Worksheets.TableStyles.addPivotTableStyle(...)` | Yerleşik hazır ayarlar yeterli olmadığında kullanın. `TableStyleElement.setElementStyle(...)` aracılığıyla yapılandırın. |
| Herhangi bir format (tek tip geçersiz kılma) | `PivotTable.formatAll(Style)` | Pivot genelinde diğer tüm stil ayarlarını geçersiz kılan kısayol. |

Şüpheye düştüğünüzde, `.xlsx` olarak kaydedin ve yerleşik temalar için `PivotTableStyleType`, özel temalar için `PivotTableStyleName` kullanın.

{{< app/cells/assistant language="java" >}}