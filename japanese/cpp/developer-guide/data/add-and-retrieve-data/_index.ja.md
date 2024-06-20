---
title: データの追加と取得
type: docs
weight: 20
url: /ja/cpp/add-and-retrieve-data/
---

{{% alert color="primary" %}} 

[ワークシートのセルへのアクセス](/cells/ja/cpp/accessing-cells-of-a-worksheet/)では、ワークシート内のセルにアクセスするための基本的なアプローチについて説明しました。この記事では、これらのアプローチの1つを使用して、異なる種類のデータをセルに追加します。

{{% /alert %}} 
## **セルへのデータの追加**
Aspose.CellsはMicrosoft Excelファイルを表す[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスを提供します。 [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスには、Excelファイル内の各ワークシートにアクセスすることを可能にする[Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)コレクションが含まれています。ワークシートは[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスによって表されます。 [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスは、[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)コレクションを提供します。[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)コレクション内の各アイテムは、[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)クラスのオブジェクトを表します。

Aspose.Cellsを使用すると、開発者は[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)クラスの[PutValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/)メソッドを呼び出すことで、ワークシート内のセルにデータを追加できます。 Aspose.Cellsは、[PutValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/)メソッドのオーバーロードされたバージョンを提供しており、開発者はこれらのオーバーロードされたバージョンの[PutValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/)メソッドを使用して、セルに異なる種類のデータ（ブール値、文字列、倍精度浮動小数点数、整数、日付/時刻など）を追加することができます。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AddAndRetrieveData-AddingDataToCells-new.cpp" >}}
### **効率の向上**
ワークシートに大量のデータを追加する場合は、まず行ごとに値を追加し、次に列ごとに追加する必要があります。このアプローチにより、アプリケーションの効率が大幅に改善されます。
## **セルからデータを取得**
Aspose.CellsはMicrosoft Excelファイルを表す[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスを提供します。 [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスには、ファイル内のワークシートにアクセスすることを可能にする[Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)コレクションが含まれています。ワークシートは[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスによって表されます。 [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスは、[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)コレクションを提供します。[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)コレクション内の各アイテムは、[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)クラスのオブジェクトを表します。

[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)クラスには、そのデータ型に応じてセルから値を取得するためのいくつかのメソッドが提供されています。これらのメソッドには次のものがあります：

- [GetStringValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/)、セルの文字列値を返します。
- [GetDoubleValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdoublevalue/)、セルの倍精度浮動小数点数値を返します。
- [GetBoolValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getboolvalue/)、セルのブール値を返します。
- [GetDateTimeValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdatetimevalue/)、セルの日付/時刻値を返します。
- [GetFloatValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getfloatvalue/)、セルの浮動小数点値を返します。
- [GetIntValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getintvalue/)、セルの整数値を返します。

フィールドが入力されていない場合、[GetDoubleValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdoublevalue/)または[GetFloatValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getfloatvalue/)は例外をスローします。

セルに含まれるデータの型は、[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)クラスの[GetType](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettype/)メソッドを使用しても確認できます。実際、[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)クラスの[GetType](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettype/)メソッドは、[CellValueType](https://reference.aspose.com/cells/cpp/aspose.cells/cellvaluetype/)列挙体に基づいており、その事前定義値が以下にリストされています:

|**セル値の種類**|**説明**|
| :- | :- |
|CellValueType_IsBool|セルの値がブール型であることを指定します。
|CellValueType_IsDateTime|セルの値が日付/時刻型であることを指定します。
|CellValueType_IsNull|空白のセルを表します。
|CellValueType_IsNumeric|セルの値が数値型であることを指定します。
|CellValueType_IsString|セルの値が文字列型であることを指定します。
|CellValueType_IsUnknown|セルの値が不明な型であることを指定します。
上記で定義されたセルの事前定義値を使用して、各セルに存在するデータの型と比較することもできます。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AddAndRetrieveData-RetrievingDataFromCells-new.cpp" >}}
