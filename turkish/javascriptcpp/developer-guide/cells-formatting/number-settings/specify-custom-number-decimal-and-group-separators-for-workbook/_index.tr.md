---
title: Çalışma Kitabı için Özel Sayı Ondalık ve Grup Ayracı Belirt
linktitle: Çalışma Kitabı için Özel Sayı Ondalık ve Grup Ayracı Belirt
type: docs
weight: 110
url: /tr/javascript-cpp/specify-custom-number-decimal-and-group-separators-for-workbook/
description: Excel de Sayı ondalık ve grup ayırıcılarını Aspose.Cells for JavaScript kullanarak C++ ile değiştirin.
keywords: özel ondalık ayırıcı excel JavaScript, C++ kullanarak özel grup ayırıcı excel JavaScript belirleyin, ondalık ve grup ayırıcıyı excel JavaScript ile değiştirin C++
---

{{% alert color="primary" %}}

Microsoft Excel'de, Ekran Görüntüsünde gösterildiği gibi **Gelişmiş Excel Seçenekleri**'nden Sistem Ayraçlarını kullanmak yerine Özel Ondalık ve Binlerce Ayraçları belirleyebilirsiniz.

Aspose.Cells, [**WorkbookSettings.numberDecimalSeparator**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#numberDecimalSeparator-string-) ve [**WorkbookSettings.numberGroupSeparator**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#numberGroupSeparator-string-) metodlarını özel ayırıcıları ayarlamak ve biçimlendirmek/parametreleri çözümlemek için sağlar.

{{% /alert %}}

## **Microsoft Excel Kullanarak Özel Ayraçları Belirtme**

Aşağıdaki ekran görüntüsü, **Gelişmiş Excel Seçenekleri**'ni ve **Özel Ayraçları** belirtmek için bölümü vurgular.

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)

## **Aspose.Cells for JavaScript kullanarak C++ ile Özel Ayırıcılar Belirtme**

Aşağıdaki örnek kod, Aspose.Cells API'sini kullanarak Belirtilmemiş Ayırıcıları belirtmeyi gösterir. Özel Sayı Ondalık ve Grup Ayırıcılarını nokta ve boşluk olarak belirtir.

### JavaScript kodu ile özel Sayı Ondalık ve Grup Ayırıcılarını belirleme

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Custom Number Separator Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Specify custom separators
            workbook.settings.numberDecimalSeparator = '.';
            workbook.settings.numberGroupSeparator = ' ';

            const worksheet = workbook.worksheets.get(0);

            // Set cell value
            const cell = worksheet.cells.get("A1");
            cell.value = 123456.789;

            // Set custom cell style
            const style = cell.style;
            style.custom = "#,##0.000;[Red]#,##0.000";
            cell.style = style;

            worksheet.autoFitColumns();

            // Save workbook as pdf
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CustomSeparator_out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```
