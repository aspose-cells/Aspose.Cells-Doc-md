---
title: Golang経由のC++でExcelファイルのレンダリング時にフォント代替の警告を取得する方法
linktitle: フォント置換に関する警告を取得
type: docs
weight: 230
url: /ja/go-cpp/get-warnings-for-font-substitution-while-rendering-excel-file/
description: Aspose.Cellsを使用してGolang経由のC++でExcelファイルをPDFにレンダリングするときのフォント代替に関する警告を取得する方法を学びます。
---

{{% alert color="primary" %}}

Microsoft ExcelファイルをPDFにレンダリングする際、Aspose.Cellsはフォントを置換する場合があります。Aspose.Cellsには、特定のフォントが置換されたことを開発者に知らせる機能が備わっており、警告を表示することができます。これは、Aspose.Cellsがレンダリング結果が元のMicrosoft Excelファイルと異なって見える理由を特定し、適切な対策を取るための有用な機能です。たとえば、不足しているフォントをインストールして、レンダリング結果が同じに見えるようにできます。

{{% /alert %}}

ExcelファイルをPDFにレンダリングする際のフォント置換警告を取得するには、`IWarningCallback`インターフェースを実装し、`PdfSaveOptions.WarningCallback`プロパティにあなたの実装したインターフェースを設定します。

以下のスクリーンショットは、次のコードで使用する元のExcelファイルを示しています。セルA6およびA7には、Microsoft Excelによって正しくレンダリングされないフォントでテキストが含まれています。

|**すべてのフォントが正しくレンダリングされているわけではありません**|
| :- |
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_1.png)|

Aspose.Cellsは、セルA6とA7のフォントを適切なフォントで置き換えます。

|**置き換えフォント**|
| :- |
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_2.png)|

## **ソースファイルと出力PDFのダウンロード**
以下のリンクからソースExcelファイルと出力されるPDFをダウンロードできます：

- [source.xlsx](5112611.xlsx)
- [output.pdf](5112616.pdf)

## **コード**
以下のコードは、`IWarningCallback`を実装し、`PdfSaveOptions.WarningCallback`にインターフェースを設定する方法を示しています。これにより、セル内のフォントが置換されるたびにAspose.Cellsが`WarningCallback.Warning()`メソッド内で警告を発信します。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetWarningsForFontSubstitutionWhileRenderingExcelFile.go" >}}
## **出力**
ExcelファイルをPDFに変換した後、警告は次のようにデバッグコンソールに出力されます。

{{< highlight java >}}
WARNING INFO: Font substitution: Font [ Athene Logos; Regular ] has been substituted in Cell [ A6 ] in Sheet [ Sheet1 ].
WARNING INFO: Font substitution: Font [ B Traffic; Regular ] has been substituted in Cell [ A7 ] in Sheet [ Sheet1 ].
{{< /highlight >}}

{{% alert color="primary" %}}

スプレッドシートに数式が含まれている場合、`Workbook.CalculateFormula`メソッドを呼び出して、スプレッドシートをPDFに変換する直前に数式依存値を再計算し、正しい値をレンダリングさせることが最良です。

{{% /alert %}}
