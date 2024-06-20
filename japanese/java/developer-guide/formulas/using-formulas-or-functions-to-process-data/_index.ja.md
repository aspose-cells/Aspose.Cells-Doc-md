---
title: フォーミュラや関数を使用してデータを処理する
type: docs
weight: 5
url: /ja/java/get-and-set-formula/
---

{{% alert color="primary" %}}

Microsoft Excel の魅力的な機能の1つは、フォーミュラや関数を使用してデータを処理する能力です。Microsoft Excel は、複雑な計算を迅速に実行するための組み込みの関数とフォーミュラのセットを提供します。Aspose.Cells も、開発者が値を簡単に計算できる大規模な組み込みの関数とフォーミュラを提供します。また、Aspose.Cells はアドイン関数をサポートします。さらに、Aspose.Cells は Aspose.Cells での配列および R1C1 フォーミュラをサポートします。

{{% /alert %}}

## **フォーミュラと関数を使用する**

Aspose.Cells は Microsoft Excel ファイルを表す [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) クラスは Excel ファイル内の各ワークシートにアクセスを可能にする [**Worksheets**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets) コレクションを含みます。ワークシートは [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) クラスは [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) コレクションを提供します。[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) コレクションの各アイテムは [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) クラスのオブジェクトを表します。

[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) クラスが提供するプロパティやメソッドを使用してセルにフォーミュラを適用することができます。詳細は以下で議論されます。

- [組み込みの関数を使用する](/cells/ja/java/using-formulas-or-functions-to-process-data/#using-built-in-functions)
- [アドイン関数を使用する](/cells/ja/java/using-formulas-or-functions-to-process-data/#using-add-in-functions)
- [配列フォーミュラを使用する](/cells/ja/java/using-formulas-or-functions-to-process-data/#using-array-formula)
- [R1C1形式の数式の作成](/cells/ja/java/using-formulas-or-functions-to-process-data/#using-r1c1-formula)。

## **組み込み関数の使用**

組み込みの関数または数式は、開発者の努力と時間を削減するために準備された関数です。[組み込みの関数の一覧](/cells/ja/java/supported-formula-functions/)をご覧ください。 関数はアルファベット順にリストされています。将来的にはさらに多くの関数がサポートされます。

Aspose.Cellsは、Microsoft Excelが提供するほとんどの数式または関数をサポートしています。 開発者はAPIまたは[デザイナースプレッドシート](/cells/ja/java/what-is-a-designer-spreadsheet/)を通じてこれらの数式を使用できます。 Aspose.Cellsは、数学、文字列、ブール、日付/時刻、統計、データベース、検索、参照の数式の豊富なセットをサポートしています。

セルに数式を追加するには、[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell)クラスの[**Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula)プロパティを使用します。たとえば、**複雑な数式**。

{{< highlight java >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

、Aspose.Cellsでは複雑な数式もサポートされています。セルに数式を適用する際は、常に文字列を等号（=）で始めてマイクロソフトExcelで数式を作成するときと同様に関数パラメータを区切るためにコンマ（,）を使用してください。

以下の例では、ワークシートの[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)コレクションの最初のセルに複雑な数式が適用されています。この数式では、Aspose.Cellsで提供される組み込みの**IF**関数が使用されています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-ProcessDataUsingBuiltinfunction-1.java" >}}

## **アドイン関数の使用**

Excelアドインとして含めたいユーザー定義の数式があるかもしれません。[**Cell.Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula)関数を設定すると組み込み関数は正常に動作しますが、アドイン関数を設定する必要があります。

Aspose.Cellsは[**Worksheets.RegisterAddInFunction()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#registerAddInFunction(java.lang.String,%20java.lang.String,%20boolean))を使用してアドイン関数を登録する機能を提供しています。その後、[**Cell.Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) = anyFunctionFromAddInとすると、出力されるExcelファイルにはアドイン関数からの計算された値が含まれます。

以下のサンプルコードでは、アドイン関数の登録を行います。同様に、「test_udf.xlsx」という出力ファイルをダウンロードして結果を確認することもできます。

[TestUDF.xlam](TestUDF.xlam)

[test_udf.xlsx](test_udf.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Formulas-RegisterAndCallFuncFromAddIn-1.java" >}}

## **配列数式の使用**

配列数式は、数式を構成する関数への個々の数値の代わりに配列と連動する数式です。配列数式が表示されると、以下に示すように波括弧（{}）で囲まれています。

**セルG2に配列数式を設定** 

![todo:image_alt_text](using-formulas-or-functions-to-process-data_1.png)

いくつかのMicrosoft Excel関数は値の配列を返します。配列数式を使用して複数の結果を計算するには、配列を配列引数と同じ行数および列数のセル範囲に入力してください。

配列数式をセルに適用するには、[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell)クラスの[**setArrayFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setArrayFormula(java.lang.String,%20int,%20int))メソッドを呼び出すことができます。[**setArrayFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setArrayFormula(java.lang.String,%20int,%20int))メソッドは次のパラメータを取ります。

- **配列数式**、配列数式。
- **行数**、配列数式の結果を設定する行数。
- **列数**、配列数式の結果を設定する列数。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-ProcessDataUsingArrayFunction-1.java" >}}

## **R1C1形式の数式の使用**

R1C1参照スタイルの数式を、[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell)クラスの[**setR1C1Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#R1C1Formula)プロパティを使用してセルに適用します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-ProcessDataUsingR1C1-1.java" >}}

