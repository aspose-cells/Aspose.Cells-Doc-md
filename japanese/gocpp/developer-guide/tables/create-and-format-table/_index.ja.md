---
title: 表の作成と書式設定
type: docs
weight: 10
url: /ja/go-cpp/create-and-format-table/
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

Aspose.Cellsは、Microsoft Excelファイルを表す [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) クラスを提供します。 [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) クラスには、Excelファイル内の各ワークシートにアクセスできる [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) コレクションが含まれています。

ワークシートは [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) クラスで表されます。 [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) クラスは、ワークシートの管理に役立つ多くのメソッドを提供します。ワークシートに [ListObject](https://reference.aspose.com/cells/go-cpp/listobject/) を作成するには、 [GetListObjects](https://reference.aspose.com/cells/go-cpp/worksheet/getlistobjects/) コレクションメソッドを使用します。各 [ListObject] は、[ListObjectCollection](https://reference.aspose.com/cells/go-cpp/listobjectcollection/) クラスのオブジェクトであり、更に [Add](https://reference.aspose.com/cells/go-cpp/listobjectcollection/add_int_int_int_int_bool/) メソッドで範囲を指定して追加します。

指定したセル範囲により、Aspose.Cellsは [ListObject](https://reference.aspose.com/cells/go-cpp/listobject/) オブジェクトを作成します。[ListObject] クラスの属性（例: [SetShowTotals](https://reference.aspose.com/cells/go-cpp/listobject/setshowtotals/) や [GetListColumns](https://reference.aspose.com/cells/go-cpp/listobject/getlistcolumns/) など）を使用してリストを制御します。

以下の例では、前述の手順でMicrosoft Excelを使用して作成したリストオブジェクトと同じ`[ListObject]`をAspose.Cells APIを使用して作成しています。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CreatingListObjects.go" >}}

## **表の書式設定**

関連データのグループを管理および分析するには、セルの範囲をリストオブジェクト（またはExcelテーブルとも呼ばれる）に変換することが可能です。表は、関連データを含む行と列の系列であり、他の行や列のデータとは独立して管理されます。デフォルトでは、表の各列には、ヘッダー行でフィルタリングが有効になっているため、リストオブジェクトデータを素早くフィルタリングまたはソートできます。リストオブジェクトには、数値データで作業するために有用な集計関数の選択肢を提供する合計行（リスト内の特別な行）を追加できます。Aspose.Cellsでは、リスト（またはテーブル）を作成および管理するためのオプションが提供されます。

### **リストオブジェクトの書式設定**

Aspose.Cellsは、Microsoft Excelファイルを表す [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) クラスを提供します。 [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) クラスには、Excelファイル内の各ワークシートにアクセスできる [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) コレクションが含まれています。

ワークシートは [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) クラスで表されます。 [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) クラスは、ワークシートの管理に役立つ多くのメソッドを提供します。 ワークシート内に *ListObject* を作成するには、`ListObjectCollection` を使用します。各 `[ListObject]` は実際には `ListObjectCollection` クラスのオブジェクトであり、[Add](https://reference.aspose.com/cells/go-cpp/listobjectcollection/add/) メソッドを提供して `ListObject` オブジェクトを追加し、その範囲を指定します。指定されたセル範囲に基づいて、Aspose.Cells によってワークシートに *ListObject* が作成されます。 `[ListObject]` クラスの属性（例：[SetTableStyleType](https://reference.aspose.com/cells/go-cpp/listobject/settablestyletype/)）を使用して、テーブルの整形を行います。

以下の例では、ワークシートにサンプルデータを追加し、`[ListObject]` を追加し、デフォルトのスタイルを適用しています。`[ListObject]`のスタイルはMicrosoft Excel 2007/2010でサポートされています。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormatTable.go" >}}
