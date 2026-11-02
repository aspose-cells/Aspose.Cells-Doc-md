---
title: Aspose.Cells for JavaScript via C++ ile Kıvılcım Grafiğini Görüntüye ve HTML'e Dönüştürme
linktitle: Aspose.Cells for JavaScript via C++ ile Kıvılcım Grafiğini Görüntüye ve HTML'e Dönüştürme
description: Tek hücreye gömme amacıyla Aspose.Cells kıvılcım grafiklerini bağımsız görüntülere nasıl işleyeceğinizi ve kıvılcım grafiği içeren çalışma sayfalarını HtmlSaveOptions kullanarak HTML olarak nasıl dışa aktaracağınızı öğrenin.
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++, kıvılcım grafiği, sparkline.toImage, cell.embeddedImage, HtmlSaveOptions, kıvılcım grafiği işleme, kıvılcım grafiğini görüntüye dönüştürme, kıvılcım grafiğini HTML'e dışa aktarma
type: docs
weight: 120
url: /tr/javascript-cpp/convert-sparkline-to-image-and-html/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Kıvılcım grafikleri, çalışma sayfası hücrelerine yerleştirilen minyatür grafiklerdir. Aspose.Cells, her kıvılcım grafiğini bağımsız bir görüntü olarak ayırmanıza (başka bir hücreye veya harici bir rapora gömmek üzere) ve kıvılcım grafiği içeren çalışma sayfasının tamamını, tarayıcıda tabanlı dağıtım için HTML olarak dışa aktarmanıza olanak tanır. Bu makalede kullanılan `cell.embeddedImage` özelliği **Aspose.Cells 26.5 ve sonraki sürümlerinde** kullanılabilir.
{{% /alert %}}

## **Giriş**
Kıvılcım grafikleri, eğilimleri doğrudan bir çalışma sayfası içinde görselleştirmenin kompakt bir yoludur. Excel kullanıcıları bunları hücrelerinin içinde görürken, gerçek dünya kullanım senaryolarının çoğunda bir kıvılcım grafiğinin hücreden çıkması gerekir; örneğin statik bir resim olarak farklı bir hücreye gömülmesi, otomatik bir e-postaya eklenmesi veya web'de yayımlanan bir HTML raporunun parçası olarak işlenmesi gerekir.
Aspose.Cells her iki işlemi de destekler. `sparkline.toImage` yöntemi tek bir kıvılcım grafiğini `Buffer` olarak işler. Elde edilen baytlar `cell.embeddedImage` özelliğine atanarak görüntünün çalışma kitabındaki tek bir hücre içinde saklanmasını sağlar. Ayrıca `HtmlSaveOptions`, çalışma kitabının tamamını — kıvılcım grafikleriyle birlikte — kendi içeriğini taşıyan bir HTML dosyasına dönüştürmenizi sağlar. Bu makale, her iki iş akışını da baştan sona ele alır.

## **İş Akışı 1 — Kıvılcım Grafiklerini Görüntülere Dönüştürüp Hücrelere Gömme**
Bu iş akışında küçük bir kaynak değer aralığı içeren bir çalışma sayfası oluşturacak, bu aralığa üç farklı kıvılcım grafiği grubu (Line, Column ve Stacked/Win-Loss) ekleyecek, her grubu PNG olarak işleyecek ve oluşan PNG baytlarını bitişik hücrelere gömülü görüntüler olarak yazacaksınız. Nihai sonuç, hem canlı kıvılcım grafiklerini hem de oluşturulan görüntü karşılıklarını içeren tek bir `.xlsx` dosyası olacaktır.

### **Adım Adım Yönergeler**
1. Yeni bir `Workbook` oluşturun ve ilk `Worksheet` nesnesine başvuru edin.
2. `A1` ile `E1` arasındaki hücrelere beş örnek sayısal değer yerleştirin; örneğin günlük satış veya sıcaklık ölçümleri kullanabilirsiniz.
3. `worksheet.getSparklineGroups().add(...)` çağrılarak çalışma sayfasına üç `SparklineGroup` nesnesi ekleyin:
   - Veri aralığı `A1:E1` olan ve `F1` hücresine sabitlenen bir `SparklineType.Line` grubu.
   - Veri aralığı `A1:E1` olan ve `G1` hücresine sabitlenen bir `SparklineType.Column` grubu.
   - Veri aralığı `A1:E1` olan ve `H1` hücresine sabitlenen bir `SparklineType.Stacked` (kazanç/kayıp) grubu.
