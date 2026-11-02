---
title: Bir Hücreye Görsel Ekleme
linktitle: Bir Hücreye Görsel Ekleme
description: Aspose.Cells for JavaScript via C++, elektronik tablo dosyalarıyla çalışmak için kullanılan bir kitaplıktır. Bu makale, bir görseli tek bir hücreye tam olarak sığdırmanın iki yolunu açıklar. Görseli hücrenin üzerinde kayan bir nesne olarak yerleştirebilir veya doğrudan hücreye gömbilirsiniz.
keywords: Aspose.Cells, JavaScript via C++ kitaplığı, elektronik tablo, görsel ekleme, görsel gömme, hücrede görsel, görseli hücreye sığdırma, Pictures, EmbeddedImage
type: docs
weight: 80
url: /tr/javascript-cpp/inserting-an-image-into-a-cell/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells, bir görseli tek bir hücreyle ilişkilendirmenin iki farklı yolunu sunar. Kayan görsel, çalışma sayfasının çizim katmanında bulunan ve bir hücre aralığının üzerini görsel olarak kaplayan bir şekildir; gömülü görsel ise hücrenin kendi içinde saklanır ve hücrenin görüntüleme alanına sığacak şekilde otomatik olarak ölçeklenir. Düzen gereksinimlerinize en uygun yöntemi seçin.
{{% /alert %}}

## **Giriş**
Görsel raporlar, ürün katalogları, çalışan dizinleri, gösterge panoları veya envanter listeleri işlevi gören elektronik tablolar tasarlarken bir görseli tek bir hücreye tam olarak sığdırmak yaygın bir gerekliliktir. Bir görseli çok sayıda hücre üzerinde gererek veya çalışma sayfasına dağınık biçimde yerleştirmek yerine, temiz bir görselin hücreye bağlı kalmasını ve ait olduğu hücreyle hizalı olmasını isteyebilirsiniz.
Aspose.Cells bu senaryoyu birbirini tamamlayan iki şekilde destekler:
- **Yöntem 1 — Bir hücrenin üzerine kayan görsel yerleştirin.** Çalışma sayfasına bir `Picture` ekleyin, yerleşimini `picture.setPlacement(PlacementType.MoveAndSize)` ile ayarlayın ve `picture.setUpperLeftRow()`, `picture.setUpperLeftColumn()`, `picture.setLowerRightRow()` ve `picture.setLowerRightColumn()` aracılığıyla çapa hücrelerini düzenleyerek görselin tam olarak tek bir hücreyi kaplamasını sağlayın.
- **Yöntem 2 — Bir görseli doğrudan hücreye gömer.** Görsel verisi içeren `Buffer` nesnesini `cell.setEmbeddedImage(imageBuffer)` ile hücreye atayın. Görsel, hücrenin görüntüleme alanına sığacak şekilde otomatik olarak ölçeklenir ve hücreyle birlikte taşınır.
Bu makalenin kalan bölümü her iki yöntemi de ele alır, ilgili API'leri açıklar ve bunların kod içinde nasıl kullanılacağını gösterir.

## **Yöntem 1: Bir Hücrenin Üzerine Görsel Yerleştirme**
Kayan görsel, çalışma sayfasının çizim katmanında bulunan bir `Picture` nesnesidir. Tek bir hücrenin parçası olmasa da bir hücre aralığına çapalanır. Görselin çapa hücreleri, yani sol üst ve sağ alt köşeleri, görselin çalışma sayfasındaki kapsamını belirler. Varsayılan olarak, yeni eklenen bir görsel birkaç hücreyi kaplar.
Bir kayan görselin **tam olarak tek bir hücreyi** kaplaması için:
1. `worksheet.getPictures().add(row, column, imageBuffer)` kullanarak görseli ekleyin; burada `imageBuffer`, görsel verisi içeren bir `Buffer` nesnesidir. Bu işlem yeni görseli verilen hücreye çapalar.
2. Görselin sınır dikdörtgeni hedef hücreyle örtüşecek şekilde dört çapa değerini ayarlayın.
3. Kullanıcı sütun genişliğini veya satır yüksekliğini değiştirdiğinde görselin altındaki hücreyle birlikte taşınması ve yeniden boyutlandırılması için `picture.setPlacement(PlacementType.MoveAndSize)` çağrısını yapın.

