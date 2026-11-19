---
title: Üstbilgi ve Altbilgi İçindeki Akıllı İşaretçiler | Aspose.Cells .NET
linktitle: Üstbilgi ve Altbilgi Akıllı İşaretçileri | Aspose.Cells
description: Sayfa üstbilgi ve altbilgilerine çift açılı köşeli sözdizimi ve WorkbookDesigner.EnableHeaderFooterMarkers anahtarını kullanarak DataTable veya JSON veri kaynaklarıyla Smart Marker yer tutucuları ekleyin ve resimleri veri URI'larıyla bağlayın, Aspose.Cells for .NET içinde.
keywords: Aspose.Cells, Akıllı İşaretçiler, üstbilgiler, altbilgiler, üstbilgi altbilgi işaretçileri, EnableHeaderFooterMarkers, WorkbookDesigner, PageSetup, SetHeader, SetFooter, SetJsonDataSource, DataTable, veri bağlama, resim, data URI, C#
type: docs
weight: 196
url: /tr/net/smart-markers-in-headers-and-footers/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
Sayfa üstbilgileri ve altbilgileri genellikle rapor başlığı, raporlama dönemi, yazar ve departman gibi rapor meta verilerini içerir. Bu bilgi zaten çalışma kitabını doldurmak için kullanılan veri kaynağında mevcutsa, elle tekrarlamak gereksiz çoğaltma oluşturur.  
Klasik Akıllı İşaretçi sözdizimi, `&=Source.Field`, çalışma sayfası gövde hücrelerinde işlenir. `PageSetup.SetHeader` veya `PageSetup.SetFooter` aracılığıyla bir klasik işaretçiyi üstbilgi veya altbilgiye yerleştirirseniz, bu metin `WorkbookDesigner.Process()` tarafından taranan çalışma sayfası hücre ızgarasının bir parçası olmadığı için düz metin olarak kalır.  
**Aspose.Cells for .NET 26.11** ile birlikte, varsayılan olarak `false` olan `WorkbookDesigner.EnableHeaderFooterMarkers` anahtarı, `Process()`'in üstbilgi ve altbilgi bölüm dizgelerinde `<<Source.Field>>` olarak yazılmış yer tutucuları çözmesini sağlar — `Process()`'i çağırmadan önce bunu `true` olarak ayarlayın. Üstbilgi ve altbilgi yer tutucuları gövde işaretçileriyle aynı veri kaynağını kullanır.  
Her üstbilgi ve altbilgi üç adreslenebilir bölüm içerir:
- Bölüm `0` sol bölümdür.
- Bölüm `1` orta bölümdür.
- Bölüm `2` sağ bölümdür.  
`PageSetup.SetHeader(int section, string value)` ve `PageSetup.SetFooter(int section, string value)` kullanarak bu bölümleri yazın. İşlendikten sonra, tamamlanmış metni almak için `PageSetup.GetHeader(int section)` ve `PageSetup.GetFooter(int section)` kullanın.

{{% alert color="primary" %}}
`<<Source.Field>>` gibi bir yer tutucu, alan değerini metin olarak bölüm dizgesine ekler. Görseller, `(picture)` eki ve bir data-URI değeriyle bağlanır.
{{% /alert %}}

## **Üstbilgi ve Altbilgi İşaretçilerini DataTable ile Etkinleştirme**
Aşağıdaki adımları **Aspose.Cells for .NET 26.11** içinde bir `DataTable` kullanarak üstbilgi ve altbilgi yer tutucularını çözmek için izleyin:
1. `Workbook` oluşturun ve indeks `0`'da bulunan ilk `Worksheet`'i alın.
2. `PageSetup.SetHeader` ve `PageSetup.SetFooter` ile istediğiniz üstbilgi ve altbilgi bölümlerine `<<Source.Field>>` yer tutucularını yazın.
3. `DataTable` oluşturun ve tablo adı, yer tutucular tarafından kullanılan kaynak önek ile eşleşsin. Örneğin, `node` adlı bir tablo `<<node.Name>>` gibi yer tutuculara karşılık gelir.
4. Çalışma kitabı için bir `WorkbookDesigner` oluşturun.
5. İşleme başlamadan önce `designer.EnableHeaderFooterMarkers` değerini `true` olarak ayarlayın.
6. `designer.SetDataSource(table)` ile tabloyu bağlayın.
7. `designer.Process()` çağırın.
8. İşlemeden sonra, yer tutucular üstbilgi veya altbilgi metninde artık bulunmaz. Tamamlanmış bölüm dizgelerini almak için `GetHeader` ve `GetFooter` kullanın.