4. Bir `ImageOrPrintOptions` örneği oluşturun ve `imageType` özelliğini `ImageType.Png` değerine ayarlayın; böylece her kıvılcım grafiği PNG resmi olarak işlenir.
5. Çalışma kitabını `output_with_sparklines.xlsx` olarak kaydedin.

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
        const { Workbook, CellArea, ImageOrPrintOptions } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            // Yeni bir çalışma kitabı oluştur ve ilk çalışma sayfasına eriş
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            // A1:E1 hücrelerine örnek veri yerleştir
            cells.get("A1").value = 5;
            cells.get("B1").value = -3;
            cells.get("C1").value = 8;
            cells.get("D1").value = -2;
            cells.get("E1").value = 6;
            // F1 hücresine sabitlenen bir Çizgi sparkline grubu ekle (5. sütun, 0. satır)
            const lineArea = new CellArea();
            lineArea.startColumn = 5;
            lineArea.endColumn = 5;
            lineArea.startRow = 0;
            lineArea.endRow = 0;
            const lineIdx = worksheet.sparklineGroups.add(
                AsposeCells.SparklineType.Line,
                "A1:E1",
                false,
                lineArea
            );
            // G1 hücresine sabitlenen bir Sütun sparkline grubu ekle (6. sütun, 0. satır)
            const columnArea = new CellArea();
            columnArea.startColumn = 6;
            columnArea.endColumn = 6;
            columnArea.startRow = 0;
            columnArea.endRow = 0;
            const columnIdx = worksheet.sparklineGroups.add(
                AsposeCells.SparklineType.Column,
                "A1:E1",
                false,
                columnArea
            );
            // H1 hücresine sabitlenen bir Kazanç/Kayıp (Yığılmış) sparkline grubu ekle (7. sütun, 0. satır)
            const stackedArea = new CellArea();
            stackedArea.startColumn = 7;
            stackedArea.endColumn = 7;
            stackedArea.startRow = 0;
            stackedArea.endRow = 0;
            const stackedIdx = worksheet.sparklineGroups.add(
                AsposeCells.SparklineType.Stacked,
                "A1:E1",
                false,
                stackedArea
            );
            // PNG çıktısı için resim seçeneklerini yapılandır
            const imageOptions = new ImageOrPrintOptions();
            imageOptions.imageType = AsposeCells.ImageType.Png;
            // Çizgi sparkline'ı resme dönüştür ve F2 hücresine göm
            const lineSp = worksheet.sparklineGroups.get(lineIdx).sparklines.get(0);
            cells.get("F2").embeddedImage = lineSp.toImage(imageOptions);
            // Sütun sparkline'ı resme dönüştür ve G2 hücresine göm
            const columnSp = worksheet.sparklineGroups.get(columnIdx).sparklines.get(0);
            cells.get("G2").embeddedImage = columnSp.toImage(imageOptions);
            // Kazanç/Kayıp sparkline'ı resme dönüştür ve H2 hücresine göm
            const stackedSp = worksheet.sparklineGroups.get(stackedIdx).sparklines.get(0);
            cells.get("H2").embeddedImage = stackedSp.toImage(imageOptions);
            // Çalışma kitabını diske kaydet
            const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_with_sparklines.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

Yukarıdaki kod, her kıvılcım grafik gösteriminin iki biçimde bulunduğu bir çalışma kitabı üretir: 1. satıra sabitlenmiş canlı ve yerel kıvılcım grafiği ile 2. satırdaki komşu hücreye doğrudan gömülü statik PNG görüntüsü. Görüntüler dosyanın içinde bulunduğundan çalışma kitabı, gömülü görüntü başvuruları bozulmadan e-postayla gönderilebilen veya arşivlenebilen, kendi içeriğini taşıyan tek bir dosya olarak kalır.

{{% alert color="primary" %}}
Her kıvılcım grafiği grubu tek bir hücreye sabitlendiğinden, koleksiyon üzerinde yinelmek yerine grubun kıvılcım grafiklerine `group.getSparklines()[0]` indeksleyicisi aracılığıyla erişebilirsiniz. Bu yaklaşım işleme kodunu kısa tutar ve tipik "her sabitleme hücresinde bir kıvılcım grafiği" kullanım desenini yansıtır. Resim baytlarını `cell.embeddedImage` aracılığıyla saklamak Aspose.Cells 26.5 veya sonraki bir sürümü gerektirir.
{{% /alert %}}

