---
title: C++経由のJavaScriptでブックをプレビュー
linktitle: ワークブックのプレビュー 
type: docs
weight: 70
url: /ja/javascript-cpp/workbook-and-worksheet-preview/
description: Aspose.Cellsは、Microsoft ExcelのインストールなしでExcelファイルを印刷およびプレビューできるようにJavaScript経由でサポートしています。
---

## **印刷プレビュー**  

数百ページのExcelファイルをPDFや画像に変換する必要がある場合があります。これらのファイルを処理すると、多大な時間とリソースを消費します。そんな時、ワークブックとワークシートの印刷プレビュー機能が役立ちます。変換前に総ページ数を確認し、変換の可否を判断できます。この記事では、[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/)と[**SheetPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/sheetprintingpreview/)クラスを使って総ページ数を調べる方法に焦点を当てます。  

Aspose.Cellsには印刷プレビュー機能があり、そのために[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/)と[**SheetPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/sheetprintingpreview/)クラスを提供します。全ワークブックの印刷プレビューを作成するには、[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/)クラスのインスタンスを作成し、[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook/)と[**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/)オブジェクトを引数に渡します。[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/)クラスには、このプレビューのページ数を返す[**evaluatedPageCount**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/#evaluatedPageCount--)メソッドがあります。[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/)クラスと同様に、[**SheetPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/sheetprintingpreview/)クラスは特定のワークシートの印刷プレビューを生成するために使われます。ワークシートのプレビューを作成するには、[**SheetPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/sheetprintingpreview/)クラスのインスタンスを作成し、[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet/)と[**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/)オブジェクトを渡します。[**SheetPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/sheetprintingpreview/)クラスも、生成されたプレビューのページ数を返す[**evaluatedPageCount**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/#evaluatedPageCount--)メソッドを提供します。  

次のコードスニペットは、[サンプルエクセルファイル](94896177.xlsx)を使った[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/)と[**SheetPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/sheetprintingpreview/)クラスの両方の使用例を示しています。  

### **サンプルコード**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Printing Preview</title>
    </head>
    <body>
        <h1>Printing Preview Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, WorkbookPrintingPreview, SheetPrintingPreview } = AsposeCells;

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

            // Creating image/print options
            const imgOptions = new ImageOrPrintOptions();

            // Workbook printing preview
            const preview = new WorkbookPrintingPreview(workbook, imgOptions);
            const workbookPageCount = preview.evaluatedPageCount;
            console.log("Workbook page count: " + workbookPageCount);

            // Worksheet printing preview for first worksheet
            const preview2 = new SheetPrintingPreview(workbook.worksheets.get(0), imgOptions);
            const worksheetPageCount = preview2.evaluatedPageCount;
            console.log("Worksheet page count: " + worksheetPageCount);

            document.getElementById('result').innerHTML = `<p>Workbook page count: ${workbookPageCount}</p><p>Worksheet page count: ${worksheetPageCount}</p>`;
        });
    </script>
</html>
```  

上記のコードを実行した結果生成された出力は次のとおりです。  

### **コンソール出力**  

{{< highlight javascript >}}  
Workbook page count: 1  
Worksheet page count: 1  
{{< /highlight >}}  

## **高度なトピック**  
- [スプレッドシートのレンダリング用フォントの設定](/cells/ja/javascript-cpp/configuring-fonts-for-rendering-spreadsheets/)  
- [ワークシートをイメージに変換 - データ周りの空白を削除](/cells/ja/javascript-cpp/convert-worksheet-to-image-remove-whitespace-around-data/)  
- [ワークシートを画像に変換し、ページごとに画像をワークシートに変換する](/cells/ja/javascript-cpp/converting-worksheet-to-image-and-worksheet-to-image-by-page/)  
- [ImageOrPrintオプションを使用してワークシートを画像に変換](/cells/ja/javascript-cpp/converting-worksheet-to-image-using-imageorprint-options/)  
- [ワークシートのセルの範囲をイメージにエクスポート](/cells/ja/javascript-cpp/export-range-of-cells-in-a-worksheet-to-image/)  
- [希望の幅と高さでワークシートまたはチャートを画像にエクスポート](/cells/ja/javascript-cpp/export-worksheet-or-chart-into-image-with-desired-width-and-height/)  
- [ImageOrPrintOptionsを使用してワークシートから画像を抽出](/cells/ja/javascript-cpp/extract-images-from-worksheets-using-imageorprintoptions/)  
- [ワークシートのサムネイルを生成](/cells/ja/javascript-cpp/generate-thumbnail-of-the-worksheet/)  
- [印刷するものがない場合、空白ページを出力](/cells/ja/javascript-cpp/output-blank-page-when-there-is-nothing-to-print/)  
- [ページ設定および印刷オプション](/cells/ja/javascript-cpp/page-setup-and-printing-options/)  
- [ImageOrPrintOptionsのPageIndexおよびPageCountプロパティを使用したページのシーケンスをレンダリングする](/cells/ja/javascript-cpp/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/)  
- [ワークシートをグラフィックコンテキストにレンダリング](/cells/ja/javascript-cpp/render-worksheet-to-graphic-context/)  
- [ワークブックのレンダリング用に個々またはプライベートなフォントセットを指定する](/cells/ja/javascript-cpp/specify-individual-or-private-set-of-fonts-for-workbook-rendering/)
