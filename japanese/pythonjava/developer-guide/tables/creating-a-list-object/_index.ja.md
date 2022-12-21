---
title: リスト オブジェクトの作成
type: docs
weight: 20
url: /ja/python-java/creating-a-list-object/
---
たとえば、ワークシートを使用すると、さまざまな種類のリストを簡単に操作できます。電話リスト、タスク リスト。 Aspose.Cells は、リストの作成と管理をサポートします。

## **リスト オブジェクトの利点**

データのリストを実際のリスト オブジェクトに変換すると、いくつかの利点があります。

- 新しい行と列が自動的に含まれます。
- リストの下部に合計行を簡単に追加して、SUM、AVERAGE、COUNT などを表示できます。
- 右側に追加された列は、List オブジェクトに自動的に組み込まれます。
- 行と列に基づくグラフは自動的に展開されます。
- 行と列に割り当てられた名前付き範囲は、自動的に展開されます。
- リストは、偶発的な行と列の削除から保護されています。

## **Microsoft Excel を使用してリスト オブジェクトを作成する**

**リスト オブジェクトを作成するためのデータ範囲の選択** 

![todo:画像_代替_文章](picture1.png)

[リストの作成] ダイアログが表示されます。

**リストの作成ダイアログ** 

![todo:画像_代替_文章](picture2.png)

List オブジェクトを実装し、Total Row を指定する (Select**データ**、 それから**リスト**、 に続く**合計行**).

**リスト オブジェクトの作成** 

![todo:画像_代替_文章](picture3.png)

## **Aspose.Cells API を使用してリスト オブジェクトを作成する**

Aspose.Cells はクラスを提供し、[**ワークブック**](https://reference.aspose.com/cells/python/asposecells.api/Workbook)、Microsoft Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/python/asposecells.api/Workbook)クラスには[**ワークシート**](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection)Excel ファイル内の各ワークシートにアクセスできるコレクション。

ワークシートは、[**ワークシート**](https://reference.aspose.com/cells/python/asposecells.api/Worksheet)クラス。の[**ワークシート**](https://reference.aspose.com/cells/python/asposecells.api/Worksheet)クラスには、ワークシートを管理するためのさまざまなプロパティとメソッドが用意されています。を作成するには[**ListObject**](https://reference.aspose.com/cells/python/asposecells.api/ListObject)ワークシートで、使用[**リストオブジェクト**](https://reference.aspose.com/cells/python/asposecells.api/worksheet#ListObjects)のコレクション プロパティ[**ワークシート**](https://reference.aspose.com/cells/python/asposecells.api/Worksheet)クラス。各[**ListObject**](https://reference.aspose.com/cells/python/asposecells.api/ListObject)実際には、[**ListObjectCollection**](https://reference.aspose.com/cells/python/asposecells.api/ListObjectCollection)クラスは、さらに[**追加**](https://reference.aspose.com/cells/python/asposecells.api/listobjectcollection#add(int,%20int,%20int,%20int,%20boolean)List オブジェクトを追加し、リストのセル範囲を指定するメソッド。

指定されたセル範囲に従って、List オブジェクトが Aspose.Cells によってワークシートに作成されます。[**ListObject**](https://reference.aspose.com/cells/python/asposecells.api/ListObject)リストを制御するクラス。

以下の例では、同じものを作成しました[**ListObject**](https://reference.aspose.com/cells/python/asposecells.api/ListObject)上記のセクションで Microsoft Excel を使用して作成したように、Aspose.Cells for Python via Java API を使用します。

## ソースコード

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-CreatingListObject.py" >}}
