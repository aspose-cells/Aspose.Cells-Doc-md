---
title: JavaScriptとC++を使用したPDF
linktitle: Pdf
type: docs
weight: 220
url: /ja/javascript-cpp/convert-excel-to-pdf/
description: ExcelワークブックをPDFに変換する方法をAspose.Cells for JavaScript via C++で学びましょう。 
---

{{% alert color="primary" %}}
Aspose.CellsはExcelワークブックをPDFに変換することをサポートしています。この例では、Excelワークブックを完全にPDFに変換する方法を示します。
{{% /alert %}}

## **ExcelワークブックをPDFに変換する**

PDFファイルは、組織、政府部門、個人間で文書を交換するために広く使用されています。これは標準のドキュメント形式であり、ソフトウェア開発者はしばしばMicrosoft ExcelファイルをPDFドキュメントに変換する方法を見つけるよう求められます。

Aspose.Cellsは、ExcelファイルをPDFに変換する機能をサポートし、変換時に高い視覚的忠実度を維持します。

{{% alert color="primary" %}}
Aspose.Cells for JavaScript via C++は、APIとバージョン番号に関する情報を出力ドキュメントに直接書き込みます。例えば、ドキュメントをPDFにレンダリングする際、Aspose.Cells for JavaScript via C++は「PDFプロデューサー」フィールドに値を設定します（例：’Aspose.Cells v23.2’）。

出力ドキュメントでこの情報を変更することができることに注意してください。
{{% /alert %}}

### **直接変換**

