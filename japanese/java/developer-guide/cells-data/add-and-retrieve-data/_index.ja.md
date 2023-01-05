---
title: データの追加と取得
type: docs
weight: 20
url: /ja/java/add-and-retrieve-data/
---
{{% alert color="primary" %}} 

の[ワークシートの Cells へのアクセス](/cells/ja/java/accessing-cells-of-a-worksheet/)では、ワークシート内のセルにアクセスするための基本的な方法について説明しました。この記事では、これらのアプローチの 1 つを使用して、さまざまな種類のデータをセルに追加します。

{{% /alert %}} 
## **Cells にデータを追加する**
Aspose.Cells はクラスを提供し、[ワークブック](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)、Microsoft Excel ファイルを表します。の[ワークブック](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)クラスには[ワークシート コレクション](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)これにより、Excel ファイル内の各ワークシートにアクセスできます。ワークシートは、[ワークシート](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)クラス。の[ワークシート](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)クラスは[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)コレクション。の各項目[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)コレクションはのオブジェクトを表します[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)クラス。

Aspose.Cells を使用すると、開発者は、[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)クラス'[setValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value)財産。を使用することにより、[setValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value)プロパティを使用すると、ブール、文字列、倍精度、整数、日付/時刻などの値をセルに追加できます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingDataToCells-AddingDataToCells.java" >}}
### **効率の向上**
{{% alert color="primary" %}} 

を使用する場合[setValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value)プロパティを使用して大量のデータをワークシートに追加するには、最初に行ごと、次に列ごとにセルに値を追加する必要があります。このアプローチにより、アプリケーションの効率が大幅に向上します。

{{% /alert %}} 

ワークシートで作業している間、ユーザーはセルにさまざまな種類のデータを追加できます。これらのデータ項目には、ブール、整数、浮動小数点、テキスト、または日付/時刻の値が含まれる場合があります。 Aspose.Cells を使用して、データ型に従ってセルから適切な値を取得できます。
## **Cells からのデータの取得**
Aspose.Cells はクラスを提供し、[ワークブック](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)これは Excel ファイルを表します。[ワークブック](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)クラスには[ワークシート コレクション](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)これにより、Excel ファイル内の各ワークシートにアクセスできます。ワークシートは、[ワークシート](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)クラス。の[ワークシート](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)クラスは[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)コレクション。の各項目[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)コレクションはのオブジェクトを表します[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)クラス。

の[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)クラスには、開発者がデータ型に従ってセルから値を取得できるいくつかのプロパティが用意されています。これらのプロパティは次のとおりです。

- [文字列値](https://reference.aspose.com/cells/java/com.aspose.cells/cell#StringValue)、セルの文字列値。
- [DoubleValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#DoubleValue)、セルの double 値を返します。
- [ブール値](https://reference.aspose.com/cells/java/com.aspose.cells/cell#BoolValue)、セルのブール値。
- [日時値](https://reference.aspose.com/cells/java/com.aspose.cells/cell#DateTimeValue)、セルの日付/時刻値。
- [浮動小数点値](https://reference.aspose.com/cells/java/com.aspose.cells/cell#FloatValue)、セルの float 値。
- [IntValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#IntValue)、セルの整数値。

さらに、セルに含まれるデータの種類は、[タイプ](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Type)のプロパティ[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)クラス。実際、[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)クラス'[タイプ](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Type)プロパティはに基づいています[CellValueType](https://reference.aspose.com/cells/java/com.aspose.cells/CellValueType)定義済みの値が以下にリストされている列挙型:

|**Cell 値の種類**|**説明**|
|:- |:- |
|[IS_BOOL](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_BOOL)|セル値がブールであることを指定します。|
|[は_日にち_時間](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_DATE_TIME)|セル値が日付/時刻であることを指定します。|
|[IS_ERROR](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_ERROR)|セルにエラー値が含まれていることを表します|
|[無効です](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_NULL)|空白のセルを表します。|
|[IS_NUMERIC](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_NUMERIC)|セル値が数値であることを指定します。|
|[IS_STRING](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_STRING)|セル値が文字列であることを指定します。|
|[IS_UNKNOWN](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_UNKNOWN)|セル値が不明であることを指定します。|
上記の事前定義されたセル値タイプを使用して、各セルに存在するデータのタイプと比較することもできます。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-RetrievingDataFromCells-RetrievingDataFromCells.java" >}}
