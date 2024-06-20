---
title: データの検索または検索
type: docs
weight: 50
url: /ja/net/find-or-search-data/
description: Aspose.Cells for .NET APIを介して特定のデータを含むワークシート内のセルを検索する方法を学習します。
keywords: データを検索、データをサーチ、数式を含むセルを見つける、数式を含むセルを検索する、FindOptionsを使用してデータまたは数式を検索する、特定の文字列値や数字を含むセルを検索する、特定のデータを含むセルを検索する
---

{{% alert color="primary" %}}

Microsoft Excelでは、ユーザーが指定されたデータを含むワークシート内のセルを検索することができます。

{{% /alert %}}

## **指定されたデータを含むセルの検索**

### **Microsoft Excel の使用**

Microsoft Excelでは、ワークシート内の含まれる指定されたデータを持つセルを検索できます。Microsoft Excelの**検索**メニューから**編集**を選択すると、検索値を指定できるダイアログが表示されます。

ここでは、「オレンジ」の値を検索しています。Aspose.Cellsでは、指定された値を含むワークシート内のセルを検索できます。

### **Aspose.Cellsの使用**

Aspose.Cellsは、Microsoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには、Excelファイル内の各ワークシートにアクセスできる[**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)コレクションが含まれています。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスにはワークシート内のすべてのセルを表す[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクションが含まれており、[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクションにはユーザー指定データを含むワークシート内のセルを検索するためのいくつかのメソッドが提供されています。これらのメソッドのいくつかについて詳しく説明します。

{{% alert color="primary" %}}

すべての検索メソッドは、指定されたデータを検索するセルの参照を返します。

{{% /alert %}}

## **指定された数式を含むセルの検索**

開発者は、[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクションの[**Find**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index)メソッドを呼び出すことによって、ワークシート内で指定された数式を検索できます。通常、[**Find**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index)メソッドは3つのパラメータを受け入れます。

- **オブジェクト:** 検索するオブジェクト。型はint、double、DateTime、string、boolである必要があります。
- **前のセル:** 同じオブジェクトを持つ前のセル。最初から検索する場合は、このパラメーターをnullに設定できます。
- FindOptions: 必要なオブジェクトを見つけるためのオプション。

以下の例では、検索メソッドの練習にワークシートデータを使用します:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingCellsContainingFormula-1.cs" >}}

## **FindOptionsを使用したデータまたは式の検索**

異なる[**FindOptions**](https://reference.aspose.com/cells/net/aspose.cells/findoptions)を使用して、[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)の[**Find**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index)メソッドを使用して指定した値を検索することが可能です。通常、[**Find**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index)メソッドは次のパラメータを受け入れます:

- **検索値**、検索するデータまたは値。
- **前のセル**、同じ値を含んでいた最後のセル。最初から検索する場合は、このパラメーターをnullに設定できます。
- **検索オプション**、検索オプション。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingDataOrFormulasUsingFindOptions-1.cs" >}}

## **指定された文字列値を見つけることが可能です。異なる{2}を持つ{1}コレクション内に見つかった{0}メソッドを呼び出すことで。**

異なる[**FindOptions**](https://reference.aspose.com/cells/net/aspose.cells/findoptions)を持つ[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクションの中で見つかった[**Find**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index)メソッドを呼び出すことで、指定された文字列値を見つけることが可能です。

[**FindOptions.LookInType**](https://reference.aspose.com/cells/net/aspose.cells/findoptions/properties/lookintype)と[**FindOptions.LookAtType**](https://reference.aspose.com/cells/net/aspose.cells/findoptions/properties/lookattype)プロパティを指定します。次の例コードは、これらのプロパティを使用してセル内の文字列の**先頭**、または**中央**、または**末尾**にさまざまな数の文字列を探す方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingCellsContainingStringValueOrNumber-1.cs" >}}

## **高度なトピック**
- [指定したスタイルのセルを見つける](/cells/ja/net/find-cells-with-specific-style/)
- [セルの値がシングルクォートマークで始まるかどうかを検索](/cells/ja/net/find-if-the-cell-value-starts-with-single-quote-mark/)
- [元の値を使用したデータの検索](/cells/ja/net/search-data-using-original-values/)
