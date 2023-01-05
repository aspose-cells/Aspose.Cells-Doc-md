---
title: ワークシートからのシナリオの作成、操作、または削除
linktitle: シナリオの管理
type: docs
weight: 190
url: /ja/net/create-manipulate-or-remove-scenarios-from-worksheets/
---
{{% alert color="primary" %}}

場合によっては、スプレッドシートでシナリオを作成、操作、または削除する必要があります。シナリオは「もしも」という名前のシナリオです。 1 つ以上の式によってリンクされた変数入力セルを含むモデル。シナリオを作成する前に、異なる値を挿入できるセルに依存する数式が少なくとも 1 つ含まれるようにワークシートを設計します。次の例は、Aspose.Cells API を使用してワークブックのワークシートからシナリオを作成および削除する方法を示しています。

{{% /alert %}}

Aspose.Cells は、いくつかの便利なクラスを提供します。たとえば、[**シナリオコレクション**](https://reference.aspose.com/cells/net/aspose.cells/scenariocollection), [**シナリオ**](https://reference.aspose.com/cells/net/aspose.cells/scenario), [**ScenarioInputCellCollection**](https://reference.aspose.com/cells/net/aspose.cells/scenarioinputcellcollection)、 と[**シナリオ入力セル**](https://reference.aspose.com/cells/net/aspose.cells/scenarioinputcell)クラス。また、[**Worksheet.Scenarios**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/scenarios)財産。以下のサンプル コードは、いくつかのシナリオを含む XLSX Excel ファイルを開き、既存のシナリオを削除します。また、Excel ファイルを保存する前に、ワークシートに新しいシナリオを追加します。この例では、シナリオを含む非常に単純なテンプレート ファイルを使用しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreateManipulateRemoveScenarios-1.cs" >}}
