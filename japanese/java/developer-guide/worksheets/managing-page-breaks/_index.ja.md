---
title: ページブレークの管理
type: docs
weight: 30
url: /ja/java/managing-page-breaks/
---

{{% alert color="primary" %}}

改ページとは、テキストのページが終わり、次のページが始まる場所です。 Microsoft Excelはワークシートの選択したセルにいつでも改ページを追加できます。
改ページが追加されたセルでページが終わり、改ページ後のすべてのデータが次のページに印刷されます。 要するに、ページの区切りはワークシートを複数のページに分割します。 Aspose.Cellsを使用してワークシートにページを追加することも可能です。 Aspose.Cellsは、次の2種類の改ページをサポートしています。

- 横方向
- 縦方向

この記事では、Aspose.Cellsを使用してワークシートに横方向または縦方向の改ページを追加する方法について説明します。

{{% /alert %}}

## **Aspose.Cells＆改ページ**

Aspose.Cellsは、Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスを提供します。 [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスには、Excelファイル内の各ワークシートにアクセスできる[**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)が含まれています。

ワークシートは、ワークシートを管理するための幅広い範囲のプロパティとメソッドを提供する[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラスによって表されます。 改ページを追加するには、[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラスの[**HorizontalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#HorizontalPageBreaks)および[**VerticalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VerticalPageBreaks)プロパティを使用します。

[**HorizontalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#HorizontalPageBreaks)および[**VerticalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VerticalPageBreaks)プロパティは、実際には複数の改ページを含む可能性のあるコレクションです。 各コレクションには、横方向および縦方向の改ページを管理するためのいくつかのメソッドが含まれています。 これらのメソッドの使用方法については、以下で説明します。

## **ページブレークの追加**

ワークシートに改ページを追加するには、**Add**メソッドを呼び出して指定したセルに縦方向および横方向の改ページを挿入します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AddingPageBreaks-AddingPageBreaks.java" >}}

{{% alert color="primary" %}}

ページビューモードまたは印刷プレビューモードで、これらの改ページがどのように動作するかを確認できます。

{{% /alert %}}

## **すべてのページの改ページをクリアする**

ワークシートのすべての改ページをクリアするには、**Clear**メソッドを呼び出します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ClearAllPageBreaks-ClearAllPageBreaks.java" >}}

## **特定の改ページを削除する**

ワークシートから特定の改ページを削除するには、**removeAt**メソッドを呼び出して削除する改ページのインデックスを渡します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemoveSpecificPageBreak-RemoveSpecificPageBreak.java" >}}

{{% alert color="primary" %}}

**重要なこと**: ページ設定の**fit to page**プロパティ（すなわち[**FitToPagesTall**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesTall)と[**FitToPagesWide**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesWide)）を設定すると、ページの改ページ設定に影響が出ます。 そのため、ワークシートを印刷するときは、改ページ設定は考慮されませんが、ファイルにはまだ存在します。

{{% /alert %}}
