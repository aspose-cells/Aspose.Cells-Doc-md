---
title: 改ページの管理
type: docs
weight: 30
url: /ja/cpp/managing-page-breaks/
---
{{% alert color="primary" %}} 

定義によれば、改ページはテキストの流れの中で、あるページが終了して次のページが始まる場所です。 Microsoft Excel では、ワークシートの選択したセルに改ページを追加できます。

印刷中に改ページが追加されるセルの位置、ページが終了し、改ページ後の残りのすべてのデータが次のページに印刷されます。簡単に言うと、改ページは、仕様に従ってワークシートを複数のページに分割します。 Aspose.Cells を使用して、実行時にワークシートに改ページを追加することもできます。 Aspose.Cells を使用すると、開発者は 2 種類の改ページを追加できます。

- 水平改ページ
- 垂直改ページ

残りの説明では、Aspose.Cells を使用してワークシートに水平または垂直の改ページを追加する方法について説明します。

{{% /alert %}} 
##  **改ページ**
Aspose.Cells はクラスを提供します[ワークブック](https://reference.aspose.com/cells/cpp/aspose.cells/workbook)Excel ファイルを表します。の[ワークブック](https://reference.aspose.com/cells/cpp/aspose.cells/workbook)クラスには[ワークシート](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection)Excel ファイル内の各ワークシートへのアクセスを許可するコレクション。

ワークシートは次のように表されます。[ワークシート](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラス。の[ワークシート](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスは、ワークシートの管理に使用される幅広いメソッドを提供します。改ページを追加するには、[ページ区切りの追加](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/addpagebreaks)の方法[ワークシート](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラス。
###  **改ページの追加**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManagingPageBreaks-AddingPageBreaks-new.cpp" >}}
