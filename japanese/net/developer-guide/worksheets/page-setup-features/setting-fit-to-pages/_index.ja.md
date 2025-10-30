---
title: Excelを縮小ページ幅と高さに印刷するにはどうすればよいですか
type: docs
weight: 200
url: /ja/net/how-to-print-excel-as-fitted-pages-wide-and-tall/
description: この記事では、Aspose.Cellsライブラリを使用して【FitToPagesWide】と【FitToPagesTall】を設定する方法についてのコード例を示しています。
keywords: C#：FitToPagesWideとFitToPagesTallの設定方法、C#における追加方法、Excelでの設定方法、Excelでのクリア方法、広く高く印刷、ワークシートを1ページに印刷、すべての列を1ページに印刷する方法。
---

## **紹介**

 FitToPagesWideとFitToPagesTallの設定は、Microsoft Excelなどのスプレッドシートアプリケーションで、印刷時にスプレッドシートの縮尺を制御するために使用されます。これらの設定は、印刷結果が指定したページ数内に収まるように、横方向と縦方向の両方でスケーリングを行います。各設定の詳細は以下の通りです：

1. FitToPagesWide：この設定は、印刷出力が何ページの横幅に収まるべきかを指定します。たとえば、FitToPagesWideを1に設定すると、内容は1ページ幅に収まるように縮尺されます。
1. FitToPagesTall：この設定は、印刷出力が何ページの高さに収まるべきかを指定します。たとえば、FitToPagesTallを1に設定すると、内容は1ページの高さに収まるように縮尺されます。

## **FitToPagesWide と FitToPagesTall を使用する理由**
FitToPagesWideとFitToPagesTallを設定する理由は次の通りです：
1. 印刷レイアウトの制御：横と縦のページ数を指定することで、印刷された文書が見やすく整理された状態になるように保証できます。列や行がページ間で不自然に切れることも避けられます。
1. 一貫性：複数のシートやレポートを印刷する場合、これらの設定を使用すると一貫したフォーマットを維持でき、印刷されたドキュメントの比較や分析が容易になります。
1. プロフェッショナルなプレゼンテーション：内容を適切に縮尺してページ数に合わせることで、より洗練されたプレゼンテーションに仕上げることができます。

## **Excelでファイルを横長・縦長のフィットページとして印刷する方法**

Microsoft ExcelでFitToPagesWideとFitToPagesTallを設定するには、以下の手順に従います：

1. Excelワークブックを開き、印刷したいシートに移動します。
1. リボンのページレイアウトタブに移動します。
1. ページセットアップグループ内の、右下の小さな矢印をクリックしてページ設定ダイアログボックスを開きます。
1. ページ設定ダイアログの「ページ」タブに切り替えます。
1. スケーリングの下にある「次のページに合わせる」を選択し、必要なページ幅と高さを指定します：最初のボックスにページ幅を入力します（Fit to xページの幅）、2番目のボックスにページの高さを入力します（Fit to yページの高さ）。
<br>
<img src="2.png" width=60% />

1. 設定を適用するにはOKをクリックします。


## **Aspose.Cells を使用して Excel を横長・縦長フィットページとして印刷する方法**

指定したシートでFitToPagesWideとFitToPagesTallを設定するには、まず[サンプルファイル](input.xlsx)を読み込み、その後望ましいシートの[**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/)オブジェクトの[**Worksheet.PageSetup.FitToPagesTall**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/fittopagestall/)と[**Worksheet.PageSetup.FitToPagesWide**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/fittopageswide/)のプロパティを変更します。例としてC#のコードは次の通りです：

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-PageSetup-set-FitToPagesWide-FitToPagesTall.cs" >}}

出力結果：
<br>
<img src="1.png" width=60% />


## **Aspose.Cellsを使用したワークシートを1ページとして印刷する方法**

ワークシートを一ページに印刷するには、まず[サンプルファイル](sample.xlsx)を読み込み、その後[**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/)オブジェクトの[**PdfSaveOptions.OnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/onepagepersheet/)プロパティを設定します。C#の例は次の通りです：

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-PageSetup-OnePagePerSheet.cs" >}}

出力結果：
<br>
<img src="3.png" width=60% />


## **Aspose.Cellsを使用してワークシートのすべての列を1ページに印刷する方法**

ワークシートのすべての列を一ページに印刷するには、まず[サンプルファイル](sample.xlsx)を読み込み、その後[**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/)オブジェクトの[**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/allcolumnsinonepagepersheet/)プロパティを設定します。C#の例は次の通りです：

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-PageSetup-AllColumnsInOnePagePerSheet.cs" >}}

出力結果：
<br>
<img src="4.png" width=60% />
{{< app/cells/assistant language="csharp" >}}
