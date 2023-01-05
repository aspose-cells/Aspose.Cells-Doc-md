---
title: ワークシートからのシナリオの作成、操作、または削除
linktitle: シナリオの管理
type: docs
weight: 120
url: /ja/java/create-manipulate-or-remove-scenarios-from-worksheets/
---
{{% alert color="primary" %}}

場合によっては、スプレッドシートでシナリオを作成、操作、または削除する必要があります。シナリオとは、1 つ以上の数式によってリンクされた変数入力セルを含む名前付きの what-if モデルです。シナリオを作成する前に、異なる値を挿入できるセルに依存する数式が少なくとも 1 つ含まれるようにワークシートを設計します。次の例は、Aspose.Cells API を使用してワークシートからシナリオを作成および削除する方法を示しています。

{{% /alert %}}

 Aspose.Cells は、いくつかの便利なクラスを提供します。[**シナリオコレクション**](https://reference.aspose.com/cells/java/com.aspose.cells/ScenarioCollection), [**シナリオ**](https://reference.aspose.com/cells/java/com.aspose.cells/Scenario), [**ScenarioInputCellCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ScenarioInputCellCollection)と[**シナリオ入力セル**](https://reference.aspose.com/cells/java/com.aspose.cells/ScenarioInputCell).また、[**Worksheet.Scenarios**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Scenarios)財産。以下のサンプル コードは、XLSX Excel ファイル (いくつかのシナリオを含む) を開き、ワークシートから既存のシナリオを削除します。また、Excel ファイルを保存する前に新しいシナリオを追加します。シナリオを含む非常に単純なテンプレート ファイルを使用します。

コードの実行後、既存のシナリオが削除され、新しいシナリオがワークシートに追加されます。

**出力ファイル**

![todo:画像_代替_文章](create-manipulate-or-remove-scenarios-from-worksheets_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreateScenariosfromWorksheets-CreateScenariosfromWorksheets.java" >}}
