---
title: Aspose.Cells for C++'te PivotTable'lara stil uygulama
linktitle: PivotTable Stillerini Uygulama
description: Aspose.Cells for C++ içinde yerleşik ve özel stillerin pivot tablolara nasıl uygulanacağını öğrenin; eski XLS otomatik biçimleri, modern Excel 2007+ adlandırılmış stilleri, özel pivot tablo stilleri ve FormatAll kısayolu dahil.
keywords: Aspose.Cells C++ pivot tablo stili, PivotTableStyleType, AutoFormatType, FormatAll, özel stil, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /tr/cpp/apply-style-to-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells, hem eski pivot otomatik biçimlerini (`.xls` dosyaları için tasarlanmış) hem de modern adlandırılmış veya özel pivot tablo stillerini (`.xlsx`, `.xlsm` ve `.xlsb` dosyaları için tasarlanmış) uygulamayı destekler. Çağırmanız gereken API, çalışma kitabının yüklendiği formata değil, kaydedildiği dosya biçimine bağlıdır.

{{% /alert %}}

## **Giriş**

Aspose.Cells, pivot tablolar için iki paralel stil API'si sunar. Bunlar arasındaki seçim, okuduğunuz formata değil, çalışma kitabını kaydettiğiniz dosya biçimine göre belirlenir. Bir `.xls` dosyasından yüklenen çalışma kitabı `.xlsx` olarak yeniden kaydedilebilir; bu durumda eski API yerine modern stil API'si geçerli olur.

Eski `.xls` çıktısı için `PivotTable.AutoFormatType` özelliğini `Aspose.Cells.Pivot.PivotTableAutoFormatType` numaralandırmasıyla birlikte kullanın. Bu API, klasik Excel'in pivot tablolar için sunduğu otomatik biçim seçiciye karşılık gelir.

Modern `.xlsx`, `.xlsm` ve `.xlsb` çıktısı için iki çeşit stil API'si mevcuttur:

