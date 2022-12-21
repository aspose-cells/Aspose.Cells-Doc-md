---
title: 改ページの管理
type: docs
weight: 30
url: /ja/net/managing-page-breaks/
---
{{% alert color="primary" %}}

定義によれば、改ページとは、テキストの流れの中で、あるページが終了して次のページが始まる場所です。 Microsoft Excel では、ユーザーがワークシートの選択したセルに改ページを追加できます。

改ページが追加されるセルの位置、ページが終了し、改ページ後の残りのデータが印刷中に次のページに印刷されます。簡単に言えば、改ページは、仕様に従ってワークシートを複数のページに分割します。 Aspose.Cells を使用して、実行時にワークシートに改ページを追加することもできます。Aspose.Cells を使用すると、開発者は次の 2 種類の改ページを追加できます。

- 水平改ページ
- 垂直改ページ

残りの説明では、Aspose.Cells を使用してワークシートに水平または垂直の改ページを追加する方法について説明します。

{{% /alert %}}

## **改ページ**

Aspose.Cells は[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Excel ファイルを表すクラス。の[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Excel ファイル内の各ワークシートにアクセスできるコレクション。

ワークシートは、[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス。の[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスには、ワークシートの管理に使用されるさまざまなプロパティとメソッドが用意されています。

改ページを追加するには、[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス'[**水平改ページ**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/horizontalpagebreaks)と[**垂直改ページ**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/verticalpagebreaks)プロパティ。

の[**水平改ページ**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/horizontalpagebreaks)と[**垂直改ページ**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/verticalpagebreaks)プロパティは、複数の改ページを含むコレクションです。各コレクションには、水平および垂直の改ページを管理するためのメソッドがいくつか含まれています。

### **改ページの追加**

ワークシートに改ページを追加するには、 を呼び出して、指定したセルに垂直および水平の改ページを挿入します。[**HorizontalPageBreakCollection.Add()**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection/methods/add/index)と[**VerticalPageBreakCollection.Add()**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection/methods/add/index)メソッド。各**追加**メソッドは、ブレークを追加するセルの名前を取ります。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-AddingPageBreaks-1.cs" >}}

{{% alert color="primary" %}}

改ページ プレビュー モードまたは印刷プレビュー モードで、これらの改ページがどのように機能するかを確認できます。

{{% /alert %}}

### **すべての改ページのクリア**

ワークシート内のすべての改ページをクリアするには、[**HorizontalPageBreakCollection**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection)と[**VerticalPageBreakCollection**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection)コレクションの[**クリア（）**](https://docs.microsoft.com/en-us/dotnet/api/system.collections.collectionbase.clear?redirectedfrom=MSDN&view=netframework-4.7.2#System_Collections_CollectionBase_Clear)メソッド。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-ClearAllPageBreaks-1.cs" >}}

### **特定の改ページを削除する**

特定の改ページを削除するには、[**HorizontalPageBreakCollection.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection/methods/removeat)と[**VerticalPageBreakCollection.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection/methods/removeat)メソッド。各**削除場所**メソッドは、削除しようとしている改ページのインデックスを取得します。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-RemoveSpecificPageBreak-1.cs" >}}

## **知っておくべき重要なこと**

設定すると**ページに合わせる**プロパティ（つまり[**FitToPagesTall**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopagestall)と[**FitToPagesWide**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopageswide)ページ設定では、改ページ設定が影響を受けるため、ワークシートを印刷する場合、改ページ設定は設定されたままでも考慮されません。
