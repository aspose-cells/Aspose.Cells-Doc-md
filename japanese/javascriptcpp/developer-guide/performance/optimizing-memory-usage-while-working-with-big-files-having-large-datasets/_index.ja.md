---
title: 大規模なデータセットを扱う場合のメモリ使用量を最適化する
type: docs
weight: 110
url: /ja/javascript-cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
---

{{% alert color="primary" %}}

大規模なデータセットを含むワークブックを構築したり、大きなMicrosoft Excelファイルを読み込んだりする際、プロセスが必要とするRAMの総量は常に懸念事項です。Aspose.Cellsは、メモリ使用量を最適化するための関連するオプションとAPI呼び出しを提供します。これにより、プロセスがより効率的に動作し、より速く実行されるようになります。

セルデータのメモリ使用量を最適化するために、[**MemorySetting.Normal**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/)よりもメモリ使用量を減らすために使用します。大規模なデータセットを扱う際、デフォルトの設定を使用するよりも一定量のメモリを節約することができます。

{{% /alert %}}

## **メモリの最適化**

大規模なデータを扱う際のメモリ最適化の例をC++を使用したAspose.Cells for JavaScriptで示す

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Optimize Memory Usage Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, MemorySetting } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file or leave empty to create a new one.</p>';
                // Allow creating a new workbook even if no file selected; return only if user explicitly requires file.
            }

            // If a file is provided, open it; otherwise create a new workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // apply the setting to existing "Sheet1"
            workbook.worksheets.get(0).cells.memorySetting = MemorySetting.MemoryPreference;

            // apply the setting globally
            workbook.settings.memorySetting = MemorySetting.MemoryPreference;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Memory settings applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **注意**

デフォルトオプション[**MemorySetting.Normal**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/)はすべてのバージョンで適用されます。大量のセルデータセットを持つワークブックを構築するなどの一部の状況では、メモリ使用を最適化し、アプリケーションのメモリコストを減らすことができるかもしれませんが、このオプションは特定の状況ではパフォーマンスを低下させる可能性があります。

1. **ランダムで繰り返しセルにアクセス**: セルのコレクションにアクセスする最も効率的なシーケンスは、行ごとに1つずつセルにアクセスし、その後行ごとにアクセスすることです。特に、[**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells/)、[**RowCollection**](https://reference.aspose.com/cells/javascript-cpp/rowcollection)および[**Row**](https://reference.aspose.com/cells/javascript-cpp/row)から取得したEnumeratorで行/セルにアクセスする場合、パフォーマンスは[**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/)で最適化されます。
1. **セルや行の挿入および削除**：多くの挿入/削除操作がセル/行にある場合、[**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/)モードでは、[**MemorySetting.Normal**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/)モードと比較してパフォーマンスの低下が顕著になります。
1. **異なるセルタイプでの操作**：ほとんどのセルが文字列値や数式を含む場合、メモリコストは[**MemorySetting.Normal**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/)モードと同じになりますが、空のセルが多いか、セルの値が数値、ブール値などの場合、[**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/)オプションはパフォーマンスが向上します。
