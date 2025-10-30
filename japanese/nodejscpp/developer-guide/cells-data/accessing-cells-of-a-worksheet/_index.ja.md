---
title: ワークシートのセルへのアクセス
type: docs
weight: 10
url: /ja/nodejs-cpp/accessing-cells-of-a-worksheet/
description: この記事では、ワークシートの最大表示範囲の取得と、そのセルへのアクセス方法をAspose.Cells for Node.js via C++ APIを使って紹介します。
keywords: セルオブジェクトを取得する、セルにアクセスする、ワークシートの最大表示範囲を取得する。 
---

{{% alert color="primary" %}}

すべてのワークシートには、基本的にセルに格納されているデータを含む可能性があることを私たちは知っています（これらがワークシートの構成要素です）。セルは、行と列のシーケンスとしてワークシート全体を構築するために使用されるワークシートの基本的な部分です。ワークシートからデータにアクセスしようとする前に、そのセルにアクセスできる必要があります。したがって、このトピックでは、Aspose.Cells for Node.js via C++を使用した実行時にワークシートセルにアクセスする基本的な方法について説明します。

{{% /alert %}}

## **セルへのアクセス方法**

Aspose.Cells for Node.js via C++は、Excelファイルを表すクラス[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)を提供します。[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスには、Excelファイル内の各ワークシートへのアクセスを可能にする[**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection)があります。ワークシートは、[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスは、ワークシート内のすべてのセルを表す[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)コレクションを提供します。

[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)コレクションを使用してワークシートのセルにアクセスできます。Aspose.Cells for Node.js via C++は、ワークシート内のセルにアクセスするための3つの基本的なアプローチを提供します。

1. セル名を使用する。
1. セルの行と列のインデックスを使用します。
1. [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)コレクション内のセルインデックスを使用する

**重要：**3番目のアプローチが最も速く、1番目のアプローチが最も遅いことを記載しました。アプローチ間のパフォーマンスの違いは非常にわずかですので、使用するアプローチについてはパフォーマンスの低下を心配しないでください。

### **セルオブジェクトの取得方法（セル名による）**

開発者は[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)クラスの[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)コレクションにセルの名前をインデックスとして渡すことで、任意の特定のセルにアクセスできます。

最初に空のワークシートを作成すると、[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)コレクションの数はゼロになります。 このアプローチを使用してセルにアクセスする場合、このセルがコレクション内に存在するかどうかを確認します。 はいの場合、コレクション内のセルオブジェクトを返します。 そうでない場合は、新しい[**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)オブジェクトを作成し、そのオブジェクトを[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)コレクションに追加してからオブジェクトを返します。 このアプローチは、Microsoft Excelに慣れている場合にはセルへのアクセスの最も簡単な方法ですが、他のアプローチと比較して最も遅いです。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-AccessingCells-UsingCellName-1.js" >}}

### **セルオブジェクトの取得方法（セルの行および列インデックスによる）**

開発者は、セルの行と列のインデックスを[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)クラスの[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)コレクションに渡すことで、任意の特定のセルにアクセスできます。

このアプローチは第1のアプローチと同じように機能します。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-AccessingCells-UsingRowAndColumnIndexOfCell-1.js" >}}

### **セルオブジェクトの取得方法（セルのセルインデックスによる）**

セルは、[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)コレクションに対してセルの数値インデックスを渡すことでアクセスできます。

このアプローチを使用してセルにアクセスする場合、セルの数値インデックスが範囲外の場合、例外がスローされる可能性があります。 このアプローチを使用してセルオブジェクトにアクセスする場合、[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)コレクションへの新しいセルが追加されると数値インデックスが変更される可能性があることを知っておくことは重要です。 [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)コレクション内のセルオブジェクトは、内部的に行と列のインデックスでソートされます。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-AccessingCells-UsingCellIndexInCellsCollection-1.js" >}}

## **ワークシートの最大表示範囲の取得方法**

Node.js用のAspose.Cells for Node.js via C++は、C++を介して、ワークシートの最大表示範囲にアクセスできるようにします。最大表示範囲とは、内容のある最初と最後のセルの間の範囲であり、ワークシートの全内容をコピー、選択、または画像として表示する必要がある場合に便利です。

ワークシートの最大表示範囲には[**Cells.getMaxDisplayRange**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDisplayRange--)を使用してアクセスできます。 次のサンプルコードは、[**getMaxDisplayRange**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDisplayRange--)プロパティにアクセスする方法を示しています。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-AccessingCells-AccessingMaximumDisplayRangeofWorksheet-1.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
