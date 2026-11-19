---
title: Üst Bilgi ve Alt Bilgi Bölümlerinde Akıllı İşaretçiler | Aspose.Cells for Python via .NET
linktitle: Üstbilgi ve Altbilgi Akıllı İşaretçiler | Aspose.Cells
description: Sayfa üst ve alt bilgi bölümlerine çift açı köşeli parantez sözdizimi ve WorkbookDesigner.enable_header_footer_markers anahtarını kullanarak, özel ICellsDataTable uygulamaları veya JSON veri kaynaklarıyla Smart Marker yer tutucularını yerleştirin ve resimleri data URI’ları aracılığıyla bağlayın, Aspose.Cells for Python via .NET içinde.
keywords: Aspose.Cells, Akıllı İşaretçiler, üst bilgiler, alt bilgiler, üst bilgi alt bilgi işaretçileri, enable_header_footer_markers, WorkbookDesigner, PageSetup, set_header, set_footer, set_json_data_source, set_data_source, ICellsDataTable, özel veri tablosu, veri bağlama, resim, data URI, Aspose.Cells for Python via .NET
type: docs
weight: 196
url: /tr/python-net/smart-markers-in-headers-and-footers/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
Sayfa üst ve alt bilgi bölümleri genellikle rapor başlığı, raporlama dönemi, yazar ve bölüm gibi rapor meta verilerini içerir. Bu bilgiler çalışma kitabını doldurmak için kullanılan veri kaynağında zaten mevcutsa, bunları manuel olarak tekrarlamak gereksiz çoğaltmaya yol açar.
Klasik Akıllı İşaretçi sözdizimi, `&=Source.Field`, çalışma sayfası gövde hücrelerinde işlenir. `page_setup.set_header` veya `page_setup.set_footer` aracılığıyla bir klasik işaretçiyi üst bilgi veya alt bilgi bölümüne yerleştirirseniz, `workbook_designer.process()` tarafından taranan çalışma sayfası hücre ızgarasının bir parçası olmadığından, bu metin olduğu gibi kalır.
**Aspose.Cells for Python via .NET 26.11** sürümünden itibaren, varsayılan olarak `False` olan `workbook_designer.enable_header_footer_markers` anahtarı, `process()` yöntemi tarafından üst bilgi ve alt bilgi bölüm metinlerinde `<<Source.Field>>` şeklinde yazılmış yer tutucuların çözülmesini sağlar — `process()` çağırmadan önce bunu `True` olarak ayarlayın. Üst bilgi ve alt bilgi yer tutucuları gövde işaretçileriyle aynı veri kaynağını kullanır.
Her üst bilgi ve alt bilgi üç adreslenebilir bölüme sahiptir:
- Bölüm `0` sol bölümdür.
- Bölüm `1` ortada (merkez) bölümdür.
- Bölüm `2` sağ bölümdür.
`page_setup.set_header(section, value)` ve `page_setup.set_footer(section, value)` kullanarak bu bölümleri yazın. İşlemden sonra, tamamlanmış metni elde etmek için `page_setup.get_header(section)` ve `page_setup.get_footer(section)` yöntemlerini kullanın.

{{% alert color="primary" %}}
`<<Source.Field>>` gibi bir yer tutucu, alan değerini metin olarak bölüm dizesine ekler. Görseller, `(picture)` son eki ve bir data-URI değeriyle bağlanır.
{{% /alert %}}

## **Özel Veri Tablosu ile Üst Bilgi/Alt Bilgi İşaretçilerini Etkinleştirme**
Aşağıdaki sırayı kullanarak **Aspose.Cells for Python via .NET 26.11** içinde özel tablo veri kaynağıyla üst bilgi ve alt bilgi yer tutucularını çözün:
1. `Workbook` oluşturun ve indeks `0`'da bulunan ilk `Worksheet`'i alın.
2. `page_setup.set_header` ve `page_setup.set_footer` kullanarak istediğiniz üst bilgi ve alt bilgi bölümlerine `<<Source.Field>>` yer tutucularını yazın.
3. Tutarlı bir sınıf tanımlayın ve `ICellsDataTable` arayüzünü uygulayarak tablo satır verilerini ortaya çıkarın — sütun adları, satır sayısı ve `before_first()`, `next()`, ve `__getitem__` indeksleyicisini sağlayan bir imleç — ve yer tutucuların kullandığı kaynak önekine uygun bir kaynak adı kullanın. Örneğin, `node` adındaki bir kaynak, `<<node.Name>>` gibi yer tutucuları destekler. Düz bir Python sınıfı veya sözlük listesi bu platformda bağlanmaz; `ICellsDataTable` uygulaması özel nesne veri kaynağıdır.
4. Çalışma kitabı için bir `WorkbookDesigner` oluşturun.
5. İşlemden önce `designer.enable_header_footer_markers` değerini `True` olarak ayarlayın.
6. Tabloyu ve kaynak adını `designer.set_data_source("node", table)` ile ekleyin.
7. `designer.process()` metodunu çağırın.
8. İşlemden sonra yer tutucular artık üst bilgi veya alt bilgi metninde bulunmaz. Tamamlanmış bölüm dizelerini elde etmek için `get_header` ve `get_footer` kullanın.

