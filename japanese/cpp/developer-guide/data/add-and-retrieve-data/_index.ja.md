---
title: データの追加と取得
type: docs
weight: 20
url: /ja/cpp/add-and-retrieve-data/
---
{{% alert color="primary" %}} 

の[ワークシートの Cells へのアクセス](/cells/ja/cpp/accessing-cells-of-a-worksheet/)では、ワークシート内のセルにアクセスするための基本的な方法について説明しました。この記事では、これらのアプローチの 1 つを使用して、さまざまな種類のデータをセルに追加します。

{{% /alert %}} 
## **Cells にデータを追加する**
Aspose.Cells はクラスを提供します[Iワークブック](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)Microsoft Excel ファイルを表します。の[Iワークブック](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)クラスには[Iワークシート](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)Excel ファイル内の各ワークシートにアクセスできるコレクション。ワークシートは、[Iワークシート](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)クラス。の[Iワークシート](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)クラスは[Iセル](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)コレクション。の各項目[Iセル](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)コレクションはのオブジェクトを表します[Iセル](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)クラス。

Aspose.Cells を使用すると、開発者は、[Iセル](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)クラス[プットバリュー](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a4a5f4b8cdd54eccb4eb2ea51babcbca9)方法。 Aspose.Cells は、[プットバリュー](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a4a5f4b8cdd54eccb4eb2ea51babcbca9)開発者がさまざまな種類のデータをセルに追加できるようにするメソッド。これらのオーバーロードされたバージョンの[プットバリュー](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a4a5f4b8cdd54eccb4eb2ea51babcbca9)メソッドを使用すると、ブール値、文字列、倍精度、整数、日付/時刻などの値をセルに追加できます。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AddAndRetrieveData-AddingDataToCells.cpp" >}}
### **効率の向上**
使用する場合[プットバリュー](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a4a5f4b8cdd54eccb4eb2ea51babcbca9)メソッドを使用して大量のデータをワークシートに入れる場合は、最初に行ごと、次に列ごとにセルに値を追加する必要があります。このアプローチにより、アプリケーションの効率が大幅に向上します。
## **Cells からのデータの取得**
Aspose.Cells はクラスを提供します[Iワークブック](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)Microsoft Excel ファイルを表します。の[Iワークブック](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)クラスには[Iワークシート](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)ファイル内のワークシートへのアクセスを許可するコレクション。ワークシートは、[Iワークシート](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)クラス。の[Iワークシート](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)クラスは[Iセル](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)コレクション。の各項目[Iセル](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)コレクションはのオブジェクトを表します[Iセル](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)クラス。

の[Iセル](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)クラスには、開発者がデータ型に従ってセルから値を取得できるいくつかのメソッドが用意されています。これらの方法には次のものがあります。

- [GetStringValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ac048c664985e2cadc2404840599d7ac3)、セルの文字列値を返します。
- [GetDoubleValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a5f21cd4c755da84135176c74425f230a)、セルの double 値を返します。
- [GetBoolValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ac61870c4b1d6a68077092fb043bf8741)、セルのブール値を返します。
- [GetDateTimeValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a7932b40c41141f716b096cc521113a61)、セルの日付/時刻の値を返します。
- [GetFloatValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a4e36c4be4c76447f54f8032b17cecf44)、セルの float 値を返します。
- [GetIntValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a7acc93c97c062cbd60a7f1ab00a022d8)、セルの整数値を返します。

フィールドが入力されていない場合、[GetDoubleValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a5f21cd4c755da84135176c74425f230a)また[GetFloatValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a4e36c4be4c76447f54f8032b17cecf44)例外をスローします。

セルに含まれるデータの種類は、[Iセル](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)クラス[GetType](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a36708b1bad0bbf45cbf9577ccab101ba)方法。実際、[Iセル](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)クラス[GetType](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a36708b1bad0bbf45cbf9577ccab101ba)メソッドはに基づいています[CellValueType](https://reference.aspose.com/cells/cpp/namespace/aspose.cells#a745bf00b4815ec8dcf1bd11922fa4b62)定義済みの値が以下にリストされている列挙型:

|**Cell 値の種類**|**説明**|
|:- |:- |
|CellValueType_IsBool|セル値がブールであることを指定します。|
|CellValueType_IsDateTime|セル値が日付/時刻であることを指定します。|
|CellValueType_IsNull|空白のセルを表します。|
|CellValueType_IsNumeric|セル値が数値であることを指定します。|
|CellValueType_IsString|セル値が文字列であることを指定します。|
|CellValueType_IsUnknown|セル値が不明であることを指定します。|
上記の事前定義されたセル値タイプを使用して、各セルに存在するデータのタイプと比較することもできます。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AddAndRetrieveData-RetrievingDataFromCells.cpp" >}}
