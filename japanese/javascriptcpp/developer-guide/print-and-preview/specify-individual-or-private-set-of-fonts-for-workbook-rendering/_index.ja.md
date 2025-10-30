---
title: JavaScriptをC++経由でワークブックのレンダリングに個別またはプライベートのフォントセットを指定する
linktitle: ワークブックのレンダリング用に個々またはプライベートなフォントセットを指定する
type: docs
weight: 40
url: /ja/javascript-cpp/specify-individual-or-private-set-of-fonts-for-workbook-rendering/
description: Aspose.Cells for JavaScriptをC++で使用して、ワークブックレンダリングに個別またはプライベートのフォントセットを指定する方法を学びます。
---

## **可能な使用シナリオ**  

一般的に、すべてのワークブックに対してフォントディレクトリやフォントのリストを指定しますが、場合によっては、個別またはプライベートのフォントセットを指定する必要があります。Aspose.Cells for JavaScriptをC++で提供する[**IndividualFontConfigs**](https://reference.aspose.com/cells/javascript-cpp/individualfontconfigs)クラスを使って、ワークブックのための個別またはプライベートのフォントを指定できます。  

## **ワークブックのレンダリング用に個々またはプライベートなフォントセットを指定する**  

以下のサンプルコードは、[**IndividualFontConfigs**](https://reference.aspose.com/cells/javascript-cpp/individualfontconfigs)クラスを使用して個別またはプライベートなフォントセットを持つ[サンプルExcelファイル](67338268.xlsx)をロードします。コード内で利用される[サンプルフォント](67338271.zip)と、それによって生成される[出力PDF](67338269.pdf)も参照してください。スクリーンショットでは、フォントが正常に見つかった場合の出力PDFの見た目です。  

![todo:image_alt_text](specify-individual-or-private-set-of-fonts-for-workbook-rendering_1.png)  

## **サンプルコード**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Specify Individual Or Private Fonts Example</title>
    </head>
    <body>
        <h1>Specify Individual Or Private Fonts Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, IndividualFontConfigs } = AsposeCells;

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

            // Path of your custom font directory.
            const customFontsDir = "C:\\TempDir\\CustomFonts";

            // Specify individual font configs custom font directory.
            const fontConfigs = new IndividualFontConfigs();

            // If you comment this line or if custom font directory is wrong or 
            // if it does not contain required font then output pdf will not be rendered correctly.
            // Converted setFontFolder -> property assignment (first argument used)
            fontConfigs.fontFolder = customFontsDir;

            // Specify load options with font configs.
            const opts = new LoadOptions(AsposeCells.LoadFormat.Xlsx);
            // Converted setFontConfigs -> property assignment
            opts.fontConfigs = fontConfigs;

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load the sample Excel file with individual font configs.
            const wb = new Workbook(new Uint8Array(arrayBuffer), opts);

            // Save to PDF format.
            const outputData = wb.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSpecifyIndividualOrPrivateSetOfFontsForWorkbookRendering.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
