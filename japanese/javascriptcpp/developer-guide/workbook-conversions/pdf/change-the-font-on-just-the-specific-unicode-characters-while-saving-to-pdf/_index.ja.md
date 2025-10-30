---
title: 保存時に特定のUnicode文字だけフォントを変更する方法（C++のJavaScript経由）
linktitle: 特定のUnicode文字のみのフォントを変更してPDFに保存する
type: docs
weight: 260
url: /ja/javascript-cpp/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
description: C++のAspose.Cells for JavaScriptを使ってPDFに保存する際に特定のUnicode文字のフォントを変更する方法を学びます。 
---

{{% alert color="primary" %}} 

一部のUnicode文字は、ユーザー指定のフォントでは表示されません。そのようなUnicode文字の1つが **Non-breaking Hyphen** (U+2011) で、Unicode番号は8209です。この文字は **Times New Roman** では表示できませんが、**Arial Unicode MS** のような他のフォントでは表示できます。

Times New Romanのようなフォント内にある単語や文章の中でそのような文字が現れると、Aspose.Cellsはその文字を表示できるフォント（Arial Unicode MSなど）に変換します。一方、これは一部のユーザーには望ましくなく、その文字だけのフォントを変更したい場合があります。

この問題に対処するために、Aspose.Cellsは`PdfSaveOptions.isFontSubstitutionCharGranularity`プロパティを提供しています。これをtrueに設定すると、表示できない特定の文字だけのフォントが表示可能なフォントに変更され、残りの文章は元のフォントのままになります。

一つは`PdfSaveOptions.isFontSubstitutionCharGranularity`プロパティを設定せずに生成されたもので、もう一つはこのプロパティをtrueに設定して生成されたものです。

{{% /alert %}} 

## **例**
以下のスクリーンショットは、以下のサンプルコードによって生成された2つの出力 PDF を比較しています。

最初のPDFでは、完全な文章のフォントがタイムズ・ニュー・ローマンからArial Unicode MSに変わっていますが、これはノンブレイキングハイフンによるものです。2つ目のPDFでは、ノンブレイキングハイフンだけのフォントが変更されています。

ExcelファイルをPDF/A-1a互換のPDFフォーマットに変換する方法（Node.js via C++）

|**最初の PDF ファイル**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)|


|**2 番目の PDF ファイル**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_2.png)|
### **サンプルコード**


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
