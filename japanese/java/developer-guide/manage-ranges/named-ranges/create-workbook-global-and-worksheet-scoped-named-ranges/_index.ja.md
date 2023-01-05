---
title: ワークブック (グローバル) とワークシートのスコープ指定された名前付き範囲の作成
type: docs
weight: 10
url: /ja/java/create-workbook-global-and-worksheet-scoped-named-ranges/
---
{{% alert color="primary" %}}

Microsoft Excel では、ユーザーはワークブック (グローバル スコープとも呼ばれます) とワークシートの 2 つの異なるスコープで名前付き範囲を定義できます。

- ブック スコープを持つ名前付き範囲には、その名前を使用するだけで、そのブック内の任意のワークシートからアクセスできます。
- ワークシート スコープの名前付き範囲には、それが作成された特定のワークシートの参照を使用してアクセスします。

Aspose.Cells は、Microsoft Excel と同じ機能を提供し、ワークブックとワークシートのスコープ指定された範囲を追加します。ワークシート スコープの名前付き範囲を作成する場合、名前付き範囲でワークシート参照を使用して、ワークシート スコープの名前付き範囲として指定する必要があります。

{{% /alert %}}

次のコード サンプルは、[**範囲**](https://reference.aspose.com/cells/java/com.aspose.cells/Range)クラス。

## **ワークブック スコープで名前付き範囲を追加する**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddNamedRangeWithWorkbookScope-AddNamedRangeWithWorkbookScope.java" >}}

## **ワークシート スコープで名前付き範囲を追加する**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddNamedRangeWithWorksheetScope-AddNamedRangeWithWorkbookScope.java" >}}
