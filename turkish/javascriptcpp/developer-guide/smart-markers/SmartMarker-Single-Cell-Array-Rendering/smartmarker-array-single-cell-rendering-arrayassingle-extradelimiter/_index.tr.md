---
title: Akıllı İşaret Tek Hücre Dizisi Oluşturma | Aspose.Cells for JavaScript via C++
description: Aspose.Cells for JavaScript via C++ kullanarak Akıllı İşaretler içinde ArrayAsSingle ve ExtraDelimiter öznitelikleriyle dizi verisini tek hücreye oluşturmayı öğrenin.
linktitle: Akıllı İşaret Tek Hücre Dizisi Oluşturma | Aspose.Cells
url: /tr/javascript-cpp/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++ kitaplığı, elektronik tablo, Akıllı İşaretler, ArrayAsSingle, ExtraDelimiter, tek hücre dizisi, dizi oluşturma, şablon
type: docs
weight: 195
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells, Akıllı İşaretler aracılığıyla dizi verisini tek hücreye oluşturmayı destekler. Geliştiriciler, `ArrayAsSingle` özniteliğini `ExtraDelimiter` özniteliğiyle birlikte kullanarak dizi öğelerinin tek hücre içinde nasıl ayrılacağını denetleyebilir; bu da raporlar ve şablonlar için esnek biçimlendirme sağlar.
{{% /alert %}}

## **Giriş**
Aspose.Cells içindeki Akıllı İşaretler, `&=DataSource.Field` gibi işaret ifadeleri kullanarak elektronik tablo verisini dinamik olarak doldurmanıza olanak tanıyan güçlü ve şablon tabanlı bir özelliktir. İşaret, tasarım çalışma kitabına yerleştirilir ve şablon `WorkbookDesigner` tarafından işlendiğinde işaretler, sağlanan veri kaynağındaki değerlerle değiştirilir.
Varsayılan olarak, bir Akıllı İşaret bir dizi özelliğine başvurduğunda (örneğin `&=DataSource.Numbers`), motor diziyi genişletir ve her öğeyi ayrı bir komşu hücreye yerleştirir; bu işlem yatay olarak bir satır boyunca veya dikey olarak bir sütun boyunca gerçekleşir. Bu davranış birçok senaryoda kullanışlı olsa da, tüm diziyi öğeleri birleştirerek ve tercih ettiğiniz bir ayırıcıyla ayırarak tek bir hücreye oluşturmak isteyebileceğiniz durumlar vardır.
`ArrayAsSingle` ve `ExtraDelimiter` öznitelikleri, bir Akıllı İşaret etiketi içinde birlikte kullanıldıklarında tam olarak bu ihtiyacı karşılar. Rapor düzenlerini kompakt ve öngörülebilir tutmanızı sağlarken dizi veri kaynaklarıyla doğrudan çalışmaya devam etmenizi sağlar.

## **Bu Özelliğe Neden İhtiyaç Duyulur**

### **Varsayılan Dizi Yayma Davranışı**
Bir Akıllı İşaret bir dizi özelliğine başvurduğunda Aspose.Cells varsayılan olarak diziyi birden fazla hücreye yayıntılar. Örneğin, dört dizeden oluşan bir diziye karşılık `&=Product.Tags` gibi bir işaret, her değeri kendi hücresine yerleştirir; diğer şablon içeriğini dışarı doğru iter ve özenle tasarlanmış rapor düzenlerini bozabilir.

### **Kullanım Alanı Sınırlamaları**
Varsayılan yayma davranışının istenmeyen olduğu birçok pratik senaryo bulunur:
- **Özet biçimli raporlar**: kayıt başına tek satırlık kompakt bir düzen gerektiren raporlar.
- **Etiket, ad etiketi veya anahtar sözcük listeleri**: virgülle veya boru işaretiyle ayrılmış değerler olarak tek bir hücrede gösterilmesi gerekenler.
- **Filtre çipleri veya durum göstergeleri**: okunabilirlik amacıyla birden fazla değeri tek bir yerde gruplayanlar.
- **Alt akış işlem hatları** (CSV dışa aktarma, PDF oluşturma, posta birleştirme): hücre başına genişletilmiş bir aralık yerine tek birleştirilmiş değer bekleyenler.
- **Platformlar arası uyumluluk**: dizilerin birden fazla hücreye yayılmasını kabul edemeyen bazı tüketicilerin olduğu durumlar.

