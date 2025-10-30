---
title: セルに画像を挿入する方法
type: docs
weight: 130
url: /ja/javascript-cpp/how-to-insert-picture-in-cell/
description: C++経由でAspose.Cells for JavaScriptを使ったセルに画像を挿入する方法を学習してください。
keywords: セルに画像を挿入する方法、セルに画像を挿入する、セルに画像を配置する方法、セルの上に画像を配置する、セルに画像を配置する方法、セルの上に画像を配置する方法、セル内の画像とセルの上の画像を切り替える方法、セルに配置してセルの上に配置する方法の切り替え。
---

## **可能な使用シナリオ**
画像はワークシートに明るさを加え、コンテンツの視覚的表現を提供します。データを理解し、洞察を得るのが容易になります。画像を長年Excelで使用してきましたが、最近になって画像が実際のセル値になる機能が有効になりました。図のレイアウトを変更しても、データには引き続き添付されます。テーブルで使用したり、並べ替えたり、フィルターしたり、式に含めることができます!

## **Excelを使用してセルに画像を挿入する方法**
Excelのセルに画像を挿入する方法について、以下の手順に従います:

1. [挿入] タブをクリックし、[画像] オプションを選択します。
2. **セルに挿入** を選択します。[画像の挿入元]ドロップダウンメニューから次のソースのいずれかを選択します(**このデバイス**、**標準画像**、**オンライン画像** )。このデバイスは、デバイスから画像を挿入するためのものです。標準画像は、標準画像から画像を挿入するためのものです。オンライン画像は、ウェブから画像を挿入するためのものです。
<br>
<img src="1.png" width=60% />
3. 画像を選択してセルに挿入します。
<br>
<img src="8.png" width=60% />

## **Excelを使用してセルの上に画像を挿入する方法**
Excelでセルの上に画像を挿入する方法については、次の手順に従います:

1. [挿入] タブをクリックし、[画像] オプションを選択します。
2. **セルの上に置く** を選択します。[画像の挿入] ドロップダウンメニューから以下のソースの一つを選択します（**このデバイス**、**ストック画像**、および **オンライン画像**）。デバイスの画像を挿入するには、「このデバイス」を選択します。ストック画像の画像を挿入するには、「ストック画像」を選択します。ウェブから画像を挿入するには、「オンライン画像」を選択します。
<br>
<img src="2.png" width=60% />
3. 画像を選択し、セルの上に画像を挿入します。
<br>
<img src="3.png" width=60% />

## **Excel を使用してセル内の画像からセルの上に画像に切り替える方法**
**セル内の画像** から **セルの上に画像** に簡単に切り替えることができます。次の手順に従ってください。
1. セルを右クリックし、**画像内にセル** > **セルの上に置く** を選択します。 
<br>
<img src="4.png" width=60% />
2. 切り替え後の結果は次のようになります。
<br>
<img src="5.png" width=60% />

## **Excel を使用してセルの上に画像からセル内の画像に切り替える方法**
**セルの上に画像** から **セル内の画像** に簡単に切り替えることができます。次の手順に従ってください。
1. 画像を右クリックし、**セル内に配置** を選択します。 
<br>
<img src="6.png" width=60% />
2. 切り替え後の結果は次のようになります。
<br>
<img src="7.png" width=60% />

## **C++を使用してセルに画像を挿入する方法**
Aspose.Cellsを使用してセルに画像を挿入します。次のサンプルコードをご覧ください。例のコードを実行した後、画像がセルに挿入されます。
1. Workbook オブジェクトをインスタンス化します。 
2. 画像を挿入したいセルを取得します。
3. Cell.EmbeddedImage プロパティを設定します。 
4. 最後に、[output XLSX](out.xlsx)形式でブックを保存します。 

## **サンプルコード**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Embed Image into New Workbook</h1>
        <p>Select an image file to embed into cell D8. A new workbook will be created with "Apple" in A2.</p>
        <input type="file" id="imageInput" accept="image/*" />
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
            const imageInput = document.getElementById('imageInput');
            const resultDiv = document.getElementById('result');

            // Create a new workbook
            const workbook = new Workbook();
            const cells = workbook.worksheets.get(0).cells;

            // Set A2 value to "Apple"
            const a2 = cells.get("A2");
            a2.value = "Apple";

            // Get D8 cell
            const d8 = cells.get("D8");

            // If an image file is selected, read it and embed into D8
            if (imageInput.files.length) {
                const file = imageInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                const imgBuf = new Uint8Array(arrayBuffer);
                d8.embeddedImage = imgBuf;
            }

            // Save workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
