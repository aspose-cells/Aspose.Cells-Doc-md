---
title: Excel ファイルのレンダリング中にフォントの置換に関する警告を受け取る
type: docs
weight: 230
url: /ja/net/get-warnings-for-font-substitution-while-rendering-excel-file/
---
{{% alert color="primary" %}} 

Microsoft の Excel ファイルを PDF にレンダリングすると、Aspose.Cells がフォントに置き換わる場合があります。 Aspose.Cells は、警告を発することによって、特定のフォントが置き換えられたことを開発者に知らせる機能を提供します。これは、Aspose.Cells でレンダリングされた PDF が元の Microsoft Excel ファイルと異なって見える理由を特定して、適切なアクションを実行できるようにするのに役立つ便利な機能です。たとえば、不足しているフォントをインストールして、レンダリング結果が同じに見えるようにします。

{{% /alert %}} 

Excel ファイルを PDF にレンダリングするときにフォントの置換に関する警告を受け取るには、IWarningCallback インターフェイスを実装し、実装したインターフェイスで PdfSaveOptions.WarningCallback プロパティを設定します。

以下のスクリーンショットは、次のコードで使用するソース Excel ファイルを示しています。セル A6 と A7 に、Microsoft Excel でうまく表示されないフォントのテキストがあります。

|**すべてのフォントが正しくレンダリングされるわけではありません**|
|:- |
|![todo:画像_代替_文章](get-warnings-for-font-substitution-while-rendering-excel-file_1.png)|
Aspose.Cells は、以下に示すように、セル A6 および A7 のフォントを適切なフォントに置き換えます。

|**代替フォント**|
|:- |
|![todo:画像_代替_文章](get-warnings-for-font-substitution-while-rendering-excel-file_2.png)|
## **ソースファイルをダウンロードして PDF を出力**
ソースの Excel ファイルと出力の PDF は、次のリンクからダウンロードできます。

- [ソース.xlsx](5112611.xlsx)
- [output.pdf](5112616.pdf)
## **コード**
次のコードは、IWarningCallback を実装し、実装されたインターフェイスで PdfSaveOptions.WarningCallback プロパティを設定します。これで、任意のセルで任意のフォントが置換されるたびに、Aspose.Cells が WarningCallback.Warning() メソッド内で警告を発します。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetWarningsForFontSubstitution-1.cs" >}}
## **出力**
ソース Excel ファイルを PDF に変換した後、警告は次のようにデバッグ コンソールに出力されます。

{{< highlight "java" >}}

 WARNING INFO: Font substitution: Font [ Athene Logos; Regular ]has been substituted in Cell [ A6 ]in Sheet [ Sheet1 ].

WARNING INFO: Font substitution: Font [ B Traffic; Regular ]has been substituted in Cell [ A7 ]in Sheet [ Sheet1 ].

{{< /highlight >}}

{{% alert color="primary" %}} 

スプレッドシートに数式が含まれている場合は、スプレッドシートを PDF 形式にレンダリングする直前に Workbook.CalculateFormula メソッドを呼び出すことをお勧めします。そうすることで、数式に依存する値が再計算され、正しい値が PDF に表示されます。

{{% /alert %}}
