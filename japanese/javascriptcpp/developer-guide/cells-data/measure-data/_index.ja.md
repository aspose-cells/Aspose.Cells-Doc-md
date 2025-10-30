---
title: セル値の幅と高さをピクセル単位で計測します
linktitle: サイズを計測します
type: docs
weight: 260
url: /ja/javascript-cpp/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/
description: C++を通じてAspose.Cells for JavaScriptを使い、セル値の幅と高さをピクセル単位で測定する方法を学びます。
keywords: ピクセル単位でセル値の幅を測定（C++用JavaScript）、セル値の高さをピクセル単位で測定（C++用JavaScript）、セル値の幅をピクセル単位で取得（C++用JavaScript）、セル値の高さをピクセル単位で取得（C++用JavaScript）
---

{{% alert color="primary" %}}  

セル値の幅と高さを計算してセル内に収まるようにする必要がある場合があります。Aspose.Cells ではこの目的のために [**Cell.widthOfValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#widthOfValue--) および [**Cell.heightOfValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#heightOfValue--) のメソッドを提供しています。これらのメソッドを使用することで、セル値の幅と高さを計算し、そのセルの列の幅と行の高さをそれぞれ設定し、これによりセル値を調整またはセル内に収めることができます。  

または、Aspose.Cells APIを使用してセルまたはセル範囲の高さと幅を自動調整することも可能です。[/cells/ja/javascript-cpp/autofit-rows-and-columns/]を参照してください。  

{{% /alert %}}  

[**Cell.widthOfValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#widthOfValue--)と[**Cell.heightOfValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#heightOfValue--)メソッドの使用例を次のコードで説明します。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Get Cell Size Example</h1>
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

            // Create or load workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access cell B2 and add some value inside it
            const cell = worksheet.cells.get("B2");
            cell.value = "Welcome to Aspose!";

            // Enlarge its font to size 16
            const style = cell.style;
            style.font.size = 16;
            cell.style = style;

            // Calculate the width and height of the cell value in unit of pixels
            const widthOfValue = cell.widthOfValue;
            const heightOfValue = cell.heightOfValue;

            // Print both values to the page
            document.getElementById('result').innerHTML = `<p>Width of Cell Value: ${widthOfValue}</p><p>Height of Cell Value: ${heightOfValue}</p>`;

            // Set the row height and column width to adjust/fit the cell value inside cell
            worksheet.cells.setColumnWidthPixel(1, widthOfValue);
            worksheet.cells.setRowHeightPixel(1, heightOfValue);

            // Save the output excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';
        });
    </script>
</html>
```


## **高度なトピック**  
- [セル値のテキスト幅を取得する](/cells/ja/javascript-cpp/get-text-width-of-cell-value/)