### **Doldurduğu Boşluk**
Yerleşik bir mekanizma olmadan, geliştiriciler verileri JavaScript'te önceden işlemek zorunda kalırdı; çalışma kitabı tasarımcısına bağlamadan önce dizileri ayırıcı kullanılan dizelere birleştirirlerdi. Bu yaklaşım mantığı çoğaltır, veri modellerini karmaşıklaştırır ve hata olasılığını artırır. `ArrayAsSingle` ve `ExtraDelimiter` öznitelikleri, biçimlendirmeyi Akıllı İşaret etiketinin içinde bildirimsel olarak ele alarak bu zorunlu çalışma etrafını ortadan kaldırır.

## **Özellik Avantajları**
Akıllı İşaretler'de `ArrayAsSingle` ve `ExtraDelimiter` özniteliklerini kullanmak birkaç avantaj sağlar:
- **Tek hücrede toplanma**: Tüm dizi öğeleri tam olarak tek bir hücreye oluşturulur; bu, düzenleri kompakt ve öngörülebilir tutar.
- **Özel ayırıcı denetimi**: İstediğiniz ayırıcı dizeyi belirtin — virgül, noktalı virgül, tire, dikey çizgi, satır sonu veya özel metin.
- **Şablon tabanlı biçimlendirme**: Verileri önceden işlemek için ek kod gerekmez; biçimlendirme kuralları Akıllı İşaret etiketinin içinde bulunur.
- **Daha temiz raporlar**: Dizi verisi, komşu şablon içeriğini farklı satırlara veya sütunlara itmez.
- **Esnek veri türleri**: Dize, sayı, tarih ve ayırıcıyla birleştirilebilen diğer tüm veri türleriyle çalışır.
- **Geriye uyumluluk**: Öznitelikler belirtilmediğinde özgün yayma davranışı korunur; böylece mevcut şablonlar değişmeden çalışmaya devam eder.

## **Bu Özellik Nasıl Kullanılır**

### **Akıllı İşaret Sözdizimi**
`ArrayAsSingle` ve `ExtraDelimiter` öznitelikleri, standart Akıllı İşaret sözdiziminin parantezleri içinde anahtar-değer çiftleri olarak geçirilir. Genel sözdizimi şöyledir:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, WorkbookDesigner } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const product = {
                Tags: ["C#", "Aspose", "SmartMarker", "Excel"]
            };
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            cells.get("A1").value = "Tags";
            cells.get("A2").value = '&=Product.Tags(arrayasSingle=true, extraDelimiter=", ")';
            const designer = new WorkbookDesigner();
            designer.setWorkbook(workbook);
            designer.setDataSource("Product", product);
            designer.process();
            const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_arraySingle.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

İşaret aşağıdaki bölümlerden oluşur:
- `&=DataSource.ArrayProperty` — bağlı veri kaynağındaki dizi özelliğine başvuran standart Akıllı İşaret.
- `arrayasSingle=true` — motorun dizinin tamamını tek hücreye oluşturmasını sağlar. Tek hücre davranışını yalnızca `true` değeri tetikler.
- `extraDelimiter=", "` — dizi öğeleri arasına yerleştirilecek ayırıcıyı tanımlar. Değer bir dize sabitidir; boş, tek karakterli veya çok karakterli olabilir.

{{% alert color="primary" %}}
`extraDelimiter` özniteliği; çok karakterli ayırıcılar, özel metin veya satır sonuyla ayrılmış çıktı için `\n` gibi kaçış dizileri dâhil her türlü dize sabitini kabul eder. Dizi boşsa, oluşturulan hücre boş bırakılır.
{{% /alert %}}

