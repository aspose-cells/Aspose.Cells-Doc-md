---
title: データの追加と取得
type: docs
weight: 20
url: /ja/java/add-and-retrieve-data/
---

{{% alert color="primary" %}} 

[ワークシートのセルへのアクセス](/cells/ja/java/accessing-cells-of-a-worksheet/)では、ワークシートのセルに異なるタイプのデータを追加するための基本的なアプローチについて説明しました。

{{% /alert %}} 
## **セルへのデータの追加**
Aspose.Cellsは、Microsoft Excelファイルを表す[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)クラスを提供しています。[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) クラスには、Excelファイル内の各ワークシートにアクセスできる[WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) が含まれています。ワークシートは[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) クラスで表されます。 [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) クラスは、[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) コレクションを提供します。[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) コレクション内の各アイテムは[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) クラスのオブジェクトを表します。

Aspose.Cellsを使用すると、[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) クラスの[setValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value) プロパティを呼び出すことで、ワークシート内のセルにデータを追加できます。[setValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value) プロパティを使用することで、ブール値、文字列、倍精度浮動小数点数、整数、日付/時間などの値をセルに追加することができます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingDataToCells-AddingDataToCells.java" >}}
### **効率の向上**
{{% alert color="primary" %}} 

[setValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value) プロパティを使用してワークシートに大量のデータを追加する場合、まず行ごとにそのセルに値を追加し、次に列ごとに値を追加する必要があります。このアプローチにより、アプリケーションの効率が大幅に向上します。

{{% /alert %}} 

ワークシートで作業中、ユーザーはセルにさまざまな種類のデータを追加することができます。これらのデータ項目には、ブール値、整数、浮動小数点、テキスト、または日付/時刻の値が含まれる場合があります。Aspose.Cellsを使用して、データ型に応じてセルから適切な値を取得できます。
## **セルからデータを取得**
Aspose.Cellsには、Excelファイルを表す[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)クラスがあります。 [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) クラスには、Excelファイル内の各ワークシートへのアクセスを可能にする[WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)が含まれます。ワークシートは[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) クラスによって表されます。[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) クラスは[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)のコレクションを提供します。[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)のコレクション内の各アイテムは、[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) クラスのオブジェクトを表します。

[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) クラスには、セルから値を取得するためのいくつかのプロパティがあります。これらのプロパティには次のものがあります:

- [StringValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#StringValue)、セルの文字列値。
- [DoubleValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#DoubleValue)、セルの倍精度浮動小数点数値を返します。
- [BoolValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#BoolValue)、セルのブール値。
- [DateTimeValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#DateTimeValue)、セルの日付/時刻値。
- [FloatValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#FloatValue)、セルの浮動小数点数値。
- [IntValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#IntValue)、セルの整数値。

また、セルに含まれるデータの種類は、[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) クラスの[Type](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Type)プロパティを使用してチェックすることもできます。実際、[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) クラスの[Type](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Type)プロパティは、[CellValueType](https://reference.aspose.com/cells/java/com.aspose.cells/CellValueType)列挙型に基づいており、その事前定義値は以下のとおりです:

|**セル値の種類**|**説明**|
| :- | :- |
|[IS_BOOL](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_BOOL)|セル値がブール値であることを示します。|
|[IS_DATE_TIME](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_DATE_TIME)|セル値が日付/時刻であることを示します。|
|[IS_ERROR](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_ERROR)|セルにエラー値が含まれていることを表します|
|[IS_NULL](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_NULL)|空白のセルを表します。
|[IS_NUMERIC](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_NUMERIC)|セル値が数値であることを示します。
|[IS_STRING](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_STRING)|セル値が文字列であることを示します。
|[IS_UNKNOWN](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_UNKNOWN)|セル値が不明であることを示します。
さらに、上記の事前定義セル値タイプを使用して、各セルに含まれるデータのタイプと比較することもできます。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-RetrievingDataFromCells-RetrievingDataFromCells.java" >}}
