---
title: 改ページの管理
type: docs
weight: 30
url: /ja/net/managing-page-breaks/
description: この記事では、サンプル コードを提供し、C# API または .NET ライブラリを使用してプログラムで Excel ワークシートの改ページを追加、改ページをクリア、または特定の改ページを削除する方法を説明します。
keywords: page breaks c#, excel page breaks c#, clear page break c#, delete specific page break c#
---
{{% alert color="primary" %}}

定義によれば、改ページはテキストの流れの中で、あるページが終了して次のページが始まる場所です。 Microsoft Excel では、ワークシートの選択したセルに改ページを追加できます。

印刷時に改ページが追加されるセルの位置、ページが終了し、改ページ後の残りのデータが次のページに印刷されます。簡単に言うと、改ページは、仕様に従ってワークシートを複数のページに分割します。 Aspose.Cells を使用して、実行時にワークシートに改ページを追加することもできます。 Aspose.Cells を使用すると、開発者は 2 種類の改ページを追加できます。

- 水平改ページ
- 垂直改ページ

残りの説明では、Aspose.Cells を使用してワークシートに水平または垂直の改ページを追加する方法について説明します。

{{% /alert %}}

##  **改ページ**

Aspose.Cells は、[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Excel ファイルを表すクラス。の[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Excel ファイル内の各ワークシートへのアクセスを許可するコレクション。

ワークシートは次のように表されます。[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス。の[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスは、ワークシートの管理に使用される幅広いプロパティとメソッドを提供します。

改ページを追加するには、[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス'[**水平改ページ**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/horizontalpagebreaks)と[**垂直改ページ**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/verticalpagebreaks)プロパティ。

の[**水平改ページ**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/horizontalpagebreaks)と[**垂直改ページ**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/verticalpagebreaks)プロパティは、複数の改ページを含む可能性のあるコレクションです。各コレクションには、水平および垂直の改ページを管理するためのいくつかのメソッドが含まれています。

###  **改ページの追加**

ワークシートに改ページを追加するには、次のコマンドを呼び出して、指定したセルに垂直および水平の改ページを挿入します。[**horizontalPageBreakCollection.Add()**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection/methods/add/index)と[**verticalPageBreakCollection.Add()**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection/methods/add/index)メソッド。各**追加**このメソッドは、ブレークを追加するセルの名前を受け取ります。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-AddingPageBreaks-1.cs" >}}

{{% alert color="primary" %}}

改ページ プレビュー モードまたは印刷プレビュー モードでは、これらの改ページがどのように機能するかを確認できます。

{{% /alert %}}

###  **すべての改ページをクリアする**

ワークシート内のすべての改ページをクリアするには、[**水平PageBreakコレクション**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection)と[**垂直ページブレークコレクション**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection)コレクション」[**Clear()**](https://docs.microsoft.com/en-us/dotnet/api/system.collections.collectionbase.clear?redirectedfrom=MSDN&view=netframework-4.7.2#System_Collections_CollectionBase_Clear)メソッド。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-ClearAllPageBreaks-1.cs" >}}

###  **特定の改ページの削除**

特定の改ページを削除するには、[**horizontalPageBreakCollection.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection/methods/removeat)と[**verticalPageBreakCollection.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection/methods/removeat)メソッド。各**削除場所**このメソッドは、削除される改ページのインデックスを取得します。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-RemoveSpecificPageBreak-1.cs" >}}

##  **知っておくべき重要なこと**

設定すると**ページに合わせる**プロパティ（つまり、[**ページに合わせる背の高い**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopagestall)と[**ページ幅に合わせる**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopageswide)ページ設定設定では、改ページ設定が影響を受けるため、ワークシートを印刷する場合、改ページ設定は設定されていますが、考慮されません。
