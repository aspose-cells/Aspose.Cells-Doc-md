---
title: 行と列の自動調整
type: docs
weight: 20
url: /ja/java/autofit-rows-and-columns/
---
{{% alert color="primary" %}} 

Microsoft Excel には、セルの内容に応じてセルの幅と高さを自動サイズ変更する優れた機能があります。この機能は、Aspose.Cells ユーザーも利用でき、実行時にセルの寸法を自動サイズ変更できます。

{{% /alert %}} 
## **自動フィッティング**
Aspose.Cells はクラスを提供し、[ワークブック](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)、Microsoft Excel ファイルを表します。の[ワークブック](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスには[ワークシート](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets)Excel ファイル内の各ワークシートにアクセスできるコレクション。

ワークシートは、[ワークシート](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)クラス。の[ワークシート](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)クラスには、ワークシートを管理するためのさまざまなプロパティとメソッドが用意されています。この記事では、[ワークシート](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)行または列を自動調整するクラス。
### **行の自動調整 - シンプル**
行の幅と高さを自動サイズ変更する最も簡単な方法は、[ワークシート](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)クラス'[autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int\)） 方法。の[autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int\)) メソッドは、(サイズ変更する行の) 行インデックスをパラメーターとして受け取ります。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsandColumns-AutoFitRowsandColumns.java" >}}
### **Cells の範囲で行を自動調整**
行は多くの列で構成されています。 Aspose.Cells を使用すると、開発者は、オーバーロードされたバージョンの[autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int,%20int,%20int\)） 方法。次のパラメータを取ります。

- **行インデックス**、自動調整しようとしている行のインデックス。
- **最初の列のインデックス**、行の最初の列のインデックス。
- **最後の列のインデックス**、行の最後の列のインデックス。

の[autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int,%20int,%20int\)) メソッドは、行内のすべての列の内容をチェックしてから、行を自動調整します。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsinaRangeofCells-AutoFitRowsinaRangeofCells.java" >}}
### **列の自動調整 - シンプル**
列の幅と高さを自動サイズ変更する最も簡単な方法は、[ワークシート](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)クラス'[autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int\)） 方法。の[autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int\)メソッドは、(サイズ変更しようとしている列の) 列インデックスをパラメーターとして受け取ります。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsandColumns-AutoFitRowsandColumns.java" >}}
### **Cells の範囲で列を自動調整**
列は多くの行で構成されています。オーバーロードされたバージョンの[autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int,%20int,%20int\)) 以下のパラメータを取るメソッド:

- **列インデックス**、内容を自動調整する必要がある列のインデックスを表します
- **最初の行のインデックス**、列の最初の行のインデックスを表します
- **最後の行のインデックス**、列の最後の行のインデックスを表します

の[autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int,%20int,%20int\)メソッドは、列内のすべての行の内容をチェックしてから、列を自動調整します。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitColumnsinaRangeofCells-AutoFitColumnsinaRangeofCells.java" >}}
### **マージされた Cells の行の自動調整**
Aspose.Cells を使用すると、[AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) API. [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions)クラスが提供する[AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions#AutoFitMergedCellsType)結合されたセルの行を自動調整するために使用できるプロパティ。[AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions#AutoFitMergedCellsType)受け入れる[AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitMergedCellsType)次のメンバーを持つ列挙可能。

- [なし](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#NONE): 結合されたセルを無視します。
- [FIRST_LINE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#FIRST_LINE): 最初の行の高さのみを拡張します。
- [LAST_LINE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#LAST_LINE): 最後の行の高さのみを拡張します。
- [EACH_LINE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#EACH_LINE): 各行の高さのみを拡張します。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-AutofitRowsforMergedCells-1.java" >}}

のオーバーロードされたバージョンを使用することもできます[autoFitRows](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRows\(\)) & [autoFitColumns](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumns\(\) ) 行/列の範囲とインスタンスを受け入れるメソッド[AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions)選択した行/列を目的の位置に自動調整します[AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions)によると。

前述のメソッドのシグネチャは次のとおりです。

1.  autoFitRows(int startRow, int endRow,[AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions)オプション)
1.  autoFitColumns(int firstColumn, int lastColumn,[AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions)オプション)
## **知っておくべき重要事項**
{{% alert color="primary" %}} 

セルが結合された場合、*自動調整*メソッドは適用されません。これは、Microsoft Excel と同じ動作です。さらに、セル内のテキストが折り返されている場合、[autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int\) ) メソッドも適用されません。もう 1 つ知っておく必要があるのは、*自動調整*方法は時間がかかります。したがって、アプリケーションの効率を確保するために、これらのメソッドをできるだけ呼び出さないようにする必要があります。

{{% /alert %}}
