---
title: Excel を OFD 形式に変換
linktitle: Excel を OFD 形式に変換
description: Aspose.Cells for JavaScript via C++ は、スプレッドシートファイルを操作するための JavaScript ライブラリで、Excel ワークブックを OFD (Open Fixed-layout Document) 形式に変換できます。このアーティクルでは、Excel コンテンツを作成して OFD としてエクスポートする方法、および Aspose.Cells を使用して既存の Excel ファイルを OFD に変換する方法を説明します。
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++, JavaScript ライブラリ, スプレッドシート, Excel から OFD への変換, OFD 変換, SaveFormat.Ofd, 固定レイアウトドキュメント, ワークブックのエクスポート
type: docs
weight: 195
url: /ja/javascript-cpp/converting-excel-to-ofd-format/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells は、`SaveFormat.Ofd` 列挙値を使用して、Excel ワークブックを OFD (Open Fixed-layout Document) 形式に直接変換できます。生成される OFD ドキュメントには、ワークブックの視覚的なレイアウト、コンテンツ、結合されたセル、列幅、行高さ、フォント、色、罫線、および数値形式が保持されます。このため、固定レイアウトの出力が必要な、アーカイブ、印刷、規制当局への提出、政府への提出などのワークフローに Aspose.Cells を利用できます。
{{% /alert %}}

## **はじめに**
OFD (Open Fixed-layout Document) は、デジタル文書を固定されたページ単位のレイアウトで表現するための中国国家标准 (GB/T 33190-2016) です。ソース文書の外観を作成時の状態のまま正確に保持する必要があるユースケースでは、PDF と同様の役割を果たします。OFD は、中華人民共和国における政府への提出、規制当局への提出、電子請求書、および長期保存で広く採用されています。
Excel ワークブックを OFD に変換することは、スプレッドシートの内容を編集可能なスプレッドシートではなく、読み取り専用でレイアウトが固定された成果物として配布する必要がある場面で、一般に求められる要件です。例としては、完成した請求書を顧客に送付する、四半期ごとの財務報告書をアーカイブする、または予算スプレッドシートを規制当局に提出する、といったケースががあります。Aspose.Cells は、`SaveFormat.Ofd` 列挙値を使用することで、中間変換ステップなしでワークブックを直接 OFD に書き出し、この要件に対応します。OFD 出力には、セル値、結合範囲、フォント、色、罫線、数値形式、およびワークブックに設定されたページ設定オプションが保持されます。

{{% alert color="primary" %}}
Aspose.Cells が生成する OFD 出力は、セル内容、結合されたセル、列幅、行高さなどを含む、ソースワークブックの視覚的なレイアウトを保持します。フォント、色、罫線、配置、数値形式などのセル書式も、固定レイアウトの出力に反映されます。ワークシートに設定した用紙サイズ、向き、印刷範囲などのページ設定オプションは、生成される OFD ドキュメントのレイアウトに影響します。
{{% /alert %}}

## **Excel ワークブックを作成して OFD 形式で保存**
Aspose.Cells を使用すると、ワークブックをプログラムで作成し、データを入力した後、`SaveFormat.Ofd` 列挙値を使用して OFD 形式に直接保存できます。次の例では、請求書を新規作成します。会社のロゴ、ヘッダー情報、請求先情報、明細項目、および算出された合計金額を追加し、その後、ワークブックを OFD ドキュメントとしてエクスポートします。

