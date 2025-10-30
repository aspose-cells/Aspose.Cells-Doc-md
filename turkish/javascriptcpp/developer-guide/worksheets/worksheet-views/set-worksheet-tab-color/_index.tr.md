---
title: JavaScript ile C++ kullanarak Çalışma Sayfası Sekmesi Rengini Ayarla
linktitle: Çalışma Taşrafları Sekme Rengi Ayarla
type: docs
weight: 120
url: /tr/javascript-cpp/set-worksheet-tab-color/
description: Bu makale, JavaScript ile C++ kullanarak Excel çalışma sayfası sekmesi renginin programatik olarak nasıl ayarlandığını gösteren örnek kodu içermektedir.
keywords: excel sekme rengi ayarla JavaScript ile C++, excel sekme rengi ayarını içeren kod
---

{{% alert color="primary" %}}

Aspose.Cells, bireysel çalışma sayfası sekmelerinin rengini değiştirmenize olanak tanır, böylece onları geri kalanından ayırt edebilirsiniz. Örneğin, Giderleri kırmızı, Satışları yeşil, Varlıkları mavi vb. yapabilirsiniz.

{{% /alert %}}
## **Microsoft Excel ile Çalışma Sayfası Sekmesi Rengini Ayarlama**
1. Mevcut çalışma sayfasının altındaki sekme sayfasında bir sekmeye sağ tıklayın.
1. **Sekme rengi**'ni seçin.
1. Paletten bir renk seçin.
1. **Tamam**'a tıklayın.
## **Aspose.Cells ile Çalışma Taşraflarında Sekme Rengi Ayarı**
Aşağıdaki örnek kod, Aspose.Cells ile sekme rengini ayarlamanın nasıl yapıldığını göstermektedir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Set Worksheet Tab Color Example</title>
    </head>
    <body>
        <h1>Set Worksheet Tab Color Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const worksheet = workbook.worksheets.get(0);
            worksheet.tabColor = AsposeCells.Color.Red;
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'worksheettabcolor.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';
            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet tab color set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
