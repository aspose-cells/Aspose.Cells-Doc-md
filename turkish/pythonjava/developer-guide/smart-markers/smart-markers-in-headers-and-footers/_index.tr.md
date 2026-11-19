---
title: Başlık ve Alt Bilgi'lerde Akıllı İşaretçiler | Aspose.Cells for Python via Java
linktitle: Üstbilgi ve Altbilgi Akıllı İşaretçiler | Aspose.Cells
description: Sayfa başlıkları ve alt bilgilerinde çift açı köşeli sözdizimi ve WorkbookDesigner.setEnableHeaderFooterMarkers seçeneğini kullanarak tablo satırı veya JSON veri kaynaklarıyla Smart Marker yer tutucularını yerleştirin ve veri URI larıyla resimleri bağlayın, Aspose.Cells for Python via Java için.
keywords: Aspose.Cells, Aspose.Cells for Python via Java, Akıllı İşaretçiler, başlık, alt bilgi, başlık alt bilgi işaretçileri, setEnableHeaderFooterMarkers, WorkbookDesigner, PageSetup, setHeader, setFooter, setJsonDataSource, ICellsDataTable, özel veri tablosu, veri bağlama, resim, veri URI, Python via Java
type: docs
weight: 196
url: /tr/python-java/smart-markers-in-headers-and-footers/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
Sayfa başlıkları ve alt bilgiler genellikle rapor başlığı, raporlama dönemi, yazar ve departman gibi rapor meta verilerini içerir. Bu bilgi çalışma kitabını doldurmak için kullanılan veri kaynağında zaten mevcutsa, elle tekrar etmek gereksiz çoğaltmaya yol açar.  
Klasik Akıllı İşaretçi sözdizimi `&=Source.Field`, çalışma sayfası gövdesindeki hücrelerde işlenir. Bir klasik işaretçiyi `PageSetup.setHeader` veya `PageSetup.setFooter` aracılığıyla bir başlık ya da alt bilgiye yerleştirirseniz, başlık ve alt bilgi dizesi hücre ızgarasının bir parçası olmadığı için literal metin olarak kalır ve `WorkbookDesigner.process()` tarafından taranmaz.  
**Aspose.Cells for Python via Java 26.11** ile birlikte, varsayılan olarak `False` olan `WorkbookDesigner.setEnableHeaderFooterMarkers` seçeneği, `process()`'in `<<Source.Field>>` biçiminde yazılmış yer tutucuları başlık ve alt bilgi bölümlerinde çözmesini sağlar — `process()` çağrılmadan önce bunu `True` olarak ayarlayın. Başlık ve alt bilgi yer tutucuları gövde işaretçileriyle aynı veri kaynağını kullanır.  
Her başlık ve alt bilgi üç adreslenebilir bölüm içerir:
- Bölüm `0` sol bölümdür.
- Bölüm `1` orta bölümdür.
- Bölüm `2` sağ bölümdür.
Bu bölümleri yazmak için `PageSetup.setHeader(int section, str value)` ve `PageSetup.setFooter(int section, str value)` kullanın. İşleme sonrasında tamamlanmış metni almak için `PageSetup.getHeader(int section)` ve `PageSetup.getFooter(int section)` metodlarını kullanın.

{{% alert color="primary" %}}
`<<Source.Field>>` gibi bir yer tutucu, alan değerini bölüm dizesine metin olarak ekler. Görseller `(picture)` eki ve bir data-URI değeriyle bağlanır.
{{% /alert %}}

