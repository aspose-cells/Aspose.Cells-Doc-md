---
title: ブックおよびワークシートにスコープが制限された名前付き範囲を作成する
linktitle: 名前付き範囲
type: docs
weight: 40
url: /ja/net/create-workbook-and-worksheet-scoped-named-ranges/
---

{{% alert color="primary" %}} 

Microsoft Excelでは、ワークブック（またはグローバルスコープとしても知られています）とワークシートの2つの異なるスコープで名前付き範囲を定義できます。

- ワークブックスコープの名前付き範囲は、そのワークブック内の任意のワークシートから、名前を単純に使用することでアクセスできます。
- ワークシートスコープの名前付き範囲は、それが作成された特定のワークシートの参照でアクセスされます。

Aspose.Cellsは、ワークブックスコープとワークシートスコープの名前付き範囲の追加に関して、Microsoft Excelと同じ機能を提供します。ワークシートスコープの名前付き範囲を作成する場合、名前付き範囲にワークシートの参照を使用して、それをワークシートスコープの名前付き範囲として指定する必要があります。

{{% /alert %}} 
## **ブックスコープで名前を付けられた範囲を追加する**


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkbookScopedNamedRanges-AddWorkbookScopedNamedRange-1.cs" >}}
## **ワークシートスコープを持つ名前付き範囲を追加する**


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkbookScopedNamedRanges-WorksheetNamedRange-1.cs" >}}

## **高度なトピック**
- [アクセスの作成とコピーした名前付き範囲](/cells/ja/net/create-access-and-copy-named-ranges/)
- [名前付き範囲の書式と変更](/cells/ja/net/format-and-modify-named-ranges/)
- [外部リンク付きの範囲を取得する](/cells/ja/net/get-range-with-external-links/)
- [非連続範囲の実装](/cells/ja/net/implementing-non-sequential-ranges/)
{{< app/cells/assistant language="csharp" >}}
