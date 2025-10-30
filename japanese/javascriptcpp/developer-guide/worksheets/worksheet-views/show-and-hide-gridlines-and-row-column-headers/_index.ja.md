---
title: JavaScriptを介してC++でグリッド線や行・列の見出しの表示・非表示を行います
linktitle: グリッド線と行列ヘッダーの表示および非表示
type: docs
weight: 30
url: /ja/javascript-cpp/show-and-hide-gridlines-and-row-column-headers/
description: この記事は、C++を経由したJavaScript APIを使ってExcelワークシートのグリッド線や行・列の見出しをプログラム的に非表示または表示するサンプルコードを提供します。
---

{{% alert color="primary" %}}  
Aspose.Cellsは、デフォルトで表示されているワークシートのグリッド線の非表示および表示をサポートしています。また、ワークシートの行列ヘッダーの表示を制御する機能も提供しています。  
{{% /alert %}}  

## **グリッド線の表示と非表示**  

すべてのExcelワークシートはデフォルトでグリッド線を持っています。これにより、特定のセルにデータを入力することが簡単になります。グリッド線により、ワークシートをセルのコレクションとして表示し、各セルを簡単に識別することができます。  

### **グリッド線の表示の制御**  

Aspose.Cellsは、Microsoft Excelファイルを表す [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスは、Excelファイル内の各ワークシートにアクセスできる [**Workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) コレクションを含んでいます。ワークシートは、[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスは、ワークシートを管理するためのさまざまなプロパティとメソッドを提供します。グリッド線の表示制御には、[**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isGridlinesVisible--) プロパティを使用します。[**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isGridlinesVisible--)はブール型のプロパティで、「true」または「false」の値のみを格納できます。  

#### **グリッド線を表示する**  

[**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isGridlinesVisible--)プロパティを**true**に設定してグリッド線を表示します。  

#### **グリッド線を非表示にする**  

[**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isGridlinesVisible--)プロパティを**false**に設定してグリッド線を非表示にします。  

以下に完全な例を示します。この例では、Excelファイル（book1.xls）を開き、最初のワークシートのグリッド線を非表示にし、変更後のファイルをoutput.xlsとして保存します。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Hide Gridlines Example</title>
    </head>
    <body>
        <h1>Hide Gridlines Example</h1>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object
            // Opening the Excel file through the file data
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Hiding the grid lines of the first worksheet of the Excel file
            worksheet.isGridlinesVisible = false;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Gridlines hidden successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

## **行列ヘッダーの表示および非表示**  

Excelファイルのすべてのワークシートは、行と列で配置されたセルから構成されています。すべての行と列には、それぞれユニークな値があり、行と列、また個々のセルを識別するために使用されます。たとえば、行には数字が付いています- 1、2、3、4など- そして列はアルファベット順に並んでいます- A、B、C、Dなど- 行と列の値はヘッダーに表示されます。Aspose.Cellsを使用すると、これらの行列ヘッダーの表示を制御することができます。  

### **ワークシートの表示を制御する**  

Aspose.Cellsは、Microsoft Excelファイルを表す [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスは、Excelファイル内の各ワークシートにアクセスできる [**Workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) コレクションを含んでいます。ワークシートは、[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスは、ワークシートを管理するためのさまざまなプロパティとメソッドを提供します。行と列の見出しの表示・非表示を制御するには、[**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isRowColumnHeadersVisible--) プロパティを使用します。[**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isRowColumnHeadersVisible--)はブール型のプロパティで、「true」または「false」の値のみを格納できます。  

#### **行/列ヘッダーを表示する**  

行と列の見出しを表示するには、[**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isRowColumnHeadersVisible--) プロパティを **true** に設定します。  

#### **行/列ヘッダーを非表示にする**  

行と列の見出しを非表示にするには、[**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isRowColumnHeadersVisible--) プロパティを **false** に設定します。  

以下に完全な例を示します。この例では、Excelファイル（book1.xls）を開き、最初のワークシートの行と列の見出しを非表示にし、変更後のファイルをoutput.xlsとして保存します。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Hide Row/Column Headers</title>
    </head>
    <body>
        <h1>Hide Row and Column Headers Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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

            // Instantiating a Workbook object with the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Hiding the headers of rows and columns
            worksheet.isRowColumnHeadersVisible = false;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Headers hidden successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

{{% alert color="primary" %}}  
[**Cells.unhideRows(number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#unhideRows-number-number-number-)と[**Cells.unhideColumns(number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#unhideColumns-number-number-number-)のメソッドを使用して複数の行と列を表示させることも可能です。  
{{% /alert %}}
