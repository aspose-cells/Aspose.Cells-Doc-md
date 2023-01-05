---
title: ピボット テーブルの作成
type: docs
weight: 10
url: /ja/java/create-pivot-table/
---
## **ピボット テーブルの作成**

### **Aspose.Cells を使用してピボット テーブルを作成する**

{{% alert color="primary" %}}

Aspose.Cells では、スプレッドシートにピボット テーブルを追加できます。 Aspose.Cells には、特にピボット テーブルの作成と制御に使用される特別なクラスがいくつかあります。これらのクラスは、のプロパティを作成および設定するために使用されます。[**ピボットテーブル**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable)ピボット テーブルのビルディング ブロックとして使用されます。

ピボット テーブル オブジェクトは次のとおりです。

- [**ピボットフィールド**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotField)ピボット テーブルのフィールドを表します。
- [**ピボットフィールド コレクション**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotFieldCollection) すべてのコレクションを表します[**ピボットフィールド**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotField)ピボット テーブルのオブジェクト。
- [**ピボットテーブル**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable): ピボット テーブルを表します。
- [**ピボットテーブル コレクション**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection)ワークシート上のすべてのピボット テーブル オブジェクトのコレクションを表します。

{{% /alert %}}

### **簡単なピボット テーブルの作成**

Aspose.Cells を使用してピボット テーブルを作成するには、次の手順に従ってください。

1. を使用してワークシートのセルにデータを追加します。[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell)オブジェクトの[**setValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value)方法。このデータは、ピボット テーブルのデータ ソースとして使用されます。
1. を呼び出して、ワークシートにピボット テーブルを追加します。[**追加**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#add(com.aspose.cells.PivotTable,%20int,%20int,%20java.lang.String) ) の方法[**ピボットテーブル コレクション**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection)にカプセル化されたクラス[**ワークシート**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)物体。
1. アクセス[**ピボットテーブル**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable)からのオブジェクト[**ピボットテーブル コレクション**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection)を渡すことで[**ピボットテーブル**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable)索引。
1. にカプセル化されたピボット テーブル オブジェクト (上記で説明) のいずれかを使用します。[**ピボットテーブル**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable)ピボット テーブルを管理するオブジェクト。

{{% alert color="primary" %}}

セルの範囲をデータ ソースとして割り当てる場合、範囲は左上から右下に設定する必要があります。たとえば、「A1:C3」は有効です。 「C3:A1」は無効です。

{{% /alert %}}

以下のコード例は、上記の基本的な手順に従って単純なピボット テーブルを作成する方法を示しています。コードを実行すると、ワークシートにピボット テーブルが追加されます。

**対応するフィールドに基づくピボット テーブルの作成**

![todo:画像_代替_文章](create-pivot-table_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-CreatePivotTable-CreatePivotTable.java" >}}
