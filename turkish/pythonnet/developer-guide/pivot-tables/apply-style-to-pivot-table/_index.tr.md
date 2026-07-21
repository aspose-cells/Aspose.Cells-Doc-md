---
title: Pivot Tablolara Stil Uygulama
linktitle: Pivot Tablolara Stil Uygulama
description: Aspose.Cells for Python via .NET'te yerleşik ve özel stillerin pivot tablolara nasıl uygulanacağını öğrenin; eski XLS otomatik biçimleri, modern Excel 2007+ adlandırılmış stilleri, özel pivot tablo stilleri ve FormatAll kısayolu dahil.
keywords: Aspose.Cells Python via .NET pivot tablo stili, PivotTableStyleType, AutoFormatType, FormatAll, özel stil, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /tr/python-net/apply-style-to-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells, hem eski pivot otomatik biçimlerini (`.xls` dosyaları için tasarlanmış) hem de modern adlandırılmış veya özel pivot tablo stillerini (`.xlsx`, `.xlsm` ve `.xlsb` dosyaları için tasarlanmış) uygulamayı destekler. Çağırmanız gereken API, çalışma kitabının yüklendiği formata değil, kaydedildiği dosya formatına göre belirlenir.

{{% /alert %}}

## **Giriş**

Aspose.Cells, pivot tablolar için iki paralel stil API'si sunar. Aralarındaki seçim, okuduğunuz formata değil, çalışma kitabını kaydettiğiniz dosya formatına göre yapılır. Bir `.xls` dosyasından yüklenen çalışma kitabı `.xlsx` olarak yeniden kaydedilebilir; bu durumda eski stil API'si değil, modern stil API'si geçerli olur.

Eski `.xls` çıktısı için `PivotTable.auto_format_type` özelliğini `aspose.cells.pivot.PivotTableAutoFormatType` numaralandırmasıyla birlikte kullanın. Bu API, klasik Excel'in pivot tablolar için sunduğu otomatik biçim seçicisine karşılık gelir.

Modern `.xlsx`, `.xlsm` ve `.xlsb` çıktısı için iki stil API'si çeşidi mevcuttur:

