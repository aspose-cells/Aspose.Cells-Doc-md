---
title: JavaScriptを介したC++でワークシートやタブの表示・非表示を行います
linktitle: ワークシートとタブの表示と非表示
type: docs
weight: 10
url: /ja/javascript-cpp/show-and-hide-worksheets-and-tabs/
description: この記事は、JavaScript APIまたはJavaScriptライブラリを使用して、Excelワークシートをプログラム的に表示・非表示にするサンプルコードとともに、Excelワークブックのタブの表示・非表示についても説明します。
---

{{% alert color="primary" %}}
Aspose.Cellsはユーザーに、ワークブック内のワークシートやタブなどの要素を表示または非表示にする機能を提供します。
{{% /alert %}}

## **ワークシートの表示と非表示**

Excelファイルには1つ以上のワークシートが含まれることがあります。Excelファイルを作成するときには、作業するExcelファイルにワークシートを追加します。Excelファイル内の各ワークシートは、独自のデータや書式設定などを持つため、他のワークシートから独立しています。開発者は時々、Excelファイル内で特定のワークシートを非表示にし、他のワークシートを表示したい場合があります。そのため、Aspose.Cellsは開発者がExcelファイル内のワークシートの表示を制御することを可能にします。

Aspose.Cellsは、Excelファイルを表すクラス[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)を提供します。[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスには、Excelファイル内の各ワークシートにアクセスできる[**workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)コレクションが含まれています。

ワークシートは[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスによって表されます。[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスは、ワークシートを管理するためのさまざまなプロパティとメソッドを提供します。ワークシートの表示状態を制御するには、[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスの[**Worksheet.isVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isVisible--)プロパティを使用します。[**Worksheet.isVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isVisible--)はBoolean型のプロパティであり、**true**または**false**の値しか保存できません。

### **ワークシートを表示する**

[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスの[**Worksheet.isVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isVisible--)プロパティを**true**に設定して、ワークシートを表示します。

### **ワークシートを非表示にする**

[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスの[**Worksheet.isVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isVisible--)プロパティを**false**に設定して、ワークシートを非表示にします。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Hide Worksheet Example</title>
    </head>
    <body>
        <h1>Hide Worksheet Example</h1>
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

            // Instantiating a Workbook object by opening the Excel file from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Hiding the first worksheet of the Excel file
            worksheet.isVisible = false;

            // Saving the modified Excel file in Excel 97-2003 format
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet hidden successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **タブの表示と非表示**

Microsoft Excelの下部をよく見ると、いくつかのコントロールが表示されます。これには次のものが含まれます:

- シートタブ。
- タブのスクロールボタン。

シートタブはExcelファイル内のワークシートを表します。任意のタブをクリックするとそのワークシートに切り替えることができます。ワークブック内にワークシートが多いほど、シートタブも多く表示されます。Excelファイルに多くのワークシートが含まれている場合は、それらをナビゲートするためのボタンが必要になります。そのため、Microsoft Excelはシートタブのスクロールボタンを提供しています。

Aspose.Cellsを使用すると、開発者はExcelファイル内のシートタブとタブのスクロールボタンの表示を制御できます。

Aspose.Cellsは、Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスは、Excelファイルを管理するためのさまざまなプロパティとメソッドを提供します。Excelファイルのタブの表示状態を制御するには、開発者は[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスの[**WorkbookSettings.showTabs**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#showTabs--)プロパティを使用できます。[**WorkbookSettings.showTabs**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#showTabs--)はBoolean型のプロパティであり、**true**または**false**の値しか保存できません。

### **タブを表示する**

[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスの[**WorkbookSettings.showTabs**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#showTabs--)プロパティを**true**に設定してタブを表示します。

### **タブを非表示にする**

[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスの[**WorkbookSettings.showTabs**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#showTabs--)プロパティを**false**に設定して、Excelファイルのタブを非表示にします。

以下は、Excelファイル（book1.xls）を開き、そのタブを非表示にして修正したファイルをoutput.xlsとして保存する完全な例です。コードの実行後、ワークブックのタブが非表示になっていることが確認できます。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Hide Worksheet Tabs Example</h1>
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

            // Instantiating a Workbook object by opening the Excel file from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Hiding the tabs of the Excel file
            workbook.settings.showTabs = false;

            // To show the tabs instead, you could set:
            // workbook.settings.showTabs = true;

            // Saving the modified Excel file (Excel 97-2003 format for .xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Tabs hidden successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **タブバーの幅を制御する**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Hide Tabs</title>
    </head>
    <body>
        <h1>Hide Tabs Example</h1>
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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Hiding the tabs of the Excel file (converted setter to property)
            workbook.settings.showTabs = true;

            // Adjusting the sheet tab bar width (converted setter to property)
            workbook.settings.sheetTabBarWidth = 800;

            // Saving the modified Excel file (SaveFormat.Xls -> SaveFormat.Excel97To2003)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