```csharp
using System;
using System.Data;
using Aspose.Cells;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// Center header and center footer carry <<Source.Field>> placeholders
worksheet.PageSetup.SetHeader(1, "Quarterly Report - <<node.Name>>");
worksheet.PageSetup.SetFooter(1, "Prepared by <<node.Author>>");
DataTable table = new DataTable("node");
table.Columns.Add("Name");
table.Columns.Add("Author");
table.Rows.Add("Q4 2026", "Aspose.Cells");
WorkbookDesigner designer = new WorkbookDesigner(workbook);
designer.EnableHeaderFooterMarkers = true;
designer.SetDataSource(table);
designer.Process();
Console.WriteLine("Header: " + worksheet.PageSetup.GetHeader(1));
Console.WriteLine("Footer: " + worksheet.PageSetup.GetFooter(1));
// This prints:
// Header: Quarterly Report - Q4 2026
// Footer: Prepared by Aspose.Cells
workbook.Save("HeaderFooterSmartMarkers.xlsx");
```

## **JSON Veri Kaynağı Kullanımı**
Rapor verileri zaten JSON biçiminde mevcut olduğunda, `DataTable` yerine JSON kullanabilirsiniz. Kaynağı eklemek için `WorkbookDesigner.SetJsonDataSource(string name, string json)` çağırın.  
`name` argümanı, `DataTable` adıyla aynı rolü oynar. Örneğin, `node` adı `<<node.Company>>` ve `<<node.Title>>` gibi yer tutuculara karşılık gelir.  
`SetJsonDataSource`'a satır verilerini doğrudan geçirin:
- Bir satır dizisi, bir veya daha fazla satır nesnesi içeren bir JSON dizisi gibi, desteklenir.
- Tek bir satır nesnesi de doğrudan geçirilebilir.
- Satırları `{"rows":[...]}` gibi adlandırılmış bir üst düzey anahtar altında sarmalamayın. Bu sarmalayıcı, bu iş akışı için beklenen satır odaklı giriş biçimi değildir.  
Tek bir JSON kaynağı, aynı `Process()` çağrısı sırasında her iki işaretçi stilini de doldurabilir. Çalışma sayfası gövde hücresindeki klasik `&=` işaretçisini ve üstbilgi ve altbilgi bölümlerindeki çift açılı köşeli `<<>>` yer tutucularını çözer. Üstbilgi ve altbilgi yer tutucularının çözülmesi için hâlâ `EnableHeaderFooterMarkers`'ı etkinleştirmeniz gerekir.

```csharp
using System;
using Aspose.Cells;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// Left header, right header, and a classic body marker — one JSON source feeds all three
worksheet.PageSetup.SetHeader(0, "<<node.Company>>");
worksheet.PageSetup.SetHeader(2, "Page <<node.Title>>");
worksheet.Cells["A1"].PutValue("&=node.Company");
WorkbookDesigner designer = new WorkbookDesigner(workbook);
designer.EnableHeaderFooterMarkers = true;
designer.SetJsonDataSource("node", "[{\"Company\":\"Aspose Pty Ltd\",\"Title\":\"Half-Year Report\"}]");
designer.Process();
Console.WriteLine("Left: " + worksheet.PageSetup.GetHeader(0));
Console.WriteLine("Right: " + worksheet.PageSetup.GetHeader(2));
Console.WriteLine("Body: " + worksheet.Cells["A1"].StringValue);
// This prints:
// Left: Aspose Pty Ltd
// Right: Page Half-Year Report
// Body: Aspose Pty Ltd
workbook.Save("HeaderFooterJsonMarkers.xlsx");
```

## **Anahtar ve Çok Satırlı Kaynak Anlamı**
`EnableHeaderFooterMarkers` varsayılan olarak `false`dır ve anahtar yalnızca üstbilgi ve altbilgi `<<Source.Field>>` yer tutucularını kontrol eder. Anahtar kapalıyken, `Process()` hâlâ klasik `&=` gövde işaretçilerini çözer, ancak bir üstbilgi veya altbilgi içindeki `<<Source.Field>>` yer tutucu sabit metin olarak kalır.  
Bir üstbilgi veya altbilgi bölümü tek bir dizgi olup tekrarlanan bir bant değildir. Veri kaynağı birkaç satır içeriyorsa, ilk satır üstbilgi ve altbilgi değerlerini sağlar. Çözüldükten sonra, bu değerler normal üstbilgi veya altbilgi metni haline gelir. `Save`'i çağırdıktan sonra çalışma kitabında kalır ve kaydedilen çalışma kitabını tekrar yüklediğinizde mevcut olur.  
Aşağıdaki örnek, aynı çok satırlı `DataTable` üzerinden iki çalışma kitabı oluşturur ve devre dışı ve etkin davranışı karşılaştırır. `plainDesigner` yer tutucuyu değiştirmeden bırakırken, `enabledDesigner` ilk satırı kullanarak çözer.