## **Özel Veri Tablosu ile Başlık/Alt Bilgi İşaretçilerini Etkinleştirme**
**Aspose.Cells for Python via Java 26.11** sürümünde, özel bir tablo veri kaynağıyla başlık ve alt bilgi yer tutucularını çözmek için aşağıdaki adımları izleyin:
1. `Workbook` oluşturun ve `workbook.getWorksheets().get(0)` ile ilk `Worksheet`'i elde edin.
2. İstenen başlık ve alt bilgi bölümlerine `<<Source.Field>>` yer tutucularını `worksheet.getPageSetup().setHeader(section, value)` ve `worksheet.getPageSetup().setFooter(section, value)` ile yazın.
3. Tablo satır verisini ortaya çıkarmak için `ICellsDataTable` arayüzünü uygulayan küçük bir sınıf tanımlayın — sütun adları, satır sayısı ve `beforeFirst()`, `next()`, `get()` yöntemlerine sahip bir imleç — ve yer tutucuların kullandığı kaynak önekine uyan bir kaynak adı kullanın. Örneğin `node` adlı bir kaynak, `<<node.Name>>` gibi yer tutucuları destekler. Düz bir Python sınıfı ya da sözlük listesi bu platformda bağlanmaz; `ICellsDataTable` uygulaması özel nesne veri kaynağıdır.
4. Çalışma kitabı için bir `WorkbookDesigner` oluşturun.
5. İşleme başlamadan önce `designer.setEnableHeaderFooterMarkers(True)` çağrısını yapın.
6. Tablo ve kaynak adını `designer.setDataSource("node", table)` ile ekleyin.
7. `designer.process()` metodunu çağırın.
8. İşleme sonrasında yer tutucular başlık ya da alt bilgi metninde artık bulunmaz. Tamamlanmış bölüm dizesini almak için `worksheet.getPageSetup().getHeader(section)` ve `worksheet.getPageSetup().getFooter(section)` metodlarını kullanın.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    WorkbookDesigner,
    ICellsDataTable,
)
from jpype import JImplements, JOverride
@JImplements(ICellsDataTable)
class NodeTable:
    def __init__(self, rows):
        self._rows = rows
        self._i = -1
    @JOverride
    def getColumns(self):
        return ["Name", "Author"]
    @JOverride
    def getCount(self):
        return len(self._rows)
    @JOverride
    def beforeFirst(self):
        self._i = -1
    @JOverride
    def next(self):
        self._i += 1
        return self._i < len(self._rows)
    @JOverride
    def get(self, key):
        columns = self.getColumns()
        column_index = columns.index(key) if isinstance(key, str) else int(key)
        return self._rows[self._i][column_index]
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Center header and center footer carry <<Source.Field>> placeholders
worksheet.getPageSetup().setHeader(1, "Quarterly Report - <<node.Name>>")
worksheet.getPageSetup().setFooter(1, "Prepared by <<node.Author>>")
table = NodeTable([("Q4 2026", "Aspose.Cells")])
designer = WorkbookDesigner(workbook)
designer.setEnableHeaderFooterMarkers(True)
designer.setDataSource("node", table)
designer.process()
print("Header: " + worksheet.getPageSetup().getHeader(1))
print("Footer: " + worksheet.getPageSetup().getFooter(1))
# This prints:
# Header: Quarterly Report - Q4 2026
# Footer: Prepared by Aspose.Cells
workbook.save("HeaderFooterSmartMarkers.xlsx")
jpype.shutdownJVM()
```

## **JSON Veri Kaynağı Kullanma**
Rapor verileri zaten JSON formatında mevcutsa, özel bir `ICellsDataTable` yerine JSON kullanabilirsiniz. Kaynağı eklemek için `designer.setJsonDataSource(name, json)` metodunu çağırın.  
`name` argümanı, tablo veri kaynağı ile kullanılan kaynak adıyla aynı görevi görür. Örneğin `node` adı, `<<node.Company>>` ve `<<node.Title>>` gibi yer tutucuları destekler.  
Satır verisini doğrudan `setJsonDataSource` metoduna aktarın:
- Bir satır dizisi, bir veya daha fazla satır nesnesi içeren bir JSON dizisi, desteklenir.
- Tek bir satır nesnesi de doğrudan geçilebilir.
- Satırları `{"rows":[...]}` gibi bir üst-seviyeli ad altında sarmalamayın. Bu sarma, bu iş akışı için beklenen satır-odaklı giriş biçimi değildir.  
Tek bir JSON kaynağı, aynı `process()` çağrısı sırasında hem klasik `&=` gövde işaretçisini hem de başlık ve alt bilgi bölümlerindeki çift-açı-köşeli `<<>>` yer tutucularını çözebilir. Başlık ve alt bilgi yer tutucularının çözülebilmesi için yine `setEnableHeaderFooterMarkers` seçeneğini etkinleştirmeniz gerekir.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, WorkbookDesigner
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Left header, right header, and a classic body marker — one JSON source feeds all three
worksheet.getPageSetup().setHeader(0, "<<node.Company>>")
worksheet.getPageSetup().setHeader(2, "Page <<node.Title>>")
worksheet.getCells().get("A1").putValue("&=node.Company")
designer = WorkbookDesigner(workbook)
designer.setEnableHeaderFooterMarkers(True)
designer.setJsonDataSource(
    "node",
    '[{"Company":"Aspose Pty Ltd","Title":"Half-Year Report"}]'
)
designer.process()
print("Left: " + worksheet.getPageSetup().getHeader(0))
print("Right: " + worksheet.getPageSetup().getHeader(2))
print("Body: " + worksheet.getCells().get("A1").getStringValue())
workbook.save("HeaderFooterJsonMarkers.xlsx")
jpype.shutdownJVM()
```