```python
import aspose.cells as ac
class NodeTable(ac.ICellsDataTable):
    def __init__(self, rows):
        self._rows = rows
        self._i = -1
    @property
    def columns(self):
        return ["Name", "Author"]
    @property
    def count(self):
        return len(self._rows)
    def before_first(self):
        self._i = -1
    def next(self):
        self._i += 1
        return self._i < len(self._rows)
    def __getitem__(self, key):
        column = self.columns.index(key) if isinstance(key, str) else key
        return self._rows[self._i][column]
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Center header and center footer carry <<Source.Field>> placeholders
worksheet.page_setup.set_header(1, "Quarterly Report - <<node.Name>>")
worksheet.page_setup.set_footer(1, "Prepared by <<node.Author>>")
table = NodeTable([("Q4 2026", "Aspose.Cells")])
designer = ac.WorkbookDesigner(workbook)
designer.enable_header_footer_markers = True
designer.set_data_source("node", table)
designer.process()
print("Header: " + worksheet.page_setup.get_header(1))
print("Footer: " + worksheet.page_setup.get_footer(1))
# This prints:
# Header: Quarterly Report - Q4 2026
# Footer: Prepared by Aspose.Cells
workbook.save("HeaderFooterSmartMarkers.xlsx")
```

## **JSON Veri Kaynağı Kullanma**
Rapor verileri zaten JSON biçiminde mevcutsa, özel bir `ICellsDataTable` yerine JSON kullanabilirsiniz. Kaynağı eklemek için `workbook_designer.set_json_data_source(name, json)` metodunu çağırın.
`name` argümanı, tablo verileriyle kullanılan kaynak adıyla aynı role sahiptir. Örneğin, `node` adı `<<node.Company>>` ve `<<node.Title>>` gibi yer tutucuları destekler.
- Bir satır dizisi, bir veya daha fazla satır nesnesi içeren bir JSON dizisi gibi, desteklenir.
- Tek bir satır nesnesi de doğrudan aktarılabilir.
- Satırları `{"rows":[...]}` gibi isimlendirilmiş bir üst-seviye anahtar altında sarmalamayın. Bu sarmalayıcı, bu iş akışı için beklenen satır-odaklı giriş biçimi değildir.
Tek bir JSON kaynağı aynı `process()` çağrısı sırasında hem klasik `&=` işaretçilerini hem de üst bilgi ve alt bilgi bölümlerindeki çift-açı `<<>>` yer tutucularını çözebilir. Üst bilgi ve alt bilgi yer tutucularının çözülmesi için yine `enable_header_footer_markers` anahtarını etkinleştirmeniz gerekir.

```python
import aspose.cells as ac
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Left header, right header, and a classic body marker — one JSON source feeds all three
worksheet.page_setup.set_header(0, "<<node.Company>>")
worksheet.page_setup.set_header(2, "Page <<node.Title>>")
worksheet.cells.get("A1").put_value("&=node.Company")
designer = ac.WorkbookDesigner(workbook)
designer.enable_header_footer_markers = True
designer.set_json_data_source(
    "node",
    '[{"Company":"Aspose Pty Ltd","Title":"Half-Year Report"}]'
)
designer.process()
print("Left: " + worksheet.page_setup.get_header(0))
print("Right: " + worksheet.page_setup.get_header(2))
print("Body: " + worksheet.cells.get("A1").string_value)
# This prints:
# Left: Aspose Pty Ltd
# Right: Page Half-Year Report
# Body: Aspose Pty Ltd
workbook.save("HeaderFooterJsonMarkers.xlsx")
```

## **Anahtar ve Çok Satırlı Kaynak Semantiği**
`enable_header_footer_markers` varsayılan olarak `False`’tur ve anahtar yalnızca üst bilgi ve alt bilgi `<<Source.Field>>` yer tutucularını kontrol eder. Anahtar kapalı olduğunda, `process()` hâlâ klasik `&=` gövde işaretçilerini çözer, ancak üst bilgi veya alt bilgi içinde bir `<<Source.Field>>` yer tutucu metin olarak kalır.
Bir üst bilgi veya alt bilgi bölümü tek bir dizedir, tekrarlayan bir bant değildir. Veri kaynağı birden çok satır içeriyorsa, ilk satır üst bilgi ve alt bilgi değerlerini sağlar. Çözüldükten sonra değerler normal üst bilgi veya alt bilgi metnine dönüşür. `save` metodunu çağırdıktan sonra çalışma kitabında kalıcıdır ve kaydedilen çalışma kitabı yeniden yüklendiğinde mevcut olur.
Aşağıdaki örnek, aynı çok-satırlı tablo veri kaynağı üzerine iki çalışma kitabı oluşturarak devre dışı ve etkin davranışı karşılaştırır. `plain_designer` yer tutucuyu değiştirmeden bırakırken, `enabled_designer` ilk satırı kullanarak çözer.