### **ロゴを配置した請求書の作成**
この例では、請求書ワークシートを構築します。左上部の領域に会社のロゴ画像を挿入し、会社名と連絡先情報を入力します。結合されたセルに「INVOICE」見出しを追加し、請求書番号と日付を記録し、請求先情報を入力します。また、説明、数量、単価、合計の列を持つ明細項目表を作成し、セル数式を使用して小計、税金、総合計を計算します。`Style` および `Font` オブジェクトを使用して、太字のヘッダー、価格の通貨形式、罫線、列幅などの書式設定を適用します。最後に、`SaveFormat.Ofd` を使用して、ワークブックを `.ofd` 拡張子で保存します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
        const { Workbook, Color } = AsposeCells;
        const readyPromise = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            try {
                // 新しいワークブックを作成
                const workbook = new Workbook();
                // 最初のワークシートを取得
                const worksheet = workbook.worksheets.get(0);
                const cells = worksheet.cells;
                // 列幅を設定
                cells.setColumnWidth(0, 5);
                cells.setColumnWidth(1, 35);
                cells.setColumnWidth(2, 12);
                cells.setColumnWidth(3, 15);
                cells.setColumnWidth(4, 15);
                cells.setColumnWidth(5, 5);
                // 会社のロゴを挿入
                // ブラウザーにはファイルシステムのパスがないため、メモリ上にPNGを作成
                const logoCanvas = document.createElement("canvas");
                logoCanvas.width = 100;
                logoCanvas.height = 30;
                const logoContext = logoCanvas.getContext("2d");
                logoContext.fillStyle = "#000080";
                logoContext.fillRect(0, 0, logoCanvas.width, logoCanvas.height);
                logoContext.fillStyle = "#FFFFFF";
                logoContext.font = "bold 18px Arial";
                logoContext.fillText("ACME", 16, 21);
                const logoBlob = await new Promise(resolve => logoCanvas.toBlob(resolve, "image/png"));
                if (!logoBlob) {
                    throw new Error("Unable to create the company logo.");
                }
                const logoData = new Uint8Array(await logoBlob.arrayBuffer());
                worksheet.pictures.add(1, 1, logoData);
                // 会社名と連絡先情報
                cells.get("B3").value = "Acme Corporation";
                cells.get("B4").value = "123 Business Street";
                cells.get("B5").value = "City, State 12345";
                cells.get("B6").value = "Phone: (555) 123-4567";
                // INVOICEタイトル - セルを結合
                cells.merge(7, 1, 2, 4);
                const titleCell = cells.get("B8");
                titleCell.value = "INVOICE";
                const titleStyle = workbook.createStyle();
                titleStyle.font.isBold = true;
                titleStyle.font.size = 20;
                titleStyle.horizontalAlignment = AsposeCells.TextAlignmentType.Center;
                titleCell.style = titleStyle;
                // 請求書番号と日付
                cells.get("B11").value = "Invoice Number:";
                cells.get("C11").value = "INV-2024-001";
                cells.get("B12").value = "Date:";
                const now = new Date();
                const invoiceDate = [
                    now.getFullYear(),
                    String(now.getMonth() + 1).padStart(2, "0"),
                    String(now.getDate()).padStart(2, "0")
                ].join("-");
                cells.get("C12").value = invoiceDate;
                // 請求先セクション
                cells.get("B14").value = "Bill To:";
                cells.get("B15").value = "Client Name";
                cells.get("B16").value = "Client Address";
                cells.get("B17").value = "Client City, State";
                // 明細項目ヘッダー
                const headerDesc = cells.get("B19");
                const headerQty = cells.get("C19");
                const headerPrice = cells.get("D19");
                const headerTotal = cells.get("E19");
                headerDesc.value = "Description";
                headerQty.value = "Quantity";
                headerPrice.value = "Unit Price";
                headerTotal.value = "Total";
                const headerStyle = workbook.createStyle();
                headerStyle.font.isBold = true;
                headerStyle.font.color = Color.fromArgb(255, 255, 255);
                headerStyle.foregroundColor = Color.fromArgb(0, 0, 128);
                headerStyle.pattern = AsposeCells.BackgroundType.Solid;
                headerStyle.horizontalAlignment = AsposeCells.TextAlignmentType.Center;
                headerStyle.borders.get(AsposeCells.BorderType.TopBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                headerStyle.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                headerStyle.borders.get(AsposeCells.BorderType.LeftBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                headerStyle.borders.get(AsposeCells.BorderType.RightBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                headerDesc.style = headerStyle;
                headerQty.style = headerStyle;
                headerPrice.style = headerStyle;
                headerTotal.style = headerStyle;
                // 罫線付きの通貨形式
                const currencyStyle = workbook.createStyle();
                currencyStyle.custom = '"$"#,##0.00';
                currencyStyle.borders.get(AsposeCells.BorderType.TopBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                currencyStyle.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                currencyStyle.borders.get(AsposeCells.BorderType.LeftBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                currencyStyle.borders.get(AsposeCells.BorderType.RightBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                // 商品名・数量セル用の標準罫線形式
                const borderStyle = workbook.createStyle();
                borderStyle.borders.get(AsposeCells.BorderType.TopBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                borderStyle.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                borderStyle.borders.get(AsposeCells.BorderType.LeftBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                borderStyle.borders.get(AsposeCells.BorderType.RightBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                // 明細項目行
                const lineItems = [
                    ["Product A - Widget", 2, 50.00],
                    ["Product B - Gadget", 3, 75.00],
                    ["Product C - Service", 1, 100.00]
                ];
                for (let i = 0; i < lineItems.length; i++) {
                    const row = 20 + i;
                    const descCell = cells.get(row, 1);
                    const qtyCell = cells.get(row, 2);
                    const priceCell = cells.get(row, 3);
                    const totalCell = cells.get(row, 4);
                    descCell.value = lineItems[i][0];
                    qtyCell.value = lineItems[i][1];
                    priceCell.value = lineItems[i][2];
                    totalCell.formula = "C" + (row + 1) + "*D" + (row + 1);
                    descCell.style = borderStyle;
                    qtyCell.style = borderStyle;
                    priceCell.style = currencyStyle;
                    totalCell.style = currencyStyle;
                }
                // 小計、税金、合計
                cells.get("B24").value = "Subtotal:";
                const subtotalCell = cells.get("E24");
                subtotalCell.formula = "SUM(E21:E23)";
                cells.get("B25").value = "Tax (10%):";
                const taxCell = cells.get("E25");
                taxCell.formula = "E24*0.1";
                cells.get("B26").value = "Grand Total:";
                const grandTotalCell = cells.get("E26");
                grandTotalCell.formula = "E24+E25";
                // 合計値用の太字・通貨形式
                const totalStyle = workbook.createStyle();
                totalStyle.font.isBold = true;
                totalStyle.custom = '"$"#,##0.00';
                subtotalCell.style = totalStyle;
                taxCell.style = totalStyle;
                grandTotalCell.style = totalStyle;
                // 合計ラベル用の太字形式
                const boldStyle = workbook.createStyle();
                boldStyle.font.isBold = true;
                cells.get("B24").style = boldStyle;
                cells.get("B25").style = boldStyle;
                cells.get("B26").style = boldStyle;
                // ワークブックをOFDファイルとして保存
                const outputData = workbook.save(AsposeCells.SaveFormat.Ofd);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "Invoice.ofd";
                downloadLink.style.display = "block";
                document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                console.error(error);
                document.getElementById('result').innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
            }
        });
        </script>
    </body>
</html>
```

## **既存の Excel ファイルを OFD に変換**
Aspose.Cells は、既存の Excel ワークブックをディスクから読み込み、OFD 形式に直接エクスポートすることもできます。これは、バッチ変換パイプライン、アーカイブ用ワークフロー、および別のツールで作成したソースワークブックを固定レイアウトの成果物として再出力するだけの場合に便利です。次の例では、既存の `.xlsx` ワークブックを読み込み、セルからデータを読み取り、必要に応じてページ設定を調整し、結果を OFD ドキュメントとして保存します。

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8" />
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
            const { Workbook, CellsHelper } = AsposeCells;
            const fileInput = document.getElementById("fileInput");
            const runButton = document.getElementById("runExample");
            const downloadLink = document.getElementById("downloadLink");
            const result = document.getElementById("result");
            const readyPromise = AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            }).then(() => {
                console.log("Aspose.Cells initialized");
            });
            function formatTimestamp(date) {
                const pad = value => String(value).padStart(2, "0");
                return date.getFullYear() + "-" +
                    pad(date.getMonth() + 1) + "-" +
                    pad(date.getDate()) + " " +
                    pad(date.getHours()) + ":" +
                    pad(date.getMinutes()) + ":" +
                    pad(date.getSeconds());
            }
            function escapeHtml(value) {
                const entities = {
                    "&": "&amp;",
                    "<": "&lt;",
                    ">": "&gt;",
                    '"': "&quot;",
                    "'": "&#39;"
                };
                return String(value).replace(/[&<>"']/g, character => entities[character]);
            }
            runButton.addEventListener("click", async () => {
                try {
                    const file = fileInput.files[0];
                    if (!file) {
                        result.innerHTML = '<p style="color: red;">Please select an Excel file first.</p>';
                        return;
                    }
                    runButton.disabled = true;
                    downloadLink.style.display = "none";
                    downloadLink.removeAttribute("href");
                    // ディスク上の既存の Excel ワークブックを開く
                    const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                    // (1) 選択したセルの値を読み取り、ファイルが正常に読み込まれたことを確認する
                    const firstSheet = workbook.worksheets.get(0);
                    const cells = firstSheet.cells;
                    const output = [];
                    output.push("First sheet name: " + firstSheet.name);
                    output.push("Cell A1: " + cells.get("A1").stringValue);
                    output.push("Cell B1: " + cells.get("B1").stringValue);
                    output.push("Cell C1: " + cells.get("C1").stringValue);
                    // (2) Worksheets コレクションを反復処理して利用可能なシートを列挙する
                    output.push("");
                    output.push("Available worksheets:");
                    for (let i = 0; i < workbook.worksheets.count; i++) {
                        const ws = workbook.worksheets.get(i);
                        output.push("  [" + i + "] " + ws.name);
                    }
                    // (3) 必要に応じてタイムスタンプセルを更新し、変換日時を反映する
                    cells.get("A1").value = "Converted on: " + formatTimestamp(new Date());
                    // データブロックの先頭にサマリヘッダー行を追加する
                    cells.insertRow(0);
                    cells.get("A1").value = "Conversion Summary";
                    cells.get("A2").value = "Generated: " + formatTimestamp(new Date());
                    // (4) ワークシートの PageSetup プロパティを構成する
                    const pageSetup = firstSheet.pageSetup;
                    pageSetup.orientation = AsposeCells.PageOrientationType.Landscape;
                    pageSetup.paperSize = AsposeCells.PaperSizeType.PaperA4;
                    pageSetup.fitToPagesTall = 1;
                    pageSetup.fitToPagesWide = 1;
                    // (5) 必要に応じて OFD 出力の印刷範囲を設定する
                    const lastRow = cells.maxDataRow;
                    const lastCol = cells.maxDataColumn;
                    const lastColLetter = CellsHelper.columnIndexToName(lastCol);
                    const printArea = "A1:" + lastColLetter + (lastRow + 1);
                    pageSetup.printArea = printArea;
                    output.push("");
                    output.push("Print area set to: " + printArea);
                    // (6) ワークブックを OFD ファイルとして保存する
                    const outputData = workbook.save(AsposeCells.SaveFormat.Ofd);
                    const blob = new Blob([outputData]);
                    downloadLink.href = URL.createObjectURL(blob);
                    downloadLink.download = "SampleBook.ofd";
                    downloadLink.textContent = "Download SampleBook.ofd";
                    downloadLink.style.display = "block";
                    output.push("");
                    output.push("File successfully converted to OFD format: SampleBook.ofd");
                    result.innerHTML =
                        '<pre style="white-space: pre-wrap;">' +
                        escapeHtml(output.join("\n")) +
                        "</pre>" +
                        '<p style="color: green;">Done! Click the download link to get the result file.</p>';
                } catch (error) {
                    console.error(error);
                    const message = error && error.message ? error.message : String(error);
                    result.innerHTML = '<p style="color: red;">Error: ' + escapeHtml(message) + "</p>";
                } finally {
                    runButton.disabled = false;
                }
            });
        </script>
    </body>
</html>
```

## **関連記事**
- [セルへの画像の挿入](/cells/ja/javascript-cpp/inserting-an-image-into-a-cell/)

{{< app/cells/assistant language="javascript-cpp" >}}