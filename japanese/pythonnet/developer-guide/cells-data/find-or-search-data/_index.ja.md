---
title: データの検索または検索
type: docs
weight: 50
url: /ja/python-net/find-or-search-data/
description: Aspose.Cells for Python via .NET APIを通じて指定されたデータを含むワークシート内のセルを見つけたり検索する方法を学ぶ。
keywords: Python Excelライブラリ、Pythonでのデータ検索、Pythonでのデータ検索、PythonでのFormulaを含むセルの検索、PythonでのFormulaを含むセルの検索、PythonのFindOptionsを使用したデータまたはFormulasの検索、PythonのFindOptionsを使用したデータまたはFormulasの検索、指定された文字列値または数値を含むセルの検索、指定されたデータを含むセルの検索
---

{{% alert color="primary" %}}

Microsoft Excelでは、ユーザーが指定されたデータを含むワークシート内のセルを検索することができます。

{{% /alert %}}

## **指定されたデータを含むセルの検索**

### **Microsoft Excel の使用**

Microsoft Excelでは、ワークシート内の含まれる指定されたデータを持つセルを検索できます。Microsoft Excelの**検索**メニューから**編集**を選択すると、検索値を指定できるダイアログが表示されます。

ここでは、「オレンジ」の値を検索しています。Aspose.Cellsでは、指定された値を含むワークシート内のセルを検索できます。

### **Aspose.Cellsの使用**

Aspose.Cellsは、Microsoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)クラスには、Excelファイル内の各ワークシートにアクセスできる[**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets)コレクションが含まれています。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスにはワークシート内のすべてのセルを表す[**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells)コレクションが含まれており、[**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells)コレクションにはユーザー指定データを含むワークシート内のセルを検索するためのいくつかのメソッドが提供されています。これらのメソッドのいくつかについて詳しく説明します。

{{% alert color="primary" %}}

すべての検索メソッドは、指定されたデータを検索するセルの参照を返します。

{{% /alert %}}

## **指定された数式を含むセルの検索**

開発者は、[**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells)コレクションの[**find**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/find/#any-aspose.cells.Cell-aspose.cells.FindOptions)メソッドを呼び出すことによって、ワークシート内で指定された数式を検索できます。通常、[**find**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/find/#any-aspose.cells.Cell-aspose.cells.FindOptions)メソッドは3つのパラメータを受け入れます。

- **what:** 検索するオブジェクト。タイプはint、double、DateTime、string、boolである必要があります。
- **previous_cell:** 同じオブジェクトを持つ前のセル。このパラメータは、開始位置から検索する場合はnullに設定できます。
- **find_options:** 必要なオブジェクトを検索するためのオプション。

以下の例では、検索メソッドの練習にワークシートデータを使用します:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FindingCellsContainingFormula-1.py" >}}

## **FindOptionsを使用したデータまたは式の検索**

異なる[**FindOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/findoptions)を使用して、[**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells)の[**find**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/find/#any-aspose.cells.Cell-aspose.cells.FindOptions)メソッドを使用して指定した値を検索することが可能です。通常、[**find**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/find/#any-aspose.cells.Cell-aspose.cells.FindOptions)メソッドは次のパラメータを受け入れます:

- **what:**、検索対象のデータまたは値。
- **previous_cell**、同じ値を含む最後のセル。このパラメータは、開始位置から検索する場合はnullに設定できます。
- **find_options**、検索オプション。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FindingDataOrFormulasUsingFindOptions-1.py" >}}

## **指定された文字列値を見つけることが可能です。異なる{2}を持つ{1}コレクション内に見つかった{0}メソッドを呼び出すことで。**

異なる[**FindOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/findoptions)を持つ[**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells)コレクションの中で見つかった[**find**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/find/#any-aspose.cells.Cell-aspose.cells.FindOptions)メソッドを呼び出すことで、指定された文字列値を見つけることが可能です。

[**FindOptions.look_in_type**](https://reference.aspose.com/cells/python-net/aspose.cells/findoptions/look_in_type/)と[**FindOptions.look_at_type**](https://reference.aspose.com/cells/python-net/aspose.cells/findoptions/look_at_type/)プロパティを指定します。次の例コードは、これらのプロパティを使用してセル内の文字列の**先頭**、または**中央**、または**末尾**にさまざまな数の文字列を探す方法を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FindingCellsContainingStringValueOrNumber-1.py" >}}

## **高度なトピック**
- [指定したスタイルのセルを見つける](/cells/ja/python-net/find-cells-with-specific-style/)
- [セルの値がシングルクォートマークで始まるかどうかを検索](/cells/ja/python-net/find-if-the-cell-value-starts-with-single-quote-mark/)
- [元の値を使用したデータの検索](/cells/ja/python-net/search-data-using-original-values/)
