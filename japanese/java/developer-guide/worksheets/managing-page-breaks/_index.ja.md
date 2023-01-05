---
title: 改ページの管理
type: docs
weight: 30
url: /ja/java/managing-page-breaks/
---
{{% alert color="primary" %}}

改ページは、1 つのページが終了し、次のページが始まるテキスト内の場所です。 Microsoft Excel では、ワークシート内の選択した任意のセルに改ページを追加できます。
ページは改ページが追加されたセルで終了し、改ページの後のすべてのデータは次のページに印刷されます。簡単に言えば、改ページはワークシートを複数のページに分割します。 Aspose.Cells を使用して、実行時にワークシートに改ページを追加することもできます。Aspose.Cells は、次の 2 種類の改ページをサポートしています。

- 水平
- 垂直。

この記事では、Aspose.Cells を使用して水平または垂直の改ページをワークシートに追加する方法について説明します。

{{% /alert %}}

## **Aspose.Cells & 改ページ**

Aspose.Cells はクラスを提供し、[**ワークブック**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)これは Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスには[**ワークシート コレクション**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)これにより、Excel ファイル内の各ワークシートにアクセスできます。

ワークシートは、[**ワークシート**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)ワークシートを管理するための幅広いプロパティとメソッドを提供するクラス。改ページを追加するには、[**ワークシート**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラス'[**水平改ページ**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#HorizontalPageBreaks)と[**垂直改ページ**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VerticalPageBreaks)プロパティ。

の[**水平改ページ**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#HorizontalPageBreaks)と[**垂直改ページ**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VerticalPageBreaks)プロパティは、実際には複数の改ページを含むコレクションです。各コレクションには、水平および垂直の改ページを管理するためのメソッドがいくつか含まれています。これらのメソッドがどのように使用されるかについては、以下で説明します。

## **改ページの追加**

ワークシートに改ページを追加するには、 を呼び出して、指定したセルに垂直および水平の改ページを挿入します。[**水平改ページ**](https://reference.aspose.com/cells/java/com.aspose.cells/HorizontalPageBreakCollection)と[**垂直改ページ**](https://reference.aspose.com/cells/java/com.aspose.cells/VerticalPageBreakCollection)コレクションの**追加**メソッド。各**追加**メソッドは、改ページを追加するセル名を取ります。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AddingPageBreaks-AddingPageBreaks.java" >}}

{{% alert color="primary" %}}

改ページ プレビュー モードまたは印刷プレビュー モードで、これらの改ページがどのように機能するかを確認できます。

{{% /alert %}}

## **すべての改ページのクリア**

ワークシート内のすべての改ページをクリアするには、[**HorizontalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/HorizontalPageBreakCollection)と[**VerticalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/VerticalPageBreakCollection)コレクションの**クリア**メソッド。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ClearAllPageBreaks-ClearAllPageBreaks.java" >}}

## **特定の改ページを削除する**

ワークシート内の特定の改ページを削除するには、[**HorizontalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/HorizontalPageBreakCollection)と[**VerticalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/VerticalPageBreakCollection)コレクションの**removeAt**メソッド。各**removeAt**メソッドは、削除する改ページのインデックスを取得します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemoveSpecificPageBreak-RemoveSpecificPageBreak.java" >}}

{{% alert color="primary" %}}

**知っておくべき重要なこと** ページに合わせてプロパティを設定する場合 (つまり、[**FitToPagesTall**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesTall)と[**FitToPagesWide**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesWide)) ページ設定では、改ページ設定が影響を受けるため、ワークシートを印刷する場合、改ページ設定はファイル内にまだ存在しますが、考慮されません。

{{% /alert %}}
