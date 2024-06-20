---
title: リストオブジェクトの作成
type: docs
weight: 20
url: /ja/python-java/creating-a-list-object/
---

ワークシートの使用は、電話リスト、タスクリストなど、さまざまなタイプのリストでの作業を簡単にします。Aspose.Cellsはリストの作成と管理をサポートしています。

## **リストオブジェクトの利点**

実際のリストオブジェクトにデータリストを変換すると、いくつかの利点があります:

- 新しい行や列が自動的に含まれます。
- リストの最下部に合計、平均、カウントなどを表示するために総合行を簡単に追加できます。
- 右に追加された列は自動的にリストオブジェクトに取り込まれます。
- 行と列に基づくチャートは自動的に拡張されます。
- 行と列に割り当てられた名前付き範囲は自動的に拡張されます。
- リストは誤って行や列が削除されないように保護されています。

## **Microsoft Excelを使用してリストオブジェクトを作成する**

リストオブジェクトを作成するためのデータ範囲の選択 

![todo:image_alt_text](picture1.png)

これにより、リストの作成ダイアログが表示されます。

リストの作成ダイアログ 

![todo:image_alt_text](picture2.png)

リストオブジェクトを実装し、合計行を指定します（** データ **を選択して、** リスト **、その後** 合計行 **を選択してください）。

リストオブジェクトを作成する 

![todo:image_alt_text](picture3.png)

## **Aspose.Cells APIを使用してリストオブジェクトを作成します。**

Aspose.Cellsは、Microsoft Excelファイルを表すクラス、[**Workbook**](https://reference.aspose.com/cells/python/asposecells.api/Workbook)を提供しています。[**Workbook**](https://reference.aspose.com/cells/python/asposecells.api/Workbook) クラスには、Excelファイルの各ワークシートにアクセスするための [**Worksheets**](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection) コレクションが含まれています。

ワークシートは[**Worksheet**](https://reference.aspose.com/cells/python/asposecells.api/Worksheet)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/python/asposecells.api/Worksheet)クラスはワークシートを管理するための様々なプロパティとメソッドを提供します。ワークシートに[**ListObject**](https://reference.aspose.com/cells/python/asposecells.api/ListObject)を作成するには、[**Worksheet**](https://reference.aspose.com/cells/python/asposecells.api/Worksheet)クラスの[**ListObjects**](https://reference.aspose.com/cells/python/asposecells.api/worksheet#ListObjects)コレクションプロパティを使用してください。各[**ListObject**](https://reference.aspose.com/cells/python/asposecells.api/ListObject)は実際には[**ListObjectCollection**](https://reference.aspose.com/cells/python/asposecells.api/ListObjectCollection)クラスのオブジェクトであり、さらにリストオブジェクトを追加し、リストのセルの範囲を指定するための[**add**](https://reference.aspose.com/cells/python/asposecells.api/listobjectcollection#add(int,%20int,%20int,%20int,%20boolean))メソッドを提供します。

Aspose.Cellsによってワークシート内にリストオブジェクトが作成されます。リストを制御するために[**ListObject**](https://reference.aspose.com/cells/python/asposecells.api/ListObject)クラスの属性（ShowTotals、ListColumnsなど）を使用してください。

以下の例では、Microsoft Excelで作成したものと同じ[**ListObject**](https://reference.aspose.com/cells/python/asposecells.api/ListObject)をAspose.Cells for Python via Java APIを使用して作成しました。

## ソースコード

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-CreatingListObject.py" >}}
