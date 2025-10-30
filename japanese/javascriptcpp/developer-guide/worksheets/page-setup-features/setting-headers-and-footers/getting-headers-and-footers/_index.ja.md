---
title: JavaScript経由でC++を使用してヘッダーまたはフッターを取得する
linktitle: ヘッダーまたはフッターの取得
type: docs
weight: 30
url: /ja/javascript-cpp/get-headers-or-footers/
description: この記事では、JavaScript経由のC++ APIを使用してExcelまたはOpenOfficeファイルからプログラム的にヘッダーとフッターを取得する方法を説明します。
---

{{% alert color="primary" %}}

ヘッダーとフッターは、ページレイアウトビュー、印刷プレビュー、および印刷されたページでのみ表示されます。 

複数のワークシートでヘッダーやフッターを表示する場合は、ページ設定ダイアログボックスも使用できます。 

チャートシートやチャートなどの他のシートタイプでは、ページ設定ダイアログボックスを使用してのみヘッダーやフッターを挿入できます。

{{% /alert %}}

## **MS Excelでのヘッダーとフッターの取得**
1. ヘッダーやフッターを表示または変更したいワークシートをクリックします。
2. 表示タブの「ワークブックビュー」グループで、「ページレイアウト」をクリックします。
   Excelはワークシートをページレイアウトビューで表示します。
3. ヘッダーやフッターを表示または編集するには、ワークシートページの上（ヘッダーの下）または下（フッターの上）にある左、中央、または右のヘッダーまたはフッターテキストボックスをクリックします。


## **Aspose.Cells for JavaScript経由のC++を使用してヘッダーとフッターを取得する**
[**PageSetup.header(number)**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#header-number-)および[**PageSetup.footer(number)**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#footer-number-)メソッドを使用すると、JavaScript開発者はファイルからヘッダーまたはフッターを簡単に取得できます。

1. ブックを作成してファイルを開く。
2. ヘッダーまたはフッターを取得したいワークシートを取得します。
3. 特定のセクションIDを持つヘッダーまたはフッターを取得します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Header/Footer Reader Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

        function escapeHtml(str) {
            if (str === null || str === undefined) return '';
            return String(str)
                .replace(/&/g, '&amp;')
                .replace(/</g, '&lt;')
                .replace(/>/g, '&gt;')
                .replace(/"/g, '&quot;')
                .replace(/'/g, '&#039;');
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a new Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const sheet = workbook.worksheets.get(0);

            // Gets left section of header
            const headerLeft = sheet.pageSetup.header(0);
            // Gets center section of header
            const headerCenter = sheet.pageSetup.header(1);
            // Gets right section of header
            const headerRight = sheet.pageSetup.header(2);
            // Gets center section of footer
            const footerCenter = sheet.pageSetup.footer(1);

            const resultHtml = [
                `<p><strong>Left Header:</strong> ${escapeHtml(headerLeft)}</p>`,
                `<p><strong>Center Header:</strong> ${escapeHtml(headerCenter)}</p>`,
                `<p><strong>Right Header:</strong> ${escapeHtml(headerRight)}</p>`,
                `<p><strong>Center Footer:</strong> ${escapeHtml(footerCenter)}</p>`
            ].join('');

            document.getElementById('result').innerHTML = resultHtml;
        });
    </script>
</html>
```

## **ヘッダーとフッターをコマンドリストに解析する**
ヘッダーまたはフッターテキストには、ページ番号や現在の日付、テキストの書式設定属性などの特殊コマンドを含めることができます。

特殊コマンドは、先頭にアンパサンド（"&"）を付けた1つの文字で表されます。

ヘッダーとフッターの文字列は、ABNF文法を用いて構築されています。ビューアなしでは理解しにくいです。

Aspose.Cells for JavaScript経由のC++は、コマンドリストとしてヘッダーとフッターを解析する[**PageSetup.commands(string)**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#commands-string-)メソッドを提供します。

次のコードは、ヘッダーまたはフッターをコマンドリストとして解析し、コマンドを処理する方法を示しています：

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Header/Footer Commands Example</title>
    </head>
    <body>
        <h1>Header/Footer Commands Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Instantiate a Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const sheet = workbook.worksheets.get(0);

            // Gets left section of header
            const headerSection = sheet.pageSetup.header(0);
            const commands = sheet.pageSetup.commands(headerSection) || [];

            const items = [];
            commands.forEach(c => {
                const type = c.type;
                switch (type) {
                    case AsposeCells.HeaderFooterCommandType.SheetName:
                        // embedded the name of the sheet to header or footer
                        items.push('<li>SheetName command found (embeds sheet name)</li>');
                        break;
                    default:
                        items.push(`<li>Command type: ${type}</li>`);
                        break;
                }
            });

            if (!items.length) {
                items.push('<li>No header/footer commands found.</li>');
            }

            resultDiv.innerHTML = `<ul>${items.join('')}</ul>`;

            // Save the (possibly unchanged) workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'HeaderFooter_result.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Result Workbook';
        });
    </script>
</html>
```
