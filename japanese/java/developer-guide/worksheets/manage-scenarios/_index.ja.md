---
title: ワークシートからシナリオを作成、操作、または削除する
linktitle: シナリオの管理
type: docs
weight: 120
url: /ja/java/create-manipulate-or-remove-scenarios-from-worksheets/
---

{{% alert color="primary" %}}

時々、スプレッドシートでシナリオを作成、操作、または削除する必要があります。 シナリオは、1つまたは複数の数式によってリンクされた変数入力セルを含む名前付きのwhat-ifモデルです。 シナリオを作成する前に、異なる値を挿入できるセルに依存する少なくとも1つの数式を含むワークシートを設計します。 以下の例では、Aspose.Cells APIを使用してワークシートからシナリオを作成および削除する方法を示します。

{{% /alert %}}

Aspose.Cellsは、 [**ScenarioCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ScenarioCollection)、[**Scenario**](https://reference.aspose.com/cells/java/com.aspose.cells/Scenario)、[**ScenarioInputCellCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ScenarioInputCellCollection)、および[**ScenarioInputCell**](https://reference.aspose.com/cells/java/com.aspose.cells/ScenarioInputCell)などの便利なクラスを提供します。 また、[**Worksheet.Scenarios**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Scenarios)プロパティも提供しています。 以下のサンプルコードでは、（いくつかのシナリオを含む）XLSX Excelファイルを開いて、既存のシナリオをワークシートから削除し、Excelファイルを保存する前に新しいシナリオを追加します。 これは、シナリオを含む非常にシンプルなテンプレートファイルを使用します。

コードを実行すると、既存のシナリオが削除され、新しいシナリオがワークシートに追加されます。

**出力ファイル**

![todo:image_alt_text](create-manipulate-or-remove-scenarios-from-worksheets_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreateScenariosfromWorksheets-CreateScenariosfromWorksheets.java" >}}
