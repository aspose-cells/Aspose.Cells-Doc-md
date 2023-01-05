---
title: テーブルの作成とフォーマット
type: docs
weight: 10
url: /ja/cpp/create-and-format-table/
---
## **テーブルの作成**
スプレッドシートの利点の 1 つは、電話番号リスト、タスク リスト、取引リスト、資産または負債のリストなど、さまざまな種類のリストを作成できることです。複数のユーザーが協力して、さまざまなリストを使用、作成、および維持できます。

Aspose.Cells は、リストの作成と管理をサポートしています。
### **リスト オブジェクトの利点**
データのリストを実際のリスト オブジェクトに変換すると、多くの利点があります。

- 新しい行と列が自動的に含まれます。
- リストの下部に合計行を簡単に追加して、SUM、AVERAGE、COUNT などを表示できます。
- 右側に追加された列は、List オブジェクトに自動的に組み込まれます。
- 行と列に基づくグラフは自動的に展開されます。
- 行と列に割り当てられた名前付き範囲は、自動的に展開されます。
- リストは、偶発的な行と列の削除から保護されています。
### **Microsoft Excel を使用してリスト オブジェクトを作成する**

|**List オブジェクトを作成するためのデータ範囲の選択**|
|:- |
|![todo:画像_代替_文章](jHcNq4o.png)|
[リストの作成] ダイアログが表示されます。

|**リストの作成ダイアログ**|
|:- |
|![todo:画像_代替_文章](kJmukRF.png)|
データの List オブジェクトを実装し、合計行を指定する (選択**データ**、 それから**リスト**、 に続く**合計行**).

|**リスト オブジェクトの作成**|
|:- |
|![todo:画像_代替_文章](ECSGVdR.png)|
### **Aspose.Cells API を使用**
Aspose.Cells はクラスを提供します[Iワークブック](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)Microsoft Excel ファイルを表します。の[Iワークブック](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)クラスには[Iワークシート](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)Excel ファイル内の各ワークシートにアクセスできるコレクション。

ワークシートは、[Iワークシート](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)クラス。の[Iワークシート](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)クラスには、ワークシートを管理するためのさまざまなメソッドが用意されています。を作成するには[IListObject](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object)ワークシートでは、[GetIListObjects](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#a4356bc4b8cffee624891f10ea49a4705)の回収方法[Iワークシート](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)クラス。実際、各 `[IListObject]` は、[IListObjectCollection](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object_collection)クラスは、さらに[追加](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object_collection#ae4afda31b69b75a78558a65bef65ee42)`[IListObject]` オブジェクトを追加し、リストのセル範囲を指定するメソッド。

指定されたセル範囲に従って、Aspose.Cells オブジェクトが Aspose.Cells によって作成されます。属性を使用します (たとえば、[ShowTotals](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object#a9026460927f035f374f5e1ea74e639f2)と[ListColumns](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object#afeeb7bfabd0971e9fe34a09f0b83ae73)など) `[IListObject]` クラスのリストを制御します。

以下の例では、上記のセクションで Microsoft Excel を使用して作成したのと同じ Aspose.Cells API を使用して `[IListObject]` を作成しています。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-CreatingListObjects.cpp" >}}
## **テーブルをフォーマットする**
関連するデータのグループを管理および分析するために、セルの範囲をリスト オブジェクト (Excel テーブルとも呼ばれます) に変換することができます。テーブルは、他の行や列のデータとは独立して管理される関連データを含む一連の行と列です。既定では、テーブルのすべての列のヘッダー行でフィルター処理が有効になっているため、リスト オブジェクト データをすばやくフィルター処理または並べ替えることができます。各合計行セルの集計関数のドロップダウン リストを提供するリスト オブジェクトに、合計行 (数値データの操作に役立つ集計関数の選択を提供するリスト内の特別な行) を追加できます。 Aspose.Cells は、リスト (またはテーブル) を作成および管理するためのオプションを提供します。
### **リスト オブジェクトの書式設定**
Aspose.Cells はクラスを提供します[Iワークブック](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)Microsoft Excel ファイルを表します。の[Iワークブック](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)クラスには[Iワークシート](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)Excel ファイル内の各ワークシートにアクセスできるコレクション。

ワークシートは、[Iワークシート](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)クラス。の[Iワークシート](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)クラスには、ワークシートを管理するためのさまざまなメソッドが用意されています。を作成するには*ListObject*ワークシートでは、`IListObjectCollection` を使用します。実際には、各 `[IListObject]` は `IListObjectCollection` クラスのオブジェクトであり、さらに[追加](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object_collection#ae4afda31b69b75a78558a65bef65ee42)メソッドを使用して `[IListObject]` オブジェクトを追加し、含まれるセルの範囲を指定します。指定されたセル範囲に従って、*ListObject*は Aspose.Cells によってワークシートに作成されます。属性を使用します (たとえば、[表スタイルの種類](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object#a5de8b5321b0ccb30dfb09cefe6536462)`[IListObject]` クラスの ) を使用して、要件に合わせてテーブルをフォーマットします。

次の例では、サンプル データをワークシートに追加し、`[IListObject]` を追加して、既定のスタイルを適用します。 `[IListObject]` スタイルは Microsoft Excel 2007/2010 でサポートされています。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-FormatTable.cpp" >}}
