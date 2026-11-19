---
title: Başlık ve Alt Bilgilerde Akıllı İşaretçiler | Aspose.Cells for Node.js via Java
linktitle: Üstbilgi ve Altbilgi Akıllı İşaretçiler | Aspose.Cells for Node.js via Java
description: JSON veri kaynaklarını kullanarak çift açılı köşeli sözdizimi ve WorkbookDesigner.setEnableHeaderFooterMarkers ayarıyla sayfa başlık ve altbilgilerine Akıllı İşaretçi yer tutucuları ekleyin ve veri URI'ları aracılığıyla resimleri bağlayın, Aspose.Cells for Node.js via Java için.
keywords: Aspose.Cells for Node.js via Java, Akıllı İşaretçiler, başlık, altbilgi, başlık altbilgi işaretçileri, setEnableHeaderFooterMarkers, WorkbookDesigner, PageSetup, setHeader, setFooter, setJsonDataSource, JSON satırları, veri bağlama, resim, veri URI, JavaScript
type: docs
weight: 196
url: /tr/nodejs-java/smart-markers-in-headers-and-footers/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
Sayfa başlıkları ve altbilgileri genellikle rapor başlığı, raporlama dönemi, yazar ve departman gibi rapor meta verilerini içerir. Bu bilgiler, çalışma kitabını doldurmak için kullanılan veri kaynağında zaten mevcutsa, manuel olarak tekrar edilmesi gereksiz çoğalmaya neden olur.
Klasik Akıllı İşaretçi sözdizimi, `&=Source.Field`, çalışma sayfası gövde hücrelerinde işlenir. Eğer bir klasik işaretçiyi `PageSetup.setHeader` veya `PageSetup.setFooter` aracılığıyla bir başlık ya da altbilgiye koyarsanız, `WorkbookDesigner.process()` tarafından taranan çalışma sayfası hücre ızgarasının bir parçası olmadığından düz metin olarak kalır.
**Aspose.Cells for Node.js via Java 26.11**'den itibaren, varsayılan olarak `false` olan `WorkbookDesigner.setEnableHeaderFooterMarkers` ayarı, `process()` metodunun başlık ve altbilgi bölüm dizelerinde `<<Source.Field>>` şeklinde yazılmış yer tutucuları çözmesini sağlar. `process()` çağırmadan önce `designer.setEnableHeaderFooterMarkers(true)` yapın. Başlık ve altbilgi yer tutucuları, gövde işaretçileriyle aynı veri kaynağını kullanır.
Her başlık ve altbilgi üç adreslenebilir bölüm içerir:
- Bölüm `0` sol bölümdür.
- Bölüm `1` orta bölümdür.
- Bölüm `2` sağ bölümdür.
Bu bölümleri yazmak için `PageSetup.setHeader(int section, String value)` ve `PageSetup.setFooter(int section, String value)` kullanın. İşlemden sonra tamamlanmış metni elde etmek için `PageSetup.getHeader(int section)` ve `PageSetup.getFooter(int section)` kullanın.

{{% alert color="primary" %}}
`<<Source.Field>>` gibi bir yer tutucu, alan değerini bölüm metnine metin olarak ekler. Görseller `(picture)` eki ve bir veri-URI değeri ile bağlanır.
{{% /alert %}}

