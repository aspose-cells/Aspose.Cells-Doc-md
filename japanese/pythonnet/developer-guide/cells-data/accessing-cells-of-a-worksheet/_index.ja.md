---
title: ワークシートのセルへのアクセス
type: docs
weight: 10
url: /ja/python-net/accessing-cells-of-a-worksheet/
description: この記事では、Aspose.Cells for Python via .NET APIを使用してワークシートの最大表示範囲を取得し、セルにアクセスする方法を示します。
keywords: Python Excelライブラリ、セルオブジェクトの取得、セルのアクセス、セルオブジェクトの行と列インデックスによる取得、セルインデックスによるセルオブジェクトの取得、ワークシートの最大表示範囲の取得。 
---

{{% alert color="primary" %}}

すべてのワークシートには基本的にセルに格納されたデータが含まれることを知っています（ワークシートは、セルから構成されています）。 セルはワークシート全体を行と列のシーケンスとして構築するために使用されるワークシートの基本的な部分です。 ワークシートからデータにアクセスしようとする前に、そのセルにアクセスする必要があります。 したがって、このトピックでは、実行時にAspose.Cells for Python via .NETを使用してワークシートのセルにアクセスするための基本的なアプローチについて説明します。

{{% /alert %}}

## **セルへのアクセス方法**

Aspose.Cells for Python via .NETは、Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)クラスを提供します。 [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) クラスには、Excelファイル内の各ワークシートにアクセスできる[**WorksheetCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection)が含まれています。 ワークシートは[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスによって表されます。 [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスには、ワークシート内のすべてのセルを表す[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)コレクションが含まれています。

[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)コレクションを使用してワークシート内のセルにアクセスできます。 Aspose.Cells for Python via .NETには、ワークシート内のセルにアクセスするための3つの基本的なアプローチが用意されています。

1. セル名を使用する。
1. セルの行と列のインデックスを使用します。
1. [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)コレクション内のセルインデックスを使用する

**重要：**3番目のアプローチが最も速く、1番目のアプローチが最も遅いことを記載しました。アプローチ間のパフォーマンスの違いは非常にわずかですので、使用するアプローチについてはパフォーマンスの低下を心配しないでください。

### **セルオブジェクトの取得方法（セル名による）**

開発者は[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)クラスの[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)コレクションにセルの名前をインデックスとして渡すことで、任意の特定のセルにアクセスできます。

最初に空のワークシートを作成すると、[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)コレクションの数はゼロになります。 このアプローチを使用してセルにアクセスする場合、このセルがコレクション内に存在するかどうかを確認します。 はいの場合、コレクション内のセルオブジェクトを返します。 そうでない場合は、新しい[**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell)オブジェクトを作成し、そのオブジェクトを[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)コレクションに追加してからオブジェクトを返します。 このアプローチは、Microsoft Excelに慣れている場合にはセルへのアクセスの最も簡単な方法ですが、他のアプローチと比較して最も遅いです。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-AccessingCells-UsingCellName-1.py" >}}

### **セルオブジェクトの取得方法（セルの行および列インデックスによる）**

開発者は、セルの行と列のインデックスを[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)クラスの[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)コレクションに渡すことで、任意の特定のセルにアクセスできます。

このアプローチは第1のアプローチと同じように機能します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-AccessingCells-UsingRowAndColumnIndexOfCell-1.py" >}}

### **セルオブジェクトの取得方法（セルのセルインデックスによる）**

セルは、[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)コレクションに対してセルの数値インデックスを渡すことでアクセスできます。

このアプローチを使用してセルにアクセスする場合、セルの数値インデックスが範囲外の場合、例外がスローされる可能性があります。 このアプローチを使用してセルオブジェクトにアクセスする場合、[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)コレクションへの新しいセルが追加されると数値インデックスが変更される可能性があることを知っておくことは重要です。 [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)コレクション内のセルオブジェクトは、内部的に行と列のインデックスでソートされます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-AccessingCells-UsingCellIndexInCellsCollection-1.py" >}}

## **ワークシートの最大表示範囲の取得方法**

Aspose.Cells for Python via .NETを使用すると、ワークシートの最大表示範囲にアクセスできます。 最大表示範囲は、コンテンツを持つ最初のセルと最後のセルの間のセルの範囲です。 これは、ワークシートの全内容をコピー、選択、または画像で表示する必要がある場合に役立ちます。

ワークシートの最大表示範囲には[**Worksheet.cells.max_display_range**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_display_range/)を使用してアクセスできます。 次のサンプルコードは、[**MaxDisplayRange**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_display_range/)プロパティにアクセスする方法を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-AccessingCells-AccessingMaximumDisplayRangeofWorksheet-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
