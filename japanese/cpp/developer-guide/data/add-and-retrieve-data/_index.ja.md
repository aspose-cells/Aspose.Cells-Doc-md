---
title: データの追加と取得
type: docs
weight: 20
url: /ja/cpp/add-and-retrieve-data/
---
{{% alert color="primary" %}} 

で[ワークシートの Cells へのアクセス](/cells/ja/cpp/accessing-cells-of-a-worksheet/)では、ワークシート内のセルにアクセスするための基本的なアプローチについて説明しました。この記事では、これらのアプローチの 1 つを使用して、さまざまな種類のデータをセルに追加します。

{{% /alert %}} 
##  **Cellsにデータを追加する**
Aspose.Cells はクラスを提供します[ワークブック](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)これは Microsoft Excel ファイルを表します。の[ワークブック](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスには[ワークシート](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)Excel ファイル内の各ワークシートへのアクセスを許可するコレクション。ワークシートは次のように表されます。[ワークシート](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラス。の[ワークシート](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスが提供する[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)コレクション。の各項目[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)コレクションはオブジェクトを表します[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)クラス。

 Aspose.Cells を使用すると、開発者は、[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)クラス[PutValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/)方法。 Aspose.Cells は、オーバーロードされたバージョンの[PutValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/)開発者がさまざまな種類のデータをセルに追加できるメソッド。これらのオーバーロードされたバージョンの使用[PutValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/)メソッドを使用すると、ブール値、文字列、倍精度浮動小数点数、整数、日付/時刻などの値をセルに追加できます。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AddAndRetrieveData-AddingDataToCells-new.cpp" >}}
###  **効率の向上**
使用する場合[PutValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/)大量のデータをワークシートに入力する方法では、最初に行ごと、次に列ごとにセルに値を追加する必要があります。このアプローチにより、アプリケーションの効率が大幅に向上します。
##  **Cells からのデータの取得**
Aspose.Cells はクラスを提供します[ワークブック](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)これは Microsoft Excel ファイルを表します。の[ワークブック](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスには[ワークシート](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)ファイル内のワークシートへのアクセスを許可するコレクション。ワークシートは次のように表されます。[ワークシート](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラス。の[ワークシート](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスが提供するのは[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)コレクション。の各項目[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)コレクションはオブジェクトを表します[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)クラス。

の[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)クラスには、開発者がデータ型に応じてセルから値を取得できるようにするメソッドがいくつか用意されています。これらの方法には次のものが含まれます。

- [GetStringValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/)、セルの文字列値を返します。
- [GetDoubleValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdoublevalue/)、セルの double 値を返します。
- [GetBoolValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getboolvalue/)、セルのブール値を返します。
- [GetDateTimeValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdatetimevalue/)、セルの日付/時刻値を返します。
- [GetFloatValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getfloatvalue/)、セルの浮動小数点値を返します。
- [GetIntValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getintvalue/)、セルの整数値を返します。

フィールドが入力されていない場合、次のセルが表示されます。[GetDoubleValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdoublevalue/)または[GetFloatValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getfloatvalue/)例外をスローします。

セルに含まれるデータの種類は、[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)クラス[GetType](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettype/)方法。実際、[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)クラス[GetType](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettype/)方法はに基づいています[CellValueType](https://reference.aspose.com/cells/cpp/aspose.cells/cellvaluetype/)事前定義された値が以下にリストされている列挙体。

|**Cell 値のタイプ**|**説明**|
| :- | :- |
|CellValueType_IsBool|セル値がブール値であることを指定します。|
|CellValueType_IsDateTime|セル値が日付/時刻であることを指定します。|
|CellValueType_IsNull|空白のセルを表します。|
|CellValueType_IsNumeric|セル値が数値であることを指定します。|
|CellValueType_IsString|セル値が文字列であることを指定します。|
|CellValueType_IsUnknown|セル値が不明であることを指定します。|
上記の事前定義されたセル値のタイプを使用して、各セルに存在するデータのタイプと比較することもできます。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AddAndRetrieveData-RetrievingDataFromCells-new.cpp" >}}