```python
import aspose.cells as ac
class NodeTable(ac.ICellsDataTable):
    def __init__(self, rows):
        self._rows = rows
        self._i = -1
    @property
    def columns(self):
        return ["Name"]
    @property
    def count(self):
        return len(self._rows)
    def before_first(self):
        self._i = -1
    def next(self):
        self._i += 1
        return self._i < len(self._rows)
    def __getitem__(self, key):
        column = self.columns.index(key) if isinstance(key, str) else key
        return self._rows[self._i][column]
rows = [("First Row",), ("Second Row",)]
# Without the switch the placeholder stays literal text
plain_workbook = ac.Workbook()
plain_sheet = plain_workbook.worksheets[0]
plain_sheet.page_setup.set_header(1, "<<node.Name>>")
plain_designer = ac.WorkbookDesigner(plain_workbook)
plain_designer.set_data_source("node", NodeTable(rows))
plain_designer.process()
# With the switch on, the FIRST row of a multi-row source wins
enabled_workbook = ac.Workbook()
enabled_sheet = enabled_workbook.worksheets[0]
enabled_sheet.page_setup.set_header(1, "<<node.Name>>")
enabled_designer = ac.WorkbookDesigner(enabled_workbook)
enabled_designer.enable_header_footer_markers = True
enabled_designer.set_data_source("node", NodeTable(rows))
enabled_designer.process()
print("Without switch: " + plain_sheet.page_setup.get_header(1))
print("With switch: " + enabled_sheet.page_setup.get_header(1))
# This prints:
# Without switch: <<node.Name>>
# With switch: First Row
enabled_workbook.save("HeaderFooterMarkersEnabled.xlsx")
```

## **Üst Bilgi veya Alt Bilgiye Resim Bağlama**
`(picture)` son eki bir resmi üst bilgi veya alt bilgi bölümüne bağlar. Resmin görünmesini istediğiniz yere `<<node.logo(picture)>>` yazın ve alan değerini bir data URI olarak sağlayın — `data:image/png;base64,` öneki ve ardından görüntü baytlarının Base64 metni. `data:` öneki olmadan yalnızca Base64 dizesi bir resim gömmez.
`process()` sonrasında:
1. Yer tutucu `&G` ile değiştirilir; bu, standart üst bilgi ve alt bilgi resim kodudur. İşaretçi, bölüm dizesi içinde bir kod haline geldiği için `Logo: <<node.logo(picture)>>` gibi daha uzun metinlerin içinde yer alabilir.
2. Görüntü baytları, ilgili çalışma sayfasının üst bilgi/alt bilgi çizim katmanına eklenen bir medya parçası olarak çalışma kitabına gömülür; böylece resim üst bilgi veya alt bilgiyle birlikte yazdırılır.

```python
import aspose.cells as ac
import base64
class LogoTable(ac.ICellsDataTable):
    def __init__(self, rows):
        self._rows = rows
        self._i = -1
    @property
    def columns(self):
        return ["logo"]
    @property
    def count(self):
        return len(self._rows)
    def before_first(self):
        self._i = -1
    def next(self):
        self._i += 1
        return self._i < len(self._rows)
    def __getitem__(self, key):
        column = self.columns.index(key) if isinstance(key, str) else key
        return self._rows[self._i][column]
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# The (picture) suffix binds the image named by the data-URI field into the header
worksheet.page_setup.set_header(1, "Logo: <<node.logo(picture)>>")
with open("logo.png", "rb") as image_file:
    logo_data_uri = "data:image/png;base64," + base64.b64encode(image_file.read()).decode("ascii")
table = LogoTable([(logo_data_uri,)])
designer = ac.WorkbookDesigner(workbook)
designer.enable_header_footer_markers = True
designer.set_data_source("node", table)
designer.process()
print("Header: " + worksheet.page_setup.get_header(1))
# This prints:
# Header: Logo: &G
workbook.save("HeaderFooterPicture.xlsx")
```

Yazdırılan `&G`, Excel’in üst bilgiyi işlerken yorumladığı resim kodudur — `logo.png` baytları artık `HeaderFooterPicture.xlsx` içinde bulunur ve kodun yerine resim yazdırılır.
Üst bilgi ve alt bilgi Akıllı İşaretçilerini kullanmak için `set_header` ve `set_footer` metodlarıyla sol, orta ve sağ üst bilgi veya alt bilgi bölümlerine `<<Source.Field>>` yer tutucularını yazın. `process()` çağırmadan önce `WorkbookDesigner` üzerinde `enable_header_footer_markers` değerini `True` olarak ayarlayın ve değerleri özel bir `ICellsDataTable` uygulamasıyla `set_data_source("node", table)` ya da `set_json_data_source(name, json)` ile sağlayın. Tamamlanmış bölümleri `get_header` ve `get_footer` ile okuyun. Aynı veri kaynağı, bir işlem aşamasında gövde işaretçileri ve üst bilgi/alt bilgi yer tutucularını besleyebilir. Bir bölüme resim bağlamak için `(picture)` son ekini data-URI değeriyle ekleyin.

## **İlgili Makaleler**
- [Akıllı İşaretçi Tek Hücre Dizi Oluşturma](/cells/tr/python-net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)

{{< app/cells/assistant language="python-net" >}}