### **Adım Adım İş Akışı**
Aşağıdaki iş akışı, Akıllı İşaretler kullanılarak bir dizinin tek hücreye nasıl oluşturulacağını açıklar.
1. **Veri kaynağını hazırlayın**: Dizi döndüren bir özelliği sunan bir nesne (veya veri yapısı) oluşturun. Özellik, dize, sayı veya desteklenen diğer herhangi bir değer türünden oluşan bir dizi döndürebilir.
2. **Tasarım çalışma kitabı oluşturun**: Yeni bir `Workbook` oluşturun, başlık satırı ekleyin ve dizi özelliğine başvuran, `arrayasSingle` ve `extraDelimiter` özniteliklerini içeren bir Akıllı İşaret hücresi yerleştirin.
3. **`WorkbookDesigner` örneğini oluşturun**: Bir `WorkbookDesigner` nesnesi oluşturun, tasarım çalışma kitabını bu nesneye ekleyin ve veri kaynağınızı `setDataSource` yöntemiyle bağlayın.
4. **İşaretleri işleyin**: Akıllı İşaretleri genişletmek ve çalışma kitabını gerçek verilerle doldurmak için `workbookDesigner.process()` yöntemini çağırın.
5. **Sonucu kaydedin**: Oluşturulan çalışma kitabını diskte XLSX veya desteklenen diğer bir dosya biçiminde kaydedin.

### **Kod Örneği 1 — Temel Dize Dizisi Oluşturma**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample" disabled>Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        class Student {
            constructor(scores) {
                this.Scores = scores;
            }
        }
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            document.getElementById("runExample").disabled = false;
            console.log("Aspose.Cells initialized");
        });
        document.getElementById("runExample").addEventListener("click", async () => {
            const student = new Student([95, 88, 76, 100, 67]);
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            cells.get("A1").value = "Scores";
            cells.get("A2").value = student.Scores.join(" - ");
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], {
                type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            });
            const downloadLink = document.getElementById("downloadLink");
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_numericArray.xlsx";
            downloadLink.style.display = "block";
            document.getElementById("result").innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

### **Kod Örneği 2 — Özel Ayırıcılı Sayı Dizisi**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, WorkbookDesigner, SaveFormat } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const order = {
                Items: ["Apple", "Banana", "Cherry", "Date"]
            };
            const workbook = new Workbook();
            const sheet = workbook.worksheets.get(0);
            const cells = sheet.cells;
            // Section 1: Default Smart Marker - values spread horizontally across cells
            cells.get("A1").value = "Default Spreading Behavior:";
            cells.get("A2").value = "&=Order.Items";
            // Section 2: New single-cell rendering using arrayasSingle and extraDelimiter
            cells.get("A4").value = "Single Cell Rendering (arrayasSingle=true):";
            cells.get("A5").value = '&=Order.Items(arrayasSingle=true, extraDelimiter="; ")';
            // Bind the data source and process Smart Markers
            const designer = new WorkbookDesigner();
            designer.setWorkbook(workbook);
            designer.setDataSource("Order", order);
            designer.process();
            // Save the resulting workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_comparison.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

### **Kod Örneği 3 — Varsayılan Davranış ile ArrayAsSingle Davranışının Karşılaştırılması**

### **Notlar ve En İyi Uygulamalar**
`ArrayAsSingle` ve `ExtraDelimiter` öznitelikleriyle çalışırken aşağıdaki noktaları göz önünde bulundurun:
- `extraDelimiter` değeri bir dize sabiti olarak ele alınır; şablon işleyicinin yorumlayabileceği özel karakterler için kaçış uygulayın.
- `arrayasSingle` özniteliği mantıksal bir değer (`true` / `false`) kabul eder. Tek hücre davranışını yalnızca `true` tetikler; diğer her değer varsayılan yayma davranışına geri döner.
- Dizi boş veya `null` ise hücre boş bırakılır (veya veri türüne bağlı olarak boş bir dize içerir).
- Özellik, nesne veri kaynaklarıyla ve bir sütunun dizilere ayrılabildiği tablusal veri kaynaklarıyla da çalışır.
- Satır sonuyla ayrılmış çıktı için ayırıcı değeri olarak `\n` kullanın.

## İlgili Makaleler

{{< app/cells/assistant language="javascript-cpp" >}}