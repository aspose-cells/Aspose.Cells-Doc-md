---
title: ワークシートのセルへのアクセス
type: docs
weight: 10
url: /ja/java/accessing-cells-of-a-worksheet/
---

{{% alert color="primary" %}} 

すべてのワークシートには基本的にセル（ワークシートが構成されている）に格納されているデータが含まれることを知っています。セルはワークシートの基本部分であり、ワークシート全体を行と列の連続として構築するために使用されます。ワークシートからデータにアクセスしようとする前に、そのセルにアクセスする必要があります。したがって、このトピックでは、Aspose.Cellsを使用して実行時にワークシートのセルにアクセスするための基本的なアプローチについて説明します。

{{% /alert %}} 
## **セルへのアクセス**
Aspose.Cellsは、Microsoft Excelファイルを表す[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスを提供しています。 [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスには、Excelファイル内の各ワークシートにアクセスできる[WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)コレクションが含まれています。ワークシートは[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)クラスで表されます。 [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)クラスは、ワークシート内のすべてのセルを表す[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)コレクションを提供します。

Aspose.Cellsは、セルへのアクセスのための異なる基本的なアプローチを提供しています：

1. [セル名を使用](/cells/ja/java/accessing-cells-of-a-worksheet/)
1. [行＆列インデックスを使用](/cells/ja/java/accessing-cells-of-a-worksheet/)
### **セル名の使用**
開発者は、ワークシートの[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) コレクションにそのセル名を渡すことで、任意の特定のセルにアクセスできます。

開始時に空のワークシートを作成した場合、[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) コレクションの数はゼロです。このアプローチを使用してセルにアクセスすると、そのセルがコレクションに存在するかどうかをチェックし、存在する場合はそれを返します。存在しない場合は、新しい[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) オブジェクトを作成し、そのオブジェクトを[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) コレクションに追加してから返します。Microsoft Excelに精通している場合、このアプローチはセルにアクセスする一番簡単な方法ですが、他のアプローチよりも遅くなります。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-UsingCellName-UsingCellName.java" >}}



### **セルの行と列のインデックスの使用**
開発者は、その行と列のインデックスを[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) コレクションに渡すことで、任意の特定のセルにアクセスできます。

このアプローチは第1のアプローチと同じように機能します。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-UsingRowAndColumnIndexOfCell-UsingRowAndColumnIndexOfCell.java" >}}
### **関連記事**
{{% alert color="primary" %}} 

- [名前付き範囲](/cells/ja/java/named-ranges/)

{{% /alert %}} 
## **ワークシートの最大表示範囲へのアクセス**
Aspose.Cellsは、ワークシートの最大表示範囲にアクセスすることができます。最大表示範囲(コンテンツを持つ最初のセルと最後のセルの範囲)は、ワークシート全体の内容をコピー、選択、または表示する必要がある場合に便利です。

ワークシートの最大表示範囲には、[Worksheet.getCells().getMaxDisplayRange()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDisplayRange)を使用してアクセスできます。

次の図には、選択したワークシートの最大表示範囲がA1：G15に示されています。

**このワークシートの最大表示範囲を表示する** 

![todo:image_alt_text](accessing-cells-of-a-worksheet_1.png)

以下のサンプルコードは、[MaxDisplayRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDisplayRange) プロパティにアクセスする方法を示しています。コードは次の出力を生成します。

{{< highlight java >}}

 Maximum Display Range: =Sheet1!$A$1:$G$15

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AccessingMaximumDisplayRangeofWorksheet-AccessingMaximumDisplayRangeofWorksheet.java" >}}
{{< app/cells/assistant language="java" >}}
