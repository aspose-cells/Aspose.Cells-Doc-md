---
title: Hücreye Resim Ekleme Nasıl Yapılır
type: docs
weight: 130
url: /tr/javascript-cpp/how-to-insert-picture-in-cell/
description: Aspose.Cells for JavaScript kullanılarak bir hücreye resim nasıl eklenir öğrenin.
keywords: Hücreye Resim Eklemeyi, Hücreler Üzerine Resim Eklemeyi, Hücreye Resim Koymayı, Hücreler Üzerine Resim Koymayı, Resmi Hücreye Koymayı, Resmi Hücreler Üzerine Koymayı, Hücrede Resim Nasıl Yerleştirilir, Hücreler Üzerine Resim Nasıl Yerleştirilir, Resim Yerleştirmenin Arasında Geçiş Yapmayı, Hücre İçinde Yerleştirme ve Hücreler Üzerine Resim Arasında Geçiş Yapmayı
---

## **Olası Kullanım Senaryoları**
Resim çalışma sayfanıza bir canlılık katar ve içeriğin görsel bir temsilini sağlar. Ayrıca, verileri anlamanızı kolaylaştırır ve içgörüler elde etmenizi sağlar. Yıllardır Excel'de resimleri kullanabiliyor olmanıza rağmen, excel resimlerin gerçek hücre değerleri haline gelme özelliğini ancak son zamanlarda etkinleştirdi. Resim düzeni değiştirilse bile, hâlâ veriye bağlı kalacaktır. Tablolarda, sıralamada, süzmede, formüllerde kullanabilirsiniz, vs!

## **Excel Kullanarak Hücreye Resim Ekleme**
Excel'de bir hücreye resim eklemek için şu adımları izleyin:

1. Ekle sekmesine gidin ve Resimler seçeneğine tıklayın.
2. **Hücreye Yerleştir**'i seçin. **Resim Ekleme Yerinden** açılır menüsünden aşağıdaki kaynaklardan birini seçin (**Bu Cihaz**, **Stok Resimler** ve **Çevrimiçi Resimler**). Bu Cihaz, cihazınızdan resim eklemek için. Stok Resimler, stok resimlerden resim eklemek için. Çevrimiçi Resimler, webden resim eklemek için.
<br>
<img src="1.png" width=60% />
3. Resmi seçin ve bir hücreye resim ekleyin.
<br>
<img src="8.png" width=60% />

## **Excel Kullanarak Hücrelerin Üzerine Resim Ekleme**
Excel'de hücrelerin üzerine resim eklemek için şu adımları izleyin:

1. Ekle sekmesine gidin ve Resimler seçeneğine tıklayın.
2. **Hücrelerin Üzerine Yerleştir**'i seçin. **Resim Ekleme Yerinden** açılır menüsünden aşağıdaki kaynaklardan birini seçin (**Bu Cihaz**, **Stok Resimler** ve **Çevrimiçi Resimler**). Bu Cihaz, cihazınızdan resim eklemek için. Stok Resimler, stok resimlerden resim eklemek için. Çevrimiçi Resimler, webden resim eklemek için.
<br>
<img src="2.png" width=60% />
3. Resmi seçin ve hücrelerin üzerine resim ekleyin.
<br>
<img src="3.png" width=60% />

## **Hücredeki Resimden Hücrelerin Üzerindeki Resimlere Nasıl Geçilir**
Kolayca **Hücredeki Resimden Hücrelerin Üzerindeki Resimlere** geçebilirsiniz. Lütfen şu adımları izleyin:
1. Hücreye sağ tıklayın ve **Hücredeki Resim** > **Hücrelerin Üzerine Yerleştir** seçeneğini seçin. 
<br>
<img src="4.png" width=60% />
2. Değiştirdikten sonra sonuç aşağıdaki gibidir:
<br>
<img src="5.png" width=60% />

## **Hücrelerin Üzerindeki Resimden Hücredeki Resime Nasıl Geçilir**
Kolayca **Hücrelerin Üzerindeki Resimden Hücredeki Resime** geçebilirsiniz. Lütfen şu adımları izleyin:
1. Resme sağ tıklayın ve **Hücre içine Yerleştir** seçeneğini seçin. 
<br>
<img src="6.png" width=60% />
2. Değiştirdikten sonra sonuç aşağıdaki gibidir:
<br>
<img src="7.png" width=60% />

## **Kuralım nasıl ve Aspose.Cells for JavaScript kullanarak hücreye Resim Ekleme**
Aspose.Cells kullanarak hücreye resim ekleme. Lütfen aşağıdaki örnek kodu görün. Örnek kodu yürüttükten sonra, bir resim hücreye eklenecektir.
1. Bir Workbook nesnesi oluşturun. 
2. Resmi yerleştirmek istediğiniz hücreyi alın.
3. Cell.EmbeddedImage özelliğini ayarlayın. 
4. Son olarak, çalışma kitabını [çıktı XLSX](out.xlsx) formatında kaydeder. 

## **Örnek Kod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Embed Image into New Workbook</h1>
        <p>Select an image file to embed into cell D8. A new workbook will be created with "Apple" in A2.</p>
        <input type="file" id="imageInput" accept="image/*" />
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
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const imageInput = document.getElementById('imageInput');
            const resultDiv = document.getElementById('result');

            // Create a new workbook
            const workbook = new Workbook();
            const cells = workbook.worksheets.get(0).cells;

            // Set A2 value to "Apple"
            const a2 = cells.get("A2");
            a2.value = "Apple";

            // Get D8 cell
            const d8 = cells.get("D8");

            // If an image file is selected, read it and embed into D8
            if (imageInput.files.length) {
                const file = imageInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                const imgBuf = new Uint8Array(arrayBuffer);
                d8.embeddedImage = imgBuf;
            }

            // Save workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