- `PivotTable.PivotTableStyleType`, yerleşik adlandırılmış stillerden birini seçer (açık ve koyu temalar, Excel 2017'de eklenen stiller dahil). Bu ön ayarlar salt okunurdur.
- `PivotTable.PivotTableStyleName`, `Worksheets.TableStyles.AddPivotTableStyle(...)` aracılığıyla kendinizin tanımladığı özel bir stili seçer. Ön ayarların sunduğundan farklı renkleri, kenarlıkları veya yazı tiplerini değiştirmek istediğinizde özel stiller gereklidir.

Ek olarak, `PivotTable.FormatAll(Style)`, tek bir `Style` nesnesini pivot tablonun her hücresine uygulayan ve yukarıdaki stil adı API'lerinden hangisi kullanılırsa kullanılsın üzerine yazan bir kısayoldur. Bu, altta yatan temadan bağımsız olarak tek tip bir görünüm gerektiğinde kullanışlıdır.

## **Eski XLS Ön Ayar Otomatik Biçimini Uygulama**

`PivotTable.AutoFormatType`, `Aspose.Cells.Pivot.PivotTableAutoFormatType` numaralandırmasından bir değer kabul eder. Kullanılabilir değerler `Report1` ile `Report10`, `Classic` ve `Table1` ile `Table10` arasındadır.

{{% alert color="primary" %}}

`AutoFormatType` yalnızca çalışma kitabı `.xls` olarak kaydedildiğinde dikkate alınır. Aynı çalışma kitabı `.xlsx`, `.xlsm` veya `.xlsb` olarak kaydedildiğinde Excel bu özelliği yoksayar ve `PivotTableStyleType` ile `PivotTableStyleName` ayarlarına geri döner.

{{% /alert %}}

Aşağıdaki örnek yeni bir çalışma kitabı yükler, Fruit/Year/Amount örnek verilerini doldurur, bir pivot tablo ekler, `PivotTableAutoFormatType.Report5` uygular ve sonucu `.xls` olarak kaydeder.

{{% alert color="primary" %}}

**Neden sütun alanı yok?** Report serisi otomatik biçimleri (`Report1`–`Report10`, `Table1`–`Table10`), klasik Excel'de yalnızca satır alanları ve değerler içeren **tek boyutlu özet tablolar** için tasarlanmıştı — sütun alanı başlıkları için yerleşik bir biçimlendirmeleri yoktur. Özet tablonuzun sütun alanlarına ihtiyacı varsa, bunun yerine aşağıdaki Senaryo 2'deki modern `PivotTableStyleType` ön ayarlarını kullanın; bunlar modern Excel'in kullandığı iki boyutlu düzen için tasarlanmıştır.

{{% /alert %}}

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Yeni bir çalışma kitabı oluştur
    Workbook workbook;

    // İlk çalışma sayfasını al
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Başlık satırı (Fruit, Year, Amount) ile kaynak verileri doldur
    // ve 2020 ve 2021 yıllarında üzüm, yaban mersini, kivi, kiraz'ı kapsayan 9 veri satırı
    sheet.GetCells().Get(0, 0).PutValue(u"Fruit");
    sheet.GetCells().Get(0, 1).PutValue(u"Year");
    sheet.GetCells().Get(0, 2).PutValue(u"Amount");

    sheet.GetCells().Get(1, 0).PutValue(u"grape");
    sheet.GetCells().Get(1, 1).PutValue(2020);
    sheet.GetCells().Get(1, 2).PutValue(50);

    sheet.GetCells().Get(2, 0).PutValue(u"blueberry");
    sheet.GetCells().Get(2, 1).PutValue(2020);
    sheet.GetCells().Get(2, 2).PutValue(30);

    sheet.GetCells().Get(3, 0).PutValue(u"kiwi");
    sheet.GetCells().Get(3, 1).PutValue(2020);
    sheet.GetCells().Get(3, 2).PutValue(25);

    sheet.GetCells().Get(4, 0).PutValue(u"cherry");
    sheet.GetCells().Get(4, 1).PutValue(2020);
    sheet.GetCells().Get(4, 2).PutValue(40);

    sheet.GetCells().Get(5, 0).PutValue(u"grape");
    sheet.GetCells().Get(5, 1).PutValue(2021);
    sheet.GetCells().Get(5, 2).PutValue(60);

    sheet.GetCells().Get(6, 0).PutValue(u"blueberry");
    sheet.GetCells().Get(6, 1).PutValue(2021);
    sheet.GetCells().Get(6, 2).PutValue(35);

    sheet.GetCells().Get(7, 0).PutValue(u"kiwi");
    sheet.GetCells().Get(7, 1).PutValue(2021);
    sheet.GetCells().Get(7, 2).PutValue(28);

    sheet.GetCells().Get(8, 0).PutValue(u"cherry");
    sheet.GetCells().Get(8, 1).PutValue(2021);
    sheet.GetCells().Get(8, 2).PutValue(45);

    sheet.GetCells().Get(9, 0).PutValue(u"grape");
    sheet.GetCells().Get(9, 1).PutValue(2020);
    sheet.GetCells().Get(9, 2).PutValue(45);

    // E3 hedef hücresine, "Pivot1" adıyla, A1:C10 kaynak aralığını kullanarak bir pivot tablo ekle
    int pivotIndex = sheet.GetPivotTables().Add(u"A1:C10", u"E3", u"Pivot1");
    PivotTable pivotTable = sheet.GetPivotTables().Get(pivotIndex);

    // Alanları ata: Fruit -> Satırlar, Year -> Sütunlar, Amount -> Veri
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // Eski XLS hazır otomatik biçimi "Report5" uygula
    pivotTable.SetAutoFormatType(PivotTableAutoFormatType::Report5);

    // Çalışma kitabını eski .xls formatında kaydet
    workbook.Save(u"output.xls");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Modern Adlandırılmış Ön Ayar Pivot Tablo Stilini Uygulama**

`PivotTable.PivotTableStyleType`, `Aspose.Cells.PivotTableStyleType` numaralandırmasından bir değer kabul eder. Numaralandırma, `PivotTableStyleLight1` ile `PivotTableStyleLight28` arasındaki açık temaları ve `PivotTableStyleDark1` ile `PivotTableStyleDark28` arasındaki koyu temaları kapsar. Excel 2017'de eklenen stiller (açık ve koyu temaların ikinci dalgası) aynı numaralandırma üzerinden erişilebilir.

Bu, modern dosya biçimleri için önerilen API'dir. Eski otomatik biçimden farklı olarak, burada seçilen stil Excel tarafından aslına uygun şekilde işlenir ve diğer Office araçlarıyla yapılan gidiş-dönüş işlemlerinde kaybolmaz.

Aşağıdaki örnek aynı Fruit/Year/Amount verilerini kullanır, özdeş bir pivot tablo oluşturur, `PivotTableStyleDark1` uygular ve çalışma kitabını `.xlsx` olarak kaydeder.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");

    cells.Get(u"A2").PutValue(u"Grape");
    cells.Get(u"B2").PutValue(2020);
    cells.Get(u"C2").PutValue(100);

    cells.Get(u"A3").PutValue(u"Blueberry");
    cells.Get(u"B3").PutValue(2020);
    cells.Get(u"C3").PutValue(150);

    cells.Get(u"A4").PutValue(u"Kiwi");
    cells.Get(u"B4").PutValue(2020);
    cells.Get(u"C4").PutValue(200);

    cells.Get(u"A5").PutValue(u"Cherry");
    cells.Get(u"B5").PutValue(2020);
    cells.Get(u"C5").PutValue(180);

    cells.Get(u"A6").PutValue(u"Grape");
    cells.Get(u"B6").PutValue(2021);
    cells.Get(u"C6").PutValue(120);

    cells.Get(u"A7").PutValue(u"Blueberry");
    cells.Get(u"B7").PutValue(2021);
    cells.Get(u"C7").PutValue(170);

    cells.Get(u"A8").PutValue(u"Kiwi");
    cells.Get(u"B8").PutValue(2021);
    cells.Get(u"C8").PutValue(210);

    cells.Get(u"A9").PutValue(u"Cherry");
    cells.Get(u"B9").PutValue(2021);
    cells.Get(u"C9").PutValue(190);

    cells.Get(u"A10").PutValue(u"Grape");
    cells.Get(u"B10").PutValue(2021);
    cells.Get(u"C10").PutValue(130);

    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C10", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    pivotTable.SetPivotTableStyleType(PivotTableStyleType::PivotTableStyleDark1);

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Özel Bir Pivot Tablo Stili Tanımlama ve Uygulama**

Yerleşik ön ayarlar değiştirilemez. Renkleri, kenarlıkları veya yazı tiplerini geçersiz kılmanız gerektiğinde özel bir pivot stili tanımlamalısınız. İş akışı üç adımdan oluşur:

1. `Worksheets.TableStyles.AddPivotTableStyle(string name)` aracılığıyla çalışma kitabının `TableStyles` koleksiyonuna özel bir stil ekleyin. Bu, yeni oluşturulan stilin dizinini döndürür.
2. `TableStyle.TableStyleElements.Add(TableStyleElementType)` aracılığıyla öğeler (`WholeTable` veya `GrandTotalRow` gibi) ekleyerek stili yapılandırın, ardından her öğeye `TableStyleElement.SetElementStyle(Style)` aracılığıyla bir `Style` atayın.
3. `PivotTable.PivotTableStyleName` özelliğini stilin adına ayarlayarak özel stili pivota uygulayın. Bu özellik yerleşik ön ayarları seçtiğinden burada `PivotTableStyleType` kullanmayın.

{{% alert color="primary" %}}

`PivotTableStyleName` ve `PivotTableStyleType` birbirinin yerine kullanılamaz. Yerleşik ön ayarlar için `PivotTableStyleType`, `AddPivotTableStyle` aracılığıyla tanımladığınız özel stiller için `PivotTableStyleName` kullanın. İkisini birden ayarlamak zararsızdır, ancak yalnızca amaçlanan kaynağa uyan işlenir.

{{% /alert %}}

Kullanılabilir `TableStyleElementType` değerleri `WholeTable`, `FirstRow`, `LastRow`, `FirstColumn`, `LastColumn`, `GrandTotalRow`, `GrandTotalColumn`, `PageFieldLabels` ve `PageFieldValues` öğelerini içerir.

Aşağıdaki örnek, `WholeTable` üzerinde ince siyah kenarlık ve `GrandTotalRow` üzerinde kırmızı kalın yazı tipi içeren özel bir pivot stili tanımlar, ardından bunu `PivotTableStyleName` aracılığıyla uygular ve `.xlsx` olarak kaydeder.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    Cells cells = worksheet.GetCells();

    // Kaynak verileri doldur: başlık satırı + 9 veri satırı (A1:C10)
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");

    cells.Get(u"A2").PutValue(u"Grape");
    cells.Get(u"B2").PutValue(2020);
    cells.Get(u"C2").PutValue(100);

    cells.Get(u"A3").PutValue(u"Blueberry");
    cells.Get(u"B3").PutValue(2020);
    cells.Get(u"C3").PutValue(200);

    cells.Get(u"A4").PutValue(u"Kiwi");
    cells.Get(u"B4").PutValue(2020);
    cells.Get(u"C4").PutValue(300);

    cells.Get(u"A5").PutValue(u"Cherry");
    cells.Get(u"B5").PutValue(2020);
    cells.Get(u"C5").PutValue(400);

    cells.Get(u"A6").PutValue(u"Grape");
    cells.Get(u"B6").PutValue(2021);
    cells.Get(u"C6").PutValue(500);

    cells.Get(u"A7").PutValue(u"Blueberry");
    cells.Get(u"B7").PutValue(2021);
    cells.Get(u"C7").PutValue(600);

    cells.Get(u"A8").PutValue(u"Kiwi");
    cells.Get(u"B8").PutValue(2021);
    cells.Get(u"C8").PutValue(700);

    cells.Get(u"A9").PutValue(u"Cherry");
    cells.Get(u"B9").PutValue(2021);
    cells.Get(u"C9").PutValue(800);

    cells.Get(u"A10").PutValue(u"Grape");
    cells.Get(u"B10").PutValue(2021);
    cells.Get(u"C10").PutValue(900);

    // A1:C10'dan kaynaklanan, E3'e sabitlenmiş ve "Pivot1" adlı pivot tablo ekle
    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C10", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // Adım 1: yeni bir özel pivot tablo stili kaydet ve dizinini yakala
    int styleIndex = workbook.GetWorksheets().GetTableStyles().AddPivotTableStyle(u"CustomPivotStyle");
    TableStyle tableStyle = workbook.GetWorksheets().GetTableStyles().Get(styleIndex);

    // Adım 2: bir WholeTable öğesi ekle ve dört tarafa ince siyah kenarlık uygula
    int wholeTableElementIndex = tableStyle.GetTableStyleElements().Add(TableStyleElementType::WholeTable);
    TableStyleElement wholeTableElement = tableStyle.GetTableStyleElements().Get(wholeTableElementIndex);
    Style wholeTableStyle = workbook.CreateStyle();
    wholeTableStyle.GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Thin);
    wholeTableStyle.GetBorders().Get(BorderType::TopBorder).SetColor(Color::Black());
    wholeTableStyle.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Thin);
    wholeTableStyle.GetBorders().Get(BorderType::BottomBorder).SetColor(Color::Black());
    wholeTableStyle.GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Thin);
    wholeTableStyle.GetBorders().Get(BorderType::LeftBorder).SetColor(Color::Black());
    wholeTableStyle.GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Thin);
    wholeTableStyle.GetBorders().Get(BorderType::RightBorder).SetColor(Color::Black());
    wholeTableElement.SetElementStyle(wholeTableStyle);

    // Adım 3: bir GrandTotalRow öğesi ekle ve kalın kırmızı yazı tipi uygula
    int grandTotalElementIndex = tableStyle.GetTableStyleElements().Add(TableStyleElementType::GrandTotalRow);
    TableStyleElement grandTotalElement = tableStyle.GetTableStyleElements().Get(grandTotalElementIndex);
    Style grandTotalStyle = workbook.CreateStyle();
    grandTotalStyle.GetFont().SetIsBold(true);
    grandTotalStyle.GetFont().SetColor(Color::Red());
    grandTotalElement.SetElementStyle(grandTotalStyle);

    // Adım 4: özel stili ada göre uygula (yerleşik ön ayarlar için olan PivotTableStyleType'a göre DEĞİL)
    pivotTable.SetPivotTableStyleName(u"CustomPivotStyle");

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **FormatAll ile Her Pivot Hücresine Tek Bir Stil Uygulama**

