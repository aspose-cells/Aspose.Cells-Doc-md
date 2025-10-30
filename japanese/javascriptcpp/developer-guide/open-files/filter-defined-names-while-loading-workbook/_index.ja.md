---
title: C++経由でJavaScriptを使用してブックの読み込み時に定義された名前をフィルターする
linktitle: ワークブックを読み込む際に定義名をフィルタリングする
type: docs
weight: 50
url: /ja/javascript-cpp/filter-defined-names-while-loading-workbook/
---

## **可能な使用シナリオ**

Aspose.Cellsは、ワークブック内の定義名をフィルタまたは削除することを可能にします。読み込み時に定義名をロードするには[**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/javascript-cpp/loaddatafilteroptions/)を使用し、削除するには[**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/javascript-cpp/loaddatafilteroptions/)を使用してください。ただし、定義名を削除すると、ワークブック内の数式が壊れる可能性があります。

## **ワークブックを読み込む際に定義名をフィルタリングする**

以下のサンプルコードは、定義名を含むセル（=SUM(MyName1, MyName2)）があるセルC1に数式を含むサンプルExcelファイル（61767860.xlsx）を読み込みます。読み込み時に[**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/javascript-cpp/loaddatafilteroptions/)を使用して定義名を削除しているため、出力Excelファイル（61767861.xlsx）のセルC1の数式は壊れ、「#NAME?」と表示されます。以下のスクリーンショットは、サンプルExcelファイルに対するコードの効果を示しています。

![todo:image_alt_text](filter-defined-names-while-loading-workbook_1.png)

## **サンプルコード**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Filter Defined Names While Loading Workbook</title>
    </head>
    <body>
        <h1>Filter Defined Names While Loading Workbook</h1>
        <input type="file" id="fileInput" accept=".xlsx,.xls" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, LoadFilter, LoadDataFilterOptions, Utils } = AsposeCells;

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

            // Specify the load options
            let opts = new LoadOptions();
            // We do not want to load defined names
            opts.loadFilter = new LoadFilter(~LoadDataFilterOptions.DefinedNames);

            // Load the workbook with load options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), opts);

            // Save the output Excel file, it will break the formula in C1 if defined names were removed
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputFilterDefinedNamesWhileLoadingWorkbook.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">FilterDefinedNamesWhileLoadingWorkbook executed successfully. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
