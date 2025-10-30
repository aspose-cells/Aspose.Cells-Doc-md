---
title: 表の作成と書式設定
type: docs
weight: 10
url: /ja/cpp/create-and-format-table/
---

## **テーブルの作成**
スプレッドシートの利点の1つは、電話リスト、タスクリスト、取引のリスト、資産リスト、負債リストなど、さまざまなタイプのリストを作成できることです。複数のユーザーが協力して、さまざまなリストを利用、作成、維持することができます。

Aspose.Cellsはリストの作成と管理をサポートしています。
### **リストオブジェクトの利点**
実際のリストオブジェクトにデータのリストを変換するときの利点はいくつかあります。

- 新しい行や列が自動的に含まれます。
- リストの最下部に合計、平均、カウントなどを表示するために総合行を簡単に追加できます。
- 右に追加された列は自動的にリストオブジェクトに取り込まれます。
- 行と列に基づくチャートは自動的に拡張されます。
- 行と列に割り当てられた名前付き範囲は自動的に拡張されます。
- リストは誤って行や列が削除されないように保護されています。
### **Microsoft Excelを使用してリストオブジェクトを作成する**

|**リストオブジェクトを作成するためのデータ範囲の選択**|
| :- |
|![todo:image_alt_text](jHcNq4o.png)|
これにより、リストの作成ダイアログが表示されます。

|**リストを作成するダイアログ**|
| :- |
|![todo:image_alt_text](kJmukRF.png)|
データを指定してリストオブジェクトを実装し、合計行を指定します（**データ**を選択し、**リスト**、その後**合計行**を選択します）。

|**リストオブジェクトを作成する**|
| :- |
|![todo:image_alt_text](ECSGVdR.png)|
### **Aspose.Cells APIを使用する**
Aspose.Cellsは、Microsoft Excelファイルを表す[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) クラスを提供します。[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) クラスには、Excelファイル内の各ワークシートにアクセスを可能にする[Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) コレクションが含まれています。

[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) クラスでワークシートが表されます。[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) クラスには、ワークシートを管理するための多くのメソッドが提供されています。ワークシート内に[ListObject](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/) を作成するには、[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) クラスの[GetListObjects](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getlistobjects/) コレクションメソッドを使用します。各`[ListObject]`は実際には、さらに[Add](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobjectcollection/add/) メソッドを提供する[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) クラスの[ListObjectCollection](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobjectcollection/) クラスのオブジェクトであり、リストのセルの範囲を指定します。

指定されたセル範囲に従って、Aspose.Cellsによって`[ListObject]`オブジェクトが作成されます。リストの操作には、`[ListObject]` クラスの属性（たとえば[SetShowTotals](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/setshowtotals/)や[GetListColumns](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/getlistcolumns/)など）を使用します。

以下の例では、前述の手順でMicrosoft Excelを使用して作成したリストオブジェクトと同じ`[ListObject]`をAspose.Cells APIを使用して作成しています。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-CreatingListObjects-new.cpp" >}}
## **表の書式設定**
関連データのグループを管理および分析するには、セルの範囲をリストオブジェクト（またはExcelテーブルとも呼ばれる）に変換することが可能です。表は、関連データを含む行と列の系列であり、他の行や列のデータとは独立して管理されます。デフォルトでは、表の各列には、ヘッダー行でフィルタリングが有効になっているため、リストオブジェクトデータを素早くフィルタリングまたはソートできます。リストオブジェクトには、数値データで作業するために有用な集計関数の選択肢を提供する合計行（リスト内の特別な行）を追加できます。Aspose.Cellsでは、リスト（またはテーブル）を作成および管理するためのオプションが提供されます。
### **リストオブジェクトの書式設定**
Aspose.Cellsは、Microsoft Excelファイルを表す[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) クラスを提供します。[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) クラスには、Excelファイル内の各ワークシートにアクセスを可能にする[Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) コレクションが含まれています。

[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) クラスでワークシートが表されます。[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) クラスには、ワークシートを管理するための多くのメソッドが提供されています。ワークシート内に*ListObject*を作成するには、`ListObjectCollection`を使用します。それぞれの`[ListObject]`は実際には、さらに`ListObjectCollection` クラスの`Add`(https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobjectcollection/add/) メソッドを提供する`[ListObject]`オブジェクトを追加し、それが包括すべきセルの範囲を指定します。指定されたセルの範囲に応じて、Aspose.Cellsはワークシート内に*ListObject*を作成します。リストの書式設定には、`[ListObject]` クラスの属性（たとえば[SetTableStyleType](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/settablestyletype/)）を使用します。

以下の例では、ワークシートにサンプルデータを追加し、`[ListObject]` を追加し、デフォルトのスタイルを適用しています。`[ListObject]`のスタイルはMicrosoft Excel 2007/2010でサポートされています。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-FormatTable-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