```csharp
using System;
using System.Data;
using Aspose.Cells;
DataTable table = new DataTable("node");
table.Columns.Add("Name");
table.Rows.Add("First Row");
table.Rows.Add("Second Row");
// Without the switch the placeholder stays literal text
Workbook plainWorkbook = new Workbook();
Worksheet plainSheet = plainWorkbook.Worksheets[0];
plainSheet.PageSetup.SetHeader(1, "<<node.Name>>");
WorkbookDesigner plainDesigner = new WorkbookDesigner(plainWorkbook);
plainDesigner.SetDataSource(table);
plainDesigner.Process();
// With the switch on, the FIRST row of a multi-row source wins
Workbook enabledWorkbook = new Workbook();
Worksheet enabledSheet = enabledWorkbook.Worksheets[0];
enabledSheet.PageSetup.SetHeader(1, "<<node.Name>>");
WorkbookDesigner enabledDesigner = new WorkbookDesigner(enabledWorkbook);
enabledDesigner.EnableHeaderFooterMarkers = true;
enabledDesigner.SetDataSource(table);
enabledDesigner.Process();
Console.WriteLine("Without switch: " + plainSheet.PageSetup.GetHeader(1));
Console.WriteLine("With switch: " + enabledSheet.PageSetup.GetHeader(1));
// This prints:
// Without switch: <<node.Name>>
// With switch: First Row
enabledWorkbook.Save("HeaderFooterMarkersEnabled.xlsx");
```

## **Üstbilgi veya Altbilgiye Resim Bağlama**
`(picture)` eki, bir resmi üstbilgi veya altbilgi bölümüne bağlar. Görselin görüneceği yerde `<<node.logo(picture)>>` yazın ve alan değerini bir data-URI olarak sağlayın — `data:image/png;base64,` önekini ekleyip görüntü baytlarının Base64 metnini ekleyin. `data:` öneki olmadan yalnızca Base64 dizesi bir resmi gömmeyecek.  

`Process()` sonrasında:
1. Yer tutucu `&G` ile değiştirilir; bu, standart üstbilgi ve altbilgi resim kodudur. İşaretçi, bölüm dizgesi içinde bir kod haline geldiği için `Logo: <<node.logo(picture)>>` gibi daha uzun metinlerin içinde yer alabilir.
2. Görüntü baytları, çalışma sayfasının üstbilgi/altbilgi çizim katmanına eklenen bir medya parçası olarak çalışma kitabına gömülür, böylece resim üstbilgi veya altbilgiyle birlikte yazdırılır.

```csharp
using System;
using System.Data;
using System.IO;
using Aspose.Cells;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// The (picture) suffix binds the image named by the data-URI field into the header
worksheet.PageSetup.SetHeader(1, "Logo: <<node.logo(picture)>>");
DataTable table = new DataTable("node");
table.Columns.Add("logo");
table.Rows.Add("data:image/png;base64," + Convert.ToBase64String(File.ReadAllBytes("logo.png")));
WorkbookDesigner designer = new WorkbookDesigner(workbook);
designer.EnableHeaderFooterMarkers = true;
designer.SetDataSource(table);
designer.Process();
Console.WriteLine("Header: " + worksheet.PageSetup.GetHeader(1));
// This prints:
// Header: Logo: &G
workbook.Save("HeaderFooterPicture.xlsx");
```

Yazdırılan `&G`, Excel'in üstbilgiyi işlerken yorumladığı resim kodudur — `logo.png` baytları artık `HeaderFooterPicture.xlsx` içinde bulunur ve resim kodun yerine yazdırılır.  
Üstbilgi ve altbilgi Akıllı İşaretçilerini kullanmak için, `SetHeader` ve `SetFooter` ile sol, orta ve sağ üstbilgi veya altbilgi bölümlerine `<<Source.Field>>` yer tutucularını yazın. `Process()`'i çağırmadan önce `WorkbookDesigner` üzerinde `EnableHeaderFooterMarkers`'ı `true` olarak ayarlayın ve değerleri `SetDataSource(DataTable)` veya `SetJsonDataSource` aracılığıyla sağlayın. Tamamlanmış bölümleri `GetHeader` ve `GetFooter` ile okuyun. Aynı veri kaynağı bir işlem geçişinde gövde işaretçilerini ve üstbilgi veya altbilgi yer tutucularını doldurabilir. Bir bölüme resim bağlamak için `(picture)` ekini bir data-URI değeriyle ekleyin.

## **İlgili Makaleler**
- [SmartMarker Tek Hücre Dizi İşleme](/cells/tr/net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)

{{< app/cells/assistant language="csharp" >}}