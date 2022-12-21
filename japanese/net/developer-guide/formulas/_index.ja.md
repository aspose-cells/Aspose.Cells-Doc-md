---
title: Excel ファイルの数式を管理する
linktitle: 数式
type: docs
weight: 122
url: /ja/net/using-formulas-or-functions-to-process-data/
description: Aspose.Cells は、Excel ファイルの数式を簡単に取得、設定、および計算できます。
---
## **序章**

Microsoft Excel の魅力的な機能の 1 つは、数式と関数を使用してデータを処理できることです。 Microsoft Excel には、ユーザーが複雑な計算をすばやく実行するのに役立つ一連の組み込み関数と数式が用意されています。 Aspose.Cells には、開発者が値を簡単に計算するのに役立つ組み込み関数と数式の膨大なセットも用意されています。 Aspose.Cellsもアドイン機能に対応。さらに、Aspose.Cells は Aspose.Cells の配列と R1C1 数式をサポートします。

## **数式と関数の使用**

Aspose.Cells はクラスを提供し、[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)、Microsoft Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Excel ファイル内の各ワークシートにアクセスできるコレクション。ワークシートは、[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス。の[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスは[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクション。 Cells コレクションの各アイテムは、[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)クラス。

によって提供されるプロパティとメソッドを使用して、数式をセルに適用することができます。[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)クラスについては、以下で詳しく説明します。

- 組み込み関数の使用。
- アドイン機能の使用。
- 配列数式の操作。
- R1C1 フォーミュラの作成。

## **組み込み関数の使用**

組み込み関数または数式は、開発者の労力と時間を削減するために既製の関数として提供されます。見る[組み込み関数のリスト](/cells/ja/net/supported-formula-functions/) Aspose.Cells でサポートされています。関数はアルファベット順にリストされています。今後、さらに多くの機能がサポートされる予定です。

 Aspose.Cells は、Microsoft Excel で提供されるほとんどの数式または関数をサポートしています。開発者は、API または[デザイナースプレッドシート](/cells/ja/net/what-is-a-designer-spreadsheet/). Aspose.Cells は、数学、文字列、ブール、日付/時刻、統計、データベース、ルックアップ、および参照式の膨大なセットをサポートしています。

使用[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)クラス'[**方式**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula)セルに数式を追加するプロパティ。**複雑な数式**、 例えば

{{< highlight "java" >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

、Aspose.Cells でもサポートされています。数式をセルに適用するときは、Microsoft Excel で数式を作成するときと同じように、常に等号 (=) で文字列を開始し、カンマ (,) を使用して関数パラメーターを区切ります。

以下の例では、ワークシートの最初のセルに複雑な数式が適用されています。[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクション。式は組み込みの**もしも**Aspose.Cellsが提供する機能です。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingBuiltinfunction-1.cs" >}}

## **アドイン機能の使用**

Excelアドインとして含めたいユーザー定義の数式をいくつか持つことができます。 cell.Formula 関数を設定する場合、組み込み関数は正常に機能しますが、アドイン関数を使用してカスタム関数または数式を設定する必要があります。

 Aspose.Cells は、アドイン関数を使用して登録する機能を提供します。[**Worksheets.RegisterAddInFunction()**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/registeraddinfunction/index).その後、cell.Formula = anyFunctionFromAddIn を設定すると、出力 Excel ファイルには AddIn 関数から計算された値が含まれます。

以下のサンプルコードのアドイン機能を登録するために、以下のXLAMファイルをダウンロードする必要があります。同様に、出力ファイル「test_udf.xlsx」をダウンロードして、出力を確認できます。

[TestUDF.xlam](81920908.xlam)

[test_udf.xlsx](81920909.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-RegisterAndCallFuncFromAddIn-1.cs" >}}

## **配列数式の使用**

配列数式は、数式を構成する関数への引数として、個々の数値ではなく配列を取る数式です。配列数式を表示するときは、中かっこ ({}) で囲みます。

Microsoft 一部の Excel 関数は、値の配列を返します。配列数式を使用して複数の結果を計算するには、配列引数と同じ行数と列数のセル範囲に配列を入力します。

を呼び出して、配列数式をセルに適用することができます。[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)クラス'[**SetArray式**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setarrayformula)方法。の[**SetArray式**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setarrayformula)メソッドは次のパラメータを取ります。

- **配列数式**、配列数式。
- **行の数**、配列数式の結果を入力する行数。
- **列の数**、配列数式の結果を入力する列の数。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingArrayFunction-1.cs" >}}

## **R1C1式の使用**

を追加**R1C1**セルへのスタイル式の参照[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)クラス'[**R1C1式**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/r1c1formula)財産。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingR1C1-1.cs" >}}

## **先行トピック**
- [先例と扶養家族](/cells/ja/net/precedents-and-dependents/)
- [数式で外部リンクを設定する](/cells/ja/net/set-external-links-in-formulas/)
- [新しい行にデータを入力しながら、テーブルまたはリスト オブジェクトに数式を自動的に適用する](/cells/ja/net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)
- [名前付き範囲の数式の設定](/cells/ja/net/setting-formula-for-named-range/)
- [数式の設定 - 英語以外のユーザーへの通知](/cells/ja/net/setting-formulas-notice-for-non-english-users/)
- [共有式の設定](/cells/ja/net/setting-shared-formula/)
- [共有数式の最大行を指定する](/cells/ja/net/specify-maximum-rows-of-shared-formula/)
- [サポートされている Excel 関数](/cells/ja/net/supported-formula-functions/)

