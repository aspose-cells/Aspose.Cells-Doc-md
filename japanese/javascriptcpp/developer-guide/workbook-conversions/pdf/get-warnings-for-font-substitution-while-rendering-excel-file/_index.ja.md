---
title: C++経由のAspose.Cells for JavaScriptを使ったExcelファイルのレンダリング時のフォント代替の警告を取得する
linktitle: Excelファイルをレンダリングする際にフォントの置換ワーニングを取得
type: docs
weight: 230
url: /ja/javascript-cpp/get-warnings-for-font-substitution-while-rendering-excel-file/
description: C++経由のAspose.Cells for JavaScriptを使用して、ExcelファイルをPDFにレンダリングする際にフォント代替に関する警告を取得する方法を学ぶ。
---

{{% alert color="primary" %}}  

Microsoft ExcelファイルをPDFにレンダリングする際、Aspose.Cellsはフォントを置換する場合があります。Aspose.Cellsには、特定のフォントが置換されたことを開発者に知らせる機能が備わっており、警告を表示することができます。これは、Aspose.Cellsがレンダリング結果が元のMicrosoft Excelファイルと異なって見える理由を特定し、適切な対策を取るための有用な機能です。たとえば、不足しているフォントをインストールして、レンダリング結果が同じに見えるようにできます。

{{% /alert %}}  

ExcelファイルをPDFにレンダリングする際のフォント置換警告を取得するには、IWarningCallbackインターフェースを実装し、PdfSaveOptions.warningCallbackプロパティに設定します。

以下のスクリーンショットは、次のコードで使用する元のExcelファイルを示しています。セルA6およびA7には、Microsoft Excelによって正しくレンダリングされないフォントでテキストが含まれています。

|**すべてのフォントが正しくレンダリングされているわけではありません**|  
| :- |  
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_1.png)|  
Aspose.Cellsは、セルA6とA7のフォントを適切なフォントで置き換えます。

|**置き換えフォント**|  
| :- |  
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_2.png)|  
## **ソースファイルと出力PDFのダウンロード**  
以下のリンクからソースExcelファイルと出力PDFをダウンロードできます

- [source.xlsx](5112611.xlsx)  
- [output.pdf](5112616.pdf)  
## **コード**  
以下のコードは、IWarningCallbackを実装し、PdfSaveOptions.warningCallbackプロパティに設定しています。これにより、セル内でフォントが置換された場合、Aspose.CellsはWarningCallback.Warning()メソッド内で警告を発します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - GetWarningsForFontSubstitution</title>
    </head>
    <body>
        <h1>GetWarningsForFontSubstitution Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions } = AsposeCells;

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

        class GetWarningsForFontSubstitution {
            static warning(info) {
                if (info.type === AsposeCells.WarningType.FontSubstitution) {
                    console.log("WARNING INFO: " + info.description);
                }
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Prepare PDF save options and assign warning callback
            const options = new PdfSaveOptions();
            options.warningCallback = GetWarningsForFontSubstitution;

            // Save workbook as PDF
            const outputData = workbook.save(SaveFormat.Pdf, options);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```  
## **出力**  
ExcelファイルをPDFに変換した後、警告は次のようにデバッグコンソールに出力されます。

{{< highlight java >}}  

 WARNING INFO: Font substitution: Font [ Athene Logos; Regular ] has been substituted in Cell [ A6 ] in Sheet [ Sheet1 ].  

WARNING INFO: Font substitution: Font [ B Traffic; Regular ] has been substituted in Cell [ A7 ] in Sheet [ Sheet1 ].  

{{< /highlight >}}  

{{% alert color="primary" %}}  

スプレッドシートに数式が含まれている場合、スプレッドシートをPDF形式にレンダリングする直前にWorkbook.calculateFormulaメソッドを呼び出すのがベストです。これにより、数式に依存する値が再計算され、正しい値がPDFに表示されます。

{{% /alert %}}
