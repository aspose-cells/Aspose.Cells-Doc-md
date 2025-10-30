---
title: JavaScriptをC++経由で使用したページ設定と印刷オプション
linktitle: ページ設定および印刷オプション
type: docs
weight: 60
url: /ja/javascript-cpp/page-setup-and-printing-options/
---

{{% alert color="primary" %}}  
開発者は、印刷プロセスを制御するためにページ設定と印刷設定を構成する必要があります。Aspose.Cellsではページ設定と印刷設定を制御するためのさまざまなオプションがサポートされています。  

この記事では、C++経由のJavaScriptを使用してコンソールアプリケーションを作成し、Aspose.Cells APIを使ってページ設定と印刷オプションをワークシートに適用する方法をわかりやすく説明します。  
{{% /alert %}}  

## **ページ設定および印刷設定の操作**  

この例では、Microsoft Excelでワークブックを作成し、Aspose.Cellsを使用してページ設定と印刷オプションを設定しました。  

### **Aspose.Cellsを使用してページ設定オプションを設定する**  

まず、Microsoft Excelで簡単なワークシートを作成します。次に、ページ設定オプションを適用します。コードを実行すると、以下のスクリーンショットのようにページ設定オプションが変更されます。  

|**出力ファイル。**|  
| :- |  
|![todo:image_alt_text](page-setup-and-printing-options_1.png)|  

1. Microsoft Excelのワークシートにいくつかのデータを作成します。  
   1. Microsoft Excelで新しいブックを開きます。  
   1. いくつかのデータを追加します。  
1. ページ設定オプションを設定します。  
   ファイルにページ設定オプションを適用します。以下は、新しいオプションが適用される前のデフォルトオプションのスクリーンショットです。  

|**デフォルトのページ設定オプション。**|  
| :- |  
|![todo:image_alt_text](page-setup-and-printing-options_2.png)|  

1. Aspose.Cellsをダウンロードしてインストールします。  
   1. [ダウンロード](https://downloads.aspose.com/cells/javascript-cpp) Aspose.Cells for JavaScriptをC++で入手してください。  
   1. 開発コンピュータにインストールします。  
      すべてのAsposeのコンポーネントは、インストールされると評価モードで動作します。評価モードには時間制限はなく、生成された文書にウォーターマークを注入するだけです。  
1. プロジェクトを作成します。  
   1. JavaScript環境を開始します。  
   1. 新しいコンソールアプリケーションを作成します。  
      この例ではJavaScriptコンソールアプリケーションを示しますが、C++のバインディングも使用できます。  
1. 参照を追加します。  
   1. この例ではAspose.Cellsを使用するため、プロジェクトにそのコンポーネントへの参照を追加します。例：  
      …\Program Files\Aspose\Aspose.Cells\Bin\JavaScript-Cpp\Aspose.Cells.node  
1. APIを呼び出すアプリケーションを記述します。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Page Setup Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PageOrientationType, PaperSizeType } = AsposeCells;

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

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Access page setup as a property
            const pageSetup = worksheet.pageSetup;

            // Setting the orientation to Portrait
            pageSetup.orientation = PageOrientationType.Portrait;

            // Setting the number of pages to which the length of the worksheet will be spanned
            pageSetup.fitToPagesTall = 1;

            // Setting the number of pages to which the width of the worksheet will be spanned
            pageSetup.fitToPagesWide = 1;

            // Setting the paper size to A4
            pageSetup.paperSize = PaperSizeType.PaperA4;

            // Setting the print quality of the worksheet to 1200 dpi
            pageSetup.printQuality = 1200;

            // Setting the first page number of the worksheet pages
            pageSetup.firstPageNumber = 2;

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'PageSetup_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Page setup modified successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

### **印刷オプションの設定**  

ページ設定設定には、ワークシートページの印刷方法を制御するいくつかの印刷オプション（シートオプションとも呼ばれる）も提供されます。これにより、ユーザーは次のような操作ができます。  

- ワークシートの特定の印刷エリアを選択します。
- タイトルを印刷する。
- グリッド線を印刷する。
- 行/列見出しを印刷します。
- 下書き品質を実現する。
- コメントを印刷する。
- セルエラーを印刷する。
- ページ順序を定義する。  

次の例では、上記の例（PageSetup.xls）で作成されたファイルに印刷オプションを適用します。以下のスクリーンショットは、新しいオプションが適用される前のデフォルトの印刷オプションを示しています。  

|**入力ドキュメント**|  
| :- |  
|![todo:image_alt_text](page-setup-and-printing-options_3.png)|  
コードを実行すると、印刷オプションが変更されます。  

|**出力ファイル**|  
| :- |  
|![todo:image_alt_text](page-setup-and-printing-options_4.png)|  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Page Setup Example</title>
    </head>
    <body>
        <h1>Page Setup Example</h1>
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

            // Open the workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            const pageSetup = worksheet.pageSetup;

            // Specifying the cells range (from A1 cell to E30 cell) of the print area
            pageSetup.printArea = "A1:E30";

            // Defining column numbers A & E as title columns
            pageSetup.printTitleColumns = "$A:$E";

            // Defining row numbers 1 as title rows
            pageSetup.printTitleRows = "$1:$2";

            // Allowing to print gridlines
            pageSetup.printGridlines = true;

            // Allowing to print row/column headings
            pageSetup.printHeadings = true;

            // Allowing to print worksheet in black & white mode
            pageSetup.blackAndWhite = true;

            // Allowing to print comments as displayed on worksheet
            pageSetup.printComments = AsposeCells.PrintCommentsType.PrintInPlace;

            // Allowing to print worksheet with draft quality
            pageSetup.printDraft = true;

            // Allowing to print cell errors as N/A
            pageSetup.printErrors = AsposeCells.PrintErrorsType.PrintErrorsNA;

            // Setting the printing order of the pages to over then down
            pageSetup.order = AsposeCells.PrintOrderType.OverThenDown;

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'PageSetup_Print_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Page setup applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