### **Görseli Tek Bir Hücreye Çapalama**
Görselin çapası, sıfırdan başlayan dört dizin değeriyle belirlenir:
- `picture.getUpperLeftRow()` ve `picture.setUpperLeftRow(value)` — görselin üst kenarının bulunduğu satırın dizini.
- `picture.getUpperLeftColumn()` ve `picture.setUpperLeftColumn(value)` — görselin sol kenarının bulunduğu sütunun dizini.
- `picture.getLowerRightRow()` ve `picture.setLowerRightRow(value)` — görselin alt kenarının bulunduğu satırın dizini. Görselin alt kenarını `r` satırının alt kenarına yerleştirmek için bunu `r + 1` olarak ayarlayın.
- `picture.getLowerRightColumn()` ve `picture.setLowerRightColumn(value)` — görselin sağ kenarının bulunduğu sütunun dizini. Görselin sağ kenarını `c` sütununun sağ kenarına yerleştirmek için bunu `c + 1` olarak ayarlayın.

{{% alert color="primary" %}}
Aspose.Cells içindeki satır ve sütun dizinleri **sıfırdan başlar**. C6 hücresinin satır dizini 5, sütun dizini 2'dir. Sağ alt çapa koordinatlarında bir birimlik hata, görselin bitişik hücreye taşmış gibi görünmesinin en yaygın nedenidir.
{{% /alert %}}

### **Yerleşim Davranışını Denetleme**
`picture.getPlacement()` ve `picture.setPlacement(value)` metotları, kullanıcı altındaki satır veya sütunu yeniden boyutlandırdığında görselin nasıl davranacağını denetlemek için `PlacementType` enum değerlerini kullanır. Tek hücrelik görseller için önerilen değer `PlacementType.MoveAndSize`'dir. Bu değer, görselin altındaki hücreyle birlikte taşınmasını ve yeniden boyutlandırılmasını sağlayarak görselin hücreye tam olarak sığmasını korur.

### **Adım Adım Talimatlar**
1. Yeni bir `Workbook` oluşturun veya var olan birini açın.
2. Hedef `Worksheet` nesnesine `workbook.getWorksheets().getAt(0)` yoluyla erişin.
3. Görsel dosyasını diskten bir `Buffer` nesnesine okuyun; örneğin Node.js `fs.readFileSync` kullanabilirsiniz.
4. C6 hücresine çapalanmış bir görsel eklemek için `worksheet.getPictures().add(5, 2, imageBuffer)` çağrısını yapın. Bu metot, yeni görselin `Pictures` koleksiyonundaki dizinini döndürür; ilgili `Picture` nesnesini almak için bu dizini kullanın.
5. Görselin yalnızca C6 hücresini kaplaması için dört çapa koordinatını ayarlayın: `picture.setUpperLeftRow(5)`, `picture.setUpperLeftColumn(2)`, `picture.setLowerRightRow(6)` ve `picture.setLowerRightColumn(3)`.
6. Sütun veya satır yeniden boyutlandırıldığında görseli C6 ile hizalı tutmak için `picture.setPlacement(PlacementType.MoveAndSize)` çağrısını yapın.
7. Yalnızca C6 hücresinde görsel bulunduğunu göstermek için çevredeki hücrelere isteğe bağlı olarak örnek metin ekleyin.
8. Çalışma kitabını diskte bir `.xlsx` dosyası olarak kaydedin.
Aşağıdaki kod, bu yöntemin tamamını gösterir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".png,image/png" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const file = fileInput.files[0];
            if (!file) {
                document.getElementById('result').innerHTML =
                    '<p style="color: red;">Please select a PNG image.</p>';
                return;
            }
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const imageData = new Uint8Array(await file.arrayBuffer());
            const picIndex = worksheet.pictures.add(5, 2, imageData);
            const picture = worksheet.pictures.get(picIndex);
            picture.upperLeftRow = 5;
            picture.upperLeftColumn = 2;
            picture.lowerRightRow = 6;
            picture.lowerRightColumn = 3;
            picture.placement = AsposeCells.Drawing.PlacementType.MoveAndSize;
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Yöntem 2: Bir Görseli Doğrudan Hücreye Gömer**
Aspose.Cells, hücreye bağlı görseller için daha basit bir mekanizma sunar: `cell.setEmbeddedImage(imageBuffer)` metodu. Bu metotla görsel verisi atamak, görseli doğrudan hücreye, satır içi içerik gibi ekler.

