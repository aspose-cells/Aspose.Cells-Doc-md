---
title: ワークシートからシナリオを作成、操作、または削除する
linktitle: シナリオの管理
type: docs
weight: 190
url: /ja/net/create-manipulate-or-remove-scenarios-from-worksheets/
description: この記事では、C#ライブラリと.NET APIを使用してExcelワークシートのシナリオをプログラムで作成、操作、または削除する方法が説明されています。
keywords: C#でシナリオワークシートを作成、Excelワークシートからシナリオを削除、C#でシナリオワークシートを操作する
---

{{% alert color="primary" %}}

時折、スプレッドシートでシナリオを作成、操作、または削除する必要があります。シナリオとは、1つ以上の数式によってリンクされた可変の入力セルを含む名前付きの'仮定'モデルです。シナリオを作成する前に、異なる値が挿入できるセルに依存する1つ以上の数式を含むワークシートの設計を行います。以下の例は、Aspose.CellsのAPIを使用してワークシートからシナリオを作成および削除する方法を示しています。

{{% /alert %}}

Aspose.Cellsには、例えば、[**ScenarioCollection**](https://reference.aspose.com/cells/net/aspose.cells/scenariocollection)、[**Scenario**](https://reference.aspose.com/cells/net/aspose.cells/scenario)、[**ScenarioInputCellCollection**](https://reference.aspose.com/cells/net/aspose.cells/scenarioinputcellcollection)、および[**ScenarioInputCell**](https://reference.aspose.com/cells/net/aspose.cells/scenarioinputcell)のクラスなど、いくつかの便利なクラスが提供されています。また、[**Worksheet.Scenarios**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/scenarios)プロパティも提供されています。以下のサンプルコードは、いくつかのシナリオを含むXLSX形式のExcelファイルを開き、既存のシナリオを削除し、Excelファイルを保存する前にワークシートに新しいシナリオを追加します。この例では、シナリオを含む非常にシンプルなテンプレートファイルが使用されています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreateManipulateRemoveScenarios-1.cs" >}}
