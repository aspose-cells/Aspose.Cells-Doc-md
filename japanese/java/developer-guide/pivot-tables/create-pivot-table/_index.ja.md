---
title: ピボットテーブルを作成する
type: docs
weight: 10
url: /ja/java/create-pivot-table/
---

## **ピボットテーブルの作成**

### **Aspose.Cells を使用してピボットテーブルを作成する**

{{% alert color="primary" %}}

Aspose.Cells を使用して、スプレッドシートにピボットテーブルを追加することができます。Aspose.Cells には、特定のクラスを使用してピボットテーブルを作成および制御するための特別なクラスがいくつかあります。これらのクラスは、ピボットテーブルの構築ブロックとして使用されます。

ピボットテーブルのオブジェクトは次のとおりです:

- [**PivotField**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotField): ピボットテーブルのフィールドを表します。
- [**PivotFieldCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotFieldCollection): ピボットテーブル内のすべての [**PivotField**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotField) オブジェクトのコレクションを表します。
- [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable): ピボットテーブルを表します。
- [**PivotTableCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection): ワークシート上のすべてのピボットテーブルオブジェクトのコレクションを表します。

{{% /alert %}}

### **シンプルなピボットテーブルの作成**

Aspose.Cells を使用してピボットテーブルを作成するには、以下の手順に従ってください:

1. [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) オブジェクトの [**setValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value) メソッドを使用してワークシートセルにデータを追加します。このデータはピボットテーブルのデータソースとして使用されます。
1. [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#add(com.aspose.cells.PivotTable,%20int,%20int,%20java.lang.String)) クラスの [**PivotTableCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection) メソッドを呼び出してワークシートにピボットテーブルを追加します。このデータはピボットテーブルのデータソースとして使用されます。
1. [**PivotTableCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection) から [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable) オブジェクトにアクセスして、[**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable) のインデックスを渡します。
1. [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable) オブジェクトにカプセル化されたピボットテーブル内のいずれかのピボットテーブルオブジェクトを使用して、ピボットテーブルを管理します。

{{% alert color="primary" %}}

データソースとしてセルの範囲を割り当てる場合、範囲は左上から右下に設定する必要があります。例えば、「A1:C3」は有効であり、「C3:A1」は無効です。

{{% /alert %}}

以下のコード例は、上記の基本的な手順に従って簡単なピボットテーブルを作成する方法を示しています。コードを実行すると、ワークシートにピボットテーブルが追加されます:

**対応するフィールドに基づいてピボットテーブルを作成する**

![todo:image_alt_text](create-pivot-table_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-CreatePivotTable-CreatePivotTable.java" >}}
