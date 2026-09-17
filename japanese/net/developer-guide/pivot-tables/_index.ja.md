---
title: ピボットテーブルを挿入する
description: Excelスプレッドシートファイルのピボットテーブルを作成し、書式を設定する。
linktitle: ピボットテーブル
url: /ja/net/pivot-tables/
type: docs
weight: 160
keywords: ピボットテーブルを作成し、ピボットテーブルを挿入し、ピボットテーブルを書式設定します。
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **ピボットテーブルの作成**
Aspose.Cellsを使用してプログラムでスプレッドシートにピボットテーブルを追加することができます。

### **ピボットテーブルオブジェクトモデル**
Aspose.Cellsには、ピボットテーブルを作成し制御するための[**Aspose.Cells.Pivot**](https://reference.aspose.com/cells/net/aspose.cells.pivot)名前空間内の特別なクラスがあります。これらのクラスは、ピボットテーブルの構成要素である[**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)オブジェクトを作成および設定するために使用されます。オブジェクトには以下のものがあります:
- [**PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield)は、[**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)のフィールドを表します。
- [**PivotFieldCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection)は、[**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)のすべての[**PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield)オブジェクトのコレクションを表します。
- [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)は、ワークシート上のPivotTableを表します。
- [**PivotTableCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection)は、ワークシート上のすべての[**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)オブジェクトのコレクションを表します。

### **Aspose.Cellsを使用して簡単なピボットテーブルを作成する**
1. [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)オブジェクトの[**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)メソッドを使用してワークシートにデータを追加します。
   このデータは、ピボットテーブルのデータソースとして使用されます。
1. ワークシートにピボットテーブルを追加するために、[**PivotTables**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection)コレクションの[**add**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/add/index)メソッドを呼び出します。このメソッドはWorksheetオブジェクトでカプセル化されています。
1. 新しい[**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)オブジェクトを[**PivotTables**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection)コレクションから取得します。このコレクションはPivotTableのインデックスを渡すことでアクセスできます。
1. ピボットテーブルを管理するために、上記で説明した[**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)のいずれかを使用します。
例のコードを実行すると、ワークシートにピボットテーブルが追加されます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-CreatePivotTable-1.cs" >}}

{{% alert color="primary" %}}
データソースとしてセル範囲を割り当てるときには、範囲は左上から右下に向かっている必要があります。例えば、「A1:C3」は有効ですが、「C3:A1」は無効です。
{{% /alert %}}

{{< app/cells/assistant language="csharp" >}}