---
title: オートフィルタを更新した後のすべての非表示行のインデックスを取得する 
type: docs  
weight: 320  
url: /ja/javascript-cpp/get-all-hidden-rows-indices-after-refreshing-autofilter/  
description: AutoFilterをリフレッシュした後にすべての非表示行のインデックスを取得する方法について学びます。  
keywords: AutoFilterをリフレッシュした後のすべての非表示行インデックスを取得するJavaScript（C++使用）  
---

## **可能な使用シナリオ**  

ワークシートにオートフィルタを適用すると、一部の行が自動的に非表示になります。ただし、Excelのエンドユーザーにより手動で既に非表示にされている行もあるため、AutoFilterによる非表示と手動非表示の区別が難しい場合があります。Aspose.Cells for JavaScript（C++）は、この問題を`Array` [**AutoFilter.refresh(hideRows)**](https://reference.aspose.com/cells/javascript-cpp/autofilter/#refresh-boolean-)を使って対処します。この方法は、自動フィルタによって非表示にされたが、手動ではない行のインデックスすべてを返します。  

## **オートフィルタの更新後の非表示行インデックスの取得**  

Excelのエンドユーザーによって手動で非表示になった行を含む[サンプルExcelファイル](64716909.xlsx)をロードし、自動フィルターを適用・更新し、非表示の行のインデックスを返す[**AutoFilter.refresh(hideRows)**](https://reference.aspose.com/cells/javascript-cpp/autofilter/#refresh-boolean-)メソッドを使用した例。これらのインデックスとセルの名前・値もコンソールに出力されます。  

## **サンプルコード**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Get Hidden Rows After Refreshing AutoFilter</title>
    </head>
    <body>
        <h1>Get Hidden Rows After Refreshing AutoFilter</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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

            // Instantiating a Workbook object from file input
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Apply autofilter
            worksheet.autoFilter.addFilter(0, "Orange");

            // True means it will refresh autofilter and return hidden rows.
            const rowIndices = worksheet.autoFilter.refresh(true);

            console.log("Printing Rows Indices, Cell Names and Values Hidden By AutoFilter.");
            console.log("--------------------------");

            let output = '<p>Printing Rows Indices, Cell Names and Values Hidden By AutoFilter.</p><pre>';
            rowIndices.forEach(r => {
                const cell = worksheet.cells.get(r, 0);
                console.log(`${r}\t${cell.name}\t${cell.stringValue}`);
                output += `${r}\t${cell.name}\t${cell.stringValue}\n`;
            });
            output += '</pre>';

            resultDiv.innerHTML = output;
        });
    </script>
</html>
```


## **コンソール出力**  

{{< highlight java >}}  

Printing Rows Indices, Cell Names and Values Hidden By AutoFilter.  

\--------------------------  

1       A2      Apple  

2       A3      Apple  

3       A4      Apple  

6       A7      Apple  

7       A8      Apple  

11      A12     Pear  

12      A13     Pear  

{{< /highlight >}}