## **Anahtar ve Çok Satırlı Kaynak Anlamı**
Başlık ve alt bilgi işaretçi ayarı varsayılan olarak `False` dır ve `designer.setEnableHeaderFooterMarkers(True)` yalnızca başlık ve alt bilgi `<<Source.Field>>` yer tutucularını kontrol eder. Anahtar kapalıyken `process()` klasik `&=` gövde işaretçilerini hâlâ çözer, ancak bir başlık ya da alt bilgi içinde `<<Source.Field>>` yer tutucusu metin olarak kalır.  
Bir başlık ya da alt bilgi bölümü tek bir dizedir, tekrar eden bir bant değildir. Veri kaynağı birden fazla satır içeriyorsa, ilk satır başlık ve alt bilgi değerlerini sağlar. Çözüldükten sonra değerler sıradan başlık ya da alt bilgi metni haline gelir. `workbook.save(...)` çağrısı yapıldıktan sonra çalışma kitabında kalırlar ve kaydedilen çalışma kitabı yeniden yüklendiğinde bulunurlar.  
Aşağıdaki örnek, aynı çok-satırlı tablo veri kaynağı üzerinde iki çalışma kitabı oluşturarak devre dışı ve etkin davranışı karşılaştırır. `plainDesigner` yer tutucuyu değiştirmez, `enabledDesigner` ise ilk satırı kullanarak çözer.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    WorkbookDesigner,
    ICellsDataTable,
)
from jpype import JImplements, JOverride
@JImplements(ICellsDataTable)
class NodeTable:
    def __init__(self, rows):
        self._rows = rows
        self._i = -1
    @JOverride
    def getColumns(self):
        return ["Name"]
    @JOverride
    def getCount(self):
        return len(self._rows)
    @JOverride
    def beforeFirst(self):
        self._i = -1
    @JOverride
    def next(self):
        self._i += 1
        return self._i < len(self._rows)
    @JOverride
    def get(self, key):
        columns = self.getColumns()
        column_index = columns.index(key) if isinstance(key, str) else int(key)
        return self._rows[self._i][column_index]
