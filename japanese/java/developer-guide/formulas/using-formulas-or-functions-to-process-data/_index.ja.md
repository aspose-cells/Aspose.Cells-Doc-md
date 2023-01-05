---
title: 数式または関数を使用してデータを処理する
type: docs
weight: 5
url: /ja/java/get-and-set-formula/
---
{{% alert color="primary" %}}

Microsoft Excel の魅力的な機能の 1 つは、数式と関数を使用してデータを処理できることです。 Microsoft Excel には、ユーザーが複雑な計算をすばやく実行するのに役立つ一連の組み込み関数と数式が用意されています。 Aspose.Cells には、開発者が値を簡単に計算するのに役立つ組み込み関数と数式の膨大なセットも用意されています。 Aspose.Cellsもアドイン機能に対応。さらに、Aspose.Cells は Aspose.Cells の配列と R1C1 数式をサポートします。

{{% /alert %}}

## **数式と関数の使用**

Aspose.Cells はクラスを提供し、[**ワークブック**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)、Microsoft Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスには[**ワークシート**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets)Excel ファイル内の各ワークシートにアクセスできるコレクション。ワークシートは、[**ワークシート**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラス。の[**ワークシート**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラスは[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)コレクション。の各項目[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)コレクションはのオブジェクトを表します[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell)クラス。

によって提供されるプロパティとメソッドを使用して、数式をセルに適用することができます。[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell)クラスについては、以下で詳しく説明します。

- [組み込み関数の使用](/cells/ja/java/using-formulas-or-functions-to-process-data/#using-built-in-functions).
- [アドイン機能の使用](/cells/ja/java/using-formulas-or-functions-to-process-data/#using-add-in-functions).
- [配列数式の操作](/cells/ja/java/using-formulas-or-functions-to-process-data/#using-array-formula).
- [R1C1 式の作成](/cells/ja/java/using-formulas-or-functions-to-process-data/#using-r1c1-formula).

## **組み込み関数の使用**

組み込み関数または数式は、開発者の労力と時間を削減するために既製の関数として提供されます。見る[組み込み関数のリスト](/cells/ja/java/supported-formula-functions/).関数はアルファベット順にリストされています。今後、さらに多くの機能がサポートされる予定です。

 Aspose.Cells は、Microsoft Excel で提供されるほとんどの数式または関数をサポートしています。開発者は、API または[デザイナースプレッドシート](/cells/ja/java/what-is-a-designer-spreadsheet/)Aspose.Cells は、数学、文字列、ブール、日付/時刻、統計、データベース、ルックアップ、および参照式の膨大なセットをサポートしています。

使用[**方式**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula)のプロパティ[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell)セルに数式を追加するクラス。**複雑な数式**、 例えば

{{< highlight "java" >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

、Aspose.Cells でもサポートされています。数式をセルに適用するときは、Microsoft Excel で数式を作成するときと同じように、常に等号 (=) で文字列を開始し、カンマ (,) を使用して関数パラメーターを区切ります。

以下の例では、ワークシートの最初のセルに複雑な数式が適用されています。[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)コレクション。式は組み込みの**もしも**Aspose.Cellsが提供する機能です。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-ProcessDataUsingBuiltinfunction-1.java" >}}

## **アドイン機能の使用**

Excel アドインとして含めたいユーザー定義の数式をいくつか持つことができます。設定時[**Cell.Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula)関数組み込み関数は正常に機能しますが、アドイン関数を使用してカスタム関数または数式を設定する必要があります。

 Aspose.Cells は、アドイン関数を使用して登録する機能を提供します。[**Worksheets.RegisterAddInFunction()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#registerAddInFunction(java.lang.String,%20java.lang.String,%20boolean)）。その後、設定すると[**Cell.Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) anyFunctionFromAddIn の場合、出力 Excel ファイルには AddIn 関数から計算された値が含まれます。

以下のサンプルコードのアドイン機能を登録するために、XLAM以降のファイルをダウンロードする必要があります。同様に、出力ファイル「test_udf.xlsx」をダウンロードして、出力を確認できます。

[TestUDF.xlam](TestUDF.xlam)

[test_udf.xlsx](test_udf.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Formulas-RegisterAndCallFuncFromAddIn-1.java" >}}

## **配列数式の使用**

配列数式は、数式を構成する関数の引数として、個々の数値ではなく配列を操作する数式です。配列数式を表示するときは、以下のように中かっこ ({}) で囲みます。

**セルG2に配列数式を設定する** 

![todo:画像_代替_文章](using-formulas-or-functions-to-process-data_1.png)

Microsoft 一部の Excel 関数は、値の配列を返します。配列数式を使用して複数の結果を計算するには、配列引数と同じ行数と列数のセル範囲に配列を入力します。

を呼び出して、配列数式をセルに適用することができます。[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell)クラス'[**setArray式**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setArrayFormula(java.lang.String,%20int,%20int)） 方法。の[**setArray式**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setArrayFormula(java.lang.String,%20int,%20int)メソッドは、次のパラメーターを取ります。

- **配列数式**、配列数式。
- **行の数**、配列数式の結果を入力する行数。
- **列の数**、配列数式の結果を入力する列の数。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-ProcessDataUsingArrayFunction-1.java" >}}

## **R1C1式の使用**

適用する**R1C1**セルへのスタイル式の参照[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell)クラス'[**setR1C1式**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#R1C1Formula)財産。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-ProcessDataUsingR1C1-1.java" >}}

