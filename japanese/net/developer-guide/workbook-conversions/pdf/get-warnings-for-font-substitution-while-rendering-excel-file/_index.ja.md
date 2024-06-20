---
title: Excelファイルをレンダリングする際にフォントの置換ワーニングを取得
type: docs
weight: 230
url: /ja/net/get-warnings-for-font-substitution-while-rendering-excel-file/
---

{{% alert color="primary" %}} 

Microsoft ExcelファイルをPDFにレンダリングする際、Aspose.Cellsはフォントを置換する場合があります。Aspose.Cellsには、特定のフォントが置換されたことを開発者に知らせる機能が備わっており、警告を表示することができます。これは、Aspose.Cellsがレンダリング結果が元のMicrosoft Excelファイルと異なって見える理由を特定し、適切な対策を取るための有用な機能です。たとえば、不足しているフォントをインストールして、レンダリング結果が同じに見えるようにできます。

{{% /alert %}} 

ExcelファイルをPDFにレンダリングする際、フォントの置き換えに関する警告を受け取るには、IWarningCallbackインターフェースを実装し、PdfSaveOptions.WarningCallbackプロパティを実装したインターフェースに設定します。

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
次のコードは、IWarningCallbackを実装し、PdfSaveOptions.WarningCallbackプロパティを実装したインターフェースに設定します。これにより、Aspose.Cellsが任意のセルでフォントが置き換えられるたびに、Aspose.CellsはWarningCallback.Warning()メソッド内で警告を発生させます。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetWarningsForFontSubstitution-1.cs" >}}
## **出力**
ExcelファイルをPDFに変換した後、警告は次のようにデバッグコンソールに出力されます。

{{< highlight java >}}

 WARNING INFO: Font substitution: Font [ Athene Logos; Regular ] has been substituted in Cell [ A6 ] in Sheet [ Sheet1 ].

WARNING INFO: Font substitution: Font [ B Traffic; Regular ] has been substituted in Cell [ A7 ] in Sheet [ Sheet1 ].

{{< /highlight >}}

{{% alert color="primary" %}} 

スプレッドシートに数式が含まれている場合、スプレッドシートをPDF形式にレンダリングする直前にWorkbook.CalculateFormulaメソッドを呼び出すことが最善です。これにより、数式に依存した値が再計算され、正しい値がPDFに表示されます。

{{% /alert %}}