## **JSON Satır Verileriyle Başlık ve Alt Bilgi İşaretçilerini Etkinleştirme**
**Aspose.Cells for Node.js via Java 26.11**'de başlık ve altbilgi yer tutucularını JSON satır verileriyle çözmek için aşağıdaki sırayı izleyin:
1. `Workbook` oluşturun ve `workbook.getWorksheets().get(0)` ile ilk `Worksheet`'i alın.
2. İstenen başlık ve altbilgi bölümlerine `<<Source.Field>>` yer tutucularını `PageSetup.setHeader` ve `PageSetup.setFooter` ile yazın.
3. Satır verilerini satır nesnelerinden oluşan bir JSON dizisi olarak hazırlayın ve yer tutucuların kullandığı kaynak önekine karşılık gelen bir kaynak adı seçin. Örneğin, `node` adlı bir kaynak `<<node.Name>>` gibi yer tutucuları destekler. `setDataSource` yöntemine gönderilen düz JavaScript nesneleri ve dizileri bu platformda bağlanmaz — JSON desteklenen tablo biçimidir.
4. Çalışma kitabı için bir `WorkbookDesigner` oluşturun.
5. İşleme başlamadan önce `designer.setEnableHeaderFooterMarkers(true)` çağırın.
6. JSON'ı `designer.setJsonDataSource("node", '[{"Name":"...","Author":"..."}]')` ile ekleyin.
7. `designer.process()` metodunu çağırın.
8. İşlemeden sonra yer tutucular başlık veya altbilgi metninde artık bulunmaz. Tamamlanmış bölüm dizelerini almak için `getHeader` ve `getFooter` kullanın.

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
// Center header and center footer carry <<Source.Field>> placeholders
worksheet.getPageSetup().setHeader(1, "Quarterly Report - <<node.Name>>");
worksheet.getPageSetup().setFooter(1, "Prepared by <<node.Author>>");
const designer = new AsposeCells.WorkbookDesigner(workbook);
designer.setEnableHeaderFooterMarkers(true);
designer.setJsonDataSource(
  "node",
  '[{"Name":"Q4 2026","Author":"Aspose.Cells"}]'
);
designer.process();
console.log("Header: " + worksheet.getPageSetup().getHeader(1));
console.log("Footer: " + worksheet.getPageSetup().getFooter(1));
// This prints:
// Header: Quarterly Report - Q4 2026
// Footer: Prepared by Aspose.Cells
workbook.save("HeaderFooterSmartMarkers.xlsx");
```

## **JSON Veri Kaynağı Kullanımı**
Rapor verileri zaten JSON olarak mevcutsa, tek bir `setJsonDataSource` çağrısı tüm işaretçi stillerini besleyebilir. Kaynağı eklemek için `WorkbookDesigner.setJsonDataSource(String name, String json)` metodunu çağırın.
`name` parametresi, yer tutucular tarafından kullanılan kaynak adını belirler. Örneğin, `node` adı `<<node.Company>>` ve `<<node.Title>>` gibi yer tutucuları destekler.
Satır verilerini doğrudan `setJsonDataSource` metoduna geçirin:
- Bir satır dizisi, bir veya daha fazla satır nesnesi içeren bir JSON dizisi gibi, desteklenir.
- Tek bir satır nesnesi de doğrudan geçirilebilir.
- Satırları `{"rows":[...]}` gibi adlandırılmış bir üst anahtar altında sarmalamayın. Bu sarmalayıcı, bu iş akışı için beklenen satır-odaklı girdi biçimi değildir.
Tek bir JSON kaynağı, aynı `process()` çağrısı içinde hem klasik `&=` gövde işaretçisini hem de başlık ve altbilgi bölümlerindeki çift açılı köşeli `<<>>` yer tutucularını çözebilir. Başlık ve altbilgi yer tutucularının çözülmesi için yine `designer.setEnableHeaderFooterMarkers(true)` çağrısı yapılmalıdır.

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
// Left header, right header, and a classic body marker — one JSON source feeds all three
worksheet.getPageSetup().setHeader(0, "<<node.Company>>");
worksheet.getPageSetup().setHeader(2, "Page <<node.Title>>");
worksheet.getCells().get("A1").putValue("&=node.Company");
const designer = new AsposeCells.WorkbookDesigner(workbook);
designer.setEnableHeaderFooterMarkers(true);
designer.setJsonDataSource("node", '[{"Company":"Aspose Pty Ltd","Title":"Half-Year Report"}]');
designer.process();
console.log("Left: " + worksheet.getPageSetup().getHeader(0));
console.log("Right: " + worksheet.getPageSetup().getHeader(2));
console.log("Body: " + worksheet.getCells().get("A1").getStringValue());
// This prints:
// Left: Aspose Pty Ltd
// Right: Page Half-Year Report
// Body: Aspose Pty Ltd
workbook.save("HeaderFooterJsonMarkers.xlsx");
```

## **Anahtar ve Çok Satırlı Kaynak Anlamı**
`setEnableHeaderFooterMarkers` varsayılan olarak `false`tır ve ayar yalnızca başlık ve altbilgi `<<Source.Field>>` yer tutucularını kontrol eder. Anahtar kapalıyken `process()` hâlâ klasik `&=` gövde işaretçilerini çözer, ancak bir başlık ya da altbilgi içindeki `<<Source.Field>>` yer tutucu düz metin olarak kalır.
Bir başlık ya da altbilgi bölümü tek bir dizedir, tekrar eden bir bant değildir. Veri kaynağı birden çok satır içeriyorsa, ilk satır başlık ve altbilgi değerlerini sağlar. Çözüldükten sonra değerler sıradan başlık ya da altbilgi metni haline gelir. `save` metodunu çağırdıktan sonra çalışma kitabında kalır ve kaydedilen çalışma kitabını yeniden yüklediğinizde de mevcut olur.
Aşağıdaki örnek, aynı çok satırlı JSON kaynağı üzerine iki çalışma kitabı oluşturarak devre dışı ve etkin davranışı karşılaştırır. `plainDesigner` yer tutucuyu değiştirmezken, `enabledDesigner` ilk satırı kullanarak çözer.

