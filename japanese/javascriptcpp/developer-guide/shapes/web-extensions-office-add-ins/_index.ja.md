---
title: Web拡張機能  JavaScriptをC++経由で使用したOffice追加機能
linktitle: Web拡張機能  Officeアドイン
type: docs
weight: 130
url: /ja/javascript-cpp/web-extensions-office-add-ins/
---

Web拡張機能は、Officeアプリケーションを拡張し、Office文書のコンテンツとやり取りします。Web拡張機能は、ユーザーエクスペリエンスと生産性を向上させるためにOfficeクライアントに追加機能を提供します。

Aspose.CellsもWeb拡張機能と連携する機能を提供しています。

## **Web拡張機能の追加**

ExcelにWeb拡張機能（Officeアドイン）を追加できます。**挿入**タブをクリックし、その後**ストア**/**アドインを取得**リンクをクリックしてください。アドインボックスで目的のアドインを参照して追加します。

Aspose.Cellsは、[**WebExtension**](https://reference.aspose.com/cells/javascript-cpp/webextension)と[**WebExtensionTaskPane**](https://reference.aspose.com/cells/javascript-cpp/webextensiontaskpane)クラスを使用してWeb拡張を追加する機能も提供します。次のコード例は、[**WebExtension**](https://reference.aspose.com/cells/javascript-cpp/webextension)と[**WebExtensionTaskPane**](https://reference.aspose.com/cells/javascript-cpp/webextensiontaskpane)クラスを使用してExcelファイルにWeb拡張を追加する方法を示しています。詳細は[出力Excelファイル](89849869.xlsx)を参照してください。

### **サンプルコード**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Add Web Extension Example</title>
    </head>
    <body>
        <h1>Add Web Extension Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, WebExtensionStoreType, Utils } = AsposeCells;

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

            // Create a new workbook or load from selected file
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access web extensions and task panes collections from worksheets
            const extensions = workbook.worksheets.webExtensions;
            const taskPanes = workbook.worksheets.webExtensionTaskPanes;

            // Add new web extension and task pane
            const extensionIndex = extensions.add();
            const taskPaneIndex = taskPanes.add();

            // Configure the extension reference
            const extension = extensions.get(extensionIndex);
            extension.reference.id = "wa104379955";
            extension.reference.storeName = "en-US";
            extension.reference.storeType = WebExtensionStoreType.OMEX;

            // Configure the task pane
            const taskPane = taskPanes.get(taskPaneIndex);
            taskPane.isVisible = true;
            taskPane.dockState = "right";
            taskPane.webExtension = extension;

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'AddWebExtension_Out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Web extension and task pane added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Web拡張機能情報へのアクセス**

Aspose.Cellsは、Excelファイル内のWeb拡張情報にアクセスする機能を提供します。次のコード例は、[サンプルExcelファイル](89849870.xlsx)をロードし、Web拡張情報にアクセスする方法を示しています。結果はコンソール出力から確認できます。

### **サンプルコード**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Web Extensions Task Panes Example</title>
    </head>
    <body>
        <h1>Web Extensions Task Panes Example</h1>
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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing web extension task panes collection
            const taskPanes = workbook.worksheets.webExtensionTaskPanes;

            const lines = [];
            for (let i = 0; i < taskPanes.count; i++) {
                const taskPane = taskPanes.get(i);
                lines.push("Width: " + taskPane.width);
                lines.push("IsVisible: " + taskPane.isVisible);
                lines.push("IsLocked: " + taskPane.isLocked);
                lines.push("DockState: " + taskPane.dockState);

                const webExt = taskPane.webExtension;
                const reference = webExt.reference;
                lines.push("StoreName: " + reference.storeName);
                lines.push("StoreType: " + reference.storeType);
                lines.push("WebExtension.Id: " + webExt.id);
                lines.push("---------------------------------");
            }

            document.getElementById('result').innerHTML = '<pre>' + lines.join("\n") + '</pre>';
        });
    </script>
</html>
```

### **コンソール出力**

{{< highlight javascript >}}

Width: 350

IsVisible: True

IsLocked: False

DockState: right

StoreName: en-US

StoreType: OMEX

WebExtension.Id: 95D7ECE8-1355-492B-B6BF-27D25D0B0EEF

{{< /highlight >}}
