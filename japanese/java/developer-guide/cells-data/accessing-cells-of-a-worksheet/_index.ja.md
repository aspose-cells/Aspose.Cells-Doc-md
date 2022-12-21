---
title: ワークシートの Cells へのアクセス
type: docs
weight: 10
url: /ja/java/accessing-cells-of-a-worksheet/
---
{{% alert color="primary" %}} 

すべてのワークシートには、基本的にセル (ワークシートを構成するセル) に格納されているデータが含まれている可能性があることがわかっています。セルは、一連の行と列としてワークシート全体を構築するために使用されるワークシートの基本的な部分です。ワークシートからデータにアクセスする前に、そのセルにアクセスする必要があります。したがって、このトピックでは、実行時に Aspose.Cells を使用してワークシート セルにアクセスするための基本的な方法について説明します。

{{% /alert %}} 
## **Cellsにアクセス**
Aspose.Cells はクラスを提供し、[ワークブック](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)Microsoft Excel ファイルを表します。の[ワークブック](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスには[ワークシート コレクション](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)Excel ファイル内の各ワークシートにアクセスできるコレクション。ワークシートは、[ワークシート](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)クラス。の[ワークシート](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)クラスは[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)ワークシート内のすべてのセルを表すコレクション。

を使用できます[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)ワークシートのセルにアクセスするためのコレクション。 Aspose.Cells は、セルにアクセスするためのさまざまな基本的なアプローチを提供します。

1. [セル名の使用](/cells/ja/java/accessing-cells-of-a-worksheet/).
1. [行と列のインデックスの使用](/cells/ja/java/accessing-cells-of-a-worksheet/).
### **Cell名を使用**
開発者は、セル名を[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)のコレクション[ワークシート](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)クラス。

最初に空白のワークシートを作成すると、[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)コレクションはゼロです。このアプローチを使用してセルにアクセスすると、このセルがコレクションに存在するかどうかがチェックされます。はいの場合、コレクション内のセル オブジェクトを返します。それ以外の場合は、新しいセル オブジェクトを作成します。[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/Cell)オブジェクト、オブジェクトを[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)コレクションを作成し、オブジェクトを返します。 Microsoft Excel に慣れている場合、このアプローチはセルにアクセスする最も簡単な方法ですが、他のアプローチよりも遅くなります。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-UsingCellName-UsingCellName.java" >}}



### **Cell の行と列のインデックスを使用する**
開発者は、行と列のインデックスを[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)のコレクション[ワークシート](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)クラス。

このアプローチは、最初のアプローチと同じように機能します。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-UsingRowAndColumnIndexOfCell-UsingRowAndColumnIndexOfCell.java" >}}
### **関連記事**
{{% alert color="primary" %}} 

- [名前付き範囲](/cells/ja/java/named-ranges/)

{{% /alert %}} 
## **ワークシートの最大表示範囲へのアクセス**
Aspose.Cells を使用すると、開発者はワークシートの最大表示範囲にアクセスできます。最大表示範囲 (内容のある最初のセルと最後のセルの間のセルの範囲) は、ワークシートの内容全体をイメージでコピー、選択、または表示する必要がある場合に役立ちます。

を使用して、ワークシートの最大表示範囲にアクセスできます。[Worksheet.getCells().getMaxDisplayRange()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDisplayRange).

次の図では、選択したワークシートの最大表示範囲は A1:G15 です。

**このワークシートの最大表示範囲を表示しています** 

![todo:画像_代替_文章](accessing-cells-of-a-worksheet_1.png)

次のサンプル コードは、[MaxDisplayRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDisplayRange)財産。コードは次の出力を生成します。

{{< highlight "java" >}}

 Maximum Display Range: =Sheet1!$A$1:$G$15

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AccessingMaximumDisplayRangeofWorksheet-AccessingMaximumDisplayRangeofWorksheet.java" >}}