```javascript
const AsposeCells = require("aspose.cells");
const table = '[{"Name":"First Row"},{"Name":"Second Row"}]';
// Without the switch the placeholder stays literal text
const plainWorkbook = new AsposeCells.Workbook();
const plainSheet = plainWorkbook.getWorksheets().get(0);
plainSheet.getPageSetup().setHeader(1, "<<node.Name>>");
const plainDesigner = new AsposeCells.WorkbookDesigner(plainWorkbook);
plainDesigner.setJsonDataSource("node", table);
plainDesigner.process();
// With the switch on, the FIRST row of a multi-row source wins
const enabledWorkbook = new AsposeCells.Workbook();
const enabledSheet = enabledWorkbook.getWorksheets().get(0);
enabledSheet.getPageSetup().setHeader(1, "<<node.Name>>");
const enabledDesigner = new AsposeCells.WorkbookDesigner(enabledWorkbook);
enabledDesigner.setEnableHeaderFooterMarkers(true);
enabledDesigner.setJsonDataSource("node", table);
enabledDesigner.process();
console.log("Without switch: " + plainSheet.getPageSetup().getHeader(1));
console.log("With switch: " + enabledSheet.getPageSetup().getHeader(1));
// This prints:
// Without switch: <<node.Name>>
// With switch: First Row
enabledWorkbook.save("HeaderFooterMarkersEnabled.xlsx");
```

## **Bir Resmi Başlık veya Alt Bilgiye Bağlama**
`(picture)` eki, bir resmi başlık ya da altbilgi bölümüne bağlar. Resmin görünmesini istediğiniz yere `<<node.logo(picture)>>` yazın ve alan değerini bir veri URI’si olarak sağlayın — `data:image/png;base64,` önekinin ardından resim baytlarının Base64 metni gelir. `data:` öneki olmayan yalnızca Base64 dizesi bir resim gömmez.
`process()` sonrası:
1. Yer tutucu, standart başlık ve altbilgi resim kodu olan `&G` ile değiştirilir. İşaretçi, bölüm dizesi içinde bir kod haline geldiği için `Logo: <<node.logo(picture)>>` gibi daha uzun metinlerin içinde de bulunabilir.
2. Resim baytları, ilgili çalışma sayfasının başlık/altbilgi çizim katmanına eklenmiş bir medya parçası olarak çalışma kitabına gömülür; bu sayede resim başlık ya da altbilgi ile birlikte yazdırılır.

```javascript
const AsposeCells = require("aspose.cells");
const fs = require("fs");
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
// The (picture) suffix binds the image named by the data-URI field into the header
worksheet.getPageSetup().setHeader(1, "Logo: <<node.logo(picture)>>");
const table = [
    {
        logo: "data:image/png;base64," + fs.readFileSync("logo.png").toString("base64")
    }
];
const designer = new AsposeCells.WorkbookDesigner(workbook);
designer.setEnableHeaderFooterMarkers(true);
designer.setJsonDataSource("node", JSON.stringify(table));
designer.process();
console.log("Header: " + worksheet.getPageSetup().getHeader(1));
// This prints:
// Header: Logo: &G
workbook.save("HeaderFooterPicture.xlsx");
```

Yazdırılan `&G`, Excel’in başlığı işlerken yorumladığı resim kodudur — `logo.png` baytları artık `HeaderFooterPicture.xlsx` içinde bulunur ve resim kodun yerine yazdırılır.
Başlık ve altbilgi Akıllı İşaretçilerini kullanmak için `setHeader` ve `setFooter` ile sol, orta ve sağ bölümlere `<<Source.Field>>` yer tutucularını yazın. `process()` çağırmadan önce `designer.setEnableHeaderFooterMarkers(true)` yapın ve değerleri `designer.setJsonDataSource(name, json)` ile sağlayın. Tamamlanmış bölümleri `getHeader` ve `getFooter` ile okuyun. Aynı veri kaynağı, bir işleme aşamasında gövde işaretçilerini ve başlık/altbilgi yer tutucularını besleyebilir. Bir bölüme resim bağlamak için `(picture)` ekini veri-URI değeriyle ekleyin.

## **İlgili Makaleler**
- [SmartMarker Tek Hücre Dizi İşleme](/tr/nodejs-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)

{{< app/cells/assistant language="nodejs-java" >}}