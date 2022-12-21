---
title: 改ページの管理
type: docs
weight: 30
url: /ja/cpp/managing-page-breaks/
---
{{% alert color="primary" %}} 

定義によれば、改ページとは、テキストの流れの中で、あるページが終了して次のページが始まる場所です。 Microsoft Excel では、ユーザーがワークシートの選択したセルに改ページを追加できます。

改ページが追加されるセルの位置、ページが終了し、改ページ後の残りのすべてのデータが印刷中に次のページに印刷されます。簡単に言えば、改ページは、仕様に従ってワークシートを複数のページに分割します。 Aspose.Cells を使用して、実行時にワークシートに改ページを追加することもできます。Aspose.Cells を使用すると、開発者は次の 2 種類の改ページを追加できます。

- 水平改ページ
- 垂直改ページ

残りの説明では、Aspose.Cells を使用してワークシートに水平または垂直の改ページを追加する方法について説明します。

{{% /alert %}} 
## **改ページ**
Aspose.Cells はクラスを提供します[Iワークブック](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)これは Excel ファイルを表します。の[Iワークブック](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)クラスには[ワークシート](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)Excel ファイル内の各ワークシートにアクセスできるコレクション。

ワークシートは、[Iワークシート](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)クラス。の[Iワークシート](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)クラスには、ワークシートの管理に使用されるさまざまなメソッドが用意されています。改ページを追加するには、[AddPageBreaks](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#a5f8dd5624b81e0ee2e7455f2b83380f6)の方法[Iワークシート](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)クラス。
### **改ページの追加**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManagingPageBreaks-AddingPageBreaks.cpp" >}}
