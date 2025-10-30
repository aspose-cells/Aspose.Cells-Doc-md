---
title: Hücre İçine HTML Zengin Metin Ekleme
linktitle: Html Dize Değeri
type: docs
weight: 50
url: /tr/javascript-cpp/adding-html-rich-text-inside-the-cell/
description: Aspose.Cells for JavaScript kullanarak hücre içine HTML Zengin Metin nasıl eklenir öğrenin.
keywords: HTML Zengin Metin Hücreye JavaScript kullanarak ekle, html zengin metni hücreye JavaScript ile ayarla, hücreye HTML Zengin Metin ekle JavaScript ile C++
---

{{% alert color="primary" %}}

Aspose.Cells, Microsoft Excel odaklı HTML'yi XLS/XLSX biçimine dönüştürmeyi destekler. Yani, Microsoft Excel tarafından oluşturulan HTML tekrar XLS/XLSX biçimine çevrilebilir.

Benzer şekilde, Aspose.Cells, basit bir HTML varsa onu HTML Zengin Metin'e dönüştürebilir. Aspose.Cells, bu tür basit bir HTML'yi alıp biçimlendirilmiş hücre metnine dönüştürebilen [**Cell.htmlString**](https://reference.aspose.com/cells/javascript-cpp/cell/#htmlString-string-) özelliğini sağlar.

{{% /alert %}}

Aşağıdaki kod örneği, hücre içine HTML zengin metin eklemenin nasıl yapıldığını gösterir. Lütfen çıktı Excel dosyasının ekran görüntüsüne bakın.

![todo:image_alt_text](adding-html-rich-text-inside-the-cell_1)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells HTML String Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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
            let workbook;

            // If a file is provided, open it; otherwise create a new workbook
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access cell A1
            const cell = worksheet.cells.get("A1");

            // Set HTML formatted string to the cell (converted setter -> property)
            cell.htmlString = "<Font Style=\"FONT-WEIGHT: bold;FONT-STYLE: italic;TEXT-DECORATION: underline;FONT-FAMILY: Arial;FONT-SIZE: 11pt;COLOR: #ff0000;\">This is simple HTML formatted text.</Font>";

            // Save the workbook to XLSX format and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">HTML string written to A1. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


## İlgili Makaleler

- [HTML kullanarak Hücre Değeri Ayarıyla Madde İmleri Göster](/cells/tr/javascript-cpp/display-bullets-by-setting-cell-value-using/)
- [Hücreden HTML5 dizesi al](/cells/tr/javascript-cpp/get-html5-string-from-cell/)
