---
title: テーブルの作成とフォーマット
type: docs
weight: 10
url: /ja/cpp/create-and-format-table/
---
##  **テーブルの作成**
スプレッドシートの利点の 1 つは、電話リスト、タスク リスト、取引、資産、負債のリストなど、さまざまな種類のリストを作成できることです。複数のユーザーが協力して、さまざまなリストを使用、作成、保守できます。

Aspose.Cells はリストの作成と管理をサポートしています。
###  **リストオブジェクトの利点**
データのリストを実際のリスト オブジェクトに変換すると、多くの利点があります。

- 新しい行と列が自動的に追加されます。
- リストの下部に合計行を簡単に追加して、SUM、AVERAGE、COUNT などを表示できます。
- 右側に追加された列は、List オブジェクトに自動的に組み込まれます。
- 行と列に基づくグラフは自動的に展開されます。
- 行と列に割り当てられた名前付き範囲は自動的に展開されます。
- リストは行や列が誤って削除されないように保護されています。
###  **Microsoft Excel を使用したリスト オブジェクトの作成**

|**リストオブジェクトを作成するデータ範囲の選択**|
| :- |
|![todo:image_alt_text](jHcNq4o.png)|
これにより、「リストの作成」ダイアログが表示されます。

|**「リストの作成」ダイアログ**|
| :- |
|![todo:image_alt_text](kJmukRF.png)|
データの List オブジェクトを実装し、合計行を指定します (*Data**、*List**、*Total Row** の順に選択します)。

|**リストオブジェクトの作成**|
| :- |
|![todo:image_alt_text](ECSGVdR.png)|
###  **Aspose.Cells API を使用する**
Aspose.Cells はクラスを提供します[ワークブック](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)これは Microsoft Excel ファイルを表します。の[ワークブック](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスには[ワークシート](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)Excel ファイル内の各ワークシートへのアクセスを許可するコレクション。

ワークシートは次のように表されます。[ワークシート](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラス。の[ワークシート](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスは、ワークシートを管理するための幅広いメソッドを提供します。を作成するには[リストオブジェクト](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/)ワークシートでは、[GetListObjects](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getlistobjects/)の収集方法[ワークシート](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラス。実際、各 `[ListObject]` は[リストオブジェクトコレクション](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobjectcollection/)クラスはさらに、[追加](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobjectcollection/add/)`[ListObject]` オブジェクトを追加し、リストのセル範囲を指定するメソッド。

指定されたセル範囲に従って、`[ListObject]` オブジェクトは Aspose.Cells によって作成されます。属性を使用します (たとえば、[SetShowTotals](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/setshowtotals/)そして[GetListColumns](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/getlistcolumns/)など) `[ListObject]` クラスのリストを制御します。

以下の例では、上のセクションで Microsoft Excel を使用して作成したのと同じ `[ListObject]` を、Aspose.Cells API を使用して作成しました。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-CreatingListObjects-new.cpp" >}}
##  **表のフォーマットを設定する**
関連するデータのグループを管理および分析するために、セル範囲をリスト オブジェクト (Excel テーブルとも呼ばれます) に変換することができます。テーブルは、他の行や列のデータとは独立して管理される関連データを含む一連の行と列です。デフォルトでは、テーブルの各列のヘッダー行でフィルタリングが有効になっているため、リスト オブジェクト データをすばやくフィルタリングまたは並べ替えることができます。各合計行セルに集計関数のドロップダウン リストを提供するリスト オブジェクトに、合計行 (数値データの操作に便利な集計関数の選択を提供するリスト内の特別な行) を追加できます。 Aspose.Cells は、リスト (またはテーブル) を作成および管理するためのオプションを提供します。
###  **リストオブジェクトの書式設定**
Aspose.Cells はクラスを提供します[ワークブック](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)これは Microsoft Excel ファイルを表します。の[ワークブック](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスには[ワークシート](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)Excel ファイル内の各ワークシートへのアクセスを許可するコレクション。

ワークシートは次のように表されます。[ワークシート](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラス。の[ワークシート](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスは、ワークシートを管理するための幅広いメソッドを提供します。を作成するには*リストオブジェクト*ワークシートでは、`ListObjectCollection` を使用します。各 `[ListObject]` は、実際には `ListObjectCollection` クラスのオブジェクトであり、さらに[追加](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobjectcollection/add/)`[ListObject]` オブジェクトを追加するメソッドを使用し、オブジェクトが包含するセルの範囲を指定します。指定されたセル範囲に従って、*リストオブジェクト*は、Aspose.Cells によってワークシートに作成されます。属性を使用します (例:[SetTableStyleType](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/settablestyletype/)`[ListObject]` クラスの ) を使用して、要件に合わせてテーブルをフォーマットします。

以下の例では、サンプル データをワークシートに追加し、`[ListObject]` を追加して、デフォルトのスタイルをそれに適用します。 `[ListObject]` スタイルは、Microsoft Excel 2007/2010 でサポートされています。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-FormatTable-new.cpp" >}}
