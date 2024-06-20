---
title: Excelファイルの数式を管理する
linktitle: 数式
type: docs
weight: 122
url: /ja/net/using-formulas-or-functions-to-process-data/
description: Aspose.CellsはExcelファイルの数式を簡単に取得、設定、および計算できます。
description: Aspose.Cells for NET APIを通じてExcelファイルの数式を管理する方法を学ぶ。
keywords: C# で数式を計算する方法、C# を使用した数式と関数、C# での組み込み関数の管理、C# でのアドイン関数の使用方法、C# を介した配列式の使用方法、C# での R1C1 数式の使用方法。
---

## **紹介**

Microsoft Excel の魅力的な機能の1つは、数式と関数を使ってデータを処理する能力です。Microsoft Excel は、複雑な計算を迅速に行うための組み込み関数と数式を提供しています。Aspose.Cells も、開発者が値を簡単に計算できるようにする豊富な組み込み関数と数式を提供しています。Aspose.Cells はアドイン関数もサポートしています。さらに、Aspose.Cells は Aspose.Cells での配列と R1C1 数式もサポートしています。

## **数式と関数の使用方法**

Aspose.Cells は、Microsoft Excel ファイルを表す [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) クラスには、Excel ファイル内の各ワークシートにアクセスするための [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) コレクションが含まれています。ワークシートは [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) クラスは [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) コレクションを提供します。Cells コレクション内の各アイテムは、[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) クラスのオブジェクトを表します。

詳細については、[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) クラスが提供するプロパティとメソッドを使用してセルに数式を適用することが可能です。

- 組み込み関数の使用。
- アドイン関数の使用。
- 配列式の操作。
- R1C1 数式の作成。

## **組み込み関数の使用方法**

組み込み関数や数式は、開発者の労力と時間を削減するために提供される使用準備が整った関数です。Aspose.Cells でサポートされる [組み込み関数のリスト](/cells/ja/net/supported-formula-functions/)。関数はアルファベット順にリストされています。将来的には、さらに多くの関数がサポートされる予定です。

Aspose.Cells は、Microsoft Excel が提供するほとんどの数式や関数をサポートしています。開発者は、API または [デザイナースプレッドシート](/cells/ja/net/what-is-a-designer-spreadsheet/) を介してこれらの数式を使用できます。Aspose.Cells は、数学、文字列、真偽値、日付/時刻、統計、データベース、検索と参照などの豊富な数式をサポートしています。

セルに数式を追加するためには、[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) クラスの [**Formula**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula) プロパティを使用します。例えば **複雑な数式** など

{{< highlight java >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

、Aspose.Cellsでは複雑な数式もサポートされています。セルに数式を適用する際は、常に文字列を等号（=）で始めてマイクロソフトExcelで数式を作成するときと同様に関数パラメータを区切るためにコンマ（,）を使用してください。

以下の例では、ワークシートの [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) コレクションの最初のセルに複雑な数式が適用されています。この数式は、Aspose.Cells が提供する組み込みの **IF** 関数を使用しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingBuiltinfunction-1.cs" >}}

## **アドイン関数の使用方法**

Excel アドインとして含めたいユーザー定義の数式を持つことができます。セル.Formula 関数を使用すると組み込み関数は正常に動作しますが、アドイン関数を使用してカスタム関数や数式を設定する必要があります。

Aspose.Cells は、[**Worksheets.RegisterAddInFunction()**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/registeraddinfunction/index) を使用してアドイン関数を登録する機能を提供します。その後、cell.Formula = anyFunctionFromAddIn と設定すると、出力される Excel ファイルには、アドイン関数から計算された値が含まれます。

以下のサンプルコードの中でアドイン関数を登録するために XLAM ファイルをダウンロードできます。同様に、出力ファイル "test_udf.xlsx" もダウンロードして出力を確認することができます。

[TestUDF.xlam](81920908.xlam)

[test_udf.xlsx](81920909.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-RegisterAndCallFuncFromAddIn-1.cs" >}}

## **配列式の使用方法**

配列式は、数式を構成する関数に個々の数値ではなく配列を引数として取る数式です。配列式が表示されると、括弧({})で囲まれています。

いくつかのMicrosoft Excel関数は値の配列を返します。配列数式を使用して複数の結果を計算するには、配列を配列引数と同じ行数および列数のセル範囲に入力してください。

配列式をセルに適用するには、[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) クラスの [**SetArrayFormula**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setarrayformula) メソッドを呼び出します。[**SetArrayFormula**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setarrayformula) メソッドは以下のパラメータを取ります:

- **配列数式**、配列数式。
- **行数**、配列数式の結果を設定する行数。
- **列数**, 配列式の結果を入力する列数。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingArrayFunction-1.cs" >}}

## **R1C1 数式の使用方法**

セルに **R1C1** 参照スタイルの数式を [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) クラスの [**R1C1Formula**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/r1c1formula) プロパティを使用して追加します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingR1C1-1.cs" >}}

## **高度なトピック**
- [先行および後行](/cells/ja/net/precedents-and-dependents/)
- [数式で外部リンクを設定する](/cells/ja/net/set-external-links-in-formulas/)
- [新しい行にデータを入力する際に、表やリストオブジェクトの式を自動的に伝播させる](/cells/ja/net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)
- [名前付き範囲の式の設定](/cells/ja/net/setting-formula-for-named-range/)
- [数式の設定 - 英語以外のユーザーへの通知](/cells/ja/net/setting-formulas-notice-for-non-english-users/)
- [共有数式の設定](/cells/ja/net/setting-shared-formula/)
- [共有式の最大行数を指定](/cells/ja/net/specify-maximum-rows-of-shared-formula/)
- [サポートされているExcel関数](/cells/ja/net/supported-formula-functions/)

