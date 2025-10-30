---
title: マージンの設定（JavaScript経由C++）
linktitle: マージンの設定
type: docs
weight: 20
url: /ja/javascript-cpp/setting-margins/
description: この記事では、サンプルコードを使ってExcelワークシートのマージンを設定する方法と、JavaScript APIを使用してページ中央、ヘッダー、フッターのマージンをプログラム的に設定する方法について説明します。
keywords: Excelワークシートのマージンを中央に設定（JavaScript経由C++）、ヘッダーとフッターのマージンを設定（JavaScript経由C++）
---

{{% alert color="primary" %}}

Aspose.CellsはMicrosoft Excelのページ設定オプションを完全にサポートしています。開発者は印刷プロセスを制御するためにワークシートのページ設定設定を構成する必要があります。このトピックでは、Aspose.Cellsを使用してページ余白を設定する方法について説明します。

{{% /alert %}}

## **マージンの設定**

Aspose.Cells for JavaScriptをC++で使用すると、Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスがあります。[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスには[**Workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)コレクションが含まれ、Excelファイル内の各ワークシートにアクセスできます。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスで表されます。

[**Worksheet.pageSetup**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#pageSetup--)プロパティはワークシートのページ設定オプションを設定するために使用されます。[**Worksheet.pageSetup**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#pageSetup--)属性は[**Worksheet.pageSetup**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#pageSetup--)クラスのオブジェクトで、印刷されるワークシートのページレイアウトオプションを設定することを可能にします。[**Worksheet.pageSetup**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#pageSetup--)クラスはさまざまなプロパティとメソッドを提供し、ページ設定オプションの設定に使用されます。

### **ページ余白**

[**Worksheet.pageSetup**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#pageSetup--)クラスメンバーを使用してページの余白（左、右、上、下）を設定します。以下にページ余白を指定するために使用されるいくつかのメンバーを示します：

- [**PageSetup.leftMargin**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#leftMargin--)
- [**PageSetup.rightMargin**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#rightMargin--)
- [**PageSetup.topMargin**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#topMargin--)
- [**PageSetup.bottomMargin**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#bottomMargin--)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Set Page Margins Example</title>
    </head>
    <body>
        <h1>Set Page Margins Example</h1>
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
                // Proceed with a new empty workbook if no file selected
            }

            const file = fileInput.files.length ? fileInput.files[0] : null;
            let workbook;
            if (file) {
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            const worksheets = workbook.worksheets;
            const worksheet = worksheets.get(0);
            const pageSetup = worksheet.pageSetup;

            pageSetup.bottomMargin = 2;
            pageSetup.leftMargin = 1;
            pageSetup.rightMargin = 1;
            pageSetup.topMargin = 3;

            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SetMargins_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Page margins set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **ページの中央に配置**

ページを横方向および縦方向に中央揃えに配置することは可能です。そのための便利なメンバーとして[**Worksheet.pageSetup**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#pageSetup--)クラスの[**PageSetup.centerHorizontally**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#centerHorizontally--)と[**PageSetup.centerVertically**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#centerVertically--)があります。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Center On Page</title>
    </head>
    <body>
        <h1>Center On Page Example</h1>
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
            // Create a workbook object (blank workbook)
            const workbook = new Workbook();

            // Get the worksheets in the workbook
            const worksheets = workbook.worksheets;

            // Get the first (default) worksheet
            const worksheet = worksheets.get(0);

            // Get the pagesetup object
            const pageSetup = worksheet.pageSetup;

            // Specify Center on page Horizontally and Vertically
            pageSetup.centerHorizontally = true;
            pageSetup.centerVertically = true;

            // Save the Workbook in Excel 97-2003 format (.xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CenterOnPage_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook processed successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

### **ヘッダーとフッタのマージン**

ヘッダーとフッターの余白を設定するには、[**Worksheet.pageSetup**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#pageSetup--)クラスのメンバーである[**PageSetup.headerMargin**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#headerMargin--)と[**PageSetup.footerMargin**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#footerMargin--)を使います。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Set Header/Footer Margins</title>
    </head>
    <body>
        <h1>Set Header/Footer Margins Example</h1>
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
            // Create a new workbook (equivalent to new AsposeCells.Workbook() in JavaScript)
            const workbook = new Workbook();

            // Get the worksheets collection
            const worksheets = workbook.worksheets;

            // Get the first (default) worksheet
            const worksheet = worksheets.get(0);

            // Get the pageSetup object
            const pageSetup = worksheet.pageSetup;

            // Specify Header / Footer margins (converted from setHeaderMargin/setFooterMargin)
            pageSetup.headerMargin = 2;
            pageSetup.footerMargin = 2;

            // Save the Workbook as Excel 97-2003 format
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CenterOnPage_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook processed successfully. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
