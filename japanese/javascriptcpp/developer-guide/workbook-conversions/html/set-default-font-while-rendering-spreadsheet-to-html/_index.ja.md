---
title: JavaScriptを使用してC++でスプレッドシートをHTMLにレンダリングするときにデフォルトのフォントを設定します。
linktitle: HTMLにスプレッドシートをレンダリングする際のデフォルトフォントを設定する
type: docs
weight: 370
url: /ja/javascript-cpp/set-default-font-while-rendering-spreadsheet-to/
---

{{% alert color="primary" %}}
Aspose.Cellsを使用すると、スプレッドシートをHTMLにレンダリングする際にデフォルトフォントを設定することができます。そのためには、[**HtmlSaveOptions.defaultFontName**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#defaultFontName--)を使用してください。このプロパティは、スプレッドシート内に無効または存在しないフォントを持つセルがある場合に役立ちます。その場合、[**HtmlSaveOptions.defaultFontName**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#defaultFontName--)プロパティで指定したフォントでセルがレンダリングされます。
{{% /alert %}}

## スプレッドシートをHTMLにレンダリングする際のデフォルトフォントの設定

次のサンプルコードは、ブックを作成し、最初のワークシートのセルB4にテキストを追加し、そのフォントを未知の/存在しないフォントに設定します。それからブックを異なるデフォルトフォント名（Courier New、Arial、Times New Romanなど）でHTML形式で保存します。

スクリーンショットは、[**HtmlSaveOptions.defaultFontName**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#defaultFontName--) プロパティを介して異なるデフォルトフォント名を設定した効果を示しています。

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-html_1.png)

このコードは、異なる{0}を指定して生成された[出力HTMLファイルとCourier New](5115516)、[Arial](5115518)、[Times New Roman](5115517)を生成します。

## サンプルコード

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
        <a id="downloadLink1" style="display: none;">Download Result 1</a><br/>
        <a id="downloadLink2" style="display: none;">Download Result 2</a><br/>
        <a id="downloadLink3" style="display: none;">Download Result 3</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions, Utils } = AsposeCells;

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
            // Creating a new workbook and accessing first worksheet.
            const wb = new Workbook();
            const ws = wb.worksheets.get(0);

            // Access cell B4 and add some text inside it.
            const cell = ws.cells.get("B4");
            cell.value = "This text has some unknown or invalid font which does not exist.";

            // Set the font of cell B4 which is unknown.
            const st = cell.style;
            st.font.name = "UnknownNotExist";
            st.font.size = 20;
            cell.style = st;

            // Prepare HtmlSaveOptions and save three variants with different default fonts.
            const opts = new HtmlSaveOptions();

            // 1) Default font Courier New
            opts.defaultFontName = "Courier New";
            const outputData1 = wb.save(SaveFormat.Html, opts);
            const blob1 = new Blob([outputData1], { type: "text/html" });
            const downloadLink1 = document.getElementById('downloadLink1');
            downloadLink1.href = URL.createObjectURL(blob1);
            downloadLink1.download = 'out_courier_new_out.htm';
            downloadLink1.style.display = 'block';
            downloadLink1.textContent = 'Download out_courier_new_out.htm';

            // 2) Default font Arial
            opts.defaultFontName = "Arial";
            const outputData2 = wb.save(SaveFormat.Html, opts);
            const blob2 = new Blob([outputData2], { type: "text/html" });
            const downloadLink2 = document.getElementById('downloadLink2');
            downloadLink2.href = URL.createObjectURL(blob2);
            downloadLink2.download = 'out_arial_out.htm';
            downloadLink2.style.display = 'block';
            downloadLink2.textContent = 'Download out_arial_out.htm';

            // 3) Default font Times New Roman
            opts.defaultFontName = "Times New Roman";
            const outputData3 = wb.save(SaveFormat.Html, opts);
            const blob3 = new Blob([outputData3], { type: "text/html" });
            const downloadLink3 = document.getElementById('downloadLink3');
            downloadLink3.href = URL.createObjectURL(blob3);
            downloadLink3.download = 'times_new_roman_out.htm';
            downloadLink3.style.display = 'block';
            downloadLink3.textContent = 'Download times_new_roman_out.htm';

            document.getElementById('result').innerHTML = '<p style="color: green;">Files generated successfully. Click the download links above to save the HTML files.</p>';
        });
    </script>
</html>
```
