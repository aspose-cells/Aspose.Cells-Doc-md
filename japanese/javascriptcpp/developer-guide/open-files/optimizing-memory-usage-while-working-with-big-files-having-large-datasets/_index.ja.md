---
title: 大規模なデータセットを含む大きなファイルのメモリ使用量を最適化しながら作業する方法をJavaScript経由でC++で解説
linktitle: 大規模なデータセットを扱う場合のメモリ使用量を最適化する
type: docs
weight: 180
url: /ja/javascript-cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
---

{{% alert color="primary" %}}

大規模なデータセットを含むワークブックを作成したり、大きなMicrosoft Excelファイルを読み取ったりする際、必要なRAMの総量は常に懸念事項です。これに対処するための措置があります。Aspose.Cells for JavaScriptをC++で使用すると、メモリの削減や最適化を行うためのオプションやAPI呼び出しを提供し、処理をより効率的かつ高速にすることができます。

セルのデータのメモリ使用を最適化し、総合的なメモリコストを減らすために [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/) オプションを使用してください。大規模なセルデータセットを構築する際、デフォルトの設定（[**MemorySetting.Normal**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/)）に比べて一定量のメモリを節約することができます。

{{% /alert %}}

## **メモリの最適化**

### **大きなExcelファイルの読み取り**

以下の例は、最適化モードで大きなMicrosoft Excelファイルを読み取る方法を示しています。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - LoadOptions MemorySetting</title>
    </head>
    <body>
        <h1>LoadOptions MemorySetting Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions, MemorySetting, SaveFormat, Utils } = AsposeCells;

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

            // Specify the LoadOptions
            const opt = new LoadOptions();
            // Set the memory preferences (converted from setMemorySetting)
            opt.memorySetting = MemorySetting.MemoryPreference;

            // Instantiate the Workbook - load the big Excel file with options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), opt);

            // Save the workbook to XLSX and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook loaded with MemoryPreference. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

### **大きなExcelファイルの書き込み**

以下の例は、大規模なデータセットをワークシートに書き込む方法を最適化モードで示しています。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Memory Setting Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Memory Setting Example</h1>
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
            if (!fileInput.files.length) {
                // If no file is selected, create a new workbook (similar to new AsposeCells.Workbook() in Node)
                // and proceed to set memory settings and populate sheets.
            }

            // Load workbook from file if provided, otherwise create empty workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Set the memory preferences on the workbook settings
            workbook.settings.memorySetting = AsposeCells.MemorySetting.MemoryPreference;

            // Note: The memory settings also would not work for the default sheet i.e., "Sheet1" etc. automatically created by the Workbook
            // To change the memory setting of existing sheets, change memory setting for them manually:
            let cells = workbook.worksheets.get(0).cells;
            cells.memorySetting = AsposeCells.MemorySetting.MemoryPreference;

            // Input large dataset into the cells of the worksheet.
            // Your code goes here.
            // Example: populate a few cells to demonstrate
            const firstCell = cells.get(0, 0);
            firstCell.value = "Sample Data 1";
            cells.get(1, 0).value = "Sample Data 2";

            // Get cells of the newly created Worksheet "Sheet2" whose memory setting is same with the one defined in WorkbookSettings:
            const sheet2 = workbook.worksheets.add("Sheet2");
            const cells2 = sheet2.cells;
            // .........
            // Input large dataset into the cells of the worksheet.
            // Your code goes here.
            // Example: populate a few cells in Sheet2
            cells2.get(0, 0).value = "Sheet2 Data 1";
            cells2.get(1, 0).value = "Sheet2 Data 2";

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Result';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **注意**

デフォルトオプションの[**MemorySetting.Normal**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/)はすべてのバージョンに適用されます。大規模なセルデータセットを持つワークブック作成などの特定の状況では、[**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/)オプションがメモリ使用を最適化し、アプリケーションのメモリコストを削減することができます。ただし、このオプションは一部の特定のケースではパフォーマンス低下を引き起こすこともあります。

1. **セルへのランダムかつ繰り返しアクセス**：セルコレクションへのアクセスに最も効率的な順序は、1行ごとにセルをアクセスし、その後行ごとに進む方法です。特に、[**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)、[**RowCollection**](https://reference.aspose.com/cells/javascript-cpp/rowcollection)、[**Row**](https://reference.aspose.com/cells/javascript-cpp/row)から取得した列挙子を使用して行やセルにアクセスすると、[**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/)を使用した場合にパフォーマンスが最大化します。
2. **セルや行の挿入と削除**：セルや行への挿入/削除操作が多い場合、*MemoryPreference*モードでは*Normal*モードに比べてパフォーマンスの低下が顕著になることに注意してください。
3. **異なるセルタイプの操作**：ほとんどのセルが文字列値や数式を含む場合、メモリコストは*Normal*モードと同じですが、多くの空セルや、数値、ブール値などが含まれる場合、[**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/)オプションはより良いパフォーマンスを提供します。
