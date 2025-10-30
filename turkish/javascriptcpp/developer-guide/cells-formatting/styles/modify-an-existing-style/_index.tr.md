---
title: Mevcut Stili Değiştirme
linktitle: Mevcut Stili Değiştirme
description: Aspose.Cells, hücre stillerini değiştirmeyi sağlayan çalışan bir JavaScript kütüphanesidir. Bu makale, mevcut bir hücre stilini düzenlemenin yollarını tanıtarak, kullanıcıların hücrelerin görünümünü ihtiyaçlarına göre değiştirmelerine olanak tanır.
keywords: Mevcut stilleri değiştirin, uygulamanın görünümünü özelleştirin, kılavuzlar, öğreticiler, yardım belgeleri, geliştirme belgeleri, API referansları, örnek kodlar, indirmeler, destek.
type: docs
weight: 90
url: /tr/javascript-cpp/modify-an-existing-style/
---

{{% alert color="primary" %}}

Aynı biçimlendirme seçeneklerini hücrelere uygulamak için yeni bir biçimlendirme stili nesnesi oluşturun. Bir biçimlendirme stili nesnesi, yazı tipi, yazı tipi boyutu, girinti, sayı, kenar, desen vb. gibi biçimlendirme özelliklerinin bir kombinasyonudur, adlandırılır ve bir küme olarak saklanır. Uygulandığında, bu stildeki tüm biçimlendirme uygulanır.

Ayrıca var olan bir stili kullanabilir, çalışma kitabı ile kaydedebilir ve aynı özelliklere sahip bilgileri biçimlendirmek için kullanabilirsiniz.

Hücreler açıkça biçimlendirilmediğinde, **Normal** stili (çalışma kitabının varsayılan stili) uygulanır. Microsoft Excel, Comma, Currency ve Percent dahil olmak üzere birkaç önceden tanımlanmış stile ek olarak Normal stili de tanımlar.

Aspose.Cells, bu stillerin herhangi birini veya kendi istediğiniz özelliklere sahip herhangi bir stilini değiştirmenize olanak tanır.

{{% /alert %}}

## **Microsoft Excel Kullanımı**

Microsoft Excel 97-2003'te bir stil güncellemek için:

1. **Format** menüsünde **Stil**'e tıklayın.
1. Değiştirmek istediğiniz stili **Stil adı** listesinden seçin.
1. **Değiştir**'e tıklayın.
1. Biçim Hücreleri iletişim kutusundaki sekmeleri kullanarak istediğiniz stil seçeneklerini seçin.
1. **Tamam**'a tıklayın.
1. **Stil içerir** altında istediğiniz stil özelliklerini belirtin.
1. Kaydetmek ve seçili aralığa uygulamak için **Tamam**'a tıklayın.

## **C++ kullanarak Aspose.Cells for JavaScript ile**

Aşağıdaki örnekler [**Style.update()**](https://reference.aspose.com/cells/javascript-cpp/style/#update--) metodunun nasıl kullanılacağını gösterir.

### **Stil Oluşturma ve Değiştirme**

Bu örnek, bir [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) nesnesi oluşturur, onu bir hücre aralığına uygular ve [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) nesnesini değiştirir. Yapılan değişiklikler otomatik olarak hücreye ve stili uygulanan aralığa yansıtılır.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Aspose.Cells Style Example</h1>
        <p>Select an existing Excel file to modify or leave empty to create a new workbook.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');

            // Instantiate workbook from uploaded file or create a new one
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Create a new style object.
            const style = workbook.createStyle();

            // Set the number format.
            style.number = 14;

            // Set the font color to red color.
            style.font.color = AsposeCells.Color.Red;

            // Name the style.
            style.name = "Date1";

            // Get the first worksheet cells.
            const cells = workbook.worksheets.get(0).cells;

            // Specify the style (described above) to A1 cell.
            const cellA1 = cells.get("A1");
            cellA1.style = style;

            // Create a range (B1:D1).
            const range = cells.createRange("B1", "D1");

            // Initialize styleflag object.
            const flag = new AsposeCells.StyleFlag();

            // Set all formatting attributes on.
            flag.all = true;

            // Apply the style (described above) to the range.
            range.applyStyle(style, flag);

            // Modify the style (described above) and change the font color from red to black.
            style.font.color = AsposeCells.Color.Black;

            // Done! Since the named style (described above) has been set to a cell and range, 
            // The change would be reflected(new modification is implemented) to cell(A1) and 
            // Range (B1:D1).
            style.update();

            // Save the excel file. 
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book_styles.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


### **Mevcut Bir Stili Değiştirmek**

Bu örnek, zaten bir diziye uygulanmış olan bir stil olan Yüzde'nin bulunduğu basit bir şablon Excel dosyasını kullanır. Örnek:

1. İlgili stili alır,
1. Stil nesnesi oluşturur ve
1. Stil biçimlendirmesini değiştirir.

Değişiklikler otomatik olarak uygulanan aralığa uygulanır.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Apply Named Style Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Color, Utils } = AsposeCells;

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
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create a workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the named style "Percent" via the styles collection
            const style = workbook.styles.get("Percent");

            // Change the number format to "0.00%".
            style.number = 11;

            // Set the font color.
            style.font.color = Color.Red;

            // Update the style so ranges using this named style are updated.
            style.update();

            // Save the workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book2.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Style updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