table = NodeTable([
    ("First Row",),
    ("Second Row",),
])
# Without the switch the placeholder stays literal text
plain_workbook = Workbook()
plain_sheet = plain_workbook.getWorksheets().get(0)
plain_sheet.getPageSetup().setHeader(1, "<<node.Name>>")
plain_designer = WorkbookDesigner(plain_workbook)
plain_designer.setDataSource("node", table)
plain_designer.process()
# With the switch on, the FIRST row of a multi-row source wins
enabled_workbook = Workbook()
enabled_sheet = enabled_workbook.getWorksheets().get(0)
enabled_sheet.getPageSetup().setHeader(1, "<<node.Name>>")
enabled_designer = WorkbookDesigner(enabled_workbook)
enabled_designer.setEnableHeaderFooterMarkers(True)
enabled_designer.setDataSource("node", table)
enabled_designer.process()
print("Without switch: " + plain_sheet.getPageSetup().getHeader(1))
print("With switch: " + enabled_sheet.getPageSetup().getHeader(1))
# This prints:
# Without switch: <<node.Name>>
# With switch: First Row
enabled_workbook.save("HeaderFooterMarkersEnabled.xlsx")
jpype.shutdownJVM()
```

## **Bir Resmi Başlık ya da Alt Bilgiye Bağlama**
`(picture)` eki, bir resmi başlık ya da alt bilgi bölümüne bağlar. Resmin görünmesini istediğiniz yere `<<node.logo(picture)>>` yazın ve alan değerini bir data URI olarak sağlayın — ön ek `data:image/png;base64,` ve ardından resim baytlarının Base64 metni. Çözülen resim bir `byte[]` dizisi olarak işlenir. `data:` ön ekine sahip olmayan yalın Base64 dizesi bir resim yerleştirmez.  
`process()` sonrasında:
1. Yer tutucu `&G` ile değiştirilir; bu, standart başlık ve alt bilgi resim kodudur. İşaretçi, bölüm dizesi içinde kod haline geldiği için `Logo: <<node.logo(picture)>>` gibi daha uzun metinlerde bulunabilir.
2. Resim baytları, çalışma kitabına o çalışma sayfasının başlık/alt bilgi çizim katmanına eklenmiş bir medya parçası olarak gömülür; böylece resim başlık ya da alt bilgiyle birlikte yazdırılır.

```python
import base64
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    WorkbookDesigner,
    ICellsDataTable,
)
from jpype import JImplements, JOverride
@JImplements(ICellsDataTable)
class NodeTable:
    def __init__(self, rows):
        self._rows = rows
        self._i = -1
    @JOverride
    def getColumns(self):
        return ["logo"]
    @JOverride
    def getCount(self):
        return len(self._rows)
    @JOverride
    def beforeFirst(self):
        self._i = -1
    @JOverride
    def next(self):
        self._i += 1
        return self._i < len(self._rows)
    @JOverride
    def get(self, key):
        columns = self.getColumns()
        column_index = columns.index(key) if isinstance(key, str) else int(key)
        return self._rows[self._i][column_index]
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# The (picture) suffix binds the image named by the data-URI field into the header
worksheet.getPageSetup().setHeader(1, "Logo: <<node.logo(picture)>>")
with open("logo.png", "rb") as image_file:
    image_bytes = image_file.read()
logo_data = "data:image/png;base64," + base64.b64encode(image_bytes).decode("ascii")
table = NodeTable([(logo_data,)])
designer = WorkbookDesigner(workbook)
designer.setEnableHeaderFooterMarkers(True)
designer.setDataSource("node", table)
designer.process()
print("Header: " + worksheet.getPageSetup().getHeader(1))
# This prints:
# Header: Logo: &G
workbook.save("HeaderFooterPicture.xlsx")
jpype.shutdownJVM()
```

Yazdırılan `&G`, Excel’in başlığı işlerken yorumladığı resim kodudur — `logo.png` baytları artık `HeaderFooterPicture.xlsx` içinde bulunur ve resim kodun yerini alır.  
Başlık ve alt bilgi Akıllı İşaretçilerini kullanmak için, sol, orta ve sağ başlık ya da alt bilgi bölümlerine `setHeader` ve `setFooter` ile `<<Source.Field>>` yer tutucularını yazın. `designer.setEnableHeaderFooterMarkers(True)` metodunu `process()` çağrısından önce çalıştırın ve değerleri ya `designer.setDataSource("node", table)` ile özel bir `ICellsDataTable` uygulaması ya da `designer.setJsonDataSource(name, json)` ile sağlayın. Tamamlanmış bölümleri `getHeader` ve `getFooter` metodlarıyla okuyun. Aynı veri kaynağı, tek bir işleme geçişinde gövde işaretçilerini ve başlık/alt bilgi yer tutucularını besleyebilir. Bir bölüme resmi bağlamak için `(picture)` ekini bir data-URI değeriyle ekleyin.

## **İlgili Makaleler**
- [SmartMarker Tek Hücre Dizi İşleme](/cells/tr/python-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)

{{< app/cells/assistant language="python" >}}