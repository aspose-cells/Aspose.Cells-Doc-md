---
title: JavaScriptを使用したC++経由でセル参照に基づく画像を挿入する
linktitle: セル参照に基づいて画像を挿入する
type: docs
weight: 150
url: /ja/javascript-cpp/insert-a-picture-based-on-cell-reference/
description: Aspose.Cells for JavaScriptをC++経由で使用し、セル参照に基づいてワークシートに画像を挿入する方法を学びます。セルデータを画像として表示します。
---

{{% alert color="primary" %}}
時々、空の画像があり、Formula Barでセル参照を設定して画像内のデータや内容を表示する必要があります。 Aspose.Cellsはこの機能（Microsoft Excel 2010）をサポートしています。
{{% /alert %}}

## セル参照に基づいて画像を挿入する

C++経由のAspose.Cells for JavaScriptは、ワークシートのセルの内容を画像シェイプとして表示することをサポートしています。画像を表示したいセルの内容とリンクさせることができます。そのセルまたはセル範囲はグラフィックオブジェクトにリンクされているため、そのセルのデータを変更すると自動的にグラフィックオブジェクトに反映されます。ワークシートに画像を追加するには、[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)オブジェクトの[**ShapeCollection.addPicture(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addPicture-number-number-number-number-uint8array-)メソッドを呼び出します。セル範囲は、[**Picture**](https://reference.aspose.com/cells/javascript-cpp/picture)オブジェクトの[**Picture.formula**](https://reference.aspose.com/cells/javascript-cpp/picture/#formula--)属性を使用して指定します。

### コード例

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Referenced Picture Example</h1>
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
            // Instantiate a new Workbook
            const workbook = new Workbook();
            // Get the first worksheet's cells collection
            const cells = workbook.worksheets.get(0).cells;

            // Add string values to the cells
            cells.get("A1").value = "A1";
            cells.get("C10").value = "C10";

            // Get the conditional icon's image data
            const imagedata = AsposeCells.ConditionalFormattingIcon.iconImageData(AsposeCells.IconSetType.TrafficLights31, 0);
            // Create a stream based on the image data
            const stream = Uint8Array.from(imagedata);

            // Add a blank picture to the D1 cell
            const pic = workbook.worksheets.get(0).shapes.addPicture(0, 3, stream, 10, 10);
            // Specify the formula that refers to the source range of cells
            pic.formula = "A1:C10";
            // Update the shapes selected value in the worksheet
            workbook.worksheets.get(0).shapes.updateSelectedValue();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'referencedpicture.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