`PivotTable.FormatAll(Style)`, pivot tablonun veri alanı, satır ve sütun başlıkları ile toplamlar dahil her hücresine tek bir `Style` nesnesi uygulayan bir kısayoldur. `PivotTableStyleType` veya `PivotTableStyleName` aracılığıyla daha önce ayarlanmış olan her şey geçersiz kılınır.

{{% alert color="primary" %}}

`FormatAll`, hem `PivotTableStyleType` hem de `PivotTableStyleName` üzerine yazar. Bunu yalnızca pivotun tamamında temadan bağımsız tek tip bir görünüm gerektiğinde kullanın.

{{% /alert %}}

Aşağıdaki örnek, sarı düz dolgu, kalın koyu mavi yazı tipi ve tüm kenarlarda ince siyah kenarlıklar içeren bir `Style` oluşturur, ardından bunu `FormatAll` ile uygular ve `.xlsx` olarak kaydeder.

```cpp
#include "Aspose.Cells.h"
#include <string>

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
    Aspose::Cells::Startup();

    Workbook wb;
    Worksheet worksheet = wb.GetWorksheets().Get(0);

    // Başlık satırı
    worksheet.GetCells().Get(u"A1").PutValue(u"Fruit");
    worksheet.GetCells().Get(u"B1").PutValue(u"Year");
    worksheet.GetCells().Get(u"C1").PutValue(u"Amount");

    // Veri satırları
    worksheet.GetCells().Get(u"A2").PutValue(u"Grape");
    worksheet.GetCells().Get(u"B2").PutValue(2020);
    worksheet.GetCells().Get(u"C2").PutValue(5000);

    worksheet.GetCells().Get(u"A3").PutValue(u"Blueberry");
    worksheet.GetCells().Get(u"B3").PutValue(2020);
    worksheet.GetCells().Get(u"C3").PutValue(3000);

    worksheet.GetCells().Get(u"A4").PutValue(u"Kiwi");
    worksheet.GetCells().Get(u"B4").PutValue(2020);
    worksheet.GetCells().Get(u"C4").PutValue(4000);

    worksheet.GetCells().Get(u"A5").PutValue(u"Cherry");
    worksheet.GetCells().Get(u"B5").PutValue(2020);
    worksheet.GetCells().Get(u"C5").PutValue(2000);

    worksheet.GetCells().Get(u"A6").PutValue(u"Grape");
    worksheet.GetCells().Get(u"B6").PutValue(2021);
    worksheet.GetCells().Get(u"C6").PutValue(6000);

    worksheet.GetCells().Get(u"A7").PutValue(u"Blueberry");
    worksheet.GetCells().Get(u"B7").PutValue(2021);
    worksheet.GetCells().Get(u"C7").PutValue(3500);

    worksheet.GetCells().Get(u"A8").PutValue(u"Kiwi");
    worksheet.GetCells().Get(u"B8").PutValue(2021);
    worksheet.GetCells().Get(u"C8").PutValue(4500);

    worksheet.GetCells().Get(u"A9").PutValue(u"Cherry");
    worksheet.GetCells().Get(u"B9").PutValue(2021);
    worksheet.GetCells().Get(u"C9").PutValue(2500);

    worksheet.GetCells().Get(u"A10").PutValue(u"Grape");
    worksheet.GetCells().Get(u"B10").PutValue(2021);
    worksheet.GetCells().Get(u"C10").PutValue(5500);

    // Pivot tablo ekle: kaynak aralık A1:C10, hedef hücre E3, ad "Pivot1"
    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C10", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

    // Pivot alanlarını ata
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // Pivot tablosunun her hücresine uygulanacak bir Stil oluştur
    Style style = wb.CreateStyle();
    style.SetForegroundColor(Color::Yellow());
    style.SetPattern(BackgroundType::Solid);
    style.GetFont().SetIsBold(true);
    style.GetFont().SetColor(Color::DarkBlue());
    style.GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Thin);
    style.GetBorders().Get(BorderType::TopBorder).SetColor(Color::Black());
    style.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Thin);
    style.GetBorders().Get(BorderType::BottomBorder).SetColor(Color::Black());
    style.GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Thin);
    style.GetBorders().Get(BorderType::LeftBorder).SetColor(Color::Black());
    style.GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Thin);
    style.GetBorders().Get(BorderType::RightBorder).SetColor(Color::Black());

    // FormatAll uygula
    pivotTable.FormatAll(style);

    // Çalışma kitabını kaydet
    wb.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Hangi Stil API'sini Kullanmalıyım?**

Stil API'si seçimi, kaydettiğiniz dosya biçimine bağlıdır. Hızlı bir başvuru olarak aşağıdaki tabloyu kullanın.

| Hedef dosya biçimi | Kullanılacak API | Notlar |
|---|---|---|
| `.xls` (eski) | `PivotTable.AutoFormatType` | `Aspose.Cells.Pivot.PivotTableAutoFormatType` değerleri (ör. `Report1`–`Report10`, `Classic`, `Table1`–`Table10`). Modern biçimlerde kaydederken yoksayılır. |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, yerleşik stil) | `PivotTable.PivotTableStyleType` | `Aspose.Cells.PivotTableStyleType` değerleri (açık/koyu temalar, Excel 2017 eklemeleri dahil). |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, özel stil) | `PivotTable.PivotTableStyleName` + `Worksheets.TableStyles.AddPivotTableStyle(...)` | Yerleşik ön ayarlar yeterli olmadığında kullanın. `TableStyleElement.SetElementStyle(...)` aracılığıyla yapılandırın. |
| Herhangi bir biçim (tek tip geçersiz kılma) | `PivotTable.FormatAll(Style)` | Pivotun tamamındaki diğer tüm stil ayarlarının üzerine yazan kısayol. |

Kararsız kaldığınızda, `.xlsx` olarak kaydedin ve yerleşik temalar için `PivotTableStyleType`, özel temalar için `PivotTableStyleName` kullanın.

{{< app/cells/assistant language="cpp" >}}