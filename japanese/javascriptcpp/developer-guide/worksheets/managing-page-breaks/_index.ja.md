---
title: ページの区切り点を管理（JavaScript/C++）
linktitle: ページブレークの管理
type: docs
weight: 30
url: /ja/javascript-cpp/managing-page-breaks/
description: この記事では、サンプルコードとともに、Aspose.Cells for JavaScriptをC++で使用してExcelワークシート内の特定のページ区切りを追加、クリア、削除する方法を解説します。
keywords: ページ区切り（JavaScript/C++）、Excelのページ区切り（JavaScript）、ページ区切りのクリア（JavaScript/C++）、特定のページ区切りの削除（C++）
---

{{% alert color="primary" %}}

定義によると、ページブレークはテキストフローの中で１つのページが終わり、次のページが始まる場所です。Microsoft Excelでは、ユーザーは任意の選択したワークシートのセルにページブレークを追加できます。

ページブレークが追加されるセルの位置によっては、ページが終了し、ページブレークの後のデータの残りが次のページで印刷されます。単純に言えば、ページブレークは、指定に応じてワークシートを複数のページに分割します。Aspose.Cellsを使用して、実行時にワークシートにページブレークを追加することもできます。Aspose.Cellsでは、以下の2種類のページブレークを追加できます。

- 水平ページブレーク
- 垂直ページブレーク

後続の議論では、Aspose.Cellsを使用して、どのようにしてワークシートに水平または垂直のページブレークを追加できるかについて説明します。

{{% /alert %}}

## **ページブレーク**

Aspose.Cells for JavaScriptをC++で使用して[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスを提供し、Excelファイルを表現します。[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスには[**workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)コレクションが含まれ、これによりExcelファイル内の各ワークシートにアクセスできます。

ワークシートは[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスによって表されます。[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスは、ワークシートを管理するために使用される幅広い範囲のプロパティとメソッドを提供しています。

ページブレークを追加するには、[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスの[**worksheet.horizontalPageBreaks**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#horizontalPageBreaks--)および[**worksheet.verticalPageBreaks**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#verticalPageBreaks--)プロパティを使用します。

[**worksheet.horizontalPageBreaks**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#horizontalPageBreaks--)および[**worksheet.verticalPageBreaks**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#verticalPageBreaks--)プロパティは、いくつかのページブレークを含む可能性があるコレクションであり、各コレクションには水平および垂直ページブレークを管理するためのいくつかのメソッドが含まれています。

### **ページブレークの追加**

ワークシートにページブレークを追加するには、指定されたセルで垂直および水平のページブレークを挿入します。[**HorizontalPageBreakCollection.add(number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/horizontalpagebreakcollection/#add-number-number-number-)と[**VerticalPageBreakCollection.add(number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/verticalpagebreakcollection/#add-number-number-number-)メソッドを呼び出します。各**add**メソッドは、ブレークを追加するセルの名前を受け取ります。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Adding Page Breaks Example</h1>
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

            // If a file is provided, open it; otherwise create a new workbook
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

            // Add a page break at cell Y30
            worksheet.horizontalPageBreaks.add("Y30");
            worksheet.verticalPageBreaks.add("Y30");

            // Save the Excel file (Excel 97-2003 format .xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'AddingPageBreaks_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Page breaks added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

ページビューモードまたは印刷プレビューモードで、これらの改ページがどのように動作するかを確認できます。

{{% /alert %}}

### **特定の改ページを削除する**

特定のページブレークを削除するには、[**HorizontalPageBreakCollection.removeAt(number)**](https://reference.aspose.com/cells/javascript-cpp/horizontalpagebreakcollection/#removeAt-number-)と[**VerticalPageBreakCollection.removeAt(number)**](https://reference.aspose.com/cells/javascript-cpp/verticalpagebreakcollection/#removeAt-number-)メソッドを呼び出します。各**removeAt**メソッドは、削除対象のページブレークのインデックスを受け取ります。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Remove Specific Page Break Example</title>
    </head>
    <body>
        <h1>Remove Specific Page Break Example</h1>
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

            // Removing a specific page break
            worksheet.horizontalPageBreaks.removeAt(0);
            worksheet.verticalPageBreaks.removeAt(0);

            // Saving the Excel file (Excel 97-2003 format for .xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'RemoveSpecificPageBreak_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Page breaks removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **重要なこと**

ページ設定の**fitToPages**（[**PageSetup.fitToPagesTall**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#fitToPagesTall--)と[**PageSetup.fitToPagesWide**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#fitToPagesWide--)）プロパティを設定すると、ページブレーク設定に影響し、印刷時にページブレーク設定が考慮されませんが、設定自体は維持されます。
