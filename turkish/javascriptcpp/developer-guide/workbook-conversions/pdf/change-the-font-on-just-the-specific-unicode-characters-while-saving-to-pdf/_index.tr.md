---
title: Yalnızca belirli Unicode karakterlerin yazı tipini değiştirirken PDF ye kaydetme ile JavaScript üzerinden C++ kullanın
linktitle: PDF ye kaydederken belirli Unicode karakterlerinin yazı tipini değiştirin
type: docs
weight: 260
url: /tr/javascript-cpp/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
description: Belirli Unicode karakterlerin yazı tipini değiştirmeyi [Workbook.calculateFormula()](https //reference.aspose.com/cells/javascript cpp/workbook/#calculateFormula ) yöntemini PDF ye dönüştürmeden önce çağırarak öğrenin. Bu, formüle bağlı değerlerin yeniden hesaplanmasını sağlar ve PDF de doğru değerler görünür. 
---

{{% alert color="primary" %}} 

Bazı Unicode karakterleri, kullanıcı tarafından belirtilen font tarafından görüntülenemez. Bu tür bir Unicode karakter **Bilinmeyen Kesme** (U+2011)'dır ve Unicode numarası 8209'dur. Bu karakter **Times New Roman** ile görüntülenemez, ancak **Arial Unicode MS** gibi diğer fontlarla görüntülenebilir.

Bu tür bir karakter, Times New Roman gibi belirli bir yazı tipinde bir sözcük veya cümle içinde yer alıyorsa, Aspose.Cells tüm sözcüğün veya cümlenin yazı tipini bu karakteri gösterebilecek bir yazı tipine, örneğin Arial Unicode'dan MS'ye değiştirir.

Ancak, bu kullanıcılar için istenmeyen bir davranıştır ve yalnızca belirli karakterin yazı tipinin değiştirilmesini isterler; tüm kelimenin veya cümlenin yazı tipinin değiştirilmesi değil.

Bu sorunu çözmek için Aspose.Cells, sadece gösterilebilir olmayan belirli karakterlerin yazı tipini değiştiren ve diğer kısmın orijinal yazı tipinde kalmasını sağlayan `PdfSaveOptions.isFontSubstitutionCharGranularity` özelliğini sağlar. Bu özelliği true olarak ayarlamanız gerekir.

{{% /alert %}} 

## **Örnek**
Aşağıdaki ekran görüntüsü, aşağıdaki örnek kodu ile oluşturulan iki PDF'yi karşılaştırır.

İlk dosya, `PdfSaveOptions.isFontSubstitutionCharGranularity` özelliği ayarlanmadan oluşturulmuş, diğer ise bu özelliğin true olarak ayarlandığı dosyadır.

İlk PDF'de, Tüm cümlenin yazı tipi Non-Breaking Hyphen nedeniyle Times New Roman'dan Arial Unicode MS'ye değişti. İkinci PDF'de ise sadece Non-Breaking Hyphen'in yazı tipi değişti.

|**İlk Pdf Dosyası**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)|


|**İkinci Pdf Dosyası**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_2.png)|
### **Örnek Kod**


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
        <a id="downloadLink1" style="display: none; margin-right: 10px;">Download Result PDF 1</a>
        <a id="downloadLink2" style="display: none;">Download Result PDF 2</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions } = AsposeCells;

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
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '<p>Running example...</p>';

            // Create workbook object
            const workbook = new Workbook();

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access cells
            const cell1 = worksheet.cells.get("A1");
            const cell2 = worksheet.cells.get("B1");

            // Set the styles of both cells to Times New Roman
            let style = cell1.style;
            style.font.name = "Times New Roman";
            cell1.style = style;
            cell2.style = style;

            // Put the values inside the cell
            cell1.value = "Hello without Non-Breaking Hyphen";
            cell2.value = "Hello" + String.fromCharCode(8209) + " with Non-Breaking Hyphen";

            // Autofit the columns
            worksheet.autoFitColumns();

            // Save to Pdf without setting PdfSaveOptions.IsFontSubstitutionCharGranularity
            const outputData1 = workbook.save(SaveFormat.Pdf);
            const blob1 = new Blob([outputData1]);
            const downloadLink1 = document.getElementById('downloadLink1');
            downloadLink1.href = URL.createObjectURL(blob1);
            downloadLink1.download = 'SampleOutput_out.pdf';
            downloadLink1.style.display = 'inline-block';
            downloadLink1.textContent = 'Download SampleOutput_out.pdf';

            // Save to Pdf after setting PdfSaveOptions.IsFontSubstitutionCharGranularity to true
            const opts = new PdfSaveOptions();
            opts.isFontSubstitutionCharGranularity = true;
            const outputData2 = workbook.save(SaveFormat.Pdf, opts);
            const blob2 = new Blob([outputData2]);
            const downloadLink2 = document.getElementById('downloadLink2');
            downloadLink2.href = URL.createObjectURL(blob2);
            downloadLink2.download = 'SampleOutput2_out.pdf';
            downloadLink2.style.display = 'inline-block';
            downloadLink2.textContent = 'Download SampleOutput2_out.pdf';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Use the download links to get the generated PDFs.</p>';
        });
    </script>
</html>
```
