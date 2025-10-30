---
title: レンダリング用の行自動調整（JavaScriptをC++で）
linktitle: 描画用に行を自動調整する
type: docs
weight: 130
url: /ja/javascript-cpp/autofit-rows-for-rendering/
description: Excelのレンダリング用に行を自動調整する方法をAspose.Cells for JavaScriptをC++で学びます。保存したPDFファイル内の文字切り詰めを防ぎます。
---

一般に、セル内のすべてのテキストを表示したい場合、Microsoft Excelの通常ビューで100%ズームを設定して行を自動調整できます。これにより、通常ビューでテキストが完全に見えるようになり、印刷やPDFとして保存した場合も正しく表示されます。

しかし、一部の場合には、行の自動調整は通常表示では問題なく動作しますが、印刷ビューに切り替えたりファイルをPDFとして保存すると、テキストがクリッピングされることがあります。ソースファイル [Book1.xlsx](Book1.xlsx) とスクリーンショットを確認してください。

![印刷ビューでテキストが切り取られた場合](text_clipped_in_printview.png)

保存されたPDFファイルでテキストがクリップされるのを防ぎたい場合は、[AutoFitterOptions.forRendering](https://reference.aspose.com/cells/javascript-cpp/autofitteroptions/#forRendering--) オプションを使用して行の自動調整が可能です。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Autofit Rows and Save as PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, AutoFitterOptions, SaveFormat, Utils } = AsposeCells;

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

            // Init workbook instance from uploaded file.
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Set autofit options for rendering.
            const autoFitterOptions = new AutoFitterOptions();
            autoFitterOptions.forRendering = true;

            // Autofit rows with options on first worksheet.
            const worksheet = workbook.worksheets.get(0);
            worksheet.autoFitRows(autoFitterOptions);

            // Save to pdf.
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

今、テキストは出力された PDF ファイルで切り取られていません。

![保存した PDF でテキストが切り取られていない場合](text_not_clipped_in_saved_pdf.png)