## **İş Akışı 2 — Kıvılcım Grafiği Çalışma Sayfasını HTML'e Dışa Aktarma**
Çalışma kitabı canlı kıvılcım grafiklerini (ve isteğe bağlı olarak gömülü görüntü karşılıklarını) içerdiğinde, çalışma sayfasının tamamı HTML olarak kaydedilerek web'de yayımlanabilir. `HtmlSaveOptions` sınıfı bu dışa aktarma işlemini denetlemek için gereken seçenekleri sunar; bu iş akışında İş Akışı 1 ile oluşturulan `output_with_sparklines.xlsx` dosyasını yeniden kullanarak temiz, tek sayfalık bir HTML belgesine dönüştüreceğiz.

### **Adım Adım Yönergeler**
1. İş Akışı 1 ile oluşturulan `output_with_sparklines.xlsx` dosyasının çalışma dizininde diskte bulunduğundan emin olun.
2. Bu dosyayı yeni bir `Workbook` örneğine yükleyin.
3. Bir `HtmlSaveOptions` örneği oluşturun ve `exportActiveWorksheetOnly` özelliğini `true` değerine ayarlayın; böylece oluşturulan HTML dosyası, çalışma kitabının tamamı yerine yalnızca etkin çalışma sayfasını içerir.
4. HTML çıktısını diske yazmak için `workbook.save("sparklines.html", htmlOptions)` çağrısını yapın.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, HtmlSaveOptions } = AsposeCells;
        AsposeCells.onReady({
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
            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }
            try {
                const file = fileInput.files[0];
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const htmlOptions = new HtmlSaveOptions();
                htmlOptions.exportActiveWorksheetOnly = true;
                const outputData = workbook.save(AsposeCells.SaveFormat.Html, htmlOptions);
                const blob = new Blob([outputData], { type: "text/html" });
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "sparklines.html";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                console.error(error);
                result.innerHTML = `<p style="color: red;">${error.message}</p>`;
            }
        });
    </script>
</html>
```

Yukarıdaki kod, İş Akışı 1'deki kıvılcım grafiği içeren çalışma kitabını taşınabilir bir HTML dosyasına dönüştürür. Kıvılcım grafikleri, oluşturulan HTML tablosunun içinde satır içi görüntüler olarak işlenir; böylece son kullanıcılar Excel'in yüklü olmasına gerek kalmadan eğilimleri herhangi bir modern tarayıcıda görüntüleyebilir. `exportActiveWorksheetOnly` özelliğini `true` değerine ayarlayarak gizli çalışma sayfalarını veya yardımcı verileri yanlışlıkla yayımlamaktan kaçınır; yalnızca kullanıcıya şu anda görünen çalışma sayfası dışa aktarılır.

{{% alert color="primary" %}}
`HtmlSaveOptions` sınıfı; `exportHiddenWorksheet`, `exportImagesAsBase64` ve `encoding` gibi çıktıyı ayrıntılı biçimde yapılandırmak için ek özellikler sunar. Bu özellikleri dağıtım hedefinize uygun şekilde yapılandırın.
{{% /alert %}}

## **API Özeti**
Yukarıdaki iş akışları, birlikte çalışan küçük bir Aspose.Cells API kümesine dayanır.
- `SparklineGroup` ve `worksheet.getSparklineGroups()` koleksiyon erişimcisi, her kıvılcım grafiği grubunun türünü (Line, Column, Stacked), veri aralığını ve sabitlenme hücresini tanımlamak için kullanılır. Bu makalede her grup tek bir hücreye sabitlendiğinden gruba `worksheet.getSparklineGroups()[i]` üzerinden erişilir.
- `Sparkline` türü ve `group.getSparklines()[0]` indeksleyicisi, grup içindeki bireysel kıvılcım grafiğini döndürür. Örnekte her grup tam olarak bir kıvılcım grafiği içerdiğinden yineleme döngüsüne gerek yoktur.
- `sparkline.toImage(imageOrPrintOptions)`, kıvılcım grafiğinin görüntüsünü `Buffer` olarak döndüren işleme yöntemidir. Döndürülen baytlar doğrudan `cell.embeddedImage` özelliğine atanabilir.
- `HtmlSaveOptions.exportActiveWorksheetOnly` (Boolean), HTML dışa aktarımını etkin çalışma sayfasıyla sınırlar. Tek sayfalık raporlar oluşturulurken `HtmlSaveOptions` sınıfının en sık kullanılan özelliklerinden biridir.
- `ImageOrPrintOptions.imageType`, `toImage` ile işleme yaparken ve çalışma sayfalarını görüntü olarak yazdırırken kullanılan görüntü biçimini (örneğin `ImageType.Png`) seçer.

{{< app/cells/assistant language="javascript-cpp" >}}