Aspose.Cells for JavaScript via C++は、他のソフトウェアに依存せずにスプレッドシートからPDFへの変換をサポートしています。[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスの[**save(string, SaveFormat)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveformat-)メソッドを使ってExcelファイルをPDFとして保存するだけです。[**save(string, SaveFormat)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveformat-)メソッドは、ネイティブExcelファイルをPDFに変換する[**SaveFormat.Pdf**](https://reference.aspose.com/cells/javascript-cpp/saveformat)列挙型メンバーを提供します。

以下の手順に従って、Excelスプレッドシートを直接PDF形式に変換します:

1. 空のコンストラクタを呼び出して[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスのオブジェクトをインスタンス化します。
1. 既存のテンプレートファイルを開いたり読み込んだりするか、ワークブックをゼロから作成している場合は、この手順をスキップします。
1. Aspose.CellsのAPIを使用して、スプレッドシート上で作業を行います（入力データ、書式設定の適用、数式の設定、画像の挿入など）。
1. スプレッドシートコードが完了したら、[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスの[**save(string, SaveFormat)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveformat-)メソッドを呼び出して、スプレッドシートを保存します。

ファイル形式はPDFである必要がありますので、[**SaveFormat**](https://reference.aspose.com/cells/javascript-cpp/saveformat)列挙型から*Pdf*（事前に定義された値）を選択して最終的なPDFドキュメントを生成します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Excel to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF</button>
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

            // Instantiate the Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save the document in PDF format
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion to PDF completed! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

### **高度な変換**

異なる属性を設定するために[**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions)クラスを使用したり、出力PDFの印刷、フォント、セキュリティ、圧縮設定を制御するために[**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions)クラスの異なるプロパティを設定することもできます。 

[**PdfSaveOptions.compliance**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#compliance--)は最も重要なプロパティで、PDFの標準遵守レベルを設定できます。現在はPDF 1.4、PDF 1.5、PDF 1.6、PDF 1.7、PDF/A-1a、PDF/A-1b、PDF/A-2a、PDF/A-2b、PDF/A-2u、PDF/A-3a、PDF/A-2ab、PDF/A-3u形式に保存できます。PDF/A形式では、出力ファイルのサイズが通常のPDFファイルよりも大きくなります。

#### **PDF/A準拠ファイルへのワークブックの保存**

以下のコードスニペットは、[**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions) クラスを使用してExcelファイルをPDF/A準拠のPDF形式に保存する方法を示しています。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Create PDF/A from Workbook</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;"></a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, PdfCompliance } = AsposeCells;

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
            // Instantiate new workbook
            const workbook = new Workbook();

            // Insert a value into the A1 cell in the first worksheet
            workbook.worksheets.get(0).cells.get(0, 0).value = "Testing PDF/A";

            // Define PdfSaveOptions
            const pdfSaveOptions = new PdfSaveOptions();

            // Set the compliance type
            pdfSaveOptions.compliance = PdfCompliance.PdfA1b;

            // Save the file to PDF with options
            const outputData = workbook.save(SaveFormat.Pdf, pdfSaveOptions);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF/A File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF/A created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}
ご注意：[**PdfSaveOptions.compliance**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#compliance--)プロパティは、Aspose.Cells for JavaScript via C++ 5.3.0のリリースとともに追加されました。
{{% /alert %}}

#### **PDF作成時間の設定**

[**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions) クラスを使用すると、PDF作成時刻を取得または設定することができます。次のコードは、[**PdfSaveOptions.createdTime**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#createdTime--) プロパティを使用してPDFファイルの作成時刻を設定する方法を示しています。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Excel to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, PdfSaveOptions, SaveFormat, Utils } = AsposeCells;

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

            // Create an instance of PdfSaveOptions
            const options = new PdfSaveOptions();
            options.createdTime = new Date();

            // Save the workbook to PDF format while passing the object of PdfSaveOptions
            const outputData = workbook.save(SaveFormat.Pdf, options);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

#### **ContentCopyForAccessibilityオプションの設定**

[**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions) クラスを使用すると、変換されたPDFのコンテンツアクセスを制御するためのPDF [**PdfSecurityOptions.accessibilityExtractContent**](https://reference.aspose.com/cells/javascript-cpp/pdfsecurityoptions/#accessibilityExtractContent--) オプションを取得または設定できます。

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Aspose.Cells Example - Convert to PDF with Security Options</title>
    </head>
    <body>
        <h1>Convert Excel to PDF with Security Options</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF</button>
        <a id="downloadLink" style="display: none;"></a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, PdfSecurityOptions, Utils } = AsposeCells;

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

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create an instance of PdfSaveOptions
            const pdfSaveOpt = new PdfSaveOptions();

            // Create an instance of PdfSecurityOptions
            const securityOptions = new PdfSecurityOptions();

            // Set AccessibilityExtractContent to false (converted from setAccessibilityExtractContent(false))
            securityOptions.accessibilityExtractContent = false;

            // Set the security option in the PdfSaveOptions (converted from setSecurityOptions)
            pdfSaveOpt.securityOptions = securityOptions;

            // Save the workbook to PDF format while passing the PdfSaveOptions
            const outputData = workbook.save(SaveFormat.Pdf, pdfSaveOpt);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outFile.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

#### **PDFへのカスタムプロパティのエクスポート**

[**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions) クラスを使用すると、元のワークブック内のカスタムプロパティをPDFにエクスポートすることができます。プロパティのエクスポート方法を指定するために [**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/javascript-cpp/pdfcustompropertiesexport/) 列挙型が提供されています。これらのプロパティは、次の画像に示すように、Adobe Acrobat Readerで[ファイル]をクリックして[プロパティ]オプションをクリックすることで観察することができます。テンプレートファイル "sourceWithCustProps.xlsx" は[こちら](sourceWithCustProps.xlsx)からダウンロードでき、解析用の出力PDFファイル "outSourceWithCustProps" は[こちら](outSourceWithCustProps.pdf)で利用できます。

![todo:image_alt_text](convert-excel-workbook-to-pdf_1.png)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Excel to PDF with Custom Properties</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, PdfCustomPropertiesExport } = AsposeCells;

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

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create an instance of PdfSaveOptions
            const pdfSaveOptions = new PdfSaveOptions();

            // Set CustomPropertiesExport property to PdfCustomPropertiesExport.Standard
            pdfSaveOptions.customPropertiesExport = PdfCustomPropertiesExport.Standard;

            // Save the workbook to PDF format while passing the object of PdfSaveOptions
            const outputData = workbook.save(SaveFormat.Pdf, pdfSaveOptions);

            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outSourceWithCustProps.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

### **変換属性**

新しいリリースごとに変換機能を強化しています。Aspose.CellのExcelからPDFへの変換にはまだいくつかの制限があります。MapChartはPDF形式への変換時にサポートされていません。また、一部の図形オブジェクトには十分なサポートがありません。

以下の表は、Aspose.Cellsを使用してPDFにエクスポートする際に完全または部分的にサポートされているすべての機能をリストしています。この表は最終的なものではなく、すべてのスプレッドシート属性を網羅していませんが、PDFへの変換にはサポートされていないまたは部分的にサポートされている機能を特定しています。

|**ドキュメント要素**|**属性**|**サポート**|**注釈**|
| :- | :- | :- | :- |
|配置| |はい| |
|背景設定| |はい| |
|ボーダー|色|はい| |
|ボーダー|線のスタイル|はい| |
|ボーダー|線の幅|はい| |
|セルデータ| |はい| |
|コメント| |はい| |
|条件付き書式| |はい| |
|ドキュメントプロパティ| |はい| |
|図形オブジェクト| |部分的|図形オブジェクトの影や3D効果には十分なサポートがありません。WordArtとSmartArtは部分的にサポートされています。|
|フォント|サイズ|はい| |
|フォント|色|はい| |
|フォント|スタイル|はい| |
|フォント|下線|はい| |
|フォント|効果|はい||
|画像| |はい| |
|ハイパーリンク| |はい| |
|チャート|  |部分的に| MapChartはサポートされていません。|
|セルの結合|  |はい|  |
|改ページ|  |はい|  |
|ページ設定|ヘッダー/フッター|はい|  |
|ページ設定|余白|はい|  |
|ページ設定|ページの向き|はい|  |
|ページ設定|ページサイズ|はい|  |
|ページ設定|印刷範囲|はい|  |
|ページ設定|印刷タイトル|はい|  |
|ページ設定|拡大/縮小|はい|  |
|行の高さ/列の幅|  |はい|  |
|右から左への言語|  |はい|  |

{{% alert color="primary" %}}
スプレッドシートに数式が含まれている場合、PDF形式に変換する直前に [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) を呼び出すことが最善です。これにより、数式に依存する値が再計算され、PDFで正しい値がレンダリングされます。
{{% /alert %}}

## **高度なトピック**
- [名前付き目次でPDFブックマークを追加する](/cells/ja/javascript-cpp/add-pdf-bookmarks-with-named-destinations/)
- [出力PDFの空白ページを回避する](/cells/ja/javascript-cpp/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/)
- [PDFへの変換時に特定のUnicode文字のフォントを変更する](/cells/ja/javascript-cpp/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/)
- [XLSXファイルをPDF形式に変換](/cells/ja/javascript-cpp/convert-xlsx-file-to-pdf-format/)
- [PDFA-1aに準拠したExcelファイルをPDF形式に変換する](/cells/ja/javascript-cpp/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [画像やチャートを含むXLSファイルをPDFに変換](/cells/ja/javascript-cpp/convert-xls-file-with-images-or-charts-to-pdf/)
- [チャートシートの PdfBookmarkEntry を作成](/cells/ja/javascript-cpp/create-pdfbookmarkentry-for-chart-sheet/)
- [1つのPDFページでワークシートのすべての列を表示する](/cells/ja/javascript-cpp/fit-all-worksheet-columns-on-single-pdf-page/)
- [DrawObjectEventHandlerクラスを使用してPDFへのレンダリング中にDrawObjectとバインドを取得](/cells/ja/javascript-cpp/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/)
- [Excelファイルを変換する際のフォントの置換に関する警告を取得](/cells/ja/javascript-cpp/get-warnings-for-font-substitution-while-rendering-excel-file/)
- [Excel を PDF にレンダリングする際のエラーを無視](/cells/ja/javascript-cpp/ignore-errors-while-rendering-excel-to-pdf/)
- [生成されるページ数を制限する - ExcelからPDFへの変換](/cells/ja/javascript-cpp/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [PDFへ保存する際にコメントを印刷する](/cells/ja/javascript-cpp/print-comments-while-saving-to-pdf/)
- [ExcelをPDFに変換する際のOffice Add-Insのレンダリング](/cells/ja/javascript-cpp/render-office-add-ins-while-converting-excel-to-pdf/)
- [Excelのワークシートごとに1つのPDFページをレンダリング - ExcelからPDFへの変換](/cells/ja/javascript-cpp/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [Aspose.Cellsによる出力PDFでUnicode補助文字をレンダリングする](/cells/ja/javascript-cpp/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [追加された画像のリサンプリング - ExcelからPDFへの変換](/cells/ja/javascript-cpp/resampling-added-images-excel-to-pdf-conversion/)
- [異なるPDFファイルごとに各ワークシートを保存](/cells/ja/javascript-cpp/save-each-worksheet-to-a-different-pdf-file/)
- [標準または最小サイズでExcelをPDFに保存](/cells/ja/javascript-cpp/save-excel-into-pdf-with-standard-or-minimum-size/)
- [指定されたワークシートをPDFに保存](/cells/ja/javascript-cpp/save-specified-worksheets-to-pdf/)
- [PDFドキュメントをセキュアにする](/cells/ja/javascript-cpp/secure-pdf-documents/)
- [出力PDFおよび画像内の文字列の交差方法を指定](/cells/ja/javascript-cpp/specify-how-to-cross-string-in-output-pdf-and-image/)