- `PivotTable.pivot_table_style_type` yerleşik adlandırılmış stillerden birini seçer (Excel 2017'de eklenenler dahil açık ve koyu temalar). Bu hazır ayarlar salt okunurdur.
- `PivotTable.pivot_table_style_name` `workbook.worksheets.table_styles.add_pivot_table_style(...)` aracılığıyla kendinizin tanımladığı özel bir stili seçer. Hazır ayarların sunduğunun ötesinde renkleri, kenarlıkları veya yazı tiplerini değiştirmek istediğinizde özel stiller gereklidir.

Buna ek olarak, `PivotTable.format_all(Style)`, tek bir `Style` nesnesini pivot tablonun her hücresine uygulayan ve yukarıdaki stil adı API'lerinden hangisiyle ayarlanmış olursa olsun geçersiz kılan bir kısayoldur. Bu, temel alınan temadan bağımsız olarak tek tip bir görünüm gerektiğinde kullanışlıdır.

## **Eski XLS Hazır Otomatik Biçimini Uygulama**

`PivotTable.auto_format_type`, `aspose.cells.pivot.PivotTableAutoFormatType` numaralandırmasından bir değer kabul eder. Kullanılabilir değerler `REPORT_1` ile `REPORT_10`, `CLASSIC` ve `TABLE_1` ile `TABLE_10` arasındadır.

{{% alert color="primary" %}}

`auto_format_type` yalnızca çalışma kitabı `.xls` olarak kaydedildiğinde dikkate alınır. Aynı çalışma kitabı `.xlsx`, `.xlsm` veya `.xlsb` olarak kaydedildiğinde Excel bu özelliği yoksayar ve `pivot_table_style_type` ile `pivot_table_style_name` ayarlarına geri döner.

{{% /alert %}}

Aşağıdaki örnek yeni bir çalışma kitabı yükler, Fruit/Year/Amount örnek verilerini ekler, bir pivot tablo ekler, `PivotTableAutoFormatType.REPORT_5` uygular ve sonucu `.xls` olarak kaydeder.

```python
import aspose.cells as ac

# Senaryo 1: Eski tip bir XLS ön ayar otomatik biçimi uygula
# Kullanılan API: PivotTable.AutoFormatType
# Hedef dosya biçimi: .xls (eski tip)
# Eksiksiz örnekler ve veri dosyaları için lütfen https://github.com/aspose-cells/Aspose.Cells-for-.NET adresine gidin

# Yeni bir çalışma kitabı oluştur
workbook = ac.Workbook()

# İlk çalışma sayfasını al
sheet = workbook.worksheets[0]

# Başlık satırı (Fruit, Year, Amount) ve 2020 ile 2021 yıllarını kapsayan
# grape, blueberry, kiwi, cherry verileriyle 9 veri satırı içeren kaynak verileri doldur
sheet.cells[0, 0].put_value("Fruit")
sheet.cells[0, 1].put_value("Year")
sheet.cells[0, 2].put_value("Amount")

sheet.cells[1, 0].put_value("grape")
sheet.cells[1, 1].put_value(2020)
sheet.cells[1, 2].put_value(50)

sheet.cells[2, 0].put_value("blueberry")
sheet.cells[2, 1].put_value(2020)
sheet.cells[2, 2].put_value(30)

sheet.cells[3, 0].put_value("kiwi")
sheet.cells[3, 1].put_value(2020)
sheet.cells[3, 2].put_value(25)

sheet.cells[4, 0].put_value("cherry")
sheet.cells[4, 1].put_value(2020)
sheet.cells[4, 2].put_value(40)

sheet.cells[5, 0].put_value("grape")
sheet.cells[5, 1].put_value(2021)
sheet.cells[5, 2].put_value(60)

sheet.cells[6, 0].put_value("blueberry")
sheet.cells[6, 1].put_value(2021)
sheet.cells[6, 2].put_value(35)

sheet.cells[7, 0].put_value("kiwi")
sheet.cells[7, 1].put_value(2021)
sheet.cells[7, 2].put_value(28)

sheet.cells[8, 0].put_value("cherry")
sheet.cells[8, 1].put_value(2021)
sheet.cells[8, 2].put_value(45)

sheet.cells[9, 0].put_value("grape")
sheet.cells[9, 1].put_value(2020)
sheet.cells[9, 2].put_value(45)

# E3 hedef hücresinde, "Pivot1" adıyla ve A1:C10 kaynak aralığını kullanarak bir pivot tablo ekle
pivot_index = sheet.pivot_tables.add("A1:C10", "E3", "Pivot1")
pivot_table = sheet.pivot_tables[pivot_index]

# Alanları ata: Fruit -> Satırlar, Year -> Sütunlar, Amount -> Veri
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# Eski tip XLS ön ayar otomatik biçimi "Report5" uygula
# Not: Bu özellik yalnızca .xls olarak kaydederken anlamlıdır.
# .xlsx/.xlsm/.xlsb olarak kaydedildiğinde, Excel AutoFormatType özelliğini yoksayar
# ve PivotTableStyleType / PivotTableStyleName ile belirtilen biçimi kullanır.
pivot_table.auto_format_type = ac.PivotTableAutoFormatType.REPORT5

# Çalışma kitabını eski tip .xls biçiminde kaydet
workbook.save("output.xls")
```

## **Modern Adlandırılmış Hazır Pivot Tablo Stilini Uygulama**

`PivotTable.pivot_table_style_type`, `aspose.cells.PivotTableStyleType` numaralandırmasından bir değer kabul eder. Numaralandırma, `PIVOT_TABLE_STYLE_LIGHT_1` ile `PIVOT_TABLE_STYLE_LIGHT_28` arasındaki açık temaları ve `PIVOT_TABLE_STYLE_DARK_1` ile `PIVOT_TABLE_STYLE_DARK_28` arasındaki koyu temaları kapsar. Excel 2017'de eklenen stiller (açık ve koyu temaların ikinci dalgası) aynı numaralandırma üzerinden erişilebilir.

Bu, herhangi bir modern dosya formatı için önerilen API'dir. Eski otomatik biçimin aksine, burada seçilen stil Excel tarafından aslına uygun şekilde işlenir ve diğer Office araçlarıyla gidiş-dönüş işlemlerinde kaybolmaz.

Aşağıdaki örnek aynı Fruit/Year/Amount verilerini kullanır, özdeş bir pivot tablo oluşturur, `PIVOT_TABLE_STYLE_DARK_1` uygular ve çalışma kitabını `.xlsx` olarak kaydeder.

```python
import aspose.cells as ac

# Senaryo 2: PivotTableStyleType kullanarak modern bir Excel 2007+ adlandırılmış ön ayar stilini uygulayın.
# Hedef dosya formatı: .xlsx. PivotTableStyleType enum'u Aspose.Cells ad alanında bulunur
# (Aspose.Cells.Pivot'ta değil) — bu yüzden ek bir using'e ihtiyacımız yok.
# GitHub referansı: https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples/CSharp/PivotTables/ApplyStyleToPivotTable2.cs

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Başlık satırı: Meyve / Yıl / Tutar
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

# 9 veri satırı: Meyve / Yıl / Tutar
worksheet.cells["A2"].put_value("Grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(100)

worksheet.cells["A3"].put_value("Blueberry")
worksheet.cells["B3"].put_value(2020)
worksheet.cells["C3"].put_value(150)

worksheet.cells["A4"].put_value("Kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(200)

worksheet.cells["A5"].put_value("Cherry")
worksheet.cells["B5"].put_value(2020)
worksheet.cells["C5"].put_value(180)

worksheet.cells["A6"].put_value("Grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(120)

worksheet.cells["A7"].put_value("Blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(170)

worksheet.cells["A8"].put_value("Kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(210)

worksheet.cells["A9"].put_value("Cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(190)

worksheet.cells["A10"].put_value("Grape")
worksheet.cells["B10"].put_value(2021)
worksheet.cells["C10"].put_value(130)

# E3 konumunda "Pivot1" adında, A1:C10 kaynaklı bir pivot tablo ekleyin
pivot_index = worksheet.pivot_tables.add("A1:C10", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]

# Pivot alanlarını atayın: Meyve -> Satır alanı, Yıl -> Sütun alanı, Tutar -> Veri alanı
pivot_table.add_field_to_area(ac.PivotFieldType.Row, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.Column, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.Data, "Amount")

# Modern bir Excel 2007+ adlandırılmış ön ayar pivot stili uygulayın.
# PivotTableStyleType, .xlsx / .xlsm / .xlsb dosyaları için doğru API'dir; AutoFormatType
# bu formatlar için Excel tarafından yok sayılır. PivotTableStyleDark1, koyu tema
# ailesine aittir (PivotTableStyleDark1..PivotTableStyleDark28) ve aynı enum ayrıca
# daha yeni Excel 2017 açık/koyu temalarını da gösterir (PivotTableStyleLight1..Light28 / Dark1..Dark28).
pivot_table.pivot_table_style_type = ac.PivotTableStyleType.PivotTableStyleDark1

# Modern .xlsx olarak kaydedin — PivotTableStyleType'ın anlamlı olduğu format budur.
workbook.save("output.xlsx")
```

## **Özel Bir Pivot Tablo Stili Tanımlama ve Uygulama**

Yerleşik hazır ayarlar değiştirilemez. Renkleri, kenarlıkları veya yazı tiplerini geçersiz kılmanız gerektiğinde özel bir pivot stili tanımlamalısınız. İş akışı üç adımdan oluşur:

1. `workbook.worksheets.table_styles.add_pivot_table_style(name)` aracılığıyla çalışma kitabının `table_styles` koleksiyonuna özel bir stil ekleyin. Bu, yeni oluşturulan stilin dizinini döndürür.
2. `table_style.table_style_elements.add(TableStyleElementType)` üzerinden öğeler (`WHOLE_TABLE` veya `GRAND_TOTAL_ROW` gibi) ekleyerek stili yapılandırın, ardından her öğeye `table_style_element.set_element_style(Style)` ile bir `Style` atayın.
3. `PivotTable.pivot_table_style_name` öğesini stilin adına ayarlayarak özel stili pivota uygulayın. Burada `pivot_table_style_type` kullanmayın; çünkü bu özellik yerleşik hazır ayarları seçer.

{{% alert color="primary" %}}

`pivot_table_style_name` ve `pivot_table_style_type` birbirinin yerine kullanılamaz. Yerleşik hazır ayarlar için `pivot_table_style_type`, `add_pivot_table_style` aracılığıyla tanımladığınız özel stiller için `pivot_table_style_name` kullanın. İkisini birden ayarlamak zararsızdır, ancak yalnızca amaçlanan kaynağa uygun olan işlenir.

{{% /alert %}}

Kullanılabilir `TableStyleElementType` değerleri şunları içerir: `WHOLE_TABLE`, `FIRST_ROW`, `LAST_ROW`, `FIRST_COLUMN`, `LAST_COLUMN`, `GRAND_TOTAL_ROW`, `GRAND_TOTAL_COLUMN`, `PAGE_FIELD_LABELS` ve `PAGE_FIELD_VALUES`.

Aşağıdaki örnek, `WHOLE_TABLE` üzerinde ince siyah kenarlık ve `GRAND_TOTAL_ROW` üzerinde kalın kırmızı yazı tipi içeren özel bir pivot stili tanımlar, ardından bunu `pivot_table_style_name` aracılığıyla uygular ve `.xlsx` olarak kaydeder.

```python
import aspose.cells as ac
import System.Drawing

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Kaynak verileri doldur: başlık satırı + 9 veri satırı (A1:C10)
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

worksheet.cells["A2"].put_value("Grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(100)

worksheet.cells["A3"].put_value("Blueberry")
worksheet.cells["B3"].put_value(2020)
worksheet.cells["C3"].put_value(200)

worksheet.cells["A4"].put_value("Kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(300)

worksheet.cells["A5"].put_value("Cherry")
worksheet.cells["B5"].put_value(2020)
worksheet.cells["C5"].put_value(400)

worksheet.cells["A6"].put_value("Grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(500)

worksheet.cells["A7"].put_value("Blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(600)

worksheet.cells["A8"].put_value("Kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(700)

worksheet.cells["A9"].put_value("Cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(800)

worksheet.cells["A10"].put_value("Grape")
worksheet.cells["B10"].put_value(2021)
worksheet.cells["C10"].put_value(900)

# A1:C10'dan kaynaklanan, E3'e sabitlenmiş, "Pivot1" adlı pivot tablo ekle
pivot_index = worksheet.pivot_tables.add("A1:C10", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# Adım 1: yeni özel bir pivot tablo stili kaydet ve dizinini yakala
style_index = workbook.worksheets.table_styles.add_pivot_table_style("CustomPivotStyle")
table_style = workbook.worksheets.table_styles[style_index]

# Adım 2: bir WholeTable öğesi ekle ve dört kenara ince siyah kenarlıklar uygula
whole_table_element_index = table_style.table_style_elements.add(ac.TableStyleElementType.WHOLE_TABLE)
whole_table_element = table_style.table_style_elements[whole_table_element_index]
whole_table_style = workbook.create_style()
whole_table_style.borders[ac.BorderType.TOP_BORDER].line_style = ac.CellBorderType.THIN
whole_table_style.borders[ac.BorderType.TOP_BORDER].color = System.Drawing.Color.Black
whole_table_style.borders[ac.BorderType.BOTTOM_BORDER].line_style = ac.CellBorderType.THIN
whole_table_style.borders[ac.BorderType.BOTTOM_BORDER].color = System.Drawing.Color.Black
whole_table_style.borders[ac.BorderType.LEFT_BORDER].line_style = ac.CellBorderType.THIN
whole_table_style.borders[ac.BorderType.LEFT_BORDER].color = System.Drawing.Color.Black
whole_table_style.borders[ac.BorderType.RIGHT_BORDER].line_style = ac.CellBorderType.THIN
whole_table_style.borders[ac.BorderType.RIGHT_BORDER].color = System.Drawing.Color.Black
whole_table_element.set_element_style(whole_table_style)

# Adım 3: bir GrandTotalRow öğesi ekle ve kalın kırmızı yazı tipi uygula
grand_total_element_index = table_style.table_style_elements.add(ac.TableStyleElementType.GRAND_TOTAL_ROW)
grand_total_element = table_style.table_style_elements[grand_total_element_index]
grand_total_style = workbook.create_style()
grand_total_style.font.is_bold = True
grand_total_style.font.color = System.Drawing.Color.Red
grand_total_element.set_element_style(grand_total_style)

# Adım 4: özel stili ada göre uygula (PivotTableStyleType'a göre DEĞİL, bu yerleşik ön ayarlar içindir)
pivot_table.pivot_table_style_name = "CustomPivotStyle"

workbook.save("output.xlsx")
```

## **FormatAll ile Her Pivot Hücresine Tek Bir Stil Uygulama**

`PivotTable.format_all(Style)`, tek bir `Style` nesnesini pivot tablonun veri alanı, satır ve sütun başlıkları ile toplamlar dahil her hücresine uygulayan bir kısayoldur. `pivot_table_style_type` veya `pivot_table_style_name` aracılığıyla daha önce ayarlanmış olan her şey geçersiz kılınır.

{{% alert color="primary" %}}

`format_all`, hem `pivot_table_style_type` hem de `pivot_table_style_name` öğelerini geçersiz kılar. Bunu yalnızca tüm pivot genelinde temadan bağımsız tek tip bir görünüm gerektiğinde kullanın.

{{% /alert %}}

Aşağıdaki örnek sarı düz dolgu, kalın koyu mavi yazı tipi ve tüm kenarlarda ince siyah kenarlıklar içeren bir `Style` oluşturur, ardından bunu `format_all` ile uygular ve `.xlsx` olarak kaydeder.

```python
from System.Drawing import Color
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
from aspose.cells import BackgroundType, CellBorderType, BorderType

# Senaryo 4: FormatAll kullanarak her pivot tablo hücresine tek bir Stil uygulama
# Kullanılan API: PivotTable.FormatAll(Style)
# Hedef format: .xlsx
# GitHub referansı: Aspose.Cells-for-.NET deposuna bakın — pivot tablo stil örnekleri

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Kaynak verileri doldur: başlık satırı (satır 1) + 9 veri satırı (satır 2-10)
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

worksheet.cells["A2"].put_value("Grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(5000)

worksheet.cells["A3"].put_value("Blueberry")
worksheet.cells["B3"].put_value(2020)
worksheet.cells["C3"].put_value(3000)

worksheet.cells["A4"].put_value("Kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(4000)

worksheet.cells["A5"].put_value("Cherry")
worksheet.cells["B5"].put_value(2020)
worksheet.cells["C5"].put_value(2000)

worksheet.cells["A6"].put_value("Grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(6000)

worksheet.cells["A7"].put_value("Blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(3500)

worksheet.cells["A8"].put_value("Kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(4500)

worksheet.cells["A9"].put_value("Cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(2500)

worksheet.cells["A10"].put_value("Grape")
worksheet.cells["B10"].put_value(2021)
worksheet.cells["C10"].put_value(5500)

# Pivot tablo ekle: kaynak aralığı A1:C10, hedef hücre E3, ad "Pivot1"
pivot_index = worksheet.pivot_tables.add("A1:C10", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]

# Pivot alanlarını ata: Fruit -> Satır alanı, Year -> Sütun alanı, Amount -> Veri alanı
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")

# Pivot tablosunun her hücresine uygulanacak bir Stil oluştur
style = workbook.create_style()
style.foreground_color = Color.Yellow
style.pattern = BackgroundType.SOLID
style.font.is_bold = True
style.font.color = Color.DarkBlue
style.borders[BorderType.TOP_BORDER].line_style = CellBorderType.THIN
style.borders[BorderType.TOP_BORDER].color = Color.Black
style.borders[BorderType.BOTTOM_BORDER].line_style = CellBorderType.THIN
style.borders[BorderType.BOTTOM_BORDER].color = Color.Black
style.borders[BorderType.LEFT_BORDER].line_style = CellBorderType.THIN
style.borders[BorderType.LEFT_BORDER].color = Color.Black
style.borders[BorderType.RIGHT_BORDER].line_style = CellBorderType.THIN
style.borders[BorderType.RIGHT_BORDER].color = Color.Black

# FormatAll uygula: bu tek stili pivot tablosunun her hücresine zorla uygular,
# daha önce ayarlanmış olan PivotTableStyleType / PivotTableStyleName değerlerini geçersiz kılar
pivot_table.format_all(style)

# Çalışma kitabını modern .xlsx formatında kaydet
workbook.save("output.xlsx")
```

## **Hangi Stil API'sini Kullanmalıyım?**

Stil API'si seçimi, kaydettiğiniz dosya formatına bağlıdır. Hızlı bir başvuru olarak aşağıdaki tabloyu kullanın.

| Hedef dosya formatı | Kullanılacak API | Notlar |
|---|---|---|
| `.xls` (eski) | `PivotTable.auto_format_type` | `aspose.cells.pivot.PivotTableAutoFormatType` değerleri (ör. `REPORT_1`–`REPORT_10`, `CLASSIC`, `TABLE_1`–`TABLE_10`). Modern formatlar olarak kaydederken yoksayılır. |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, yerleşik stil) | `PivotTable.pivot_table_style_type` | `aspose.cells.PivotTableStyleType` değerleri (Excel 2017 eklemeleri dahil açık/koyu temalar). |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, özel stil) | `PivotTable.pivot_table_style_name` + `worksheets.table_styles.add_pivot_table_style(...)` | Yerleşik hazır ayarlar yeterli olmadığında kullanın. `table_style_element.set_element_style(...)` aracılığıyla yapılandırın. |
| Herhangi bir format (tek tip geçersiz kılma) | `PivotTable.format_all(Style)` | Pivot genelinde diğer tüm stil ayarlarını geçersiz kılan kısayol. |

Kararsız kaldığınızda, `.xlsx` olarak kaydedin ve yerleşik temalar için `pivot_table_style_type`, özel temalar için `pivot_table_style_name` kullanın.

{{< app/cells/assistant language="python" >}}