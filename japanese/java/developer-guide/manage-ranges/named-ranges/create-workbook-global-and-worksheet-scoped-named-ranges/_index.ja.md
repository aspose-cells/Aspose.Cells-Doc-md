---
title: ワークブック（グローバル）とワークシート限定の名前付き範囲の作成
type: docs
weight: 10
url: /ja/java/create-workbook-global-and-worksheet-scoped-named-ranges/
---

{{% alert color="primary" %}}

Microsoft Excelでは、ワークブック（またはグローバルスコープとしても知られています）とワークシートの2つの異なるスコープで名前付き範囲を定義できます。

- ワークブックスコープの名前付き範囲は、そのワークブック内の任意のワークシートから、名前を単純に使用することでアクセスできます。
- ワークシートスコープの名前付き範囲は、それが作成された特定のワークシートの参照でアクセスされます。

Aspose.Cellsは、ワークブックスコープとワークシートスコープの名前付き範囲の追加に関して、Microsoft Excelと同じ機能を提供します。ワークシートスコープの名前付き範囲を作成する場合、名前付き範囲にワークシートの参照を使用して、それをワークシートスコープの名前付き範囲として指定する必要があります。

{{% /alert %}}

以下のコードサンプルは、[**Range**](https://reference.aspose.com/cells/java/com.aspose.cells/Range)クラスを使用してワークブックとワークシートスコープの名前付き範囲を作成する方法を示しています。

## **ワークブックスコープを持つ名前付き範囲を追加する**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddNamedRangeWithWorkbookScope-AddNamedRangeWithWorkbookScope.java" >}}

## **ワークシートスコープを持つ名前付き範囲を追加する**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddNamedRangeWithWorksheetScope-AddNamedRangeWithWorkbookScope.java" >}}
{{< app/cells/assistant language="java" >}}
