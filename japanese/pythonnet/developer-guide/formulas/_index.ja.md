---
title: Excelファイルの数式を管理する
linktitle: 数式
type: docs
weight: 122
url: /ja/python-net/using-formulas-or-functions-to-process-data/
description: Aspose.Cells for Python via .NETは、単純にExcelファイルの数式を取得、設定、計算することができます。
description: Aspose.Cells for Python via .NET for NET APIを使ったExcelの数式管理方法について学びましょう。
keywords: Pythonで数式を計算する方法、Pythonでの数式と関数、Pythonでビルトイン関数を管理する方法、Pythonでアドイン関数を使用する方法、Python経由で配列数式を使用する方法、PythonでR1C1形式の数式を利用する方法。
---

## **紹介**

Microsoft Excelの魅力の一つは、数式と関数を用いてデータを処理できる点にあります。Microsoft Excelは、複雑な計算を迅速に行うための多数の組み込み関数と数式を提供します。Aspose.Cells for Python via .NETも、多くの組み込み関数と数式を備えており、開発者が値を簡単に計算できるようサポートします。さらにAspose.Cells for Python via .NETはアドイン関数もサポートしています。さらに、配列およびR1C1数式もサポートしています。

## **数式と関数の使用方法**

Aspose.Cells for Python via .NETは、Microsoft Excelファイルを表すクラス、[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)を提供します。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)クラスは、Excelファイル内の各ワークシートにアクセスできる[**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets)コレクションを含みます。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスで表現されます。[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスは、[**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells)コレクションを提供します。Cellsコレクションの各アイテムは、[**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell)クラスのオブジェクトを表します。

詳細については、[**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) クラスが提供するプロパティとメソッドを使用してセルに数式を適用することが可能です。

- 組み込み関数の使用。
- アドイン関数の使用。
- 配列式の操作。
- R1C1 数式の作成。

## **組み込み関数の使用方法**

組み込み関数や数式は、開発者の努力と時間を削減するためのあらかじめ用意された関数として提供されます。[Aspose.Cells for Python via .NETがサポートする組み込み関数の一覧](/cells/ja/python-net/supported-formula-functions/)を参照してください。これらの関数はアルファベット順にリストされています。今後もサポートされる関数が追加されていきます。

Aspose.Cells for Python via .NET は、Microsoft Excelで提供されるほとんどの数式や関数をサポートしています。開発者はこれらの数式をAPIを通じてまたは[デザイナースプレッドシート](/cells/ja/net/what-is-a-designer-spreadsheet/)を利用して使用できます。Aspose.Cells for Python via .NET は、膨大な数学、文字列、ブーリアン、日時、統計、データベース、検索および参照の数式をサポートします。

セルに数式を追加するためには、[**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) クラスの [**formula**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/formula) プロパティを使用します。例えば **複雑な数式** など

{{< highlight java >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

また、Aspose.Cells for Python via .NET では`IF`関数を含む関数もサポートされています。セルに数式を適用する際は、Microsoft Excelと同じように常に等号（=）で文字列を始め、関数のパラメータを区切るためにカンマ（,）を使用してください。

下記の例では、複雑な数式をワークシートの[**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)コレクションの最初のセルに適用しています。この数式は、Aspose.Cells for Python via .NETが提供するビルトインの **IF** 関数を使用しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-ProcessDataUsingBuiltinfunction-1.py" >}}

## **アドイン関数の使用方法**

Excel アドインとして含めたいユーザー定義の数式を持つことができます。セル.Formula 関数を使用すると組み込み関数は正常に動作しますが、アドイン関数を使用してカスタム関数や数式を設定する必要があります。

Aspose.Cells for Python via .NET は、[**worksheets.register_add_in_function()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/register_add_in_function)を使用してアドイン関数を登録する機能を提供します。その後、セル.Formula に anyFunctionFromAddIn を設定すると、出力されるExcelファイルにはアドイン関数からの計算結果が含まれます。

以下のサンプルコードの中でアドイン関数を登録するために XLAM ファイルをダウンロードできます。同様に、出力ファイル "test_udf.xlsx" もダウンロードして出力を確認することができます。

[TestUDF.xlam](81920908.xlam)

[test_udf.xlsx](81920909.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-RegisterAndCallFuncFromAddIn-1.py" >}}

## **配列式の使用方法**

配列式は、数式を構成する関数に個々の数値ではなく配列を引数として取る数式です。配列式が表示されると、括弧({})で囲まれています。

いくつかのMicrosoft Excel関数は値の配列を返します。配列数式を使用して複数の結果を計算するには、配列を配列引数と同じ行数および列数のセル範囲に入力してください。

配列式をセルに適用するには、[**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) クラスの [**set_array_formula**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_array_formula) メソッドを呼び出します。[**set_array_formula**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_array_formula) メソッドは以下のパラメータを取ります:

- **配列数式**、配列数式。
- **行数**、配列数式の結果を設定する行数。
- **列数**, 配列式の結果を入力する列数。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-ProcessDataUsingArrayFunction-1.py" >}}

## **R1C1 数式の使用方法**

セルに **R1C1** 参照スタイルの数式を [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) クラスの [**r1c1_formula**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/r1c1_formula) プロパティを使用して追加します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-ProcessDataUsingR1C1-1.py" >}}

## **高度なトピック**
- [先行および後行](/cells/ja/python-net/precedents-and-dependents/)
- [数式で外部リンクを設定する](/cells/ja/python-net/set-external-links-in-formulas/)
- [新しい行にデータを入力する際に、表やリストオブジェクトの式を自動的に伝播させる](/cells/ja/python-net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)
- [名前付き範囲の式の設定](/cells/ja/python-net/setting-formula-for-named-range/)
- [数式の設定 - 英語以外のユーザーへの通知](/cells/ja/python-net/setting-formulas-notice-for-non-english-users/)
- [共有数式の設定](/cells/ja/python-net/setting-shared-formula/)
- [共有式の最大行数を指定](/cells/ja/python-net/specify-maximum-rows-of-shared-formula/)
- [サポートされているExcel関数](/cells/ja/python-net/supported-formula-functions/)


{{< app/cells/assistant language="python-net" >}}
