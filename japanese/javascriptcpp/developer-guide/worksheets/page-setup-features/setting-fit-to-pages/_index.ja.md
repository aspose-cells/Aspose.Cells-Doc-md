---
title: JavaScriptとC++を使ってExcelを用紙幅と高さに合わせて印刷する方法
linktitle: Excelを縮小ページ幅と高さに印刷するにはどうすればよいですか
type: docs
weight: 200
url: /ja/javascript-cpp/how-to-print-excel-as-fitted-pages-wide-and-tall/
description: このコードは、C++経由のAspose.Cells for JavaScriptを使用して、FitToPagesWideとFitToPagesTallを設定する方法を示しています。
keywords: JavaScriptとC++を使ったFitToPagesWideとFitToPagesTallの設定方法、これらをExcelに追加する方法、クリアする方法、ページに合わせて印刷する方法、すべての列を一ページに印刷する方法
---

## **紹介**

 FitToPagesWideとFitToPagesTallの設定は、Microsoft Excelなどのスプレッドシートアプリケーションで、印刷時にスプレッドシートの縮尺を制御するために使用されます。これらの設定は、印刷結果が指定したページ数内に収まるように、横方向と縦方向の両方でスケーリングを行います。各設定の詳細は以下の通りです：

1. FitToPagesWide：この設定は、印刷出力が何ページの横幅に収まるべきかを指定します。たとえば、FitToPagesWideを1に設定すると、内容は1ページ幅に収まるように縮尺されます。
2. FitToPagesTall: この設定は、縦方向のページ数を指定します。例：FitToPagesTallを1に設定すると、内容は1ページの高さに収まるようにスケールされます。

## **FitToPagesWide と FitToPagesTall を使用する理由**
FitToPagesWideとFitToPagesTallを設定する理由は次の通りです：
1. 印刷レイアウトの制御：横と縦のページ数を指定することで、印刷された文書が見やすく整理された状態になるように保証できます。列や行がページ間で不自然に切れることも避けられます。
2. 一貫性: 複数のシートやレポートを印刷する場合、これらの設定を使用すると一貫したフォーマットを保て、比較や分析が容易になります。
3. 専門的なプレゼンテーション: 内容を適切にスケーリングして指定ページ数に収めることで、よりプロフェッショナルで洗練されたデータの提示が可能となります。

## **Excelでファイルを横長・縦長のフィットページとして印刷する方法**

Microsoft ExcelでFitToPagesWideとFitToPagesTallを設定するには、以下の手順に従います：

1. Excelワークブックを開き、印刷したいシートに移動します。
2. リボンのページレイアウトタブに移動します。
3. ページ設定グループの右下にある矢印をクリックし、ページ設定ダイアログボックスを開きます。
4. ページ設定ダイアログのページタブに進みます。
6. スケーリングの下で、「Fit to」を選択し、横と縦のページ数を指定します：最初のボックスに望むページの横数を入力します（Fit to x pages wide）。次のボックスに望むページの縦数を入力します（Fit to y pages tall）。
<br>
<img src="2.png" width=60% />

設定を適用するにはOKをクリックします。

## ** C++経由のAspose.Cells for JavaScriptを使用してExcelを用紙幅と高さに合わせて印刷する方法**

 指定したワークシートのFitToPagesWideとFitToPagesTallを設定するには、まず[サンプルファイル](input.xlsx)をロードし、その後、望ましいワークシートの [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/) オブジェクトの [**PageSetup.fitToPagesTall**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#fitToPagesTall--) と [**PageSetup.fitToPagesWide**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#fitToPagesWide--) プロパティを変更します。以下はJavaScriptの例です：

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Set Worksheet Fit To Pages and Save as PDF</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Setting the number of pages to which the length of the worksheet will be spanned
            worksheet.pageSetup.fitToPagesTall = 1;

            // Setting the number of pages to which the width of the worksheet will be spanned
            worksheet.pageSetup.fitToPagesWide = 1;

            // Saving the workbook as PDF
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_net.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

出力結果：
<br>
<img src="1.png" width=60% />

## **  ワークシートを1ページで印刷するには、C++経由のAspose.Cells for JavaScriptを使用して実行します。**

 ワークシートを1ページに印刷するには： まず、[サンプルファイル](sample.xlsx)をロードし、その後、[**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/)オブジェクトの[**PdfSaveOptions.onePagePerSheet**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#onePagePerSheet--)プロパティを設定します。JavaScriptの例は以下のとおりです：

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>One Page Per Sheet to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, Utils } = AsposeCells;

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

            // Loads the workbook which contains hidden external links
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const options = new PdfSaveOptions();
            options.onePagePerSheet = true;

            // Save the workbook to PDF format and provide download link
            const outputData = workbook.save(SaveFormat.Pdf, options);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'OnePagePerSheet.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

出力結果：
<br>
<img src="3.png" width=60% />

## **Aspose.Cells for JavaScriptを使用したC++での1ページにすべての列を印刷する方法**

ワークシートのすべての列を1ページに印刷するには、まず[サンプルファイル](sample.xlsx)を読み込み、次に[**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/)オブジェクトの[**PdfSaveOptions.allColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#allColumnsInOnePagePerSheet--)プロパティを設定します。JavaScriptの例は以下のとおりです：

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>All Columns In One Page Per Sheet Example</h1>
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

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create PdfSaveOptions and set allColumnsInOnePagePerSheet property
            const options = new AsposeCells.PdfSaveOptions();
            options.allColumnsInOnePagePerSheet = true;

            // Save the workbook to PDF format with the options
            const outputData = workbook.save(SaveFormat.Pdf, options);
            const blob = new Blob([outputData], { type: 'application/pdf' });

            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'AllColumnsInOnePagePerSheet.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

出力結果：
<br>
<img src="4.png" width=60% />
