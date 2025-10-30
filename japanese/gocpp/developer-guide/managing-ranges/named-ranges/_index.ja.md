---
title: GO言語とC++経由でワークブックとワークシートのスコープ付き名前付き範囲を作成します
linktitle: 名前付き範囲
type: docs
weight: 40
url: /ja/go-cpp/create-workbook-and-worksheet-scoped-named-ranges/
description: Aspose.Cellsを使用してGO言語とC++経由でワークブックとワークシートのスコープ付き名前付き範囲を作成する方法を学びます。
---

{{% alert color="primary" %}} 

Microsoft Excelでは、ワークブック（またはグローバルスコープとしても知られています）とワークシートの2つの異なるスコープで名前付き範囲を定義できます。

- ワークブックスコープの名前付き範囲は、そのワークブック内の任意のワークシートから、名前を単純に使用することでアクセスできます。
- ワークシートスコープの名前付き範囲は、それが作成された特定のワークシートの参照でアクセスされます。

Aspose.Cellsは、ワークブックスコープとワークシートスコープの名前付き範囲の追加に関して、Microsoft Excelと同じ機能を提供します。ワークシートスコープの名前付き範囲を作成する場合、名前付き範囲にワークシートの参照を使用して、それをワークシートスコープの名前付き範囲として指定する必要があります。

{{% /alert %}} 

## **ブックスコープで名前を付けられた範囲を追加する**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-NamedRanges.go" >}}
## **ワークシートスコープを持つ名前付き範囲を追加する**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-NamedRanges-1.go" >}}
## **高度なトピック**
- [アクセスの作成とコピーした名前付き範囲](/cells/ja/cpp/create-access-and-copy-named-ranges/)
- [名前付き範囲の書式と変更](/cells/ja/cpp/format-and-modify-named-ranges/)
- [外部リンク付きの範囲を取得する](/cells/ja/cpp/get-range-with-external-links/)
- [非連続範囲の実装](/cells/ja/cpp/implementing-non-sequential-ranges/)

