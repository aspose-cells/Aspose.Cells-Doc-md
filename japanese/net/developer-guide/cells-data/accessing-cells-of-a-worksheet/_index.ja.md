---
title: ワークシートのセルへのアクセス
type: docs
weight: 10
url: /ja/net/accessing-cells-of-a-worksheet/
description: この記事では、ワークシートの最大表示範囲を取得し、Aspose.Cells for .NET API を介してセルにアクセスする方法を示しています。
keywords: セルオブジェクトを取得する、セルにアクセスする、ワークシートの最大表示範囲を取得する。 
---

{{% alert color="primary" %}}

すべてのワークシートには基本的にセル（ワークシートが構成されている）に格納されているデータが含まれることを知っています。セルはワークシートの基本部分であり、ワークシート全体を行と列の連続として構築するために使用されます。ワークシートからデータにアクセスしようとする前に、そのセルにアクセスする必要があります。したがって、このトピックでは、Aspose.Cellsを使用して実行時にワークシートのセルにアクセスするための基本的なアプローチについて説明します。

{{% /alert %}}

## **セルへのアクセス方法**

Aspose.Cells は、Excel ファイルを表す [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) クラスには、Excel ファイル内の各ワークシートにアクセスするための [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) が含まれています。ワークシートは [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) クラスは、ワークシート内のすべてのセルを表す [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) コレクションを提供します。

[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) コレクションを使用してワークシート内のセルにアクセスできます。Aspose.Cells はワークシート内のセルにアクセスするために3つの基本的な方法を提供しています：

1. セル名を使用する。
1. セルの行と列のインデックスを使用します。
1. [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクション内のセルインデックスを使用する

**重要：**3番目のアプローチが最も速く、1番目のアプローチが最も遅いことを記載しました。アプローチ間のパフォーマンスの違いは非常にわずかですので、使用するアプローチについてはパフォーマンスの低下を心配しないでください。

### **セルオブジェクトの取得方法（セル名による）**

開発者は[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)クラスの[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)コレクションにセルの名前をインデックスとして渡すことで、任意の特定のセルにアクセスできます。

最初に空のワークシートを作成すると、[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクションの数はゼロになります。 このアプローチを使用してセルにアクセスする場合、このセルがコレクション内に存在するかどうかを確認します。 はいの場合、コレクション内のセルオブジェクトを返します。 そうでない場合は、新しい[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)オブジェクトを作成し、そのオブジェクトを[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクションに追加してからオブジェクトを返します。 このアプローチは、Microsoft Excelに慣れている場合にはセルへのアクセスの最も簡単な方法ですが、他のアプローチと比較して最も遅いです。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingCellName-1.cs" >}}

### **セルオブジェクトの取得方法（セルの行および列インデックスによる）**

開発者は、セルの行と列のインデックスを[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)クラスの[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)コレクションに渡すことで、任意の特定のセルにアクセスできます。

このアプローチは第1のアプローチと同じように機能します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingRowAndColumnIndexOfCell-1.cs" >}}

### **セルオブジェクトの取得方法（セルのセルインデックスによる）**

セルは、[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクションに対してセルの数値インデックスを渡すことでアクセスできます。

このアプローチを使用してセルにアクセスする場合、セルの数値インデックスが範囲外の場合、例外がスローされる可能性があります。 このアプローチを使用してセルオブジェクトにアクセスする場合、[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクションへの新しいセルが追加されると数値インデックスが変更される可能性があることを知っておくことは重要です。 [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクション内のセルオブジェクトは、内部的に行と列のインデックスでソートされます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingCellIndexInCellsCollection-1.cs" >}}

## **ワークシートの最大表示範囲の取得方法**

Aspose.Cellsは、ワークシートの最大表示範囲にアクセスすることができます。最大表示範囲(コンテンツを持つ最初のセルと最後のセルの範囲)は、ワークシート全体の内容をコピー、選択、または表示する必要がある場合に便利です。

ワークシートの最大表示範囲には[**Worksheet.Cells.MaxDisplayRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange)を使用してアクセスできます。 次のサンプルコードは、[**MaxDisplayRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange)プロパティにアクセスする方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-AccessingMaximumDisplayRangeofWorksheet-1.cs" >}}
