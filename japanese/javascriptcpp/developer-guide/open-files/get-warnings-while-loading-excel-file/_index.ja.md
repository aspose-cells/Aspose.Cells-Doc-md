---
title: JavaScriptとC++を使用してExcelファイルの読み込み時に警告を取得する方法
linktitle: Excelファイルの読み込み時に警告を取得する
type: docs
weight: 110
url: /ja/javascript-cpp/get-warnings-while-loading-excel-file/
description: Aspose.Cells for JavaScriptを使用してExcelファイルを読み込む際の警告のキャプチャ方法を学び、破損しているが読み込み可能なワークブックを効果的に処理します。
---

## **可能な使用シナリオ**

時には、ある程度破損しているが読み込めるワークブックを読み込もうとするユーザーもいます。そのような場合、Aspose.Cellsは読み込み時に警告をスローします。これらの警告は、[**IWarningCallback**](https://reference.aspose.com/cells/javascript-cpp/iwarningcallback)インターフェースを実装し、[**LoadOptions.warningCallback**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#warningCallback--)プロパティを設定することでキャッチできます。

## **Excelファイルの読み込み中に警告を受け取る**

以下のサンプルコードは、読み込み時に警告を取得する例です。サンプルExcelファイル（sampleDuplicateDefinedName.xlsx）を読み込むと、[**DuplicateDefinedName**](https://reference.aspose.com/cells/javascript-cpp/warningtype)警告がスローされます。この警告は、[**IWarningCallback.warning(WarningInfo)**](https://reference.aspose.com/cells/javascript-cpp/iwarningcallback/#warning-warninginfo-)メソッドによって捕捉され、警告メッセージがコンソールに出力されます。その後、ワークブックは[出力Excelファイル](outputDuplicateDefinedName.xlsx)として保存されます。Microsoft Excelでファイルを開くと、スクリーンショットのようにこの警告も表示されます。

![todo:image_alt_text](get-warnings-while-loading-excel-file_1.png)

## **サンプルコード**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Warning Callback Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Warning Callback Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, WarningType } = AsposeCells;

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

        // Implement IWarningCallback interface to catch warnings while loading workbook
        class WarningCallback extends AsposeCells.IWarningCallback {
            warning(warningInfo) {
                if (warningInfo.type === AsposeCells.WarningType.DuplicateDefinedName) {
                    console.log("Duplicate Defined Name Warning: " + warningInfo.description);
                }
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create load options and set the WarningCallback property 
            // to catch warnings while loading workbook
            const options = new LoadOptions();
            options.warningCallback = new WarningCallback();

            // Load the source excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer), options);

            // Save the workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputDuplicateDefinedName.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Resulting Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook processed successfully. Check console for warnings.</p>';
        });
    </script>
</html>
```

## **コンソール出力**



{{< highlight java >}}

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Introduction!$D$16:$D$17

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Panel!$B$228

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:'Queries '!$D$14:$D$16

{{< /highlight >}}
