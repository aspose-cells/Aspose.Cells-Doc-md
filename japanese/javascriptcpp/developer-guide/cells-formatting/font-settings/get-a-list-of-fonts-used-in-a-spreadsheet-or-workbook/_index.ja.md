---
title: スプレッドシートまたはワークブックで使用されるフォントのリストを取得する
linktitle: スプレッドシートまたはワークブックで使用されるフォントのリストを取得する
description: Aspose.Cells for JavaScript経由でC++を使用して、スプレッドシートまたはワークブックで使用されているフォントのリストを取得する方法を学びます。この記事では、ドキュメントからフォント情報を取得する方法を示します。
keywords: Aspose.Cells、JavaScript via C++、スプレッドシート、ワークブック、フォント、リスト
type: docs
weight: 20
url: /ja/javascript-cpp/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/
---

## **可能な使用シナリオ**

レンダリング目的でワークブックで使用されているフォントを知ることはしばしば必要です。ワークブックをPDFや画像に変換する場合、Aspose.Cells は必要なすべてのフォントがシステムにインストールされているか、または **fonts ディレクトリ** に存在する必要があります。Aspose.Cells が必要なフォントを見つけられない場合、他の適切なフォントで置き換えようとします。これにより、PDFや画像の不要なレンダリングが発生し、適切なフォントの検索に処理時間がかかります。

そのようなケースに対処するには、ワークブックが使用しているフォントを知る必要があります。Windows環境の場合はシステムにそのフォントをインストールし、LinuxやWindows環境の場合はフォントディレクトリに配置します。

C++経由のAspose.Cells for JavaScriptは、ワークブックまたはスプレッドシートに使用されているすべてのフォントのリストを返す[**Workbook.fonts**](https://reference.aspose.com/cells/javascript-cpp/workbook/#fonts--)メソッドを提供します。

## **スプレッドシートまたはブックで使用されているフォントのリストを取得する**

次のサンプルコードは、元のExcelファイルをロードし、それに使用されているフォントのリストを取得します。ダミーフォントがいくつか追加されているダミーワークシートが含まれています。コードがワークブック内のすべてのフォントを印刷すると、これらのダミーフォントも印刷されます。以下のスクリーンショットは、[サンプルExcelファイル](25395211.xlsx)とダミーフォントのリストを示しています。

![todo:image_alt_text](get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook_1.png)

## **サンプルコード**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Get Fonts Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Get Fonts from Workbook</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Get Fonts</button>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get all the fonts inside the workbook (converted from getFonts())
            const fonts = workbook.fonts;

            // Print all the fonts into the result div
            if (!fonts || fonts.length === 0) {
                document.getElementById('result').innerHTML = '<p>No fonts found in the workbook.</p>';
                return;
            }

            let html = '<h2>Fonts in Workbook</h2><ul>';
            for (let i = 0; i < fonts.length; i++) {
                html += `<li>${fonts[i].toString()}</li>`;
            }
            html += '</ul>';
            document.getElementById('result').innerHTML = html;
        });
    </script>
</html>
```


## **コンソール出力**



{{< highlight java >}}

Aspose.Cells.Font [ Calibri; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Arial; 10; Regular; Color [A=255, R=0, G=0, B=0] ]

Aspose.Cells.Font [ Calibri; 10; Bold; Color [Black] ]

Aspose.Cells.Font [ Calibri; 10; Regular; Color [A=255, R=128, G=128, B=128] ]

Aspose.Cells.Font [ Calibri; 10; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Bold; Color [A=255, R=255, G=255, B=255] ]

Aspose.Cells.Font [ Calibri; 36; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 20; Bold; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 11; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 11; Bold; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 11; Bold; Color [A=255, R=255, G=255, B=255] ]

Aspose.Cells.Font [ Calibri; 11; Italic; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Bold; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [Black] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=41, G=74, B=78] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=41, G=74, B=78] ]

Aspose.Cells.Font [ Calibri; 12; Regular; Color [A=255, R=41, G=74, B=78] ]

Aspose.Cells.Font [ Calibri; 11; Regular; Color [A=255, R=41, G=74, B=78] ]

Aspose.Cells.Font [ Calibri; 11; Bold; Color [A=255, R=255, G=255, B=255] ]

Aspose.Cells.Font [ Dummy-Arial-X; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Arial-Y; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Arial-Z; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Times-I; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Times-II; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Times-III; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Calibri; 10.5; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 20; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 11; Regular; Color [A=255, R=55, G=98, B=104] ]

{{< /highlight >}}
