---
title: ピボットテーブルを挿入する
linktitle: ピボットテーブル
type: docs
weight: 160
url: /ja/nodejs-cpp/create-pivot-table/
description: Excelスプレッドシートファイルのピボットテーブルを作成し、書式を設定する。
---

## **ピボットテーブルの作成**

Aspose.Cells for Node.js via C++を使って、ピボットテーブルをプログラム的にスプレッドシートに追加することが可能です。

### **ピボットテーブルオブジェクトモデル**

Aspose.Cells for Node.js via C++は、ピボットテーブルを作成・制御するための特別なクラスセットを提供します。これらのクラスは、[**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable)オブジェクトを作成・設定するために使われ、これがピボットテーブルの基本構造となります。次のオブジェクトがあります：

- [**PivotField**](https://reference.aspose.com/cells/nodejs-cpp/pivotfield)は、[**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable)のフィールドを表します。
- [**PivotFieldCollection**](https://reference.aspose.com/cells/nodejs-cpp/pivotfieldcollection)は、[**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable)のすべての[**PivotField**](https://reference.aspose.com/cells/nodejs-cpp/pivotfield)オブジェクトのコレクションを表します。
- [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable)は、ワークシート上のPivotTableを表します。
- [**PivotTableCollection**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection)は、ワークシート上のすべての[**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable)オブジェクトのコレクションを表します。

### **Aspose.Cellsを使用して簡単なピボットテーブルを作成する**

1. [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)オブジェクトの[**putValue**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-)メソッドを使用してワークシートにデータを追加します。
   このデータは、ピボットテーブルのデータソースとして使用されます。
1. ワークシートにピボットテーブルを追加するために、[**PivotTables**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection)コレクションの[**add**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection/#add-string-string-string-)メソッドを呼び出します。このメソッドはWorksheetオブジェクトでカプセル化されています。
1. 新しい[**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable)オブジェクトを[**PivotTables**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection)コレクションから取得します。このコレクションはPivotTableのインデックスを渡すことでアクセスできます。
1. ピボットテーブルを管理するために、上記で説明した[**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable)のいずれかを使用します。

例のコードを実行すると、ワークシートにピボットテーブルが追加されます。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-create-pivot-table.js" >}}

{{% alert color="primary" %}}

データソースとしてセル範囲を割り当てるときには、範囲は左上から右下に向かっている必要があります。例えば、「A1:C3」は有効ですが、「C3:A1」は無効です。

{{% /alert %}}
{{< app/cells/assistant language="nodejs-cpp" >}}
