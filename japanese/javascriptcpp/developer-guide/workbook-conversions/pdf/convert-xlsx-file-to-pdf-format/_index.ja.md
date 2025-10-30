---
title: XLSXファイルをJavaScript（C++経由）でPDFフォーマットに変換します
linktitle: XLSX ファイルを PDF フォーマットに変換する
type: docs
weight: 30
url: /ja/javascript-cpp/convert-xlsx-file-to-pdf-format/
description: Excelファイル（XLSX）をPDFフォーマットに変換する方法について説明します（C++のAspose.Cells for JavaScript使用） 
---

{{% alert color="primary" %}}

PDF（Portable Document Format）は、ドキュメントの作成に使用されるソフトウェア、ハードウェア、およびオペレーティングシステムに依存せずにドキュメントを表現するフォーマットです。PDF ファイルには、テキスト、グラフィックス、画像の任意の組み合わせをデバイスに依存せず、解像度に依存しない方法で表現することができます。PDF ファイルはしばしば圧縮されるため、元のファイルよりも少ないスペースを占めます。

Microsoft ExcelファイルをPDFに変換したい場合、信頼性が高く正確で安全なソリューションが必要です。これにより、世界中にPDFドキュメントを配布できます。多くの変換ツールがありますが、元のExcelドキュメントのレイアウトを正確に保持し、画像、チャート、シェイプ、フォーマット、フォント、属性、色、ページ設定、テキストの向き、 Borders、チャートなどを正確にレンダリングする必要があります。[Aspose.Cells](https://products.aspose.com/cells/javascript-cpp/)は高忠実度の変換を保証します。

このドキュメントは、画像、チャート、フォーマットなどを含むMicrosoft ExcelドキュメントをPDFに変換する方法についての包括的な理解を提供します。そのために、Aspose.Cells APIを使ってExcelファイルをPDFに変換するJavaScript（C++経由）の簡単なコンソールアプリケーションを作成する方法を示します。この変換は高い精度と正確性をもって行われます。

{{% /alert %}}

## **ExcelをPDFに変換する**

この例では、テンプレートとしてExcelファイル（SampleInput.xlsx）を使用しています。ワークブックにはチャートと画像が含まれたシートがあります。各シートにはフォント、属性、色、シェーディング効果、境界線を使用したさまざまな書式があります。最初のシートには縦列チャート、最後には画像があります。

### **テンプレートの Excel ファイル**

テンプレートファイルには、チャートやメディアとしての画像を含む3つのワークシートがあります。最初のワークシートにはチャートがあり、最後のワークシートには画像があります（以下のスクリーンショット参照）。

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet2.png)|
| :- | :- |
|最初のワークシート**(売上予測)**|2番目のワークシート**(売上報告)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet4.png)|
|3番目のワークシート**(データ入力)**|最後のワークシート**(画像)**|

### **変換プロセス**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Excel to PDF</title>
    </head>
    <body>
        <h1>Excel to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF</button>
        <a id="downloadLink" style="display: none;"></a>
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

            // Instantiating a Workbook object with the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Saving the PDF file
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output.out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

スプレッドシートに数式が含まれている場合、[Workbook.calculateFormula()](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--)メソッドを、PDFに変換する直前に呼び出すのが最適です。これにより、数式依存の値が再計算され、正しい値がPDFに反映されます。

{{% /alert %}}

### **結果**

上記のコードを実行すると、アプリケーションディレクトリのFilesフォルダにPDFファイルが作成されます。
以下のスクリーンショットは、PDFページを示しています。ヘッダーとフッターも出力されたPDFファイルに保持されていることに注意してください。

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted2.png)|
| :- | :- |
|最初のワークシート**(売上予測)**|2番目のワークシート**(売上報告)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted4.png)|
|3番目のワークシート**(データ入力)**|最後のワークシート**(画像)**|
