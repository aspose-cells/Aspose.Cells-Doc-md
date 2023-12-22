---
title: Excelファイルの数式を管理する
linktitle: 数式
type: docs
weight: 122
url: /ja/net/using-formulas-or-functions-to-process-data/
description: Aspose.Cells は、Excel ファイルの数式を簡単に取得、設定、計算できます。
description: NET API の Aspose.Cells を使用して Excel ファイルの数式を管理する方法を学習します。
keywords: How to calculate formulas in C#, Formulas and Functions using C#, C# Manage Built-in Functions, How to Use Add-in Functions with C#, How to Use Array Formula via C#, How to Use R1C1 Formula in C#.
---
##  **導入**

Microsoft Excel の魅力的な機能の 1 つは、数式や関数を使用してデータを処理できることです。 Microsoft Excel には、ユーザーが複雑な計算を迅速に実行できるようにする一連の組み込み関数と数式が用意されています。 Aspose.Cells には、開発者が値を簡単に計算できるようにする膨大な組み込み関数と数式のセットも提供されています。 Aspose.Cells はアドイン機能もサポートしています。さらに、Aspose.Cells は Aspose.Cells の配列と R1C1 式をサポートしています。

##  **数式と関数の使用方法**

Aspose.Cells はクラスを提供します。[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)、これは Microsoft Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Excel ファイル内の各ワークシートへのアクセスを許可するコレクション。ワークシートは次のように表されます。[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス。の[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスが提供するのは[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクション。 Cells コレクション内の各項目は、[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)クラス。

によって提供されるプロパティとメソッドを使用してセルに数式を適用することができます。[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)クラスについては、以下で詳しく説明します。

- 組み込み関数の使用。
- アドイン機能を利用する。
- 配列数式の操作。
- R1C1 式を作成します。

##  **組み込み関数の使用方法**

組み込み関数または数式は、開発者の労力と時間を削減するために既製の関数として提供されます。見る[組み込み関数のリスト](/cells/ja/net/supported-formula-functions/)Aspose.Cells でサポートされています。関数はアルファベット順にリストされています。将来的にはさらに多くの機能がサポートされる予定です。

 Aspose.Cells は、Microsoft Excel が提供するほとんどの数式または関数をサポートしています。開発者は、API または[デザイナースプレッドシート](/cells/ja/net/what-is-a-designer-spreadsheet/)。 Aspose.Cells は、数学、文字列、ブール、日付/時刻、統計、データベース、検索および参照の数式の膨大なセットをサポートしています。

使用[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)クラス'[**式**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula)プロパティを使用してセルに数式を追加します。 *複雑な数式** など

{{< highlight "java" >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

、Aspose.Cells でもサポートされています。セルに数式を適用するときは、Microsoft Excel で数式を作成するときと同じように、必ず文字列を等号 (=) で始め、カンマ (,) を使用して関数パラメータを区切ります。

以下の例では、複雑な数式がワークシートの最初のセルに適用されます。[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクション。数式は組み込みを使用します**IF**Aspose.Cells によって提供される機能。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingBuiltinfunction-1.cs" >}}

##  **アドイン機能の使い方**

Excel アドインとして含めたいユーザー定義の数式をいくつか用意できます。セルを設定する場合、数式関数の組み込み関数は正常に動作しますが、アドイン関数を使用してカスタム関数または数式を設定する必要があります。

 Aspose.Cells は、を使用してアドイン関数を登録する機能を提供します。[**Worksheets.RegisterAddInFunction()**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/registeraddinfunction/index)。その後、 cell.Formula = anyFunctionFromAddIn を設定すると、出力 Excel ファイルには、AddIn 関数からの計算値が含まれます。

以下のサンプルコードでアドイン機能を登録するには、以下のXLAMファイルをダウンロードします。同様に、出力ファイル「test_udf.xlsx」をダウンロードして出力を確認できます。

[テストUDF.xlam](81920908.xlam)

[test_udf.xlsx](81920909.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-RegisterAndCallFuncFromAddIn-1.cs" >}}

##  **配列数式の使用方法**

配列数式は、数式を構成する関数の引数として、個々の数値ではなく配列を受け取る数式です。配列数式を表示する場合は、中括弧 ({}) で囲まれます。

一部の Microsoft Excel 関数は値の配列を返します。配列数式を使用して複数の結果を計算するには、配列引数と同じ行数と列数を持つセル範囲に配列を入力します。

を呼び出すことで、配列数式をセルに適用できます。[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)クラス'[**配列式の設定**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setarrayformula)方法。の[**配列式の設定**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setarrayformula)メソッドは次のパラメータを受け取ります。

- *配列式**、配列式。
- *行数**、配列数式の結果を入力する行数。
- *列数**、配列数式の結果を入力する列の数。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingArrayFunction-1.cs" >}}

##  **R1C1公式の使い方**

を追加**R1C1**スタイル式をセルに参照するには、[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)クラス'[**R1C1式**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/r1c1formula)財産。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingR1C1-1.cs" >}}

##  **アドバンストトピック**
- [先例と扶養家族](/cells/ja/net/precedents-and-dependents/)
- [数式に外部リンクを設定する](/cells/ja/net/set-external-links-in-formulas/)
- [新しい行にデータを入力するときに、テーブルまたはリスト オブジェクトに式を自動的に反映します](/cells/ja/net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)
- [名前付き範囲の式を設定する](/cells/ja/net/setting-formula-for-named-range/)
- [数式の設定 - 英語以外のユーザーへの注意](/cells/ja/net/setting-formulas-notice-for-non-english-users/)
- [共有計算式の設定](/cells/ja/net/setting-shared-formula/)
- [共有数式の最大行の指定](/cells/ja/net/specify-maximum-rows-of-shared-formula/)
- [サポートされている Excel 関数](/cells/ja/net/supported-formula-functions/)