### **Gömülü Görseller Nasıl Çalışır?**
- Görsel, çizim katmanındaki bir şekil olarak değil, hücre içeriğinin bir parçası olarak saklanır.
- Görsel, hücrenin görüntülenen alanına sığacak şekilde otomatik olarak ölçeklenir. Çapa koordinatlarına veya yerleşim ayarlarına gerek yoktur.
- Hücre, gerçek bir adrese sahip gerçek bir hücre olarak kalır; formüllerle referans alınabilir, bir satırın parçası olarak sıralanabilir veya diğer hücre düzeyi işlemlerde kullanılabilir.
Böylece, amacınız yalnızca "bu hücrenin içinde bulunan bir görsel" elde etmekse, `cell.setEmbeddedImage(imageBuffer)` en kısa seçenektir.

### **Adım Adım Talimatlar**
1. Yeni bir `Workbook` oluşturun veya var olan birini açın.
2. Hedef `Worksheet` nesnesine `workbook.getWorksheets().getAt(0)` yoluyla erişin.
3. Görsel dosyasını diskten bir `Buffer` nesnesine okuyun; örneğin Node.js `fs.readFileSync` kullanabilirsiniz.
4. Hedef hücreye bir referans alın — `worksheet.getCells().get("C6")` veya `worksheet.getCells().get(5, 2)`.
5. `Buffer` nesnesini `cell.setEmbeddedImage(imageBuffer)` ile hücreye aktarın.
6. Gömülü görsele daha belirgin bir görünüm kazandırmak için hedef satırın yüksekliğini ve sütunun genişliğini isteğe bağlı olarak ayarlayın.
7. Çalışma kitabını diskte bir `.xlsx` dosyası olarak kaydedin.
Aşağıdaki kod, bu yöntemin tamamını gösterir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".png,.jpg,.jpeg" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook } = AsposeCells;
        const asposeReady = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const downloadLink = document.getElementById('downloadLink');
            const result = document.getElementById('result');
            if (!fileInput.files || fileInput.files.length === 0) {
                result.innerHTML = '<p style="color: red;">Please select an image file.</p>';
                return;
            }
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            // C6 hedef hücresini al
            const cell = worksheet.cells.get("C6");
            // Görsel dosyasını bir bayt dizisine oku
            const imageData = new Uint8Array(await fileInput.files[0].arrayBuffer());
            // Görseli doğrudan hücreye göm
            cell.embeddedImage = imageData;
            // Gömülü görselin daha görünür olması için isteğe bağlı olarak satır yüksekliğini ve sütun genişliğini ayarla
            worksheet.cells.setColumnWidth(2, 30); // C sütunu (indeks 2)
            worksheet.cells.setRowHeight(5, 100); // 6. satır (indeks 5)
            // Sonuç çalışma kitabını .xlsx dosyası olarak kaydet
            const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xlsx";
            downloadLink.style.display = "block";
            result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Doğru Yöntemi Seçme**
Her iki yöntem de tek bir hücreye sığan bir görsel oluşturur; ancak görselin nasıl saklandığı ve nasıl davrandığı açısından farklılık gösterir:
- **Kayan görseli (Yöntem 1) şu durumlarda kullanın:**
  - Yerleşim, katmanlama veya diğer çizim nesneleriyle hizalama üzerinde daha ayrıntılı denetime ihtiyacınız olduğunda.
  - Görselin, seçilebilen, yeniden sıralanabilen veya diğer şekillerle gruplanabilen bir şekil gibi davranmasını istediğinizde.
  - `worksheet.getPictures()` üzerinden erişilen `Pictures` koleksiyonuyla çalışan mevcut kodla geriye dönük uyum gerektiğinde.
  - Çapa koordinatlarını çalışma sayfası düzenine göre dinamik olarak hesaplamanız gerektiğinde.
- **Gömülü görseli (Yöntem 2) şu durumlarda kullanın:**
  - Bir görseli hücreye eklemenin mümkün olan en basit yolunu istediğinizde.
  - Görselin diğer hücre içerikleri gibi hücreyle birlikte taşınması gerektiğinde.

## İlgili Makaleler
- [Aspose.Cells for JavaScript via C++ için Excel Kamerası](/cells/tr/javascript-cpp/excel-camera/)
- [Aspose.Cells for JavaScript via C++ için Özet Tabloya Filtre Alanları Ekleme](/cells/tr/javascript-cpp/add-page-field-in-pivot-table/)
- [Aspose.Cells for JavaScript via C++ için Özet Tablolara Biçimlendirme Uygulama](/cells/tr/javascript-cpp/apply-style-to-pivot-table/)
- [Aspose.Cells for JavaScript via C++ için Sparkline'ı Görsele ve HTML'ye Dönüştürme](/cells/tr/javascript-cpp/convert-sparkline-to-image-and-html/)

{{< app/cells/assistant language="javascript-cpp" >}}