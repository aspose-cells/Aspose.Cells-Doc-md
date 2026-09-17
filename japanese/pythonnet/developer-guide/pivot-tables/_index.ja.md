---
title: ピボットテーブルを挿入する
description: Aspose.Cells for Python via .NETでピボットテーブルを作成し、書式を設定する。
linktitle: ピボットテーブル
url: /ja/python-net/create-pivot-table/
type: docs
weight: 160
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
keywords: ピボットテーブルを作成し、ピボットテーブルを挿入し、ピボットテーブルを書式設定します。
---

## **ピボットテーブルの作成**
Aspose.Cells for Python via .NETを使用して、プログラムでピボットテーブルをスプレッドシートに追加することが可能です。

### **ピボットテーブルオブジェクトモデル**
Aspose.Cells for Python via .NETでは、ピボットテーブルを作成および制御するために使用される特別なクラスのセットが提供されています。これらのクラスは、ピボットテーブルの構成要素である[**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/)オブジェクトを作成および制御するために使用されます。オブジェクトは次のとおりです:
- [**PivotField**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/)は、[**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/)のフィールドを表します。
- [**PivotFieldCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfieldcollection)は、[**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable)のすべての[**PivotField**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield)オブジェクトのコレクションを表します。
- [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable)は、ワークシート上のPivotTableを表します。
- [**PivotTableCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection)は、ワークシート上のすべての[**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable)オブジェクトのコレクションを表します。

### **Aspose.Cellsを使用して簡単なピボットテーブルを作成する**
1. [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell)オブジェクトの[**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#str)メソッドを使用してワークシートにデータを追加します。
   このデータは、ピボットテーブルのデータソースとして使用されます。
1. ワークシートにピボットテーブルを追加するために、[**PivotTables**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection)コレクションの[**add**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/add/#str-str-str)メソッドを呼び出します。このメソッドはWorksheetオブジェクトでカプセル化されています。
1. 新しい[**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable)オブジェクトを[**PivotTables**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection)コレクションから取得します。このコレクションはPivotTableのインデックスを渡すことでアクセスできます。
1. ピボットテーブルを管理するために、上記で説明した[**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable)のいずれかを使用します。
例のコードを実行すると、ワークシートにピボットテーブルが追加されます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTable-CreatePivotTable-1.py" >}}

{{% alert color="primary" %}}
データソースとしてセル範囲を割り当てるときには、範囲は左上から右下に向かっている必要があります。例えば、「A1:C3」は有効ですが、「C3:A1」は無効です。
{{% /alert %}}

## **高度なトピック**

{{< app/cells/assistant language="python-net" >}}