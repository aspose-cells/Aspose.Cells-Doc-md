---
title: Excel XP以降の高度な保護設定をJavaScriptを使用してC++で実現
linktitle: Excel XP以降の高度な保護設定
type: docs
weight: 30
url: /ja/javascript-cpp/advanced-protection-settings-since-excel-xp/
---

{{% alert color="primary" %}}

Excel 2002またはXPのリリース以降、Microsoftは多くの高度な保護設定を追加しました。

{{% /alert %}}


## **紹介**

これらの保護設定により、ユーザーは次の操作を制限または許可できます：

- 行または列の削除。
- 内容、オブジェクト、またはシナリオの編集。
- セル、行、または列の書式設定。
- 行、列、またはハイパーリンクの挿入。
- ロックされたセルまたはロックされていないセルの選択。
- ピボットテーブルなどの使用。

Aspose.Cells for JavaScriptをC++でサポートし、Excel XP以降の高度な保護設定をすべて提供します。

### **Excel XPおよびそれ以降のバージョンを使用した高度な保護設定**

Excel XPで利用可能な保護設定を表示するには：

1. **ツール**メニューから、**保護**の後に**シートを保護**を選択します。ダイアログが表示されます。

Excel 2016で利用可能な保護設定を見るには：

1. **ファイル**メニューから、**ワークブックを保護**, その後**現在のシートを保護**を選択します。
1. **レビュー**メニューで**シートを保護**を選択します。

上記の手順に従うと、ダイアログが表示され、シートの機能の許可または制限やシートにパスワードを設定できます。

### **Aspose.Cells for JavaScriptを使用した高度な保護設定**

Aspose.Cells for JavaScriptをC++で使用し、すべての高度な保護設定をサポートします。

Aspose.Cellsは、Microsoft Excelファイルを表す [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) を提供します。[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) クラスには、Excelファイル内の各ワークシートにアクセスできる [**Worksheets**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection) コレクションが含まれています。ワークシートは [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) クラスによって表されます。

[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) クラスは、これらの高度な保護設定を適用するために使用される [**protection**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#protection--) プロパティを提供します。[**protection**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#protection--) プロパティは実際には、いくつかの制限を無効または有効にするためのいくつかのブーリアンプロパティをカプセル化した [**Protection**](https://reference.aspose.com/cells/javascript-cpp/protection) クラスのオブジェクトです。

以下は小さなサンプルアプリケーションです。それはExcelファイルを開いて、Excel XPおよびそれ以降のバージョンでサポートされる高度な保護設定のほとんどを使用します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Aspose.Cells Worksheet Protection Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const worksheet = workbook.worksheets.get(0);
            const protection = worksheet.protection;

            // Restricting users to delete columns of the worksheet
            protection.allowDeletingColumn = false;

            // Restricting users to delete row of the worksheet
            protection.allowDeletingRow = false;

            // Restricting users to edit contents of the worksheet
            protection.allowEditingContent = false;

            // Restricting users to edit objects of the worksheet
            protection.allowEditingObject = false;

            // Restricting users to edit scenarios of the worksheet
            protection.allowEditingScenario = false;

            // Restricting users to filter
            protection.allowFiltering = false;

            // Allowing users to format cells of the worksheet
            protection.allowFormattingCell = true;

            // Allowing users to format rows of the worksheet
            protection.allowFormattingRow = true;

            // Allowing users to insert columns in the worksheet
            protection.allowFormattingColumn = true;

            // Allowing users to insert hyperlinks in the worksheet
            protection.allowInsertingHyperlink = true;

            // Allowing users to insert rows in the worksheet
            protection.allowInsertingRow = true;

            // Allowing users to select locked cells of the worksheet
            protection.allowSelectingLockedCell = true;

            // Allowing users to select unlocked cells of the worksheet
            protection.allowSelectingUnlockedCell = true;

            // Allowing users to sort
            protection.allowSorting = true;

            // Allowing users to use pivot tables in the worksheet
            protection.allowUsingPivotTable = true;

            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet protection settings applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスの[**protect(ProtectionType)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#protect-protectiontype-)メソッドを使用しないでください。また、[**protection**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#protection--)プロパティを使用してファイルをExcel97-2003またはXlsx形式で保存してください。高度な保護設定はExcel XP以降のみ対応です。

{{% /alert %}}

### **セルロックの問題**

セルの編集を制限したい場合は、保護設定を適用する前にセルをロックする必要があります。そうしないと、シートが保護されていてもセルは編集可能です。Microsoft Excel XPでセルをロックするには次のダイアログを使用します：

|**Excel XPでセルをロックするダイアログ**|
| :- |
|![todo:image_alt_text](advanced-protection-settings-since-excel-xp_1.png)|

Aspose.Cells APIを使ってセルをロックすることも可能です。各セルには、Boolean型の[**Style**](https://reference.aspose.com/cells/javascript-cpp/style)書式設定と[**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--)プロパティがあります。[**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--)プロパティを**true**または**false**に設定して、セルをロックまたはアンロックします。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Protect Worksheet Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ProtectionType, Utils } = AsposeCells;

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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Lock cell A1 by setting the style property
            const cell = worksheet.cells.get("A1");
            cell.style.isLocked = true;

            // Protect the sheet now.
            worksheet.protect(ProtectionType.All);

            // Saving the modified Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Result';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet protected successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
